"""Score stored sessions.

The scoring is a pure function of sessions.jsonl, the rule files, and
the flags: per style, the violation-rate series over turn positions,
the pooled series over the complete sessions, the slope of the pooled
series, and the verdict flat or growing. The verdict threshold comes
from a per-style permutation null: the turn order of each session
shuffles, the pooled slope refits, and the threshold is the 0.95
nearest-rank quantile of the shuffled slopes. The same null yields a
one-sided p-value, stated for information; the verdict rests on the
threshold alone. The scoring also states the context depth: per
turn, the token sum of the call, and per style, the final depth of
each session against the context window, with a warning when a
depth target exists and the mean final depth misses it.
"""

from __future__ import annotations

import hashlib
import json
import random
import statistics
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path

from linter import Linter
from runner.stats import nearest_rank

Key = tuple[str, int, int]
"""(style, repeat, turn), both numbers 1-based."""

PERMUTATIONS = 10000
"""Shuffles per style for the permutation null."""

SEED = 0
"""Seed of the permutation null, so a rescore repeats the threshold."""

QUANTILE = 0.95
"""The one-sided null quantile that becomes the derived threshold."""


CONTEXT_WINDOW = 200_000
"""The assumed context window in tokens; the stream-json events do
not carry the size, so the depth fraction rests on this flag."""

DEPTH_TARGET = 0.6
"""The default target of a deep run: the mean final depth as a
fraction of the window. The value sits clearly below the compaction
region of Claude Code (near 0.8), because compaction rewrites the
context and changes what the test measures."""


@dataclass
class DriftResult:
    styles: dict[str, dict] = field(default_factory=dict)
    warnings: list[str] = field(default_factory=list)


def context_tokens(row: dict) -> int | None:
    """The context depth of one call: the uncached input, the
    cache-write, and the cache-read tokens, summed. None for a row
    from before the token fields."""
    if not isinstance(row.get("input_tokens"), int):
        return None
    return row["input_tokens"] + row["cache_creation_input_tokens"] + row["cache_read_input_tokens"]


def load_sessions(path: Path) -> dict[Key, dict]:
    """The stored turns, last (style, repeat, turn) wins."""
    rows: dict[Key, dict] = {}
    if not path.exists():
        return rows
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        row = json.loads(line)
        rows[(row["style"], row["repeat"], row["turn"])] = row
    return rows


def _turn_row(row: dict, linter: Linter) -> dict:
    report = linter.lint_text(
        row["answer"], file=f"{row['style']}/repeat-{row['repeat']}/turn-{row['turn']}"
    )
    return {
        "style": row["style"],
        "repeat": row["repeat"],
        "turn": row["turn"],
        "prompt_id": row["prompt_id"],
        "sentences": report.sentence_count,
        "violations": len(report.violations),
        "by_rule": dict(sorted(Counter(v.rule for v in report.violations).items())),
        "rate": round(report.rate, 2),
        "context_tokens": context_tokens(row),
        "answer_sha256": hashlib.sha256(row["answer"].encode("utf-8")).hexdigest(),
    }


def _pooled_series(session_pairs: list[list[tuple[int, int]]], turns: int) -> list[float]:
    """Per turn, 100 times the violations over the sentences, pooled.

    The pool spans the complete sessions at that turn position, so a
    short answer weighs by its sentence count. A zero sentence sum
    gives 0.0, the mirror of the linter rate.
    """
    series = []
    for index in range(turns):
        violations = sum(pairs[index][0] for pairs in session_pairs)
        sentences = sum(pairs[index][1] for pairs in session_pairs)
        series.append(round(100 * violations / sentences, 2) if sentences else 0.0)
    return series


def _null_stats(
    session_pairs: list[list[tuple[int, int]]],
    turns: int,
    permutations: int,
    seed: int,
    slope: float,
) -> tuple[float, float]:
    """The threshold and the p-value of the permutation null.

    Each permutation shuffles the turn order within each session, so
    the null keeps the rates and breaks only the turn positions. The
    threshold is the 0.95 nearest-rank quantile of the shuffled
    slopes. The p-value is the share of shuffled slopes at or above
    the observed slope, stated for information only.
    """
    rng = random.Random(seed)
    null = []
    for _ in range(permutations):
        shuffled = []
        for pairs in session_pairs:
            copy = list(pairs)
            rng.shuffle(copy)
            shuffled.append(copy)
        null_slope, _ = statistics.linear_regression(
            range(1, turns + 1), _pooled_series(shuffled, turns)
        )
        null.append(null_slope)
    p_value = sum(1 for null_slope in null if null_slope >= slope) / permutations
    return nearest_rank(sorted(null), QUANTILE * 100), p_value


def score_sessions(
    *,
    rows: dict[Key, dict],
    linters: dict[str, Linter],
    turns: int,
    repeats: int,
    threshold: float | None = None,
    permutations: int = PERMUTATIONS,
    seed: int = SEED,
    context_window: int = CONTEXT_WINDOW,
    depth_target: float | None = None,
) -> DriftResult:
    """Score every style of the linters mapping against the stored rows."""
    result = DriftResult()
    wanted = set(range(1, turns + 1))
    for style in sorted(linters):
        sessions: list[dict] = []
        session_pairs: list[list[tuple[int, int]]] = []
        turn_details: list[dict] = []
        finals: dict[str, int | None] = {}
        for repeat in range(1, repeats + 1):
            present = {turn for (s, r, turn) in rows if s == style and r == repeat}
            if not present:
                result.warnings.append(f"{style}: session {repeat} has no turns")
                continue
            if present != wanted:
                missing = ", ".join(str(turn) for turn in sorted(wanted - present))
                result.warnings.append(
                    f"{style}: session {repeat} misses turn(s) {missing}, "
                    "so the session is excluded"
                )
                continue
            series = []
            pairs = []
            for turn in sorted(wanted):
                detail = _turn_row(rows[(style, repeat, turn)], linters[style])
                if detail["sentences"] == 0:
                    result.warnings.append(
                        f"{style}: session {repeat} turn {turn} has no sentences"
                    )
                turn_details.append(detail)
                series.append(detail["rate"])
                pairs.append((detail["violations"], detail["sentences"]))
            sessions.append({"repeat": repeat, "series": series})
            session_pairs.append(pairs)
            finals[str(repeat)] = context_tokens(rows[(style, repeat, turns)])

        measured = [depth for depth in finals.values() if depth is not None]
        mean_final = round(statistics.mean(measured)) if measured else None
        depth = {
            "final": finals,
            "mean_final": mean_final,
            "window_fraction": (
                round(mean_final / context_window, 3) if mean_final is not None else None
            ),
        }

        if not sessions:
            result.warnings.append(f"{style}: no complete session, so the style has no verdict")
            result.styles[style] = {
                "complete_sessions": 0,
                "sessions": [],
                "pooled_series": None,
                "slope": None,
                "intercept": None,
                "threshold": None,
                "threshold_source": None,
                "null": None,
                "verdict": None,
                "depth": depth,
                "turns": [],
            }
            continue

        if depth_target is not None:
            if mean_final is None:
                result.warnings.append(
                    f"{style}: the final depth is not measured, "
                    "so the depth target cannot be checked"
                )
            elif mean_final < depth_target * context_window:
                result.warnings.append(
                    f"{style}: the mean final depth is {mean_final:,} tokens, "
                    f"{100 * mean_final / context_window:.1f} percent of the "
                    f"{context_window:,}-token window — under the "
                    f"{round(100 * depth_target)} percent target; a flat verdict "
                    "at a shallow depth is weak evidence"
                )

        pooled_series = _pooled_series(session_pairs, turns)
        slope, intercept = statistics.linear_regression(range(1, turns + 1), pooled_series)
        derived, p_value = _null_stats(session_pairs, turns, permutations, seed, slope)
        effective = derived if threshold is None else threshold
        result.styles[style] = {
            "complete_sessions": len(sessions),
            "sessions": sessions,
            "pooled_series": pooled_series,
            "slope": round(slope, 3),
            "intercept": round(intercept, 3),
            "threshold": round(effective, 3),
            "threshold_source": "derived" if threshold is None else "override",
            "null": {
                "permutations": permutations,
                "seed": seed,
                "quantile": QUANTILE,
                "threshold": round(derived, 3),
                "p_value": round(p_value, 4),
            },
            "verdict": "growing" if slope > effective else "flat",
            "depth": depth,
            "turns": turn_details,
        }
    return result

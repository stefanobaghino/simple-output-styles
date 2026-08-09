"""Build the drift summary and the drift report."""

from __future__ import annotations

import statistics
from datetime import UTC, datetime

from runner.spend import spend_section

HEADER = """\
# Drift report

Run: {run}

The report measures rule obedience across long sessions. A session is
{turns} scripted turns in one Claude Code session, with the style
active. Each turn resumes the session of the previous turn, so the
context grows. Each session runs {repeats} time(s), and each repeat
rotates the prompt order, so a hard prompt does not always sit at the
same turn position. The linter checks each answer with the rule set
of the style. The rate of a turn position pools the complete
sessions: 100 times the violations at that position over the
sentences at that position. Thus a short answer weighs by its
sentence count and cannot dominate the series. The verdict compares
the slope of the pooled series against a per-style threshold:
"growing" when the slope is larger, else "flat". The threshold comes
from a permutation null: the turn order of each session shuffles,
the pooled slope refits, and the threshold is a nearest-rank
quantile of the shuffled slopes. The same null yields a one-sided
p-value — the share of shuffled slopes at or above the observed
slope — stated for information; the verdict rests on the threshold
alone. The section of each style states
the quantile, the permutation count, and the seed. The
`--slope-threshold` flag replaces the derived threshold, and the
section then states both values.
"""

HEADER_DEEP = """\
# Drift report

Run: {run}

The report measures rule obedience across long sessions. A session is
{turns} scripted turns in one Claude Code session, with the style
active. Each turn resumes the session of the previous turn, so the
context grows. Each session follows one coherent script with heavy
turn material, and later turns reference earlier material, so the
model must read deep context while it obeys the style. A coherent
script cannot rotate, so the {repeats} repeat(s) spread over several
different scripts, and the coupling of turn position to content
averages over scripts. The shallow rotated run is the control. The
linter checks each answer with the rule set of the style. The rate
of a turn position pools the complete sessions: 100 times the
violations at that position over the sentences at that position.
Thus a short answer weighs by its sentence count and cannot dominate
the series. The verdict compares the slope of the pooled series
against a per-style threshold: "growing" when the slope is larger,
else "flat". The threshold comes from a permutation null: the turn
order of each session shuffles, the pooled slope refits, and the
threshold is a nearest-rank quantile of the shuffled slopes. The
same null yields a one-sided p-value — the share of shuffled slopes
at or above the observed slope — stated for information; the
verdict rests on the threshold alone. The
section of each style states the quantile, the permutation count,
and the seed. The `--slope-threshold` flag replaces the derived
threshold, and the section then states both values.
"""


def build_drift_summary(
    *,
    run_name: str,
    turns: int,
    repeats: int,
    slope_threshold: float | None,
    context_window: int,
    depth_target: float | None,
    styles: dict[str, dict],
    rules: dict[str, dict],
    toolchain: dict,
    run_toolchain: dict | None,
    warnings: list[str],
    mode: str | None = None,
    scripts: dict[str, str] | None = None,
) -> dict:
    summary = {
        "date": datetime.now(UTC).isoformat(timespec="seconds"),
        "run": run_name,
        "turns": turns,
        "repeats": repeats,
        "slope_threshold": slope_threshold,
        "context_window": context_window,
        "styles": styles,
        "rules": rules,
        "linter_toolchain": toolchain,
        "run_linter_toolchain": run_toolchain,
        "warnings": warnings,
    }
    # A target key lands only when a target exists, so a shallow
    # summary carries none by default; the mode keys land only in
    # deep mode, like before.
    if depth_target is not None:
        summary["depth_target"] = depth_target
    if mode is not None:
        summary["mode"] = mode
    if scripts is not None:
        summary["scripts"] = scripts
    return summary


def _rate(value: float | None) -> str:
    return "-" if value is None else f"{value:.2f}"


def _style_section(style: str, stats: dict, summary: dict) -> list[str]:
    lines = [f"## {style}", ""]
    repeats = summary["repeats"]
    if stats["complete_sessions"] == 0:
        lines += ["The style has no complete session, so the style has no verdict.", ""]
        return lines
    null = stats["null"]
    quantile = f"the {null['quantile']} quantile of {null['permutations']} shuffled slopes"
    if stats["threshold_source"] == "derived":
        threshold = f"{stats['threshold']} ({quantile}, seed {null['seed']})"
    else:
        threshold = f"{stats['threshold']} (override; the null quantile is {null['threshold']})"
    depth = stats["depth"]
    window = summary["context_window"]
    if depth["mean_final"] is None:
        depth_line = "- Final depth: not measured"
    else:
        per_repeat = " / ".join(
            f"{depth['final'][str(repeat)]:,}"
            if isinstance(depth["final"].get(str(repeat)), int)
            else "-"
            for repeat in range(1, repeats + 1)
        )
        depth_line = (
            f"- Final depth: mean {depth['mean_final']:,} tokens, "
            f"{100 * depth['mean_final'] / window:.1f} percent of the "
            f"{window:,}-token window (repeats {per_repeat})"
        )
    lines += [
        f"- Sessions: {stats['complete_sessions']}/{repeats} complete",
        f"- Slope of the pooled series: {stats['slope']} violations per 100 sentences per turn",
        f"- Slope threshold: {threshold}",
        f"- Null p-value: {null['p_value']} (the share of shuffled slopes at or above the slope)",
        f"- Verdict: {stats['verdict']}",
        depth_line,
        "",
    ]
    depth_by_turn: dict[int, list[int]] = {}
    for detail in stats["turns"]:
        value = detail.get("context_tokens")
        if isinstance(value, int):
            depth_by_turn.setdefault(detail["turn"], []).append(value)
    by_repeat = {session["repeat"]: session["series"] for session in stats["sessions"]}
    header = ["Turn", "Pooled rate", "Mean depth"] + [
        f"Repeat {repeat}" for repeat in range(1, repeats + 1)
    ]
    lines.append("| " + " | ".join(header) + " |")
    lines.append("|" + "---|" * len(header))
    for index in range(summary["turns"]):
        values = depth_by_turn.get(index + 1)
        mean_depth = f"{round(statistics.mean(values)):,}" if values else "-"
        cells = [str(index + 1), _rate(stats["pooled_series"][index]), mean_depth]
        for repeat in range(1, repeats + 1):
            series = by_repeat.get(repeat)
            cells.append(_rate(series[index]) if series is not None else "-")
        lines.append("| " + " | ".join(cells) + " |")
    lines.append("")
    return lines


def build_drift_report(summary: dict, spend: dict | None = None) -> str:
    deep = summary.get("mode") == "deep"
    header = HEADER_DEEP if deep else HEADER
    lines = [
        header.format(
            run=summary["run"],
            turns=summary["turns"],
            repeats=summary["repeats"],
        )
    ]
    if deep:
        for repeat, script_id in sorted(summary["scripts"].items(), key=lambda item: int(item[0])):
            lines.append(f"- Repeat {repeat}: script `{script_id}`")
        lines.append("")
    depth_paragraph = (
        "Each style section states the final context depth of its "
        "sessions — the uncached input, the cache-write, and the "
        "cache-read tokens of a call, summed — against the "
        f"{summary['context_window']:,}-token context window "
        "(`--context-window`)."
    )
    if summary.get("depth_target") is not None:
        depth_paragraph += (
            f" The depth target is {round(100 * summary['depth_target'])} "
            "percent of the window: a style whose mean final depth misses "
            "the target warns, because a flat verdict at a shallow depth "
            "is weak evidence."
        )
    lines += [depth_paragraph, ""]
    for style in sorted(summary["styles"]):
        lines += _style_section(style, summary["styles"][style], summary)
    lines += spend_section(spend)
    lines.append("## Warnings")
    lines.append("")
    if summary["warnings"]:
        lines += [f"- {warning}" for warning in summary["warnings"]]
    else:
        lines.append("- none")
    lines.append("")
    return "\n".join(lines)

"""Project the depth and the spend of a deep run before any call.

The projection is an estimate, not a measurement: it turns the byte
length of the script material into tokens and replays the cache
arithmetic of a resumed session. Three constants calibrate it, each
measured against the stored shallow run runs/2026-08-08-drift. The
real run measures the truth, and the drift report then replaces the
projection.
"""

from __future__ import annotations

from cost.probe import weighted_total

CONTEXT_BASE_TOKENS = 9_500
"""The context that every call carries before any script material:
the turn-1 cache read of runs/2026-08-08-drift."""

ANSWER_TOKENS = 550
"""Projected output tokens per answer: the mean output of
runs/2026-08-08-drift."""

BYTES_PER_TOKEN = 4
"""A rough prose ratio; code and log material runs denser, so the
projection leans low on such scripts."""


def project_script(script: dict, context_window: int) -> dict:
    """The projected depth and per-session token usage of one script.

    The cache arithmetic of a resumed session: every turn reads the
    whole prior context from the cache, and writes its own material
    plus the previous answer. The final answer is never written,
    because no later call re-sends it.
    """
    tokens = [
        round(len(turn["text"].encode("utf-8")) / BYTES_PER_TOKEN) for turn in script["turns"]
    ]
    cache_read = 0
    cache_creation = 0
    context = CONTEXT_BASE_TOKENS
    for index, turn_tokens in enumerate(tokens):
        cache_read += context
        new = turn_tokens + (ANSWER_TOKENS if index else 0)
        cache_creation += new
        context += new
    return {
        "id": script["id"],
        "turns": len(tokens),
        "material_tokens": sum(tokens),
        "final_depth": context,
        "window_fraction": round(context / context_window, 3),
        "session_input_tokens": len(tokens),
        "session_cache_creation_tokens": cache_creation,
        "session_cache_read_tokens": cache_read,
        "session_output_tokens": len(tokens) * ANSWER_TOKENS,
    }


def estimate_deep_run(
    *,
    scripts: list[dict],
    style_count: int,
    repeats: int,
    context_window: int,
    depth_target: float | None,
) -> dict:
    """The projection of one deep run over the whole style grid."""
    projections = [project_script(script, context_window) for script in scripts]
    sessions_per_script = style_count * repeats // len(scripts)
    totals = {
        "input_tokens": 0,
        "cache_creation_input_tokens": 0,
        "cache_read_input_tokens": 0,
    }
    output_tokens = 0
    for projection in projections:
        totals["input_tokens"] += sessions_per_script * projection["session_input_tokens"]
        totals["cache_creation_input_tokens"] += (
            sessions_per_script * projection["session_cache_creation_tokens"]
        )
        totals["cache_read_input_tokens"] += (
            sessions_per_script * projection["session_cache_read_tokens"]
        )
        output_tokens += sessions_per_script * projection["session_output_tokens"]
    return {
        "styles": style_count,
        "repeats": repeats,
        "sessions": style_count * repeats,
        "calls": style_count * repeats * projections[0]["turns"],
        "context_window": context_window,
        "depth_target": depth_target,
        "scripts": projections,
        "totals": {
            **totals,
            "output_tokens": output_tokens,
            "uncached_equivalents": weighted_total(totals),
        },
    }


def estimate_lines(estimate: dict) -> list[str]:
    """The projection as lines for a human."""
    window = estimate["context_window"]
    target = estimate["depth_target"]
    lines = [
        (
            f"Deep-run estimate: {estimate['sessions']} session(s) of "
            f"{estimate['scripts'][0]['turns']} turn(s) — {estimate['styles']} style(s) x "
            f"{estimate['repeats']} repeat(s) — {estimate['calls']} call(s)."
        ),
        (
            "The projection rests on constants calibrated against "
            f"runs/2026-08-08-drift: a {CONTEXT_BASE_TOKENS:,}-token context base, "
            f"{ANSWER_TOKENS} output tokens per answer, and {BYTES_PER_TOKEN} bytes "
            "per token. Code and log material runs denser than prose, so the "
            "projection leans low."
        ),
    ]
    for projection in estimate["scripts"]:
        line = (
            f"- {projection['id']}: material ~{projection['material_tokens']:,} tokens, "
            f"projected final depth ~{projection['final_depth']:,} tokens, "
            f"{100 * projection['final_depth'] / window:.1f} percent of the "
            f"{window:,}-token window"
        )
        if target is not None:
            verdict = "clears" if projection["final_depth"] >= target * window else "misses"
            line += f" — {verdict} the {round(100 * target)} percent target"
        lines.append(line)
    totals = estimate["totals"]
    lines.append(
        f"Projected input: ~{totals['cache_creation_input_tokens']:,} cache-write, "
        f"~{totals['cache_read_input_tokens']:,} cache-read, and "
        f"~{totals['input_tokens']:,} uncached tokens; "
        f"~{round(totals['uncached_equivalents']):,} uncached-token equivalents. "
        f"Projected output: ~{totals['output_tokens']:,} tokens."
    )
    return lines

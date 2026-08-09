"""Render the artifacts of a targets check.

targets.json holds the machine-readable summary and the check
provenance. targets.md is for a human who opens the run directory.
"""

from __future__ import annotations

from datetime import UTC, datetime


def build_targets_summary(
    *,
    styles: dict[str, list[dict]],
    run_name: str,
    targets_config_hash: dict,
    drift_run: str | None,
    warnings: list[str],
) -> dict:
    return {
        "date": datetime.now(UTC).isoformat(timespec="seconds"),
        "run": run_name,
        "targets_config": targets_config_hash,
        "drift_run": drift_run,
        "styles": styles,
        "warnings": warnings,
    }


def _rendered(value: float | None) -> str:
    return "-" if value is None else f"{value:g}"


def build_targets_report(summary: dict) -> str:
    lines = [
        "# Regression targets report",
        "",
        f"The check compares the run against {summary['targets_config']['file']}.",
        "A max limit is a cap: the observed value passes at or below it. A",
        "min limit is a floor: the observed value passes at or above it.",
        "The token axis is a bound, not a target: a value under the bound",
        "earns nothing.",
        "",
    ]
    for style, rows in summary["styles"].items():
        checked = [r for r in rows if r["verdict"] != "skipped"]
        passed = [r for r in checked if r["verdict"] == "pass"]
        lines += [f"## {style}", ""]
        lines += [f"- Axes within targets: {len(passed)}/{len(checked)}", ""]
        lines += ["| Axis | Kind | Limit | Observed | Verdict |", "|---|---|---|---|---|"]
        lines += [
            f"| {r['axis']} | {r['kind']} | {_rendered(r['limit'])} "
            f"| {_rendered(r['observed'])} | {r['verdict']} |"
            for r in rows
        ]
        lines.append("")
        notes = [r for r in rows if r.get("note")]
        if notes:
            lines += [f"- {r['axis']}: {r['note']}" for r in notes]
            lines.append("")
    lines += ["## Warnings", ""]
    lines += [f"- {warning}" for warning in summary["warnings"]] or ["- none"]
    lines.append("")
    return "\n".join(lines)

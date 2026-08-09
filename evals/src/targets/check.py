"""Check the artifacts of one run against the regression targets.

The check is a pure function of the loaded artifacts and the targets.
Every boundary is inclusive: an observed value equal to its limit
passes, like the gate threshold. The token axis is a bound, not a
target: a value under the bound earns nothing, so a pass is a pass
without degree.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from .config import TargetsConfig


@dataclass
class CheckResult:
    styles: dict[str, list[dict]] = field(default_factory=dict)
    warnings: list[str] = field(default_factory=list)


def _token_ratio(run: dict, style: str) -> float | None:
    cost = run.get("cost")
    if cost is None:
        return None
    stats = cost.get("answer_ratio", {}).get("per_style", {}).get(style)
    return None if stats is None else stats.get("ratio_of_totals")


def _fact_survival(run: dict, style: str) -> float | None:
    loss = run.get("loss")
    if loss is None:
        return None
    stats = loss.get("checks", {}).get("completeness", {}).get("per_style", {}).get(style)
    return None if stats is None else stats.get("median")


def _hedge_survival(run: dict, style: str) -> float | None:
    loss = run.get("loss")
    if loss is None:
        return None
    stats = loss.get("checks", {}).get("hedging", {}).get("per_style", {}).get(style)
    return None if stats is None else stats.get("median")


def _rank_strength(run: dict, style: str) -> float | None:
    rank = run.get("rank")
    if rank is None:
        return None
    info = (rank.get("bradley_terry", {}).get("strengths") or {}).get(style)
    return None if info is None else info.get("strength")


def _drift_slope(drift: dict | None, style: str) -> float | None:
    if drift is None:
        return None
    info = drift.get("styles", {}).get(style)
    return None if info is None else info.get("slope")


AXES = (
    ("max_token_ratio", "max", "cost.json", _token_ratio),
    ("min_fact_survival", "min", "loss.json", _fact_survival),
    ("min_hedge_survival", "min", "loss.json", _hedge_survival),
    ("min_rank_strength", "min", "rank.json", _rank_strength),
)


def _styles(run: dict) -> list[str]:
    styles: set[str] = set(run["provenance"].get("styles") or {})
    cost = run.get("cost")
    if cost is not None:
        styles.update(cost.get("answer_ratio", {}).get("per_style") or {})
    loss = run.get("loss")
    if loss is not None:
        for check in ("completeness", "hedging"):
            styles.update(loss.get("checks", {}).get(check, {}).get("per_style") or {})
    rank = run.get("rank")
    if rank is not None:
        styles.update(rank.get("bradley_terry", {}).get("strengths") or {})
    styles.discard("unstyled")
    return sorted(styles)


def _row(axis: str, kind: str, limit: float | None, observed: float | None, note: str | None):
    if limit is None or observed is None:
        verdict = "skipped"
    elif kind == "max":
        verdict = "pass" if observed <= limit else "fail"
    else:
        verdict = "pass" if observed >= limit else "fail"
    row = {"axis": axis, "kind": kind, "limit": limit, "observed": observed, "verdict": verdict}
    if note is not None:
        row["note"] = note
    return row


def check_run(run: dict, config: TargetsConfig, drift: dict | None) -> CheckResult:
    result = CheckResult()
    styles = _styles(run)
    for artifact in ("cost", "loss", "rank"):
        if run.get(artifact) is None:
            result.warnings.append(f"{artifact}.json is missing, so its axes are unchecked")

    slope_cap_skipped = False
    for style in styles:
        targets = config.styles.get(style)
        rows: list[dict] = []
        if targets is None:
            # A candidate before acceptance: the default token bound
            # applies, and the other axes wait for a calibrated row.
            note = f"no calibrated row in {config.path.name}; the default bound applies"
            observed = _token_ratio(run, style)
            rows.append(
                _row("max_token_ratio", "max", config.default_max_token_ratio, observed, note)
            )
            if observed is None and run.get("cost") is not None:
                result.warnings.append(f"{style}: no observed max_token_ratio in the run")
            for axis, kind, _, _ in AXES[1:]:
                rows.append(_row(axis, kind, None, None, "uncalibrated"))
            rows.append(_row("max_drift_slope", "max", None, None, "uncalibrated"))
            result.styles[style] = rows
            continue
        for axis, kind, artifact, extract in AXES:
            limit = getattr(targets, axis)
            observed = extract(run, style)
            note = None
            if limit is None:
                note = "no limit set"
            elif observed is None:
                if run.get(artifact.removesuffix(".json")) is None:
                    note = f"{artifact} is missing"
                else:
                    note = "not observed in the run"
                    result.warnings.append(f"{style}: no observed {axis} in the run")
            rows.append(_row(axis, kind, limit, observed, note))
        limit = targets.max_drift_slope
        observed = _drift_slope(drift, style)
        note = None
        if limit is None:
            note = "no limit set"
        elif drift is None:
            note = "no drift run passed"
            slope_cap_skipped = True
        elif observed is None:
            note = "not in the drift run"
            result.warnings.append(f"{style}: no observed max_drift_slope in the drift run")
        rows.append(_row("max_drift_slope", "max", limit, observed, note))
        result.styles[style] = rows

    if slope_cap_skipped:
        # An unchecked bound is the silent-regression channel this
        # check closes, so the skip is a warning, not a note.
        result.warnings.append("no drift run passed, so the drift-slope caps are unchecked")
    for style in sorted(config.styles):
        if style not in styles:
            result.warnings.append(f"{style}: in {config.path} but not in the run")
    return result

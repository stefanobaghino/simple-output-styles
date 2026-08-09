"""Load the regression targets.

The targets live in their own file, next to the gate policy: a target
edit changes only the pass marks, never a measured number, and thus
must not change the rule-file hashes in the provenance.
"""

from __future__ import annotations

from dataclasses import dataclass, fields
from pathlib import Path

import yaml

AXIS_KEYS = (
    "max_token_ratio",
    "min_fact_survival",
    "min_hedge_survival",
    "min_rank_strength",
    "max_drift_slope",
)


@dataclass(frozen=True)
class StyleTargets:
    """The limits of one style. A max key is a cap, a min key a floor."""

    max_token_ratio: float | None = None
    min_fact_survival: float | None = None
    min_hedge_survival: float | None = None
    min_rank_strength: float | None = None
    max_drift_slope: float | None = None


assert tuple(f.name for f in fields(StyleTargets)) == AXIS_KEYS


@dataclass(frozen=True)
class TargetsConfig:
    path: Path
    default_max_token_ratio: float
    """The token bound of a style without a calibrated row."""
    styles: dict[str, StyleTargets]


def load_targets_config(path: str | Path) -> TargetsConfig:
    path = Path(path)
    raw = yaml.safe_load(path.read_text(encoding="utf-8"))
    styles = raw.get("styles") if isinstance(raw, dict) else None
    if not isinstance(styles, dict) or not styles:
        raise ValueError(f"{path}: no styles defined")
    defaults = raw.get("defaults")
    if not isinstance(defaults, dict) or "max_token_ratio" not in defaults:
        raise ValueError(f"{path}: no defaults.max_token_ratio defined")
    loaded: dict[str, StyleTargets] = {}
    for style, entry in styles.items():
        entry = entry or {}
        # A typo must not silently skip a bound.
        for key in entry:
            if key not in AXIS_KEYS:
                raise ValueError(f"{path}: {style}: unknown axis key {key}")
        loaded[str(style)] = StyleTargets(
            **{key: None if entry.get(key) is None else float(entry[key]) for key in entry}
        )
    return TargetsConfig(
        path=path,
        default_max_token_ratio=float(defaults["max_token_ratio"]),
        styles=loaded,
    )

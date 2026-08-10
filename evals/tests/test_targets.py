"""Tests for the regression-targets check. Everything is offline: the
fixtures write stored-shaped artifacts, and no test touches the
network."""

from __future__ import annotations

import json
from pathlib import Path

import pytest
import yaml

from targets import StyleTargets, TargetsConfig, check_run, cli, load_targets_config

HERE = Path(__file__).parent
RULES_DIR = HERE.parent / "rules"
TARGETS_CONFIG = RULES_DIR / "targets.yaml"


def write_run(
    tmp_path: Path,
    *,
    ratio: float = 0.9,
    fact_median: float = 0.8,
    hedge_median: float = 0.6,
    strength: float = 1.2,
    screening: dict | None = None,
    skip: tuple[str, ...] = (),
) -> Path:
    run_dir = tmp_path / "run"
    run_dir.mkdir(parents=True)
    files = {
        "provenance": {"styles": {"alpha": {"file": "alpha.md", "sha256": "s" * 8}}},
        "cost": {"answer_ratio": {"per_style": {"alpha": {"ratio_of_totals": ratio}}}},
        "loss": {
            "checks": {
                "completeness": {"per_style": {"alpha": {"median": fact_median}}},
                "hedging": {"per_style": {"alpha": {"median": hedge_median}}},
            }
        },
        "rank": {
            "bradley_terry": {
                "strengths": {"alpha": {"strength": strength}, "unstyled": {"strength": 1.0}}
            }
        },
    }
    if screening is not None:
        files["provenance"]["screening"] = screening
    for stem, content in files.items():
        if stem in skip:
            continue
        (run_dir / f"{stem}.json").write_text(json.dumps(content), encoding="utf-8")
    return run_dir


def write_drift(tmp_path: Path, *, slope: float = 0.0, skip_style: bool = False) -> Path:
    drift_dir = tmp_path / "drift"
    drift_dir.mkdir()
    (drift_dir / "provenance.json").write_text("{}", encoding="utf-8")
    styles = {} if skip_style else {"alpha": {"slope": slope}}
    (drift_dir / "drift.json").write_text(json.dumps({"styles": styles}), encoding="utf-8")
    return drift_dir


ALPHA_TARGETS = {
    "max_token_ratio": 1.0,
    "min_fact_survival": 0.7,
    "min_hedge_survival": 0.5,
    "min_rank_strength": 1.0,
    "max_drift_slope": 0.1,
}


def write_targets(tmp_path: Path, styles: dict | None = None, default: float = 1.1) -> Path:
    targets_file = tmp_path / "targets.yaml"
    content = {
        "defaults": {"max_token_ratio": default},
        "styles": styles or {"alpha": dict(ALPHA_TARGETS)},
    }
    targets_file.write_text(yaml.safe_dump(content), encoding="utf-8")
    return targets_file


def run_cli(run_dir: Path, targets_file: Path, drift_dir: Path | None = None) -> int:
    argv = [str(run_dir), "--targets", str(targets_file)]
    if drift_dir is not None:
        argv += ["--drift", str(drift_dir)]
    return cli.main(argv)


def summary_of(run_dir: Path) -> dict:
    return json.loads((run_dir / "targets.json").read_text(encoding="utf-8"))


def rows_by_axis(summary: dict, style: str = "alpha") -> dict[str, dict]:
    return {row["axis"]: row for row in summary["styles"][style]}


def test_targets_config_loads_bounds_per_style():
    config = load_targets_config(TARGETS_CONFIG)
    assert config.default_max_token_ratio > 0
    assert config.styles["plain-language"].max_token_ratio > 0
    assert config.styles["plain-language"].min_hedge_survival > 0


# The frozen field of #79. A candidate style has a rule file but no
# targets row: it runs under defaults.max_token_ratio until acceptance
# calibrates its row, so the covered set is the field, not the rule-file
# glob. An acceptance that adds a row re-opens the field on purpose and
# extends this constant in the same change.
FIELD_STYLES = {
    "clarity-flow",
    "classic-concise",
    "developer-docs",
    "plain-language",
    "technical-simplified",
}


def test_the_shipped_targets_file_covers_every_field_style():
    config = load_targets_config(TARGETS_CONFIG)
    rule_file_styles = {
        path.name.removesuffix(".rules.yaml") for path in RULES_DIR.glob("*.rules.yaml")
    }
    assert FIELD_STYLES <= rule_file_styles
    assert set(config.styles) == FIELD_STYLES
    for style, targets in config.styles.items():
        assert targets.max_token_ratio is not None, style
        assert targets.min_fact_survival is not None, style
        assert targets.min_hedge_survival is not None, style
        assert targets.min_rank_strength is not None, style
        assert targets.max_drift_slope is not None, style


def test_targets_config_rejects_a_file_without_styles(tmp_path):
    empty = tmp_path / "targets.yaml"
    empty.write_text("{}\n")
    with pytest.raises(ValueError, match="no styles"):
        load_targets_config(empty)


def test_targets_config_rejects_a_missing_default_bound(tmp_path):
    targets_file = tmp_path / "targets.yaml"
    targets_file.write_text(yaml.safe_dump({"styles": {"alpha": dict(ALPHA_TARGETS)}}))
    with pytest.raises(ValueError, match="defaults.max_token_ratio"):
        load_targets_config(targets_file)


def test_targets_config_rejects_an_unknown_axis_key(tmp_path):
    targets_file = write_targets(tmp_path, styles={"alpha": {"max_token_ration": 1.0}})
    with pytest.raises(ValueError, match="unknown axis key max_token_ration"):
        load_targets_config(targets_file)


def test_a_run_within_every_target_exits_0(tmp_path, capsys):
    run_dir = write_run(tmp_path)
    code = run_cli(run_dir, write_targets(tmp_path), write_drift(tmp_path))
    assert code == 0
    assert "alpha: 5/5 axes within targets" in capsys.readouterr().out
    assert summary_of(run_dir)["warnings"] == []


def test_a_token_ratio_past_the_bound_fails_and_exits_1(tmp_path):
    run_dir = write_run(tmp_path, ratio=1.01)
    code = run_cli(run_dir, write_targets(tmp_path), write_drift(tmp_path))
    assert code == 1
    row = rows_by_axis(summary_of(run_dir))["max_token_ratio"]
    assert row["verdict"] == "fail"
    assert row["observed"] == 1.01


def test_the_bound_boundary_is_inclusive(tmp_path):
    run_dir = write_run(tmp_path, ratio=1.0, fact_median=0.7, strength=1.0)
    code = run_cli(run_dir, write_targets(tmp_path), write_drift(tmp_path, slope=0.1))
    assert code == 0
    assert all(row["verdict"] == "pass" for row in summary_of(run_dir)["styles"]["alpha"])


def test_a_ratio_far_under_the_bound_earns_no_bonus(tmp_path):
    near = write_run(tmp_path / "near", ratio=1.0)
    far = write_run(tmp_path / "far", ratio=0.2)
    targets_file = write_targets(tmp_path)
    run_cli(near, targets_file, write_drift(tmp_path))
    run_cli(far, targets_file, tmp_path / "drift")
    near_row = rows_by_axis(summary_of(near))["max_token_ratio"]
    far_row = rows_by_axis(summary_of(far))["max_token_ratio"]
    assert near_row["verdict"] == far_row["verdict"] == "pass"
    assert set(near_row) == set(far_row)
    assert "note" not in far_row


def test_a_fact_survival_below_the_floor_fails(tmp_path):
    run_dir = write_run(tmp_path, fact_median=0.69)
    assert run_cli(run_dir, write_targets(tmp_path), write_drift(tmp_path)) == 1
    assert rows_by_axis(summary_of(run_dir))["min_fact_survival"]["verdict"] == "fail"


def test_a_hedge_survival_below_the_floor_fails(tmp_path):
    run_dir = write_run(tmp_path, hedge_median=0.49)
    assert run_cli(run_dir, write_targets(tmp_path), write_drift(tmp_path)) == 1
    assert rows_by_axis(summary_of(run_dir))["min_hedge_survival"]["verdict"] == "fail"


def test_a_rank_strength_below_the_floor_fails(tmp_path):
    run_dir = write_run(tmp_path, strength=0.99)
    assert run_cli(run_dir, write_targets(tmp_path), write_drift(tmp_path)) == 1
    assert rows_by_axis(summary_of(run_dir))["min_rank_strength"]["verdict"] == "fail"


def test_a_drift_slope_past_the_cap_fails(tmp_path):
    run_dir = write_run(tmp_path)
    code = run_cli(run_dir, write_targets(tmp_path), write_drift(tmp_path, slope=0.11))
    assert code == 1
    assert rows_by_axis(summary_of(run_dir))["max_drift_slope"]["verdict"] == "fail"


def test_a_missing_drift_run_skips_the_slope_with_a_warning(tmp_path):
    run_dir = write_run(tmp_path)
    code = run_cli(run_dir, write_targets(tmp_path))
    assert code == 1
    summary = summary_of(run_dir)
    row = rows_by_axis(summary)["max_drift_slope"]
    assert row["verdict"] == "skipped"
    assert row["note"] == "no drift run passed"
    assert any("drift-slope caps are unchecked" in warning for warning in summary["warnings"])


def test_a_style_missing_from_the_drift_run_warns(tmp_path):
    run_dir = write_run(tmp_path)
    code = run_cli(run_dir, write_targets(tmp_path), write_drift(tmp_path, skip_style=True))
    assert code == 1
    summary = summary_of(run_dir)
    assert rows_by_axis(summary)["max_drift_slope"]["verdict"] == "skipped"
    assert any("no observed max_drift_slope" in warning for warning in summary["warnings"])


def test_a_style_absent_from_targets_gets_the_default_token_bound(tmp_path, capsys):
    run_dir = write_run(tmp_path, ratio=1.05)
    targets_file = write_targets(tmp_path, styles={"beta": dict(ALPHA_TARGETS)}, default=1.1)
    code = run_cli(run_dir, targets_file)
    summary = summary_of(run_dir)
    rows = rows_by_axis(summary)
    token = rows["max_token_ratio"]
    assert token["verdict"] == "pass"
    assert token["limit"] == 1.1
    assert "default bound applies" in token["note"]
    assert all(rows[axis]["verdict"] == "skipped" for axis in rows if axis != "max_token_ratio")
    assert "alpha: 1/1 axes within targets" in capsys.readouterr().out
    # The exit is 1 through the beta warning below, not the bound.
    assert code == 1
    assert any("beta: in" in warning for warning in summary["warnings"])


def test_a_candidate_past_the_default_bound_fails(tmp_path):
    run_dir = write_run(tmp_path, ratio=1.11)
    targets_file = write_targets(tmp_path, styles={"beta": dict(ALPHA_TARGETS)}, default=1.1)
    assert run_cli(run_dir, targets_file) == 1
    assert rows_by_axis(summary_of(run_dir))["max_token_ratio"]["verdict"] == "fail"


def test_a_style_in_targets_but_absent_from_the_run_warns(tmp_path):
    run_dir = write_run(tmp_path)
    targets_file = write_targets(
        tmp_path, styles={"alpha": dict(ALPHA_TARGETS), "beta": dict(ALPHA_TARGETS)}
    )
    code = run_cli(run_dir, targets_file, write_drift(tmp_path))
    assert code == 1
    summary = summary_of(run_dir)
    assert "beta" not in summary["styles"]
    assert any("beta" in warning and "not in the run" in warning for warning in summary["warnings"])


def test_a_missing_artifact_warns_and_skips_its_axes(tmp_path):
    run_dir = write_run(tmp_path, skip=("loss",))
    code = run_cli(run_dir, write_targets(tmp_path), write_drift(tmp_path))
    assert code == 1
    summary = summary_of(run_dir)
    rows = rows_by_axis(summary)
    assert rows["min_fact_survival"]["verdict"] == "skipped"
    assert rows["min_fact_survival"]["note"] == "loss.json is missing"
    assert rows["min_hedge_survival"]["verdict"] == "skipped"
    assert rows["max_token_ratio"]["verdict"] == "pass"
    assert any("loss.json is missing" in warning for warning in summary["warnings"])


def test_a_screening_run_is_rejected(tmp_path):
    run_dir = write_run(tmp_path, screening={"prompts": 8})
    with pytest.raises(SystemExit) as excinfo:
        run_cli(run_dir, write_targets(tmp_path))
    assert excinfo.value.code == 2


def test_cli_rejects_a_directory_without_provenance(tmp_path):
    (tmp_path / "empty").mkdir()
    with pytest.raises(SystemExit) as excinfo:
        run_cli(tmp_path / "empty", write_targets(tmp_path))
    assert excinfo.value.code == 2


def test_cli_rejects_a_drift_directory_without_drift_data(tmp_path):
    run_dir = write_run(tmp_path)
    bare = tmp_path / "bare"
    bare.mkdir()
    (bare / "provenance.json").write_text("{}", encoding="utf-8")
    with pytest.raises(SystemExit) as excinfo:
        run_cli(run_dir, write_targets(tmp_path), bare)
    assert excinfo.value.code == 2


def test_cli_writes_targets_json_and_md_with_the_config_hash(tmp_path):
    run_dir = write_run(tmp_path)
    targets_file = write_targets(tmp_path)
    run_cli(run_dir, targets_file, write_drift(tmp_path))
    summary = summary_of(run_dir)
    assert summary["run"] == "run"
    assert summary["targets_config"]["file"] == str(targets_file)
    assert summary["targets_config"]["sha256"]
    assert summary["drift_run"] == "drift"
    report = (run_dir / "targets.md").read_text(encoding="utf-8")
    assert "# Regression targets report" in report
    assert "| max_token_ratio | max | 1 | 0.9 | pass |" in report


def test_cli_is_idempotent(tmp_path):
    run_dir = write_run(tmp_path)
    targets_file = write_targets(tmp_path)
    drift_dir = write_drift(tmp_path)
    run_cli(run_dir, targets_file, drift_dir)
    first_summary = summary_of(run_dir)
    first_report = (run_dir / "targets.md").read_text(encoding="utf-8")
    run_cli(run_dir, targets_file, drift_dir)
    second_summary = summary_of(run_dir)
    second_report = (run_dir / "targets.md").read_text(encoding="utf-8")
    assert first_report == second_report
    del first_summary["date"], second_summary["date"]
    assert first_summary == second_summary


def test_check_run_skips_an_axis_without_a_limit():
    run = {
        "name": "run",
        "provenance": {"styles": {"alpha": {}}},
        "cost": {"answer_ratio": {"per_style": {"alpha": {"ratio_of_totals": 0.9}}}},
        "loss": None,
        "rank": None,
    }
    partial = TargetsConfig(
        path=TARGETS_CONFIG,
        default_max_token_ratio=1.1,
        styles={"alpha": StyleTargets(max_token_ratio=1.0)},
    )
    result = check_run(run, partial, None)
    rows = {row["axis"]: row for row in result.styles["alpha"]}
    assert rows["max_token_ratio"]["verdict"] == "pass"
    assert rows["min_fact_survival"]["verdict"] == "skipped"
    assert rows["min_fact_survival"]["note"] == "no limit set"
    assert rows["max_drift_slope"]["note"] == "no limit set"

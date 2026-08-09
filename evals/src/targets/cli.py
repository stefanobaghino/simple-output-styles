"""The command-line interface of the regression-targets check.

Exit codes: 0 when every checked axis passes and no warnings exist, 1
when an axis fails or warnings exist, 2 when the run cannot be
checked at all.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from runner.provenance import sha256_of

from .check import check_run
from .config import load_targets_config
from .report import build_targets_report, build_targets_summary


def _fail(message: str) -> SystemExit:
    print(message, file=sys.stderr)
    return SystemExit(2)


def _load_json(path: Path) -> dict | None:
    if not path.exists():
        return None
    return json.loads(path.read_text(encoding="utf-8"))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="style-targets",
        description=(
            "Check the stored artifacts of a run against the regression "
            "targets: the pre-committed numbers a style version must "
            "hold. A drift run supplies the drift-slope axis."
        ),
    )
    parser.add_argument("run_dir", help="the run directory with the stored artifacts")
    parser.add_argument("--targets", default="rules/targets.yaml", help="the targets file")
    parser.add_argument("--drift", help="the drift run directory for the slope axis")
    args = parser.parse_args(argv)

    run_dir = Path(args.run_dir)
    provenance = _load_json(run_dir / "provenance.json")
    if provenance is None:
        raise _fail(f"{run_dir}: no provenance.json, so the directory is not a run")
    # A screening run covers a prompt subset and one run, so its
    # numbers cannot demonstrate that a target holds. The mismatch is
    # a hard stop, not a warning, like the screening rule of the
    # cross-run comparison.
    if "screening" in provenance:
        raise _fail(f"{run_dir}: a screening run cannot demonstrate a target")
    run = {"name": run_dir.name, "provenance": provenance}
    for artifact in ("cost", "loss", "rank"):
        run[artifact] = _load_json(run_dir / f"{artifact}.json")

    try:
        config = load_targets_config(args.targets)
    except (OSError, ValueError) as error:
        raise _fail(str(error)) from error

    drift = None
    drift_run = None
    if args.drift:
        drift_dir = Path(args.drift)
        if _load_json(drift_dir / "provenance.json") is None:
            raise _fail(f"{drift_dir}: no provenance.json, so the directory is not a run")
        drift = _load_json(drift_dir / "drift.json")
        if drift is None:
            raise _fail(f"{drift_dir}: no drift.json, so the directory is not a drift run")
        drift_run = drift_dir.name

    result = check_run(run, config, drift)
    if not result.styles:
        raise _fail(f"{run_dir}: the run holds no styled artifacts")

    summary = build_targets_summary(
        styles=result.styles,
        run_name=run_dir.name,
        targets_config_hash={"file": str(config.path), "sha256": sha256_of(config.path)},
        drift_run=drift_run,
        warnings=result.warnings,
    )
    (run_dir / "targets.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    (run_dir / "targets.md").write_text(build_targets_report(summary), encoding="utf-8")

    all_pass = True
    for style, rows in result.styles.items():
        checked = [r for r in rows if r["verdict"] != "skipped"]
        passed = [r for r in checked if r["verdict"] == "pass"]
        all_pass = all_pass and len(passed) == len(checked)
        print(f"{style}: {len(passed)}/{len(checked)} axes within targets")
    return 0 if all_pass and not result.warnings else 1


if __name__ == "__main__":
    sys.exit(main())

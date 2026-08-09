"""The command-line interface of the second-judge agreement sample.

Every stored verdict of a run comes from one judge model, and the
style-design loop optimizes against those verdicts, so a
judge-specific verdict is a standing risk (#81). This tool re-runs
stored discrete verdicts with a second judge model and reports the
agreement rate per axis, so a judge-sensitive axis is visible before
the loop optimizes against it. Two arms exist by convention: a
cross-line arm (a weaker Claude line, a lower bound, because its
disagreement mixes ambiguity with capability) and a cross-vintage
arm (an older model of the first-judge line, capability-matched, so
its disagreement measures what a model update would move). Every
judge runs through the Claude CLI, so a second judge is a different
Claude line or vintage, never a different vendor; the human spot
check stays the cross-vendor anchor.

The tool rebuilds each judged prompt from the stored rows, with the
joins the scorers already perform and the original prompt templates,
so the second judge answers the exact stored question. The second
verdicts land in one raw file per arm, named by the requested model,
so every raw file stays single-model. The scoring is offline and
reads every arm file of the run.

Exit codes: 0 when the arms are scored and no warnings exist, 1 when
warnings exist (an axis under the agreement anchor, an unusable
second output, an incomplete arm), 2 when the run cannot be scored
at all.
"""

from __future__ import annotations

import argparse
import json
import random
import re
import sys
from datetime import UTC, datetime
from functools import partial
from pathlib import Path

from gate.cli import load_answers, run_provenance
from loss.judges import (
    CLAIMS_CHECK_PROMPT,
    FACTS_CHECK_PROMPT,
    parse_string_list,
    parse_verdicts,
)

# The private prompt builders import on purpose: the rebuilt prompt
# must be byte-identical to the prompt of the stored call.
from loss.judges import _numbered  # isort: skip
from rank.analysis import UNSTYLED
from rank.judges import CLARITY_PROMPT, parse_pick
from runner.generate import ISOLATION_FLAGS, GenerationError, Runner, subprocess_runner
from runner.hermetic import CONFIG_MODE, hermetic_call, manifest_sha256
from runner.provenance import claude_version, sha256_of
from runner.screening import screening_section
from runner.spend import spend_section, spend_summary
from runner.timing import timing_section, timing_summary
from value.analysis import select_pairs, shared_facts
from value.cli import answer_index, load_fidelity, load_raw, reconcile_meta, resolved_models
from value.judges import (
    GRADES_PROMPT,
    JUDGE_MODEL_PINS,
    JudgeSession,
    TaskPool,
    _grade_items,
    judge_prompts_sha256,
    parse_bools,
    parse_strings,
    select_balanced,
)

AXES = ("comprehension", "completeness", "hedging", "clarity")
"""The verdict axes, in report order."""

ANCHOR = 0.7
"""The agreement rate under which an axis is judge-sensitive.

The value is the documented acceptance anchor of the human spot
check, so the model-to-model bar equals the human-to-model bar.
"""

SAMPLE_SEED = 0
"""The fixed seed of the --sample draw, the spot-check precedent."""

SOURCE_FILES = ("value-raw.jsonl", "loss-raw.jsonl", "rank-raw.jsonl")
"""The raw files whose discrete verdicts this tool compares."""

AGREEMENT_PROMPTS_SHA256 = judge_prompts_sha256(
    {
        "grades": GRADES_PROMPT,
        "facts_check": FACTS_CHECK_PROMPT,
        "claims_check": CLAIMS_CHECK_PROMPT,
        "clarity": CLARITY_PROMPT,
    }
)
"""One hash over the reused verdict templates, stored in the meta row."""

META_MATCH_KEYS = ("model", "sample", "answers_sha256", "judge_prompts_sha256")


def _fail(message: str) -> SystemExit:
    print(message, file=sys.stderr)
    return SystemExit(2)


def model_slug(model: str) -> str:
    """The file-name part of an arm: the requested model, slugged."""
    return re.sub(r"[^a-z0-9.-]+", "-", model.lower())


def arm_raw_name(model: str) -> str:
    """The raw file of one arm, so every raw file stays single-model."""
    return f"agreement-{model_slug(model)}-raw.jsonl"


def build_meta(
    *,
    model: str,
    sample: int | None,
    answers_sha256: str,
    source_sha256s: dict[str, str],
    cli_version: str | None = None,
) -> dict:
    return {
        "type": "meta",
        "date": datetime.now(UTC).isoformat(timespec="seconds"),
        "claude_version": cli_version,
        "config": CONFIG_MODE,
        "config_manifest_sha256": manifest_sha256(),
        "model": model,
        "sample": sample,
        "judge_prompts_sha256": AGREEMENT_PROMPTS_SHA256,
        "source_sha256s": source_sha256s,
        "flags": list(ISOLATION_FLAGS),
        "answers_sha256": answers_sha256,
    }


def build_units(
    *,
    pairs: dict[str, list[str]],
    index: dict[tuple[str, str | None], dict],
    value_meta: dict,
    value_rows: dict[str, dict],
    loss_rows: dict[str, dict],
    rank_rows: dict[str, dict],
) -> tuple[list[dict], dict[str, int]]:
    """The comparable stored verdicts of a run, with rebuilt prompts.

    A unit is one stored verdict row plus the prompt that produced
    it, rebuilt from the stored rows with the joins the scorers
    already perform, and the parser of its verdict family. A row
    whose rebuild fails — a missing join row, or an unparseable
    output on the join path or in the row itself — carries no
    verdict to agree with, so it stays out, counted per axis. The
    extraction and free-text rows stay out by design, like in the
    freshness sample: an equality comparison of free text means
    nothing.
    """
    units: list[dict] = []
    skipped: dict[str, int] = dict.fromkeys(AXES, 0)

    facts_by_pair, _ = shared_facts(pairs, index, loss_rows)
    for key in sorted(value_rows):
        if not key.startswith("comprehension:v3:grades:"):
            continue
        parts = key.split(":")
        if len(parts) != 7:
            skipped["comprehension"] += 1
            continue
        style, prompt_id, reader_arm, replicate = parts[3], parts[4], parts[5], parts[6]
        row = value_rows[key]
        survivors = facts_by_pair.get((style, prompt_id))
        questions_row = value_rows.get(f"comprehension:v3:questions:{style}:{prompt_id}")
        reader_row = value_rows.get(
            f"comprehension:v3:reader:{style}:{prompt_id}:{reader_arm}:{replicate}"
        )
        if survivors is None or questions_row is None or reader_row is None:
            skipped["comprehension"] += 1
            continue
        facts, _ = select_balanced(
            survivors["unstyled"], survivors["styled"], value_meta["questions"]
        )
        questions = parse_strings(questions_row["output"], len(facts))
        replies = parse_strings(reader_row["output"], len(questions)) if questions else None
        stored = parse_bools(row["output"], len(questions)) if questions else None
        if questions is None or replies is None or stored is None:
            skipped["comprehension"] += 1
            continue
        references = [
            {"question": question, "reference": fact}
            for question, fact in zip(questions, facts, strict=True)
        ]
        units.append(
            {
                "key": key,
                "axis": "comprehension",
                "styles": [style],
                "prompt_id": row.get("prompt_id", prompt_id),
                "answer_sha256": row.get("answer_sha256"),
                "prompt": GRADES_PROMPT.format(items=_grade_items(references, replies)),
                "parse": partial(parse_bools, n=len(questions)),
                "stored": stored,
            }
        )

    # Two pairs with byte-identical styled texts share a check key,
    # so the seen set keeps each key one unit, and every style behind
    # the key lands in the styles list.
    seen: set[str] = set()
    by_key: dict[str, dict] = {}
    for style in sorted(pairs):
        for prompt_id in pairs[style]:
            styled = index[(prompt_id, style)]
            unstyled = index[(prompt_id, None)]
            entries = (
                (
                    "completeness",
                    f"completeness:check:{styled['sha256']}",
                    f"completeness:facts:{unstyled['sha256']}",
                    styled,
                    FACTS_CHECK_PROMPT,
                    parse_bools,
                ),
                (
                    "completeness",
                    f"completeness:reverse:{styled['sha256']}",
                    f"completeness:facts:{styled['sha256']}",
                    unstyled,
                    FACTS_CHECK_PROMPT,
                    parse_bools,
                ),
                (
                    "hedging",
                    f"hedging:check:{styled['sha256']}",
                    f"hedging:claims:{unstyled['sha256']}",
                    styled,
                    CLAIMS_CHECK_PROMPT,
                    parse_verdicts,
                ),
            )
            for axis, key, items_key, checked, template, parser in entries:
                if key in seen:
                    existing = by_key.get(key)
                    if existing is not None and style not in existing["styles"]:
                        existing["styles"].append(style)
                    continue
                seen.add(key)
                row = loss_rows.get(key)
                if row is None:
                    # An empty extraction has no check row; nothing
                    # to compare and nothing to count.
                    continue
                items_row = loss_rows.get(items_key)
                items = parse_string_list(items_row["output"]) if items_row else None
                stored = parser(row["output"], len(items)) if items else None
                if not items or stored is None:
                    skipped[axis] += 1
                    continue
                unit = {
                    "key": key,
                    "axis": axis,
                    "styles": [style],
                    "prompt_id": row.get("prompt_id", prompt_id),
                    "answer_sha256": checked["sha256"],
                    "prompt": template.format(text=checked["text"], claims=_numbered(items)),
                    "parse": partial(parser, n=len(items)),
                    "stored": stored,
                }
                by_key[key] = unit
                units.append(unit)

    text_by_sha = {arm["sha256"]: arm["text"] for arm in index.values()}
    for key in sorted(rank_rows):
        if not key.startswith("clarity:"):
            continue
        row = rank_rows[key]
        first_text = text_by_sha.get(row.get("first_sha256"))
        second_text = text_by_sha.get(row.get("second_sha256"))
        stored = parse_pick(str(row.get("output", "")))
        if first_text is None or second_text is None or stored is None:
            skipped["clarity"] += 1
            continue
        styles = [
            name for name in (row.get("first"), row.get("second")) if name and name != UNSTYLED
        ]
        units.append(
            {
                "key": key,
                "axis": "clarity",
                "styles": styles,
                "prompt_id": row.get("prompt_id"),
                "answer_sha256": None,
                "prompt": CLARITY_PROMPT.format(first=first_text, second=second_text),
                "parse": parse_pick,
                "stored": stored,
            }
        )
    return units, skipped


def sample_keys(units: list[dict], sample: int | None) -> set[str]:
    """The unit keys of a pass: everything, or a seed-0 draw per axis.

    One shared seeded generator draws the axes in sorted order, so
    the draw is deterministic over the same stored rows. The census
    is everything, so a sampled arm compares a subset of the census
    keys by construction.
    """
    if sample is None:
        return {unit["key"] for unit in units}
    keys_by_axis: dict[str, list[str]] = {}
    for unit in units:
        keys_by_axis.setdefault(unit["axis"], []).append(unit["key"])
    rng = random.Random(SAMPLE_SEED)
    selected: set[str] = set()
    for axis in sorted(keys_by_axis):
        keys = sorted(keys_by_axis[axis])
        selected.update(rng.sample(keys, min(sample, len(keys))))
    return selected


def _pin_resolved(alias: str) -> str:
    return JUDGE_MODEL_PINS.get(alias, alias)


def _check_judge_constraints(
    model: str, provenance: dict | None, first_judges: dict[str, str]
) -> list[str]:
    """Stop when the second judge equals the writer or a first judge.

    The comparison runs on the requested alias and on the pinned
    resolution, so an exact ID cannot dodge an aliased pin.
    """
    warnings = []
    writer = (provenance or {}).get("conditions", {}).get("model_requested")
    if writer is None:
        warnings.append(
            "no provenance.json with a model: the judge-differs-from-writer rule is unchecked"
        )
    elif model == writer or _pin_resolved(model) == _pin_resolved(writer):
        raise _fail(
            f"the second judge {model!r} equals the writer model of the run; "
            "the judges must differ from the writer"
        )
    for axis in AXES:
        first = first_judges[axis]
        if model == first or _pin_resolved(model) == _pin_resolved(first):
            raise _fail(
                f"the second judge {model!r} equals the first judge {first!r} of the "
                f"{axis} axis; the second judge must add another model line or vintage"
            )
    return warnings


def _judge_unit(session: JudgeSession, unit: dict, model: str) -> None:
    """One second-judge call, one task."""
    verdict = session.structured(
        validate=unit["parse"],
        key=unit["key"],
        check=unit["axis"],
        role="agreement",
        model=model,
        prompt=unit["prompt"],
        prompt_id=unit["prompt_id"],
        answer_sha256=unit["answer_sha256"],
    )
    if verdict is None:
        session.warnings.append(
            f"{unit['key']}: the second judge gave no usable verdict, "
            "so the unit counts as unusable"
        )


def _judge(
    args, run_dir: Path, units: list[dict], first_judges: dict[str, str], run: Runner
) -> list[str]:
    """Run the live second-judge calls of one arm. Returns the warnings."""
    warnings = _check_judge_constraints(args.model, run_provenance(run_dir), first_judges)
    raw_path = run_dir / arm_raw_name(args.model)
    meta_stored, rows = load_raw(raw_path)
    with hermetic_call("judge-agreement") as hermetic:
        meta = build_meta(
            model=args.model,
            sample=args.sample,
            answers_sha256=sha256_of(run_dir / "answers.jsonl"),
            source_sha256s={name: sha256_of(run_dir / name) for name in SOURCE_FILES},
            cli_version=claude_version(hermetic.binary, hermetic.env),
        )
        if meta_stored is not None:
            meta, _ = reconcile_meta(
                meta,
                meta_stored,
                match_keys=META_MATCH_KEYS,
                upgrade_keys=(),
                filename=raw_path.name,
            )

        with raw_path.open("a", encoding="utf-8") as raw_file:
            if meta_stored is None:
                raw_file.write(json.dumps(meta, ensure_ascii=False) + "\n")
                raw_file.flush()

            def sink(row: dict) -> None:
                raw_file.write(json.dumps(row, ensure_ascii=False) + "\n")
                raw_file.flush()

            session = JudgeSession(
                rows=rows, sink=sink, workdir=hermetic.workdir, run=run, env=hermetic.env
            )
            pool = TaskPool(args.parallel)
            selected = sample_keys(units, args.sample)
            for unit in units:
                if unit["key"] in selected:
                    pool.submit(partial(_judge_unit, session, unit, meta["model"]))
            try:
                pool.drain()
            except GenerationError as error:
                raise _fail(f"a judge call failed: {error}") from error
            warnings += session.warnings
    return warnings


def score_arm(units: list[dict], meta: dict, rows: dict[str, dict]) -> tuple[dict, list[str]]:
    """The agreement of one arm against the stored verdicts. Pure.

    The agreement unit is one discrete verdict: one graded quiz item,
    one checked fact, one checked claim, or one contest pick. The
    expected keys come from the sample spec of the arm's meta row, so
    an interrupted pass shows up as not-judged units instead of a
    silently smaller denominator.
    """
    expected = sample_keys(units, meta.get("sample"))
    axes: dict[str, dict] = {
        axis: {"rows": 0, "items": 0, "agreements": 0, "unusable": 0, "not_judged": 0}
        for axis in AXES
    }
    per_style: dict[str, dict[str, dict]] = {axis: {} for axis in AXES}
    for unit in units:
        if unit["key"] not in expected:
            continue
        stats = axes[unit["axis"]]
        row = rows.get(unit["key"])
        if row is None:
            stats["not_judged"] += 1
            continue
        second = unit["parse"](row["output"])
        if second is None:
            stats["unusable"] += 1
            continue
        stored = unit["stored"]
        if isinstance(stored, list):
            items = len(stored)
            agreements = sum(
                1 for mine, theirs in zip(stored, second, strict=True) if mine == theirs
            )
        else:
            items, agreements = 1, int(stored == second)
        stats["rows"] += 1
        stats["items"] += items
        stats["agreements"] += agreements
        for style in unit["styles"]:
            entry = per_style[unit["axis"]].setdefault(style, {"items": 0, "agreements": 0})
            entry["items"] += items
            entry["agreements"] += agreements
    warnings = []
    model = meta["model"]
    for axis, stats in axes.items():
        stats["rate"] = round(stats["agreements"] / stats["items"], 3) if stats["items"] else None
        stats["judge_sensitive"] = stats["rate"] is not None and stats["rate"] < ANCHOR
        if stats["judge_sensitive"]:
            warnings.append(
                f"{model}: the {axis} axis agrees at {stats['rate']}, under the {ANCHOR} "
                "anchor, so the axis is judge-sensitive for this arm"
            )
        if stats["unusable"]:
            warnings.append(
                f"{model}: {stats['unusable']} second verdicts of the {axis} axis are unusable"
            )
        if stats["not_judged"]:
            warnings.append(
                f"{model}: {stats['not_judged']} units of the {axis} axis are not judged "
                f"yet; run --judge --model {model} again"
            )
    for styles in per_style.values():
        for entry in styles.values():
            entry["rate"] = (
                round(entry["agreements"] / entry["items"], 3) if entry["items"] else None
            )
    arm = {
        "model": model,
        "model_resolved": resolved_models(rows).get(model),
        "sample": meta.get("sample"),
        "judged_date": meta.get("date"),
        "claude_version": meta.get("claude_version"),
        "judge_prompts_sha256": meta.get("judge_prompts_sha256"),
        "axes": axes,
        "per_style": per_style,
    }
    return arm, warnings


def _value(value) -> str:
    return "n/a" if value is None else str(value)


def _demote(lines: list[str]) -> list[str]:
    """A shared section, one level deeper, so each arm holds its own."""
    return [f"#{line}" if line.startswith("## ") else line for line in lines]


def build_agreement_report(
    summary: dict,
    arm_extras: list[tuple[dict | None, dict | None]],
    screening: list[str] | None = None,
) -> str:
    lines = [
        "# Second-judge agreement report",
        "",
        *(screening or []),
        "Every stored verdict of a run comes from one judge model, and",
        "the style-design loop optimizes against those verdicts. This",
        "report re-runs stored discrete verdicts with a second judge",
        "and states the agreement rate per axis, so a judge-sensitive",
        "axis is visible before the loop optimizes against it.",
        "",
        "How to read the arms: a cross-line arm (a weaker Claude line)",
        "is a lower bound, because its disagreement mixes genuine",
        "ambiguity with weaker capability. A cross-vintage arm (an",
        "older model of the first-judge line) is capability-matched,",
        "so its disagreement measures what a model update would move.",
        "An axis where only the cross-line arm disagrees points at",
        "capability; an axis where both arms disagree is",
        "judge-sensitive.",
        "",
        "The agreement unit is one discrete verdict: one graded quiz",
        "item, one checked fact, one checked claim, or one contest",
        f"pick. An axis under {ANCHOR} — the acceptance anchor of the human",
        "spot check — is marked judge-sensitive and warns. Every judge",
        "runs through the Claude CLI, so a second judge is a different",
        "Claude line or vintage, never a different vendor; the human",
        "spot check stays the cross-vendor anchor. On the",
        "comprehension axis, a cross-line grader can share the model",
        "line of the original reader, so leniency toward the reader's",
        "phrasing is possible; the cross-vintage arm is the cleaner",
        "signal there.",
        "",
        "First judges: "
        + ", ".join(f"{axis} {model}" for axis, model in summary["first_judges"].items())
        + ".",
        "",
        "## Enumerated units",
        "",
        "| Axis | Units | Skipped stored |",
        "|---|---|---|",
    ]
    for axis in AXES:
        lines.append(f"| {axis} | {summary['units'][axis]} | {summary['skipped_stored'][axis]} |")
    lines += [
        "",
        "A skipped stored row has no rebuildable verdict: a missing",
        "join row or an unparseable output on the join path.",
        "",
    ]
    for arm, (timing, spend) in zip(summary["arms"], arm_extras, strict=True):
        sample = "everything" if arm["sample"] is None else f"{arm['sample']} per axis (seed 0)"
        lines += [
            f"## Arm: {arm['model']}",
            "",
            f"Resolved model: {_value(arm['model_resolved'])}. Sample: {sample}.",
            f"Judged on {arm['judged_date']}.",
            "",
            "| Axis | Rows | Items | Agreements | Rate | Unusable | Not judged | Judge-sensitive |",
            "|---|---|---|---|---|---|---|---|",
        ]
        for axis, stats in arm["axes"].items():
            sensitive = "yes" if stats["judge_sensitive"] else "no"
            lines.append(
                f"| {axis} | {stats['rows']} | {stats['items']} | {stats['agreements']} "
                f"| {_value(stats['rate'])} | {stats['unusable']} | {stats['not_judged']} "
                f"| {sensitive} |"
            )
        lines += [
            "",
            "Per style (a style-specific disagreement is what the",
            "shared-bias risk predicts):",
            "",
            "| Axis | Style | Items | Agreements | Rate |",
            "|---|---|---|---|---|",
        ]
        for axis, styles in arm["per_style"].items():
            for style in sorted(styles):
                entry = styles[style]
                lines.append(
                    f"| {axis} | {style} | {entry['items']} | {entry['agreements']} "
                    f"| {_value(entry['rate'])} |"
                )
        lines.append("")
        lines += _demote(timing_section(timing))
        lines += _demote(spend_section(spend))
    lines += ["## Warnings", ""]
    lines += [f"- {warning}" for warning in summary["warnings"]] or ["- none"]
    lines.append("")
    return "\n".join(lines)


def main(argv: list[str] | None = None, run: Runner = subprocess_runner) -> int:
    parser = argparse.ArgumentParser(
        prog="style-agreement",
        description=(
            "Re-run the stored discrete verdicts of a run with a second "
            "judge model and report the agreement rate per axis. The "
            "prompts rebuild from the stored rows, so the second judge "
            "answers the exact stored question. Each arm lands in its "
            "own raw file, and the scoring reads every arm of the run."
        ),
    )
    parser.add_argument("run_dir", help="the run directory with the stored judge raw files")
    parser.add_argument(
        "--judge", action="store_true", help="run the live second-judge calls first"
    )
    parser.add_argument(
        "--model",
        default="haiku",
        help="the second judge: a pin-table alias or an exact model ID",
    )
    parser.add_argument(
        "--sample",
        type=int,
        default=None,
        help="seed-0 subsample size per axis (the default judges everything)",
    )
    parser.add_argument(
        "--parallel",
        type=int,
        default=8,
        help="concurrent judge calls (1 runs one call at a time)",
    )
    args = parser.parse_args(argv)

    if args.parallel < 1:
        raise _fail(f"--parallel must be 1 or more, not {args.parallel}")
    if args.sample is not None and args.sample < 1:
        raise _fail(f"--sample must be 1 or more, not {args.sample}")

    run_dir = Path(args.run_dir)
    answers = load_answers(run_dir / "answers.jsonl")
    index = answer_index(answers)
    answer_shas = {key: arm["sha256"] for key, arm in index.items()}
    fidelity_rows = load_fidelity(run_dir / "fidelity.jsonl")
    pairs, pair_warnings = select_pairs(fidelity_rows, answer_shas)

    metas: dict[str, dict] = {}
    rows_by_file: dict[str, dict[str, dict]] = {}
    for name in SOURCE_FILES:
        path = run_dir / name
        meta, rows = load_raw(path)
        if meta is None:
            raise _fail(f"{path}: the run holds no judge data; judge the run first")
        metas[name], rows_by_file[name] = meta, rows

    first_judges = {
        "comprehension": metas["value-raw.jsonl"]["models"]["grader"],
        "completeness": metas["loss-raw.jsonl"]["model"],
        "hedging": metas["loss-raw.jsonl"]["model"],
        "clarity": metas["rank-raw.jsonl"]["model"],
    }
    units, skipped = build_units(
        pairs=pairs,
        index=index,
        value_meta=metas["value-raw.jsonl"],
        value_rows=rows_by_file["value-raw.jsonl"],
        loss_rows=rows_by_file["loss-raw.jsonl"],
        rank_rows=rows_by_file["rank-raw.jsonl"],
    )
    if not units:
        raise _fail(f"{run_dir}: no stored verdict is rebuildable, so there is nothing to compare")

    judge_warnings: list[str] = []
    if args.judge:
        judge_warnings = _judge(args, run_dir, units, first_judges, run)

    arm_paths = sorted(run_dir.glob("agreement-*-raw.jsonl"))
    if not arm_paths:
        raise _fail(f"{run_dir}: no agreement data; run style-agreement {run_dir} --judge")

    arms: list[dict] = []
    arm_extras: list[tuple[dict | None, dict | None]] = []
    score_warnings: list[str] = []
    for path in arm_paths:
        arm_meta, arm_rows = load_raw(path)
        if arm_meta is None:
            raise _fail(f"{path}: the arm file holds no meta row; remove the file and judge again")
        arm, warnings = score_arm(units, arm_meta, arm_rows)
        arms.append(arm)
        arm_extras.append((timing_summary(arm_rows.values()), spend_summary(arm_rows.values())))
        score_warnings += warnings

    warnings = pair_warnings + judge_warnings + score_warnings
    summary = {
        "date": datetime.now(UTC).isoformat(timespec="seconds"),
        "run": run_dir.name,
        "anchor": ANCHOR,
        "first_judges": first_judges,
        "units": {axis: sum(1 for unit in units if unit["axis"] == axis) for axis in AXES},
        "skipped_stored": skipped,
        "arms": arms,
        "warnings": warnings,
    }
    (run_dir / "agreement.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    report = build_agreement_report(
        summary, arm_extras, screening=screening_section(run_provenance(run_dir))
    )
    (run_dir / "agreement.md").write_text(report, encoding="utf-8")

    for arm in arms:
        parts = [f"{axis} {_value(arm['axes'][axis]['rate'])}" for axis in AXES]
        print(f"{arm['model']}: " + ", ".join(parts) + " (agreement rate)")
    return 0 if not warnings else 1


if __name__ == "__main__":
    sys.exit(main())

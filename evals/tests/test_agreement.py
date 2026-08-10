"""Tests for the second-judge agreement sample. No test touches the
network: the claude subprocess is replaced with fake runners that
return canned stream-json output."""

import hashlib
import json
import threading

import pytest

from agreement import ANCHOR, arm_raw_name, build_units, cli, sample_keys, score_arm
from runner.provenance import CLI_VERSION_PIN
from value.judges import JUDGE_MODEL_PINS

UNSTYLED_TEXT = "The turtle statement holds three facts and one hedge."
ALPHA_TEXT = "The fox statement keeps two facts and the hedge."

UNSTYLED_FACTS = ["Fact one.", "Fact two.", "Fact three."]
FORWARD_MARKS = [True, True, False]
ALPHA_FACTS = ["Alpha fact."]
REVERSE_MARKS = [True]
CLAIMS = ["It may rain."]
CLAIM_VERDICTS = ["hedged"]
QUESTIONS = ["Q one?", "Q two?", "Q three?"]
STYLED_REPLIES = ["A one", "A two", "A three"]
UNSTYLED_REPLIES = ["B one", "B two", "B three"]
STYLED_GRADES = [True, False, True]
UNSTYLED_GRADES = [True, True, True]


def sha(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def stream(result_text, requested_model):
    resolved = JUDGE_MODEL_PINS.get(requested_model, requested_model)
    init = {
        "type": "system",
        "subtype": "init",
        "output_style": "default",
        "model": resolved,
    }
    result = {
        "type": "result",
        "is_error": False,
        "result": result_text,
        "usage": {
            "output_tokens": 5,
            "input_tokens": 3,
            "cache_creation_input_tokens": 2,
            "cache_read_input_tokens": 1,
        },
        "duration_ms": 10,
    }
    return "\n".join(json.dumps(event) for event in (init, result))


def write_jsonl(path, rows):
    with path.open("w", encoding="utf-8") as file:
        for row in rows:
            file.write(json.dumps(row) + "\n")


def loss_fixture_rows():
    a, u = sha(ALPHA_TEXT), sha(UNSTYLED_TEXT)
    return [
        {"type": "meta", "model": "opus", "fact_mine": "two-way", "date": "2026-08-08"},
        {"type": "call", "key": f"completeness:facts:{u}", "output": json.dumps(UNSTYLED_FACTS)},
        {
            "type": "call",
            "key": f"completeness:check:{a}",
            "prompt_id": "explanation-01",
            "answer_sha256": a,
            "output": json.dumps(FORWARD_MARKS),
        },
        {"type": "call", "key": f"completeness:facts:{a}", "output": json.dumps(ALPHA_FACTS)},
        {
            "type": "call",
            "key": f"completeness:reverse:{a}",
            "prompt_id": "explanation-01",
            "answer_sha256": u,
            "output": json.dumps(REVERSE_MARKS),
        },
        {"type": "call", "key": f"hedging:claims:{u}", "output": json.dumps(CLAIMS)},
        {
            "type": "call",
            "key": f"hedging:check:{a}",
            "prompt_id": "explanation-01",
            "answer_sha256": a,
            "output": json.dumps(CLAIM_VERDICTS),
        },
    ]


def value_fixture_rows():
    a, u = sha(ALPHA_TEXT), sha(UNSTYLED_TEXT)
    return [
        {
            "type": "meta",
            "models": {"reader": "haiku", "grader": "opus"},
            "questions": 6,
            "paraphrases": 3,
            "replicates": 1,
            "date": "2026-08-08",
        },
        {
            "type": "call",
            "key": "comprehension:v3:questions:alpha:explanation-01",
            "output": json.dumps(QUESTIONS),
        },
        {
            "type": "call",
            "key": "comprehension:v3:reader:alpha:explanation-01:styled:0",
            "output": json.dumps(STYLED_REPLIES),
        },
        {
            "type": "call",
            "key": "comprehension:v3:grades:alpha:explanation-01:styled:0",
            "prompt_id": "explanation-01",
            "answer_sha256": a,
            "output": json.dumps(STYLED_GRADES),
        },
        {
            "type": "call",
            "key": "comprehension:v3:reader:alpha:explanation-01:unstyled:0",
            "output": json.dumps(UNSTYLED_REPLIES),
        },
        {
            "type": "call",
            "key": "comprehension:v3:grades:alpha:explanation-01:unstyled:0",
            "prompt_id": "explanation-01",
            "answer_sha256": u,
            "output": json.dumps(UNSTYLED_GRADES),
        },
    ]


def rank_fixture_rows():
    a, u = sha(ALPHA_TEXT), sha(UNSTYLED_TEXT)
    return [
        {"type": "meta", "model": "opus", "date": "2026-08-08"},
        {
            "type": "call",
            "key": f"clarity:explanation-01:{a}:{u}",
            "prompt_id": "explanation-01",
            "first": "alpha",
            "second": "unstyled",
            "first_sha256": a,
            "second_sha256": u,
            "output": "1",
        },
        {
            "type": "call",
            "key": f"clarity:explanation-01:{u}:{a}",
            "prompt_id": "explanation-01",
            "first": "unstyled",
            "second": "alpha",
            "first_sha256": u,
            "second_sha256": a,
            "output": "2",
        },
    ]


def make_project(tmp_path):
    """One gated pair with stored verdicts on every axis."""
    run_dir = tmp_path / "run"
    run_dir.mkdir()
    answers = [
        {"prompt_id": "explanation-01", "style": None, "answer": UNSTYLED_TEXT},
        {"prompt_id": "explanation-01", "style": "alpha", "answer": ALPHA_TEXT},
    ]
    fidelity = [
        {
            "prompt_id": "explanation-01",
            "style": None,
            "pass": None,
            "answer_sha256": sha(UNSTYLED_TEXT),
        },
        {
            "prompt_id": "explanation-01",
            "style": "alpha",
            "pass": True,
            "answer_sha256": sha(ALPHA_TEXT),
        },
    ]
    write_jsonl(run_dir / "answers.jsonl", answers)
    write_jsonl(run_dir / "fidelity.jsonl", fidelity)
    (run_dir / "provenance.json").write_text(
        json.dumps({"conditions": {"model_requested": "sonnet"}})
    )
    write_jsonl(run_dir / "value-raw.jsonl", value_fixture_rows())
    write_jsonl(run_dir / "loss-raw.jsonl", loss_fixture_rows())
    write_jsonl(run_dir / "rank-raw.jsonl", rank_fixture_rows())
    return tmp_path


@pytest.fixture
def project(tmp_path):
    return make_project(tmp_path)


def numbered_count(prompt):
    """The count of the numbered items after the Claims heading."""
    _, _, tail = prompt.partition("Claims:")
    return sum(1 for line in tail.splitlines() if line.strip()[:2] in ("1.", "2.", "3."))


class EchoRunner:
    """Repeats every stored verdict, so every arm fully agrees."""

    def __init__(self):
        self.calls = []
        self.lock = threading.Lock()

    def __call__(self, argv, cwd, env=None):
        with self.lock:
            self.calls.append(argv)
            prompt = argv[argv.index("-p") + 1]
            model = argv[argv.index("--model") + 1]
            return stream(self.reply(prompt), model)

    def reply(self, prompt):
        if prompt.startswith("Grade the quiz answers"):
            replies = STYLED_REPLIES if STYLED_REPLIES[0] in prompt else UNSTYLED_REPLIES
            return json.dumps(STYLED_GRADES if replies is STYLED_REPLIES else UNSTYLED_GRADES)
        if prompt.startswith("For each uncertain claim"):
            return json.dumps(CLAIM_VERDICTS)
        if prompt.startswith("Check each claim"):
            marks = FORWARD_MARKS if numbered_count(prompt) == 3 else REVERSE_MARKS
            return json.dumps(marks)
        if prompt.startswith("Two texts below"):
            head, _, _ = prompt.partition("Text 2:")
            return "1" if ALPHA_TEXT in head else "2"
        raise AssertionError(f"unexpected judge prompt: {prompt[:60]}")


class PartialAgreeRunner(EchoRunner):
    """All-true lists and a fixed pick, so the rates differ per axis.

    Against the stored verdicts: comprehension agrees 5 of 6 items,
    completeness 3 of 4, hedging 1 of 1, and clarity 1 of 2 picks.
    """

    def reply(self, prompt):
        if prompt.startswith("Grade the quiz answers"):
            return json.dumps(STYLED_GRADES)
        if prompt.startswith("For each uncertain claim"):
            return json.dumps(CLAIM_VERDICTS)
        if prompt.startswith("Check each claim"):
            return json.dumps([True] * numbered_count(prompt))
        if prompt.startswith("Two texts below"):
            return "1"
        raise AssertionError(f"unexpected judge prompt: {prompt[:60]}")


def load_units(project):
    from value.analysis import select_pairs
    from value.cli import answer_index, load_raw

    run_dir = project / "run"
    answers = [
        json.loads(line) for line in (run_dir / "answers.jsonl").read_text().splitlines() if line
    ]
    index = answer_index(answers)
    answer_shas = {key: arm["sha256"] for key, arm in index.items()}
    fidelity = [
        json.loads(line) for line in (run_dir / "fidelity.jsonl").read_text().splitlines() if line
    ]
    pairs, _ = select_pairs(fidelity, answer_shas)
    value_meta, value_rows = load_raw(run_dir / "value-raw.jsonl")
    _, loss_rows = load_raw(run_dir / "loss-raw.jsonl")
    _, rank_rows = load_raw(run_dir / "rank-raw.jsonl")
    return build_units(
        pairs=pairs,
        index=index,
        value_meta=value_meta,
        value_rows=value_rows,
        loss_rows=loss_rows,
        rank_rows=rank_rows,
    )


def test_build_units_rebuilds_the_prompt_of_every_family(project):
    units, skipped = load_units(project)
    assert skipped == {"comprehension": 0, "completeness": 0, "hedging": 0, "clarity": 0}
    by_key = {unit["key"]: unit for unit in units}
    a, u = sha(ALPHA_TEXT), sha(UNSTYLED_TEXT)

    grades = by_key["comprehension:v3:grades:alpha:explanation-01:styled:0"]
    assert grades["axis"] == "comprehension"
    assert grades["stored"] == STYLED_GRADES
    # The quiz takes the two surviving unstyled facts plus the styled
    # fact, paired with the stored questions and the stored replies.
    assert "Reference: Fact one." in grades["prompt"]
    assert "Reference: Alpha fact." in grades["prompt"]
    assert "Fact three." not in grades["prompt"]
    assert "Answer: A one" in grades["prompt"]
    assert "Q three?" in grades["prompt"]

    forward = by_key[f"completeness:check:{a}"]
    assert forward["axis"] == "completeness"
    assert forward["stored"] == FORWARD_MARKS
    assert ALPHA_TEXT in forward["prompt"]
    assert "1. Fact one." in forward["prompt"]

    reverse = by_key[f"completeness:reverse:{a}"]
    assert UNSTYLED_TEXT in reverse["prompt"]
    assert "1. Alpha fact." in reverse["prompt"]

    hedging = by_key[f"hedging:check:{a}"]
    assert hedging["stored"] == CLAIM_VERDICTS
    assert "1. It may rain." in hedging["prompt"]

    contest = by_key[f"clarity:explanation-01:{a}:{u}"]
    assert contest["stored"] == 1
    assert contest["styles"] == ["alpha"]
    assert contest["prompt"].index(ALPHA_TEXT) < contest["prompt"].index(UNSTYLED_TEXT)


def test_build_units_counts_an_unparseable_stored_verdict(project):
    run_dir = project / "run"
    rows = [json.loads(line) for line in (run_dir / "rank-raw.jsonl").read_text().splitlines()]
    rows[1]["output"] = "no pick"
    write_jsonl(run_dir / "rank-raw.jsonl", rows)
    units, skipped = load_units(project)
    assert skipped["clarity"] == 1
    assert sum(1 for unit in units if unit["axis"] == "clarity") == 1


def test_sample_keys_is_deterministic_and_a_subset_of_the_census():
    units = [{"key": f"clarity:p-{number:02d}:a:b", "axis": "clarity"} for number in range(10)] + [
        {"key": f"hedging:check:{number}", "axis": "hedging"} for number in range(3)
    ]
    census = sample_keys(units, None)
    assert census == {unit["key"] for unit in units}
    drawn = sample_keys(units, 4)
    assert drawn == sample_keys(units, 4)
    assert drawn <= census
    assert sum(1 for key in drawn if key.startswith("clarity:")) == 4
    assert sum(1 for key in drawn if key.startswith("hedging:")) == 3


def run_cli(project, *extra, run=None):
    return cli.main([str(project / "run"), *extra], run=run or EchoRunner())


def test_cli_full_agreement_scores_every_axis_at_1(project, capsys):
    assert run_cli(project, "--judge") == 0
    summary = json.loads((project / "run" / "agreement.json").read_text())
    assert summary["units"] == {"comprehension": 2, "completeness": 2, "hedging": 1, "clarity": 2}
    assert summary["first_judges"]["clarity"] == "opus"
    (arm,) = summary["arms"]
    assert arm["model"] == "haiku"
    assert arm["model_resolved"] == JUDGE_MODEL_PINS["haiku"]
    assert arm["sample"] is None
    for axis, items in (("comprehension", 6), ("completeness", 4), ("hedging", 1), ("clarity", 2)):
        stats = arm["axes"][axis]
        assert (stats["items"], stats["agreements"], stats["rate"]) == (items, items, 1.0)
        assert stats["judge_sensitive"] is False
    assert arm["per_style"]["clarity"]["alpha"]["items"] == 2
    assert summary["warnings"] == []
    out = capsys.readouterr().out
    assert "haiku: comprehension 1.0, completeness 1.0, hedging 1.0, clarity 1.0" in out


def test_cli_partial_agreement_computes_the_rates_and_warns(project):
    assert run_cli(project, "--judge", run=PartialAgreeRunner()) == 1
    summary = json.loads((project / "run" / "agreement.json").read_text())
    (arm,) = summary["arms"]
    assert arm["axes"]["comprehension"]["rate"] == round(5 / 6, 3)
    assert arm["axes"]["completeness"]["rate"] == 0.75
    assert arm["axes"]["hedging"]["rate"] == 1.0
    assert arm["axes"]["clarity"]["rate"] == 0.5
    assert arm["axes"]["clarity"]["judge_sensitive"] is True
    assert arm["axes"]["completeness"]["judge_sensitive"] is False
    assert any("clarity axis agrees at 0.5" in warning for warning in summary["warnings"])
    assert any(str(ANCHOR) in warning for warning in summary["warnings"])


def test_cli_judge_writes_one_raw_file_per_arm_and_the_report_shows_both(project):
    assert run_cli(project, "--judge") == 0
    vintage = "claude-opus-4-1-20250805"
    assert run_cli(project, "--judge", "--model", vintage, "--sample", "1") == 0
    assert (project / "run" / arm_raw_name("haiku")).exists()
    assert (project / "run" / f"agreement-{vintage}-raw.jsonl").exists()
    summary = json.loads((project / "run" / "agreement.json").read_text())
    assert [arm["model"] for arm in summary["arms"]] == [vintage, "haiku"]
    vintage_arm = summary["arms"][0]
    assert vintage_arm["model_resolved"] == vintage
    assert vintage_arm["sample"] == 1
    report = (project / "run" / "agreement.md").read_text()
    assert "## Arm: haiku" in report
    assert f"## Arm: {vintage}" in report
    assert "Sample: everything." in report
    assert "Sample: 1 per axis (seed 0)." in report
    assert "### Call timing" in report
    assert "### Harness spend" in report


def test_cli_a_sampled_arm_judges_only_the_drawn_units(project):
    runner = EchoRunner()
    assert run_cli(project, "--judge", "--sample", "1", run=runner) == 0
    rows = [
        json.loads(line)
        for line in (project / "run" / arm_raw_name("haiku")).read_text().splitlines()
    ]
    calls = [row for row in rows if row.get("type") == "call"]
    # One unit per axis: comprehension, completeness, hedging, clarity.
    assert len(calls) == 4
    assert len(runner.calls) == 4
    summary = json.loads((project / "run" / "agreement.json").read_text())
    (arm,) = summary["arms"]
    assert all(stats["not_judged"] == 0 for stats in arm["axes"].values())
    assert summary["warnings"] == []


def test_cli_resume_makes_no_new_calls(project):
    assert run_cli(project, "--judge") == 0
    second = EchoRunner()
    assert run_cli(project, "--judge", run=second) == 0
    assert second.calls == []


def test_cli_offline_rescores_the_stored_rows(project):
    assert run_cli(project, "--judge") == 0
    first = json.loads((project / "run" / "agreement.json").read_text())
    assert run_cli(project) == 0
    second = json.loads((project / "run" / "agreement.json").read_text())
    first.pop("date")
    second.pop("date")
    assert first == second


def test_cli_offline_without_arm_data_exits_2(project):
    with pytest.raises(SystemExit) as error:
        run_cli(project)
    assert error.value.code == 2


def test_cli_a_missing_source_raw_file_exits_2(project):
    (project / "run" / "rank-raw.jsonl").unlink()
    with pytest.raises(SystemExit) as error:
        run_cli(project, "--judge")
    assert error.value.code == 2


def test_cli_a_meta_mismatch_exits_2(project):
    assert run_cli(project, "--judge") == 0
    with pytest.raises(SystemExit) as error:
        run_cli(project, "--judge", "--sample", "1")
    assert error.value.code == 2


def test_cli_the_second_judge_must_differ_from_the_writer(project):
    with pytest.raises(SystemExit) as error:
        run_cli(project, "--judge", "--model", "sonnet")
    assert error.value.code == 2


def test_cli_the_second_judge_must_differ_from_the_first_judge(project):
    with pytest.raises(SystemExit) as error:
        run_cli(project, "--judge", "--model", "opus")
    assert error.value.code == 2
    # The exact ID of a pinned alias cannot dodge the rule either.
    with pytest.raises(SystemExit) as error:
        run_cli(project, "--judge", "--model", JUDGE_MODEL_PINS["opus"])
    assert error.value.code == 2


def test_cli_an_unusable_second_verdict_counts_and_warns(project):
    class MuteHedging(EchoRunner):
        def reply(self, prompt):
            if prompt.startswith("For each uncertain claim"):
                return "no verdicts here"
            return super().reply(prompt)

    runner = MuteHedging()
    assert run_cli(project, "--judge", run=runner) == 1
    # The unusable output retries once before it stays unusable.
    hedging_calls = [
        argv
        for argv in runner.calls
        if argv[argv.index("-p") + 1].startswith("For each uncertain claim")
    ]
    assert len(hedging_calls) == 2
    summary = json.loads((project / "run" / "agreement.json").read_text())
    (arm,) = summary["arms"]
    assert arm["axes"]["hedging"] == {
        "rows": 0,
        "items": 0,
        "agreements": 0,
        "unusable": 1,
        "not_judged": 0,
        "rate": None,
        "judge_sensitive": False,
    }
    assert any("unusable" in warning for warning in summary["warnings"])


def test_cli_an_incomplete_arm_reports_the_not_judged_units(project):
    assert run_cli(project, "--judge") == 0
    raw_path = project / "run" / arm_raw_name("haiku")
    rows = [json.loads(line) for line in raw_path.read_text().splitlines()]
    kept = [row for row in rows if row.get("check") != "clarity"]
    write_jsonl(raw_path, kept)
    assert run_cli(project) == 1
    summary = json.loads((project / "run" / "agreement.json").read_text())
    (arm,) = summary["arms"]
    assert arm["axes"]["clarity"]["not_judged"] == 2
    assert any("not judged" in warning for warning in summary["warnings"])


def test_cli_a_pin_mismatch_exits_2_without_a_retry(project):
    class WrongModel(EchoRunner):
        def __call__(self, argv, cwd, env=None):
            with self.lock:
                self.calls.append(argv)
                prompt = argv[argv.index("-p") + 1]
                return stream(self.reply(prompt), "claude-haiku-3")

    runner = WrongModel()
    with pytest.raises(SystemExit) as error:
        run_cli(project, "--judge", "--parallel", "1", run=runner)
    assert error.value.code == 2
    assert len(runner.calls) == 1


def test_cli_judge_prompts_are_blind(project):
    runner = EchoRunner()
    assert run_cli(project, "--judge", run=runner) == 0
    assert runner.calls
    for argv in runner.calls:
        assert "--plugin-dir" not in argv
        settings = json.loads(argv[argv.index("--settings") + 1])
        assert settings["outputStyle"] == "default"
        prompt = argv[argv.index("-p") + 1]
        assert "alpha" not in prompt
        assert "styled" not in prompt.lower()


def test_cli_parallel_below_1_exits_2(project):
    with pytest.raises(SystemExit) as error:
        run_cli(project, "--parallel", "0")
    assert error.value.code == 2


def test_cli_sample_below_1_exits_2(project):
    with pytest.raises(SystemExit) as error:
        run_cli(project, "--judge", "--sample", "0")
    assert error.value.code == 2


def test_score_arm_reads_the_sample_spec_of_the_meta_row(project):
    units, _ = load_units(project)
    expected = sample_keys(units, 1)
    rows = {}
    for unit in units:
        if unit["key"] in expected:
            stored = unit["stored"]
            output = json.dumps(stored) if isinstance(stored, list) else str(stored)
            rows[unit["key"]] = {"key": unit["key"], "output": output}
    arm, warnings = score_arm(units, {"model": "haiku", "sample": 1}, rows)
    assert warnings == []
    assert all(stats["not_judged"] == 0 for stats in arm["axes"].values())
    assert arm["axes"]["clarity"]["rows"] == 1


def test_the_judge_pass_stops_when_the_cli_version_differs(project, monkeypatch, capsys):
    monkeypatch.setattr(cli, "claude_version", lambda *args: "9.9.9 (test)")
    runner = EchoRunner()
    with pytest.raises(SystemExit) as error:
        run_cli(project, "--judge", run=runner)
    assert error.value.code == 2
    assert runner.calls == []
    stderr = capsys.readouterr().err
    assert CLI_VERSION_PIN in stderr
    assert "9.9.9 (test)" in stderr

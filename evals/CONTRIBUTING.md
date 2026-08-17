# Contributing to the harness

This document holds the procedures for changing the harness and the
styles it measures. The project does not accept external pull
requests: a workflow (`.github/workflows/close-external-prs.yml`)
closes them automatically. Feedback is welcome through the
[issue forms](https://github.com/stefanobaghino/simple-output-styles/issues/new/choose);
the top-level `README.md` describes the channels.

For the design behind the procedures, see
[ARCHITECTURE.md](ARCHITECTURE.md). For how to run the tools, see
the [operations guide](OPERATIONS.md).

## Development setup

From the `evals/` directory:

1. Install the dependencies: `uv sync --locked`.
2. Run the tests: `uv run pytest`.
3. Run the linters: `uv run ruff check .` and
   `uv run ruff format --check .`.

CI (`.github/workflows/evals.yml`) runs exactly these checks on
every PR and push to main. CI never runs live evaluations: live runs
are manual, and they bill the account of the person who runs them.

## Add a style

A style has two parts: the plugin serves the style text, and the
harness measures the style. Add both parts:

1. Add the style text as `plugin/output-styles/<style>.md`. The
   file name before `.md` is the style name.
2. Add the style to the table in the top-level `README.md`, with
   the original source and the needed disclaimers.
3. Add the rule file `rules/<style>.rules.yaml`. Every harness tool
   discovers the styles from the rule files, so a style without a
   rule file is invisible to the harness. Document the exclusions
   of the style in the header comment, as
   [Rules as data](ARCHITECTURE.md#rules-as-data) describes.
4. Add a provisional threshold for the style in `rules/gate.yaml`.
   A new style has no measured rates, so calibrate the threshold
   against the first run, as the header comment of
   `rules/gate.yaml` describes. The calibration run carries a
   one-time asterisk, because the same data sets the threshold and
   takes the test.
5. Leave `rules/targets.yaml` alone for now. A candidate without a
   calibrated row runs under `defaults.max_token_ratio`, and its
   other axes stay unchecked until acceptance. Acceptance adds the
   calibrated row from the confirmation campaign, as the header
   comment of `rules/targets.yaml` describes.
6. Produce a new pair run with `uv run style-pairs`, then gate the
   run, then produce the reports. Do not extend an old run, because
   the provenance of a run records the styles of the run. To avoid
   a full re-measurement, pass `--reuse-from` with a stored run of
   the current era: the new run imports the unchanged arms and
   their judge rows, and only the new style runs live.
7. Run the drift sessions with `uv run style-drift --generate`.
8. After acceptance, add the style's measured findings to
   [RESULTS.md](RESULTS.md), with its generating runs in the Data
   sources table.

The CLI tests need no change for a new style, because they use
synthetic rules. The linter acceptance tests are per style: a new
style adds the samples `tests/samples/<style>/{clean,dirty,traps}.md`,
its expected violations in `tests/test_lint.py`, and one designed
conflict pair in the conflict map of that file.

## Add a prompt

The prompt set in `prompts/prompts.yaml` is shared: every axis reads
the same prompts, so a new prompt grows the sample of every check.
These steps grow the main set; the held-out set has
[its own procedure](#grow-the-held-out-set).

1. Append the entry at the tail of its type block, with the next
   `<type>-NN` id. Keep the counts uniform across the 4 types, and
   keep the prompt self-contained, as the file header describes.
   The tail position keeps the turn order of the drift sessions
   stable.
2. Update the prompt counts in `tests/test_pairs.py`
   (`test_prompt_set_is_complete`).
3. Add a hedge-rich prompt also to `HEDGE_RICH_IDS` in
   `src/runner/screening.py`. The mark steers the screening subset
   draw, and it lives in the code and not in the prompt file,
   because the provenance hashes the prompt file whole.
4. Update the count sentences in the
   [operations guide](OPERATIONS.md): the drift sentence ("15 of
   the 32 pair prompts" in the `style-drift` section) and the
   screening sentence ("2 hedge-rich and 6 confident prompts of
   the 32" in the screening part of the `style-campaign` section).
   The measured screening constants in `src/runner/screening.py`
   go stale with the redrawn subset and need a re-measurement
   against a campaign of the new era.

A prompt edit opens a comparability era: the provenance records the
sha256 of `prompts.yaml`, so new full runs warn against old runs in
a comparison. The screening subset also redraws, because the
stratified seed-0 draw runs over the grown id lists. Old runs stay
comparable among themselves.

### Grow the held-out set

Grow the held-out set like the main set: the next `<type>-hNN` id at
the tail of its type block, uniform counts across the 4 types, and
the counts in `tests/test_pairs.py` (`test_holdout_set_is_complete`)
updated. A change to `prompts/holdout.yaml` opens a comparability
era for held-out runs only.

## Accept a candidate style

A candidate style earns its place in stages: a screening run gives a
cheap first verdict, a full campaign confirms it, and a human anchor
checks the judge.

### Screening threshold

A screening run (`style-campaign --screening`) gives a cheap first
verdict on a candidate style, and this threshold states which
verdict earns a full campaign. Read the Bradley-Terry strengths in
the `rank.md` of the screening run. The candidate earns a full
confirmation campaign when the candidate ranks first among the
styled competitors, or when its bootstrap interval overlaps the
interval of the first-ranked styled competitor. Any other outcome
rejects the candidate, without a full campaign. A screening run
accepts no style.

### Human spot check

The judges are models, so the verdicts need a human anchor. Run this
protocol before you accept a candidate style, on the confirmation
run of that style:

1. Sort the contest keys of `rank-raw.jsonl` and draw 12 contests
   with seed 0 (for example, `random.Random(0).sample(keys, 12)`).
2. Read the two answers of each contest without the style names.
3. Record a winner or a tie per contest, before you look at the
   judge verdicts.
4. Compute the agreement rate: the contests where your record
   agrees with the judge outcome, divided by 12.
5. Write the picks and the agreement rate to `spot-check.md` in the
   run directory, and link that file in the acceptance PR.

When the agreement rate is below 0.7, do not accept the style, and
open an issue that lists the disagreements. The protocol is manual:
no tool draws the sample or computes the rate.

### Acceptance requirements

Acceptance needs, in order: the passed screening threshold, a full
confirmation campaign with its cross-run comparison, the human spot
check, and one run over the held-out prompt set as the final
overfitting check (see
[the held-out prompt set](ARCHITECTURE.md#the-held-out-prompt-set)).
Acceptance then adds the calibrated row to `rules/targets.yaml` and
the findings to [RESULTS.md](RESULTS.md). An accepted style re-opens
the style field, as
[The style field](ARCHITECTURE.md#the-style-field) describes.

## Update a pin

The writer model, the judge models, and the Claude Code CLI version
are pinned; [ARCHITECTURE.md](ARCHITECTURE.md#pins-and-comparability-eras)
lists the pins and what they protect. To upgrade one:

1. Edit the constant: `CLI_VERSION_PIN` in `src/runner/pin.py` for
   the CLI, `WRITER_MODEL_PINS` in `src/runner/generate.py` or
   `JUDGE_MODEL_PINS` in `src/value/judges.py` for a model.
2. Land the change by PR.
3. Accept the new comparability era: the cross-run comparison warns
   across the boundary, and old runs stay comparable among
   themselves. After a CLI pin move, run `uv run style-provision`
   again to fill the managed store with the new version.

At run time, `--accept-cli-version` documents an intentional
one-off upgrade: the run proceeds, the provenance records the found
version, and the comparison warns across the boundary.

## License of contributions

The Apache License 2.0 covers the harness (`evals/`), with one
exception: the rule files in `rules/` stay under the Zero-Clause BSD
license of the repository root, so anyone who forks a style can copy
its rule file and measure the fork. The License section of the
top-level `README.md` states the full split.

## Keep the documentation current

The harness documentation is a set, and each document owns one part:

| Document | Owns | Goes stale when |
|---|---|---|
| `README.md` | The quick start and the documentation map | An entry-point command or a document changes |
| `ARCHITECTURE.md` | The components, the pipeline, isolation, pins and eras, the style field | The harness design changes |
| `OPERATIONS.md` | Commands, flags, tool behaviors, exit codes, the run-data tree | Any tool changes |
| `CONTRIBUTING.md` | The procedures and this ownership map | A procedure changes |
| `RESULTS.md` | The measured findings and their sources | A style is accepted, or a new campaign becomes the reported evidence |

A change to the harness must update the owning documents in the same
PR. No automated check makes sure that the documents match the code,
so the reviewer must check it.

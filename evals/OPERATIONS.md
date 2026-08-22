# Operations guide

This document describes how to run and read every harness tool: the
flags, the behaviors, and the exit codes. For the design behind the
tools, see [ARCHITECTURE.md](ARCHITECTURE.md). For procedures such
as adding a style or accepting a candidate, see
[CONTRIBUTING.md](CONTRIBUTING.md).

## Prerequisites

The harness uses [uv](https://docs.astral.sh/uv/). Run every command
from the `evals/` directory.

> [!WARNING]
> The live tools — the pair runner, the cost probe, the judge
> passes, and the drift generation — call the Claude Code CLI on
> the account of the person who runs them, and every call bills
> that account.

The credential resolves through three routes, in order:

1. Set `ANTHROPIC_API_KEY` to bill the Console account of the key.
   The subscription credential stays out of the call.
2. Set `CLAUDE_CODE_OAUTH_TOKEN` (see `claude setup-token`) to pass
   the token through; nothing is written to disk.
3. Set neither, and an existing `~/.claude/.credentials.json` is
   copied into the hermetic config directory with mode 600 and
   removed with it.

The billing route changes the invoice of a call and never its
answer, so it opens no comparability era, and the credential never
lands in the run data. Without any credential, a tool warns and
proceeds, and the first live call fails with zero tokens spent.

The Claude Code CLI version is pinned, and every live invocation
checks it before its first billed call. Run
`uv run style-provision` once to fill the managed binary store at
`~/.local/share/style-evals/cli/<version>/claude`, so an auto-update
on the machine stops touching the runs. See
[style-provision](#style-provision) and the pins section of
[ARCHITECTURE.md](ARCHITECTURE.md#pins-and-comparability-eras).

## Common behavior of live judge tools

`style-value`, `style-loss`, and `style-rank` share one behavior
set; `style-agreement` follows it too unless its section says
otherwise.

- **Live pass and offline rescore.** `--judge` runs the live judge
  calls and appends the raw outputs to the `<tool>-raw.jsonl` of the
  run. Without `--judge`, the tool rescores the stored raw data
  offline and makes no call.
- **Parallelism.** The judge calls run several at a time, 8 by
  default; `--parallel` sets the count, and 1 runs one call at a
  time. One pool spans the checks of a tool: a call that consumes
  the output of an earlier call waits for that call only, and every
  other call starts as soon as a worker is free.
- **Retry.** A judge call that fails runs once more, and the retry
  becomes a warning, because one transient failure must not abort a
  whole pass. A second failure stops the pass. An interrupted pass
  resumes when the same invocation runs again, so a stop loses no
  data.
- **Prompt-hash guard.** The meta row of a raw file stores one
  sha256 over the judge prompt templates of the tool. A raw file
  from before the hash gets it backfilled on the next `--judge`,
  because the prompts did not change across that boundary. A stored
  hash that differs from the current templates stops the resume with
  exit code 2, because a resumed pass must not mix two prompt
  versions in one raw file.
- **Judge pins.** The judge models must differ from the writer model
  of the run, and each judge alias is pinned to one exact model ID.
  A live judge call that resolves to a different ID stops the pass
  without a retry, because the mismatch is not transient.
- **Reuse.** `--reuse-from RUN` imports the stored judge rows of
  another run whose conditions match, as
  [Reuse across runs](#reuse-across-runs) describes.
- **Timing fields.** Every stored call row holds `duration_ms`, the
  model time the CLI reports, and `wall_ms`, the wall clock of the
  subprocess; the difference is the startup cost of one CLI call.
  The reports state the means in a call-timing section, and a row
  from before the field reads as "not measured".
- **Token fields.** Every stored call row holds four token counts —
  uncached input, cache-write input, cache-read input, and output —
  plus the cache-write split by lifetime (`cache_creation`) when the
  CLI reports it. The reports state the totals of their own calls in
  a harness-spend section, with the cache-read share of the input.
  Old rows read as "not measured". Neither measurement changes a
  call condition, so old runs stay comparable.
- **Exit codes.** 0 when the checks are scored and no warnings
  exist, 1 when warnings exist (for example, a check without judge
  data), 2 when the run cannot be scored.

> [!WARNING]
> Concurrent CLI calls add up across live tools: each tool holds 8
> workers by default, so three live tools produce 24 concurrent
> calls, and workers above the account throughput add latency, not
> throughput. When the account limit rejects calls, a judge call
> that fails twice stops its pass, so lower the worker count. An
> interrupted pass resumes, so a stop loses no data.

## Tool reference

The tools appear in pipeline order. Every tool follows the shared
exit-code convention (0 clean, 1 warnings as data, 2 cannot run);
each entry states its specific meanings.

### style-provision

```
uv run style-provision [--status]
```

Fills the managed store with the pinned CLI version: from the
version store of the native installer when it holds the pin, else by
a download from the release endpoint of the official installer,
verified against the manifest checksum. The provision command is the
only part of the harness that touches the network, and only when it
downloads; run time makes no network call.

When the managed binary exists, the hermetic environment puts it at
the front of the call `PATH`, so the recorded binary, the version
check, and every measured call see the same CLI; without it, the
calls use the `PATH` `claude` plus the pin check, unchanged. A
provisioned binary still goes through the version check, so the
store is a convenience, never the guarantee. The provenance records
the resolution route (`binary_source`: managed or path) next to the
binary path; the route is machine-local, so it opens no
comparability era.

`--status` reports the store. After a pin move, run the command
again to provision the new version.

### style-lint

```
uv run style-lint FILE.md --rules rules/<style>.rules.yaml
```

Checks one Markdown file against one rule set and reports each
violation, plus a rate per 100 sentences. The linter is
deterministic and exits with code 1 when it finds a violation.

### style-pairs

```
uv run style-pairs [--parallel N] [--screening] [--holdout] [--reuse-from RUN] [--accept-cli-version]
```

Reads the prompt set in `prompts/prompts.yaml`, or another prompt
file through `--prompts`, and calls the `claude` CLI once per
answer: one answer per style and one shared unstyled answer per
prompt. Every call runs inside the isolation layer that
[ARCHITECTURE.md](ARCHITECTURE.md#hermetic-isolation) describes. A
plugin-styled arm activates the plugin-qualified style name and
loads the plugin; the arm of a built-in style (`concise`) activates
the bare CLI style name and loads no plugin, like the unstyled arm.

> [!WARNING]
> Do not run two `style-pairs` invocations at the same time.
> Without `--out`, both invocations pick the same run directory,
> because the picker takes the first incomplete run, and the two
> processes then write duplicate rows and spend duplicate calls.

The generation calls run several at a time (8 by default), and
`--parallel` sets the count. The calls do not interact, so the
concurrency changes no condition of a run. The answers land in
completion order, and every reader of the answers reads them by key,
so the row order carries no meaning.

An interrupted run resumes when the same invocation runs again. When
the default directory already holds a complete run, a repeat without
`--out` starts the next free letter suffix (`runs/<date>b`, then
`c`, and so on) and tells the choice, because a silent reuse of a
complete run produces no new sample. On a resume, the runner rejects
a directory whose stored prompt-set hash or mode differs from the
invocation, so a held-out or screening pass cannot extend a main-set
run.

`--holdout` runs the pair stage over `prompts/holdout.yaml`, under
the `runs/<date>-holdout` directory family. A main-set run never
reads or hashes `holdout.yaml`, and `--screening --holdout` is
refused; see
[the held-out prompt set](ARCHITECTURE.md#the-held-out-prompt-set).

`--reuse-from RUN` imports the stored answers of another run for the
arms whose conditions match — the prompt-set hash, the writer model
and its pin, the screening mode, and the style text identity per
styled arm (the file hash of a plugin style, the CLI version of a
built-in style) — and generates only the rest, as
[Reuse across runs](#reuse-across-runs) describes.

Exit codes: 1 when the pair set is incomplete, 2 when the writer pin
stops a call or the CLI-version pin stops the run.

### style-gate

```
uv run style-gate runs/<date>
```

Reads the answers of a run and writes the fidelity files into the
run directory. It checks every styled answer with the rules of its
style, and it checks every unstyled answer with every rule set of
the run, as a baseline: the baseline shows how much rule obedience
exists without a style. Re-gating overwrites the fidelity files,
because the gate is a pure function of the answers, the rules, and
the policy.

Exit codes: 0 when every pair passes and no warnings exist, 1 when
pairs fail or warnings exist, 2 when the run cannot be gated.

### style-cost

```
uv run style-cost runs/<date> [--probe] [--repeats N] [--reuse-from RUN] [--accept-cli-version]
```

Reads all pairs of a run — gated or not — and writes the cost files
into the run directory. The answer-length part is offline: the ratio
of a pair is the output-token count of the styled answer divided by
the output-token count of the unstyled answer, reported as a
distribution and per task type.

The input-overhead part needs a live measurement, because a stored
run holds no input-token data for it. `--probe` runs one minimal
call per arm and repeat, and takes the difference in input context
tokens between the styled call and the unstyled call of the same
repeat. Both probe arms load the plugin — also on the arm of a
built-in style — so the difference isolates the style block. `--repeats` sets the repeat count (3 by default),
and the report states the mean and the spread per style. The repeat
count changes no call condition, so old runs stay comparable, and a
stored probe in the old single-call format reads as one repeat.

The report also states a weighted overhead per style: each token
count times its price ratio against one uncached input token (a
cache write costs 1.25, a cache read costs 0.1), so the unit is
uncached-token equivalents and the number holds under any absolute
price.

The probe data lands in `cost-probe.json`, and a later `style-cost`
call without `--probe` reuses it. With `--probe --reuse-from RUN`,
the tool imports the stored probe arms of another run per style,
together with the unstyled baseline arms of their repeats, and
probes live only the styles that the source cannot serve.

Exit codes: 0 when both numbers exist and no warnings exist, 1 when
warnings exist (for example, the overhead is not measured), 2 when
the run cannot be reported.

### style-loss

```
uv run style-loss runs/<date> [--judge] [--parallel N] [--reuse-from RUN] [--accept-cli-version]
```

Reads only the gated pairs. Two checks measure what the rewrite
loses:

- **Completeness.** The judge lists the facts of the unstyled
  answer, then checks each fact against the styled answer. The check
  also mines the reverse direction: the judge lists the facts of the
  styled answer and checks each against the unstyled answer. A
  styled fact that the unstyled answer does not state counts as an
  addition, reported per pair, because material that only the
  rewrite states is otherwise invisible.
- **Hedging survival.** The judge lists the uncertain claims of the
  unstyled answer, then judges whether the styled answer keeps,
  hardens, or drops each claim. A claim that hardens becomes a false
  certainty, which is worse than a lost fact.

No judge call sees both answers of a pair: the extracted items
travel between the calls, never the source text. A check call starts
as soon as its own extraction is complete, with no barrier between
the checks. The [common behavior](#common-behavior-of-live-judge-tools)
applies, with `loss-raw.jsonl` as the raw file.

### style-value

```
uv run style-value runs/<date> [--judge] [--parallel N] [--reuse-from RUN] [--accept-cli-version]
```

Reads only the gated pairs, because rule obedience alone can produce
compliant, useless text, and this report measures whether a reader
gains anything. Three checks compare the two answers of a pair:

- **Weak-reader comprehension.** A weaker model answers quiz
  questions from one answer text, and a grader marks every reply.
  The questions come from the shared facts of the pair, which the
  content-loss check mined in both directions, so a shared fact
  exists in two wordings and the quiz takes half of its questions
  from the facts of each answer. The questions probe only material
  that both answers contain, so the score measures extraction, not
  coverage. Each answer gets several reader replicates; the pair
  outcome is the plurality over the replicate outcomes, and the
  report states the replicate agreement next to a buried-fact rate
  per arm (a "NOT IN TEXT" reply to a shared fact).
- **Ambiguity through paraphrase.** Independent restatements of one
  answer text, scored by their mutual agreement.
- **Translation round-trip.** One answer text goes to another
  language and back, scored by the lexical loss.

> [!WARNING]
> Run `style-loss <run> --judge` to completion before the first
> `style-value <run> --judge`. Each judge tool works in its own
> scratch directory, so the two tools can run at the same time on
> one run — but the comprehension check reads the shared facts from
> `loss-raw.jsonl` once, at its start, so the loss judge pass must
> be complete by then.

The paraphrase check and the round-trip check build on lexical
similarity, so a shorter text can score better, because less text
exists to diverge on. The report therefore states, per check and
style, the length confound: the correlation between the length ratio
of a pair (styled words over unstyled words) and the styled
advantage (the score gain of the styled arm). A negative value means
that the shorter styled answers score better.

The [common behavior](#common-behavior-of-live-judge-tools) applies,
with `value-raw.jsonl` as the raw file. Every judge call sees one
bare text without a style name or an arm label.

### style-rank

```
uv run style-rank runs/<date> [--judge] [--parallel N] [--reuse-from RUN] [--accept-cli-version]
```

Reads only the gated pairs, and the unstyled answer joins as its own
competitor under the reserved name `unstyled`. Per prompt and per
competitor pair, a blind judge sees the two texts side by side and
picks the clearer one, in both orders, so a position preference
cancels: the orders agree and the contest is a decisive win for the
picked competitor, or the orders disagree and the contest is a
split. A contest with an unusable pick is unscored, because a single
scored order would reintroduce the position bias that the swap
cancels.

This tool relaxes one harness invariant on purpose: a clarity
contest is a choice, so a judge call sees both answers of a prompt.
Blindness holds through the absence of labels — no prompt names a
style or an arm — and the position mapping lives only in the raw
rows. The unstyled competitor is ungated, but every styled
competitor passed its gate, and the report states the asymmetry.

A Bradley-Terry fit turns the contests into one strength per
competitor, anchored on the unstyled answer at 1.0, with a bootstrap
interval per strength. The fit stays dormant below 3 competitors,
and a competitor with zero wins or zero losses has no finite
strength. The report lists the strengths from the highest to the
lowest, and it also states the position bias of the judge, the
matchups per task type, and the length confound: the correlation
between the length ratio of a contest and the points of the longer
text.

The [common behavior](#common-behavior-of-live-judge-tools) applies,
with `rank-raw.jsonl` as the raw file.

### style-drift

```
uv run style-drift [--generate] [--scripts prompts/sessions/*.yaml] [--estimate] [--context-window N] [--depth-target F] [--out runs/<date>-drift] [--accept-cli-version]
```

Owns its own run directory, because it measures sessions, not pairs.
A session is 15 scripted turns in one Claude Code session, with the
style active: each turn resumes the session of the previous turn, so
the context grows. The turns reuse 15 of the 32 pair prompts, and
each repeat rotates the order, so a hard prompt does not always sit
at the same turn position. Session persistence stays on for these
calls, because a resumable session must persist; the session files
land in the hermetic config directory of the invocation and vanish
with it.

The linter checks every turn with the rule set of the style. The
rate of a turn position pools the complete sessions: 100 times the
violations at that position over the sentences at that position, so
a short answer weighs by its sentence count and cannot dominate the
series. The verdict per style compares the slope of the pooled
series against a per-style threshold: "growing" when the slope is
above the threshold, else "flat". The threshold comes from a
permutation null: the turn order of each session shuffles 10000
times with a fixed seed, the pooled slope refits per shuffle, and
the threshold is the 0.95 nearest-rank quantile of the shuffled
slopes. The same null yields a one-sided p-value, stated for
information; the verdict rests on the threshold alone.
`--slope-threshold` replaces the derived threshold with one fixed
value for every style, and the report then states both values. Few
short sessions give a coarse null — the quantile can then equal the
largest possible slope — so the verdict needs enough complete
sessions to be sensitive.

`--generate` runs the missing sessions; an interrupted run restarts
an incomplete session from turn 1. Without `--generate`, the tool
rescores the stored session data offline, with the derived threshold.

**Deep mode.** The shallow prompts reach only the start of the
context window: a shallow session ends near 20K tokens. `--scripts`
selects coherent session scripts, one YAML file per script in
`prompts/sessions/`. A 15-turn deep session reaches a measured final
depth between about 150K and 420K tokens, script by script, with a
per-style mean near 300K (`runs/2026-08-09-drift-deep`): the answers
of the model join the context that every later turn re-reads, so the
depth outgrows the authored material alone. Later turns of a script
reference earlier material by name, so the model must read deep
context while it obeys the style.

A coherent script cannot rotate, so each repeat runs one whole
script, and the repeats spread over the scripts: repeat r runs
script (r - 1) mod the script count, and the repeat count must
spread evenly over the scripts. The shallow rotated run stays as the
control. The scripts fix the turn count: `--turns` does not combine
with `--scripts`, and every passed script must hold the same turn
count, because the analysis pools by turn position. A deep run lands
in its own `runs/<date>-drift-deep` family, and the tool rejects an
invocation whose mode differs from the mode of the stored run. The
provenance records the mode, the sha256 per script file, and the
script per repeat; a change to a script file changes the
measurement, like a change to the prompt set.

**Context depth.** Every drift report states the context depth,
because a flat verdict at a shallow depth is weak evidence. Per
style, the report states the final depth of each session (the
uncached, cache-write, and cache-read tokens of a call, summed), the
mean, and the fraction of the context window. `--context-window`
sets the window size (200000 by default), because the stream-json
events do not carry it. A deep run also has a depth target:
`--depth-target` sets the target mean final depth as a fraction of
the window, 0.6 by default for a deep run — clearly below the
compaction region near 0.8, because compaction rewrites the context
and changes what the test measures. A shallow run has no target
unless the flag sets one, and 0 disables the check. A style whose
mean final depth misses the target warns, and the tool exits 1. The
depth fields are a pure function of the stored rows and the flags,
so a rescore of an old run states them too.

`--estimate` prints a projection of a deep run before any call: the
call count, the projected final depth per script against the window
and the target, and the projected spend in uncached-token
equivalents. The projection rests on three constants calibrated
against `runs/2026-08-08-drift`, and it leans low on code and log
material; the run measures the truth.

Exit codes: 0 when every session is complete, every verdict is flat,
and no warnings exist, 1 when a session failed or a verdict is
"growing" or warnings exist, 2 when the run cannot run or cannot be
scored.

### style-agreement

```
uv run style-agreement runs/<date> [--judge] [--model M] [--sample N] [--parallel N] [--accept-cli-version]
```

The stored verdicts of a run come from one judge model, and the
style-design loop optimizes against those verdicts, so a
judge-specific verdict is a standing risk. This tool re-runs the
stored discrete verdicts of a run with a second judge model and
reports the agreement rate per axis: comprehension (the quiz
grades), completeness (both check directions), hedging, and clarity
(the contest picks). Only the discrete verdicts enter: the
extraction and free-text rows carry nothing that an equality
comparison can score. The tool rebuilds each judged prompt from the
stored rows, with the joins the scorers already perform and the
original prompt templates, so the second judge answers the exact
stored question. By default the tool judges everything; `--sample N`
draws N verdict rows per axis with seed 0, the spot-check precedent.

Two arms exist by convention, and the report reads them together:

- A **cross-line arm** (`--model haiku`, a weaker Claude line) is a
  lower bound: its disagreement mixes genuine ambiguity with weaker
  capability. On the comprehension axis, a cross-line grader can
  share the model line of the original reader, so leniency toward
  the reader's phrasing is possible; the cross-vintage arm is the
  cleaner signal there.
- A **cross-vintage arm** (an older model of the first-judge line,
  passed as the exact model ID) is capability-matched: its
  disagreement measures what a model update would move — the risk
  the judge pin freezes.

An axis where only the cross-line arm disagrees points at
capability; an axis where both arms disagree is judge-sensitive.
Every judge runs through the Claude CLI, so a second judge is a
different Claude line or vintage, never a different vendor; the
[human spot check](CONTRIBUTING.md#human-spot-check) stays the
cross-vendor anchor.

The agreement unit is one discrete verdict: one graded quiz item,
one checked fact, one checked claim, or one contest pick. The report
states, per arm and axis, the items compared, the agreement rate,
the unusable second outputs, and a per-style breakdown, because a
style-specific disagreement is exactly what the shared-bias risk
predicts. An axis under 0.7 — the acceptance anchor of the spot
check — is marked judge-sensitive and warns. The cross-vintage
clarity rate also derives the freshness tolerance of
[Reuse across runs](#reuse-across-runs).

The second judge must differ from the writer model of the run and
from the first judge of every axis, on the requested alias and on
the pinned resolution, and the per-call pin check applies. Each arm
appends to its own raw file, `agreement-<model>-raw.jsonl`, so every
raw file stays single-model; an interrupted pass resumes when the
same invocation runs again, and a meta mismatch (another model,
another sample spec) exits with code 2. The scoring is offline,
discovers every arm file of the run, and re-runs without `--judge`.
The tool writes new files only and changes no call condition of any
stored tool, so it opens no comparability era.

Exit codes: 0 when the arms are scored and no warnings exist, 1 when
warnings exist (a judge-sensitive axis, an unusable second output,
an incomplete arm), 2 when the run cannot be scored.

### style-compare

```
uv run style-compare runs/<a> runs/<b> [...] [--out runs/<date>-compare]
```

Reads the stored artifacts of two or more runs and writes
`compare.json` and `compare.md` into its own directory, because the
comparison belongs to no single run. Per style and axis, the report
states one value per run and the spread: minimum, mean, maximum, and
the sample standard deviation. The axes are the headline scalars of
the other reports: the styled violation rate and the gated pairs
passed, the output-token ratio, the net wins per reader-value check,
the fact and hedge survival medians, the Bradley-Terry strength, and
the net wins against the unstyled competitor. The unstyled anchor
gets no section of its own, because its strength is 1.0 by
construction. The comparison is offline and makes no judge calls.

The runs must share their conditions, and a mismatch becomes a
warning, because the reader must see how far apart the conditions
are:

| Checked condition | Note |
|---|---|
| Prompt-set hash | Separates main-set, held-out, and edited prompt eras. |
| Style and rule hashes | A reworded style or rule is another measurement. |
| Writer model and its pin | Silent for a run from before the pin, whose resolution equals the stored baseline. |
| Claude CLI version | The cross-machine invariant; the binary path stays out, because an absolute path is machine-local. |
| Workdir mode; config mode and manifest hash | A run from before the hermetic directory saw the user plugins. |
| Judge parameters, resolved judge models, judge-prompt hashes | Silent for a run from before the prompt hash, whose templates did not differ. |
| Fact-mine design | The comprehension quiz depends on it. |

A missing artifact drops the axes of that artifact for that run, and
n states the run count per axis. The tool rejects a comparison that
mixes a screening run with a full run.

Exit codes: 0 when no warnings exist, 1 when warnings exist, 2 when
the comparison cannot run.

### style-targets

```
uv run style-targets runs/<date> [--targets rules/targets.yaml] [--drift runs/<date>-drift]
```

Reads the stored artifacts of one run and writes `targets.json` and
`targets.md` into the run directory. Per style and axis, it compares
the observed value against the limit in `rules/targets.yaml`: a max
limit is a cap, a min limit a floor, and every boundary is
inclusive, like the gate threshold.

The drift-slope axis reads a separate drift run through `--drift`;
without the flag, the slope caps stay unchecked, and the check
warns, because an unchecked bound is exactly the silent-regression
channel this check closes. A style without a calibrated row — a
candidate before acceptance — is checked against
`defaults.max_token_ratio` only. A screening run is rejected,
because its numbers cannot demonstrate that a target holds. The
check is offline and makes no judge calls.

Exit codes: 0 when every checked axis passes and no warnings exist,
1 when an axis fails or warnings exist, 2 when the run cannot be
checked.

### style-campaign

```
uv run style-campaign [--runs N] [--budget W] [--probe-repeats N] [--screening] [--holdout] [--reuse-from RUN] [--accept-cli-version]
```

Runs N full runs (3 by default) under one schedule, for the
cross-run comparison. `--budget` sets the total worker count across
every stage (48 by default), metered by the one worker gate that
[ARCHITECTURE.md](ARCHITECTURE.md#campaign-scheduling) describes.
The cost stage probes with 3 repeats, and `--probe-repeats` forwards
a different count to `style-cost`. The schedule of one run:

```
pairs ─→ gate ─→ loss ───────────────────→ value (comprehension)
              ├─→ value (paraphrase, round-trip) ─↗
              ├─→ rank
              └─→ cost
```

The next run starts its `pairs` stage when the previous `pairs`
stage is complete, the judge stages of the runs overlap without
constraint, and the comparison runs last, over the complete runs.
The first value invocation of a run exits 1 by design, because its
comprehension check is not judged yet; the driver reports that exit
code but does not count it.

The driver retries a stopped stage once, prints the wall clock per
stage at the end, and exits 0 only when every stage is clean. The
workers column of the final table states the observed peak of live
calls per stage. An interrupted campaign resumes through `--dirs`,
with the run directories of the interrupted campaign; a screening
resume needs `--screening` again. A 3-run campaign of the current
era expects a wall clock near 70 minutes at budget 48; a wall-clock
bar must state the budget and the era it assumes.

`--reuse-from RUN` forwards to every stage except the gate and
implies `--runs 1`, because an imported repetition measures no
variance. A reuse campaign sits outside the wall-clock bar: it makes
only the fresh calls of its field extension plus the freshness
samples.

The driver enforces the two manual-run limits by construction — the
single-`style-pairs` rule and the worker-stacking rule — and the
limits stay the rule for a manual run of the tools; see the warnings
in [style-pairs](#style-pairs) and
[Common behavior of live judge tools](#common-behavior-of-live-judge-tools).

**Screening mode.** `style-campaign --screening` screens one
candidate style: one run instead of three, over a fixed prompt
subset, with every stage of a full run. The subset draws 2 prompts
per task type from the full prompt file with seed 0, stratified over
the hedge-rich mark (`HEDGE_RICH_IDS` in `src/runner/screening.py`):
the subset holds the hedge-rich share of the full set, rounded — 2
hedge-rich and 6 confident prompts of the 32 — so a screening
verdict rests on the prompt mix a full campaign measures, not on one
class (#111). One shared seeded generator draws which types
contribute a hedge-rich prompt and which ids fill the rest, so every
screening run uses the same 8 prompts.

By design, the generation calls are about 8% of a full campaign, and
the judge calls are about 25% of one full run. The measurement
against the baseline campaign (`runs/2026-08-08` and
`runs/2026-08-08b`) grounds these design numbers in stored rows: a
screening run holds 25.5% and 24.4% of the calls of its run (8.5%
and 8.1% of the 3-run campaign), 25.3% and 24.4% of the input tokens
in uncached-token equivalents, and 23.2% and 23.6% of the output
tokens. The token shares track the call share because the stratified
subset mirrors the answer-length mix of the full set. The
measurement describes a run without reuse, and it is era-scoped: a
prompt-set change redraws the subset, stales the measured constants
in `src/runner/screening.py`, and warns on the screening block of
the provenance as well as on the prompt-set hash.

The run lands under its own `-screening` directory family, the
provenance carries a screening block, and every report of the run
starts with a screening note, because the error bars of a screening
run are wider than the error bars of a full run. `style-compare`
rejects a comparison that mixes a screening run with a full run, and
a screening run never covers the held-out set. For the verdict that
earns a full campaign, see the
[screening threshold](CONTRIBUTING.md#screening-threshold).

## Reuse across runs

A campaign re-judges every style in every run, but with a fixed
prompt set and fixed styles most calls repeat stored work.
`--reuse-from RUN` imports the stored rows of a source run and calls
only for the rest. Reuse is explicit, never the default, because the
multi-run repetition of a campaign measures variance, and a silent
cache hit turns a repetition into a copy. Reuse opens no
comparability era: an imported row is the source row plus a
`reused_from` marker, and nothing else changes. With the flag off,
the behavior is byte-identical to a run without the reuse layer.

The reuse works in two chained layers, because a fresh generation of
the same style and prompt yields a different text, and a stored
judge row speaks about the stored answer:

1. The pair runner imports the answers whose conditions match: the
   prompt-set hash, the writer model and its pin, the screening
   mode, and the style text identity per styled arm — the file hash
   of a plugin style, or the CLI version of a built-in style,
   because a built-in text ships inside the CLI binary. The source
   answers must also obey the current writer pin, because rows from
   another resolution belong to another era.
2. Each judge tool imports the stored rows that reference the
   answers of the current run. The judge keys carry the answer
   hashes, so a key hit is a content hit. The comprehension keys
   carry the style and the prompt id instead, so those rows import
   only when both arms of the pair hold the same text in both runs.
   The source must match the invocation on the META match keys of
   the resume path, minus the whole-file answers hash that the
   per-row checks replace, and the resolved judge models of the
   source must obey the current pins.

The cost probe imports per style: the arms of a style whose text
matches the source travel with the unstyled baseline arms of their
own repeats, and only the missing styles probe live.

On each import, a small fixed sample of the imported verdict rows
re-runs live: the first sorted keys per verdict family — 2 per loss
check family, 6 comprehension grades, and 6 contests. The judge can
shift between the store date of a row and the reuse date, in ways
that the key does not see, and the sample measures that shift. The
report of each tool states the reused and live counts and the
comparison per sampled key. On a verdict axis — comprehension
grades, completeness, hedging — the comparison is exact equality,
and one differing verdict is a warning. The clarity picks carry an
aggregate tolerance instead, because two judges disagree on many
picks even without drift: the second-judge sample of
`runs/2026-08-08` measured a 0.60 clarity agreement on its
capability-matched cross-vintage arm (100 picks; the cross-line
census arm agreed at 0.686 over 939). The contest sample warns only
when its disagreement count clears a one-sided binomial tail of 0.05
at that 0.40 disagreement rate — 5 of the full sample of 6, and a
sample of 3 picks or fewer clears no bar. A cross-judge rate bounds
the same-judge-over-time noise from above, so the tolerance stays
quiet on plausible noise and fires only on counts the measured
disagreement almost never produces. The probe arms carry no
freshness sample, because they are token measurements, not judge
scores.

`uv run style-campaign --reuse-from RUN` runs the whole chain. A
field extension then makes only the calls of the new style, its new
contests, and the freshness samples.

## Run data reference

Stored runs live under `runs/`, one directory per run, named
`<date>`, with a letter suffix when more than one run happens on one
date. The pair runner picks the suffix on a same-day repeat:

```
runs/<YYYY-MM-DD>/
  provenance.json   # prompt-set hash, conditions (writer pin, workdir and config modes), style hashes, linter toolchain
  answers.jsonl     # one line per answer; style null marks the unstyled answer
  report.md         # completeness, volume, call timing, environment, warnings
  fidelity.jsonl    # one line per (answer, rule set), with the pass or fail mark
  fidelity.json     # gate provenance and the per-style summary
  fidelity.md       # thresholds, marks, per-rule table, baseline comparison
  cost-probe.json   # probe provenance and the measured input overhead per style
  cost.json         # answer-length ratios and input overhead, machine-readable
  cost.md           # the token-cost report for a human
  value-raw.jsonl   # judge provenance plus one line per raw judge call
  value.json        # win/loss/tie and length confound per check and style
  value.md          # the reader-value report for a human
  loss-raw.jsonl    # judge provenance plus one line per raw judge call
  loss.json         # fact and hedge survival per style, machine-readable
  loss.md           # the content-loss report for a human
  rank-raw.jsonl    # judge provenance plus one line per raw judge call
  rank.json         # matchups, win matrix, and strengths, machine-readable
  rank.md           # the clarity-ranking report for a human
  agreement-<model>-raw.jsonl  # one file per second-judge arm: meta plus one line per raw call
  agreement.json    # the agreement rate per arm and axis, machine-readable
  agreement.md      # the second-judge agreement report for a human
  spot-check.md     # the human spot-check record and the agreement rate (manual)
  targets.json      # the regression-targets verdicts per style and axis, machine-readable
  targets.md        # the regression-targets report for a human

runs/<YYYY-MM-DD>-screening/
  # the same files as a pair run, over the fixed prompt subset; the
  # provenance carries the screening block, and every report starts
  # with the screening note

runs/<YYYY-MM-DD>-holdout/
  # the same files as a pair run, over the held-out prompt set; the
  # prompt-set hash in the provenance separates these runs from the
  # main-set runs

runs/<YYYY-MM-DD>-drift/
  provenance.json   # like the pair runs, plus the session script per repeat
  sessions.jsonl    # one line per turn, with the session-id chain
  drift.json        # pooled rate series, slope, derived threshold, null p-value, verdict, and context depth per style
  drift.md          # the drift report for a human

runs/<YYYY-MM-DD>-drift-deep/
  # the same files as a drift run, over coherent deep session
  # scripts; the provenance carries the mode, the script hashes,
  # and the script per repeat

runs/<YYYY-MM-DD>-compare/
  compare.json      # the spread per style and axis across runs, machine-readable
  compare.md        # the cross-run comparison for a human
```

A pair is not stored twice: it is the line for `(prompt, style)`
plus the line for `(prompt, null)`. The data is plain text in plain
git: no LFS, and no single file above about 5 MB. Keep raw
transcripts out; store only what the reports consume.

A row of `answers.jsonl`, a call row of a raw file, and a probe arm
can carry a `reused_from` marker: the row came from the named run
through the reuse flag, byte-identical apart from the marker. Such a
run also carries a `reuse` block in `provenance.json`,
`cost-probe.json`, and the `loss.json`, `value.json`, `rank.json`,
and `cost.json` reports, with the reused and live counts and the
freshness comparison. See [Reuse across runs](#reuse-across-runs).

## Keep this guide current

This guide owns the commands, the flags, the tool behaviors, the
exit codes, and the run-data tree. A tool change updates it in the
same PR. The ownership map of the whole documentation set lives in
[CONTRIBUTING.md](CONTRIBUTING.md#keep-the-documentation-current).

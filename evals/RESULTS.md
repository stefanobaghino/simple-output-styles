# Evaluation results

This document reports the latest measured findings for the six
shipped output styles and the Claude Code built-in Concise style,
which the harness evaluates for comparison. The top-level `README.md`
summarizes these findings qualitatively; this document carries the
numbers, their spread, and their caveats. For how the measurements
work, see [ARCHITECTURE.md](ARCHITECTURE.md).

> [!NOTE]
> Measured on 2026-08-22 and 2026-08-23, over the campaign runs
> `2026-08-22`, `2026-08-22b`, and `2026-08-22c` plus the supporting
> runs in [Data sources](#data-sources). Writer model
> `claude-sonnet-5`; judge `claude-opus-5`; weak reader
> `claude-haiku-4-5-20251001`; Claude Code CLI pinned at 2.1.239.
> The results are specific to these models, prompts, and pins: a
> model, prompt, or CLI change opens a new comparability era and
> re-opens every question. This campaign opened such an era — the
> CLI pin moved from 2.1.226 to add the built-in Concise style — so
> the numbers here are not directly comparable to the 2.1.226-era
> numbers they replace. Sections that still rest on 2.1.226-era runs
> say so explicitly.

## How to read the numbers

Each headline number is the mean over three full runs (32 prompts ×
8 arms each); the per-run values and the spread live in
[the three-run comparison](runs/2026-08-23-compare/compare.md), and
the spread is the error bar of the harness.

- **Bradley-Terry strength** comes from blind pairwise clarity
  contests, judged in both orders, with the unstyled answer anchored
  at 1.0. A strength above 1.0 means the judge picks the style over
  the unstyled answer more often than not.
- **Net wins vs unstyled** is decisive contest wins minus losses
  against the unstyled competitor, over 32 prompts.
- **Output-token ratio** is styled output tokens over unstyled
  output tokens. Below 1.0 means shorter answers.
- **Fact survival** is the fraction of the facts of the unstyled
  answer that survive in the styled answer, as the median over
  gated pairs.
- **Hedge survival** is the fraction of the hedged claims of the
  unstyled answer that stay hedged in the styled answer, as the
  median over gated pairs. A dropped hedge becomes a false
  certainty, which is worse than a lost fact.
- **Violation rate** is linter violations per 100 sentences, and
  **gated pairs** counts the pairs (of 32) whose styled answer
  passed its rule gate. The rule counts differ per style, so the
  rates are not comparable across styles — only against a style's
  own gate threshold.

## Results at a glance

Three-run means, ordered by Bradley-Terry strength:

| Style | BT strength | Net wins vs unstyled | Token ratio | Fact survival | Hedge survival | Violation rate | Gated pairs |
|---|---|---|---|---|---|---|---|
| actionable-clarity | 2.291 | +7.3 | 1.067 | 0.783 | 0.939 | 0.12 | 32.0 |
| developer-docs | 1.769 | +7.7 | 0.850 | 0.769 | 0.723 | 0.22 | 32.0 |
| plain-language | 1.298 | +5.7 | 0.860 | 0.728 | 0.861 | 0.00 | 32.0 |
| classic-concise | 0.713 | −4.0 | 0.587 | 0.733 | 0.767 | 0.24 | 32.0 |
| clarity-flow | 0.666 | −6.3 | 0.787 | 0.752 | 0.793 | 0.00 | 32.0 |
| technical-simplified | 0.476 | −8.7 | 0.910 | 0.679 | 0.291 | 7.57 | 26.7 |
| concise (built-in) | 0.347 | −14.3 | 0.580 | 0.747 | 0.731 | 0.00 | 32.0 |

The style block's fixed input overhead per request, measured by the
cost probe (identical across the three runs): concise 504 tokens,
clarity-flow 1,291, developer-docs 1,293, classic-concise 1,354,
plain-language 1,511, technical-simplified 2,041, and
actionable-clarity 2,115.

## Findings per style

The sections follow the strength order of the table.

### actionable-clarity

The clearest style of the field again: mean strength 2.291 (per-run
range 1.928 to 2.953), first among the styles in all three runs,
with +7.3 net wins against the unstyled answer. It keeps the most
content — fact survival 0.783, the highest of the field — and the
highest hedge survival (0.939). The cost is length: its mean
output-token ratio of 1.067 makes it the only style near or above
the unstyled length (1.24 in one run), and its style block adds the
largest input overhead, 2,115 tokens per request. One run
(`2026-08-22b`) missed its 0.90 hedge-survival regression floor at
0.818, the same occasional miss the 2.1.226 era recorded.

### developer-docs

Second by mean strength (1.769, up from mid-field in the 2.1.226
era) with +7.7 net wins — the most of the field — at shorter than
normal length (token ratio 0.850). It posted positive net wins on
all three reader-value checks in all three runs. Fact survival
0.769 sits just behind actionable-clarity. Its weakness stays the
hedges: survival averaged 0.723 but ranged down to 0.50, so the
direct tone sometimes turns a "maybe" into a certainty.

### plain-language

Third by mean strength (1.298) with +5.7 net wins, shorter answers
(token ratio 0.860), and zero measured violations in all three
runs. Hedge survival 0.861 is second only to actionable-clarity,
though its worst run (0.709) dipped under its 0.74 regression
floor. Fact survival 0.728 sits low in the field, as in the
2.1.226 era: the push to shorten can cut facts a reader needs.

### classic-concise

Mean strength 0.713, below the unstyled baseline (−4.0 net wins).
The concision is real — token ratio 0.587, second-shortest of the
field — and fact survival holds up (0.733), but the reader-value
checks lean negative: paraphrase −7.0 and round-trip −6.3 net wins
on average. Hedge survival 0.767 sits mid-field.

### clarity-flow

Mean strength 0.666 (−6.3 net wins), a clear step down from its
0.918 in the 2.1.226 era, and its worst run (0.439) sat far under
its old-era 0.80 regression floor. Content stays its strength:
fact survival 0.752 is third in the field, answers shorten (ratio
0.787), and it kept zero measured violations in all three runs.
Whether the clarity drop is the new CLI era or judge noise is not
separable from three runs; the spread on this axis (standard
deviation 0.201) is the widest warning sign in the comparison.

### technical-simplified

Last of the shipped styles on the chat-facing measures: strength
0.476, −8.7 net wins, fact survival 0.679, and a hedge-survival
collapse to 0.291 (0.25 to 0.33 across the runs, against a 0.40
floor calibrated in the prior era — the only target axis that
failed in all three runs). It remains the only style that fails
its own rules at scale: 7.57 violations per 100 sentences, with
26.7 of 32 pairs passing the gate on average; every excluded pair
in the campaign came from this style. It did lead the paraphrase
check (+7.7 net wins). The style is built for procedure documents,
not chat, and stays in the field for that different philosophy.

### concise (built-in)

The Claude Code built-in style, shipped in the CLI (2.1.237 and
later), not by this plugin; the harness evaluates it as a
comparison point. It is the cheapest arm by far — 504 input tokens
of fixed overhead, a quarter to a third of the plugin styles, and
the shortest answers of the field (token ratio 0.580, per-run 0.53
to 0.66). It is also fully rule-clean: zero linter violations and
32 of 32 gated pairs in all three runs, though its lintable rule
set is small, so a zero rate means less than it would for a larger
rule set. Content survives the cuts well: fact survival 0.747 is
fourth in the field, ahead of plain-language and classic-concise.

The price is clarity as this harness measures it: mean strength
0.347, last in the field and below the unstyled anchor in every
run (0.301 / 0.379 / 0.362, with bootstrap confidence intervals
entirely under 1.0), and −14.3 net wins vs unstyled, the worst of
the field. The reader-value checks lean the same way: comprehension
is a wash (−0.3 net wins mean), but paraphrase (−3.3) and
round-trip (−7.0) are negative. Hedge survival 0.731 sits
mid-field with a wide spread (0.633 to 0.834). The pattern mirrors
classic-concise, amplified: maximal brevity reads as less clear to
the judge, even though the facts largely survive. Note the judge
caveat — the clarity axis is judge-sensitive, and a brevity-first
reader may weigh these answers differently than the judge does.

## Era shift from 2.1.226

The prior published numbers came from CLI 2.1.226; this campaign
re-measured everything under 2.1.239, and the regression targets in
`rules/targets.yaml` are still calibrated on the prior era. Checked
against them, the three runs missed these axes:

- technical-simplified hedge survival failed in all three runs
  (0.25 to 0.33 against the 0.40 floor) — the one consistent break.
- clarity-flow failed rank strength in two runs (0.439, 0.738
  against 0.80) and fact survival in one (0.71 against 0.75).
- Single-run misses: actionable-clarity hedge survival (0.818
  against 0.90) and plain-language hedge survival (0.709 against
  0.74).

The ordering at the top also moved: developer-docs rose past
plain-language, and clarity-flow fell below classic-concise. With
three runs against six, era change and noise are not separable;
the misses are recorded here rather than papered over by a target
edit, and a recalibration of `targets.yaml` for the 2.1.239 era is
a decision for a follow-up change.

## Held-out check (2.1.226 era)

The design loop optimizes against the main prompt set, so the
candidate that wins there can be overfit. The held-out run
([`runs/2026-08-10-holdout`](runs/2026-08-10-holdout/rank.md))
asked 24 unseen prompts, once, under CLI 2.1.226 and without the
built-in Concise arm:

| Competitor | Strength | 95% CI |
|---|---|---|
| plain-language | 3.136 | [2.06, 4.905] |
| actionable-clarity | 1.944 | [1.293, 2.995] |
| clarity-flow | 1.407 | [0.95, 2.166] |
| developer-docs | 1.262 | [0.842, 1.836] |
| classic-concise | 1.113 | [0.741, 1.659] |
| unstyled | 1.0 | n/a |
| technical-simplified | 0.723 | [0.468, 1.1] |

The main-set winner was second here: plain-language scored highest
on the fresh prompts, though the two intervals overlap, and this is
one run of 24 prompts, so the ordering carries wide uncertainty.
No held-out run exists yet for the 2.1.239 era.

## Long-session drift

Drift asks whether a style's rule obedience degrades as a session
grows.

For the built-in Concise style, the 2.1.239-era shallow run
([`runs/2026-08-23-drift`](runs/2026-08-23-drift/drift.md), 15-turn
sessions, 3 repeats, final depth a mean 17,509 tokens — 8.8 percent
of the 200K-token window) measured zero violations at every turn
position: slope 0.0, verdict flat. The null is degenerate (a
threshold of 0.0 from an all-zero series), so the verdict says the
lintable rules never fired, not that a decline was tested against
noise.

The six plugin styles carry 2.1.226-era verdicts only. In the
shallow run
([`runs/2026-08-10-drift`](runs/2026-08-10-drift/drift.md), 15-turn
sessions, 3 repeats per style, final depth 8 to 11 percent of the
200K-token context window), every style came out flat: slopes
between −0.051 and 0.0 violations per 100 sentences per turn, except
technical-simplified at 0.581 — still under its 0.826 permutation
threshold. The deep run
([`runs/2026-08-10-drift-deep`](runs/2026-08-10-drift-deep/drift.md))
drove actionable-clarity through three coherent 15-turn scripts to a
mean final depth of 304,593 tokens — 152.3 percent of the 200K-token
window — and the verdict stayed flat with a non-degenerate null:
slope −0.022 against a 0.069 threshold, p = 0.6979.

## Judge reliability (2.1.226 era)

The verdicts come from model judges, so the harness measures how
much they can be trusted
([`runs/2026-08-08/agreement.md`](runs/2026-08-08/agreement.md), on
the five-style field before actionable-clarity and Concise joined):

| Axis | Cross-vintage arm (`claude-opus-4-5-20251101`, 100 rows/axis) | Cross-line arm (`haiku`, full census) | Verdict |
|---|---|---|---|
| comprehension | 0.977 | 0.970 | stable |
| completeness | 0.924 | 0.906 | stable |
| hedging | 0.815 | 0.804 | stable |
| clarity | 0.600 | 0.686 (939 picks) | judge-sensitive |

Comprehension, completeness, and hedging agree well across judges.
Clarity does not: both arms fall under the 0.7 anchor, so the
Bradley-Terry strengths measure a model preference that another
judge partly disagrees with. This caveat bears directly on the
Concise ranking: its last place rests on the one judge-sensitive
axis, while its strong axes (cost, fidelity, fact survival) are
deterministic or judge-stable.

The human anchor points the same way. The
[spot check](runs/2026-08-10d/spot-check.md) on the acceptance run
of actionable-clarity agreed with the clarity judge on 6 of 12
sampled contests (0.50): four disagreements reversed a decisive
judge pick, two picked a winner where the judge split. The protocol
verdict was "do not accept"; the maintainer overruled it and
recorded the overrule in that file.

## Caveats

- **Three runs, not six.** The 2.1.239-era means rest on three
  full runs; the prior era had six. The spread per axis lives in
  [the comparison](runs/2026-08-23-compare/compare.md), and the
  clarity axis moves the most (standard deviation up to 0.574 on
  Bradley-Terry strength).
- **The regression targets are prior-era.** `rules/targets.yaml`
  was calibrated on 2.1.226-era runs; the misses in
  [Era shift](#era-shift-from-21226) may be era change rather than
  style regressions.
- **Clarity rests on one judge line.** The judged axes come from
  `claude-opus-5`; the clarity axis is judge-sensitive (see
  [Judge reliability](#judge-reliability-21226-era)), and no
  agreement sample exists yet for the 2.1.239 era or the field
  that includes Concise.
- **The held-out, deep-drift, agreement, and spot-check evidence
  is 2.1.226-era.** Those runs predate the pin move and lack the
  Concise arm.
- **actionable-clarity has no independent human validation.** Its
  wording was tuned against the harness that scores it, its human
  spot check failed the acceptance anchor, and its acceptance
  stands on a recorded maintainer overrule.
- **Concise's rule gate is narrow.** The built-in style's prompt
  bans behaviors a linter can only partly see (lead-with-result
  ordering, the 1-to-3-sentence norm); its zero violation rate
  covers the lintable subset, and its styled and baseline rates
  were both zero, so the gate separated nothing in this campaign.
- **Everything is era-specific.** The numbers describe
  `claude-sonnet-5` writing, `claude-opus-5` judging, this prompt
  set, and CLI 2.1.239. A change to any of them re-opens every
  question.

## Data sources

| Run | Contributes | Key files |
|---|---|---|
| [`2026-08-22`](runs/2026-08-22/report.md), [`2026-08-22b`](runs/2026-08-22b/report.md), [`2026-08-22c`](runs/2026-08-22c/report.md) | The three 2.1.239-era campaign runs behind every headline number | `report.md`, `rank.md`, `loss.md`, `value.md`, `cost.md`, `targets.md` |
| [`2026-08-23-compare`](runs/2026-08-23-compare/compare.md) | Three-run means and spread | `compare.md` |
| [`2026-08-23-drift`](runs/2026-08-23-drift/drift.md) | Shallow drift, built-in Concise (2.1.239 era) | `drift.md` |
| [`2026-08-10-holdout`](runs/2026-08-10-holdout/rank.md) | Ranking on 24 unseen prompts (2.1.226 era) | `rank.md`, `targets.md` |
| [`2026-08-10-drift`](runs/2026-08-10-drift/drift.md) | Shallow drift, six plugin styles (2.1.226 era) | `drift.md` |
| [`2026-08-10-drift-deep`](runs/2026-08-10-drift-deep/drift.md) | Deep drift, actionable-clarity (2.1.226 era) | `drift.md` |
| [`2026-08-08`](runs/2026-08-08/agreement.md) | Second-judge agreement (five-style era) | `agreement.md` |
| [`2026-08-10d`](runs/2026-08-10d/spot-check.md) | Human spot check and the acceptance overrule | `spot-check.md` |

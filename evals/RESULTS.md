# Evaluation results

This document reports the latest measured findings for the six
shipped output styles. The top-level `README.md` summarizes these
findings qualitatively; this document carries the numbers, their
spread, and their caveats. For how the measurements work, see
[ARCHITECTURE.md](ARCHITECTURE.md).

> [!NOTE]
> Measured on 2026-08-10, over the campaign runs `2026-08-10d` to
> `2026-08-10i` plus the supporting runs in
> [Data sources](#data-sources). Writer model `claude-sonnet-5`;
> judge `claude-opus-5`; weak reader `claude-haiku-4-5-20251001`;
> Claude Code CLI pinned at 2.1.226. The results are specific to
> these models, prompts, and pins: a model, prompt, or CLI change
> opens a new comparability era and re-opens every question.

## How to read the numbers

Each headline number is the mean over six full runs (32 prompts × 7
arms each); the per-run values and the spread live in
[the six-run comparison](runs/2026-08-10c-compare/compare.md), and
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

Six-run means, ordered by Bradley-Terry strength:

| Style | BT strength | Net wins vs unstyled | Token ratio | Fact survival | Hedge survival | Violation rate | Gated pairs |
|---|---|---|---|---|---|---|---|
| actionable-clarity | 2.424 | +11.5 | 1.182 | 0.791 | 0.915 | 0.28 | 31.5 |
| plain-language | 1.558 | +6.2 | 0.848 | 0.713 | 0.940 | 0.02 | 32.0 |
| developer-docs | 1.500 | +8.0 | 0.957 | 0.751 | 0.859 | 0.25 | 32.0 |
| clarity-flow | 0.918 | −1.7 | 0.847 | 0.765 | 0.839 | 0.00 | 32.0 |
| classic-concise | 0.818 | −3.8 | 0.717 | 0.762 | 0.822 | 0.45 | 32.0 |
| technical-simplified | 0.468 | −10.0 | 0.975 | 0.660 | 0.667 | 7.32 | 27.5 |

## Findings per style

The sections follow the strength order of the table.

### actionable-clarity

The clearest style of the field: mean strength 2.424 (per-run range
1.975 to 3.144), first among the styles in five of the six runs and
second behind plain-language in one, with +11.5 net wins against the
unstyled answer. It keeps the most content — fact survival 0.791,
the highest of the field — and it leads the comprehension check
(+4.2 net wins, the only clearly positive mean). The cost is length:
its output-token ratio of 1.182 makes it the only style that writes
longer answers than the unstyled baseline, and its style block adds
the largest input overhead, 2,061 tokens per request.

Caveats:

- Hedge survival averaged 0.915 but missed the 0.90 regression
  floor in two of the six runs (0.75 in `2026-08-10g`, 0.80 in
  `2026-08-10i`), against unstyled baselines that hedge more than
  the acceptance baselines did. Where a careful answer says
  "maybe", this style sometimes sounds more certain than it should.
- On the held-out prompt set it ranked second, behind
  plain-language; see [Held-out check](#held-out-check).
- Unlike the other styles, it carries no independent human
  validation: the wording was tuned against the harness itself, and
  the [human spot check](runs/2026-08-10d/spot-check.md) of its
  acceptance agreed with the clarity judge on only 6 of 12 contests
  (0.50, under the 0.7 anchor). The maintainer accepted the style
  by explicit overrule, recorded in that file.

### plain-language

Second by mean strength (1.558) on the main set, and the best style
at keeping uncertainty: hedge survival 0.940, the highest of the
field. It shortens answers (token ratio 0.848) and stays nearly
violation-free (0.02 per 100 sentences). On the held-out set it
scored highest of all styles. Its weakness is detail: fact survival
0.713 is the lowest of the field after technical-simplified — the
push to shorten can cut facts a reader needs. Its holdout run also
missed its own hedge-survival floor (0.667 against 0.74).

### developer-docs

Third by mean strength (1.500) with +8.0 net wins against the
unstyled answer, at nearly normal length (token ratio 0.957). Fact
survival 0.751 sits mid-field, and it did well on the paraphrase
(+6.5) and round-trip (+8.0) checks. Hedge survival averaged 0.859
but ranged down to 0.667 across the runs: the direct tone sometimes
turns a "maybe" into a certainty. It passed every checked regression
axis in the latest run and on the held-out set.

### clarity-flow

Mean strength 0.918 — at the level of the unstyled baseline (−1.7
net wins), so the judge saw no clarity gain. The style still earns
its keep on content: fact survival 0.765 is second only to
actionable-clarity, it shortens answers (0.847, with the widest
per-run spread, 0.60 to 1.04), and it was the only style with zero
measured violations in all six runs.

### classic-concise

The shortest answers of the field: token ratio 0.717. Fact survival
holds up well (0.762) despite the cuts, but the concision costs
clarity: mean strength 0.818, below the unstyled baseline, with
negative net wins on the comprehension (−3.3) and round-trip (−6.7)
checks. Hedge survival 0.822 sits mid-field.

### technical-simplified

Last on every chat-facing measure: strength 0.468, −10.0 net wins,
fact survival 0.660, and hedge survival 0.667, all the lowest of
the field. It is also the only style that fails its own rules at
scale: 7.32 violations per 100 sentences (the next style is at
0.45), with only 27.5 of 32 pairs passing the gate on average. Its
holdout run exceeded its output-token bound (1.49 against the 1.15
cap), and its shallow drift slope (0.581) was the closest of the
field to a "growing" verdict, though still flat under its 0.826
threshold. The style is built for procedure documents, not chat,
and stays in the field for that different philosophy.

## Held-out check

The design loop optimizes against the main prompt set, so the
candidate that wins there can be overfit. The held-out run
([`runs/2026-08-10-holdout`](runs/2026-08-10-holdout/rank.md)) asked
24 unseen prompts, once:

| Competitor | Strength | 95% CI |
|---|---|---|
| plain-language | 3.136 | [2.06, 4.905] |
| actionable-clarity | 1.944 | [1.293, 2.995] |
| clarity-flow | 1.407 | [0.95, 2.166] |
| developer-docs | 1.262 | [0.842, 1.836] |
| classic-concise | 1.113 | [0.741, 1.659] |
| unstyled | 1.0 | n/a |
| technical-simplified | 0.723 | [0.468, 1.1] |

The main-set winner is second here: plain-language scored highest on
the fresh prompts, though the two intervals overlap, and this is one
run of 24 prompts, so the ordering carries wide uncertainty. On the
held-out [targets check](runs/2026-08-10-holdout/targets.md),
actionable-clarity passed 3 of 5 axes (fact survival 0.72 against
the 0.73 floor, hedge survival 0.75 against 0.90), plain-language
and technical-simplified passed 4 of 5, and the other three styles
passed every axis.

## Long-session drift

Drift asks whether a style's rule obedience degrades as a session
grows. In the shallow run
([`runs/2026-08-10-drift`](runs/2026-08-10-drift/drift.md), 15-turn
sessions, 3 repeats per style, final depth 8 to 11 percent of the
200K-token context window), every style came out flat: slopes
between −0.051 and 0.0 violations per 100 sentences per turn, except
technical-simplified at 0.581 — still under its 0.826 permutation
threshold.

The deep run
([`runs/2026-08-10-drift-deep`](runs/2026-08-10-drift-deep/drift.md))
drove actionable-clarity through three coherent 15-turn scripts to a
mean final depth of 304,593 tokens — 152.3 percent of the
200K-token window (per-script finals 354,264 / 392,400 / 167,114).
The verdict stayed flat with a non-degenerate null: slope −0.022
against a 0.069 threshold, p = 0.6979. The other five styles have
shallow verdicts only.

## Judge reliability

The verdicts come from model judges, so the harness measures how
much they can be trusted
([`runs/2026-08-08/agreement.md`](runs/2026-08-08/agreement.md), on
the five-style field before actionable-clarity joined):

| Axis | Cross-vintage arm (`claude-opus-4-5-20251101`, 100 rows/axis) | Cross-line arm (`haiku`, full census) | Verdict |
|---|---|---|---|
| comprehension | 0.977 | 0.970 | stable |
| completeness | 0.924 | 0.906 | stable |
| hedging | 0.815 | 0.804 | stable |
| clarity | 0.600 | 0.686 (939 picks) | judge-sensitive |

Comprehension, completeness, and hedging agree well across judges.
Clarity does not: both arms fall under the 0.7 anchor, so the
Bradley-Terry strengths measure a model preference that another
judge partly disagrees with.

The human anchor points the same way. The
[spot check](runs/2026-08-10d/spot-check.md) on the acceptance run
of actionable-clarity agreed with the clarity judge on 6 of 12
sampled contests (0.50): four disagreements reversed a decisive
judge pick, two picked a winner where the judge split. The protocol
verdict was "do not accept"; the maintainer overruled it and
recorded the overrule in that file.

## Caveats

- **The six runs are not perfectly identical.** The comparison
  warns of a gate-config hash mismatch: the gate policy changed
  between runs `d`–`f` and `g`–`i`. A threshold edit changes pass
  marks, never measured rates.
- **The extension runs reuse pre-pin baselines.** Runs
  `2026-08-10g` to `i` import stored answers from
  `runs/2026-08-07` to `2026-08-08b`; `2026-08-10i` generated 32
  answers live and imported 192, and its report warns that the
  answers come from more than one Claude Code version and plugin
  environment.
- **Clarity rests on one judge line.** The judged axes come from
  `claude-opus-5`; the clarity axis is judge-sensitive (see
  [Judge reliability](#judge-reliability)), and the second-judge
  sample covers the five-style era only — no agreement sample
  exists yet for the field that includes actionable-clarity.
- **actionable-clarity has no independent human validation.** Its
  wording was tuned against the harness that scores it, its human
  spot check failed the acceptance anchor, and its acceptance
  stands on a recorded maintainer overrule.
- **Everything is era-specific.** The numbers describe
  `claude-sonnet-5` writing, `claude-opus-5` judging, this prompt
  set, and CLI 2.1.226. A change to any of them re-opens every
  question.

## Data sources

| Run | Contributes | Key files |
|---|---|---|
| [`2026-08-10c-compare`](runs/2026-08-10c-compare/compare.md) | Six-run means and spread over `2026-08-10d`–`i`; the gate-hash warning | `compare.md` |
| [`2026-08-10-holdout`](runs/2026-08-10-holdout/rank.md) | Ranking and targets on 24 unseen prompts | `rank.md`, `targets.md` |
| [`2026-08-10i`](runs/2026-08-10i/targets.md) | Latest regression check, input overhead per style, reuse warnings | `targets.md`, `cost.md`, `report.md` |
| [`2026-08-10-drift`](runs/2026-08-10-drift/drift.md) | Shallow drift, all six styles | `drift.md` |
| [`2026-08-10-drift-deep`](runs/2026-08-10-drift-deep/drift.md) | Deep drift, actionable-clarity | `drift.md` |
| [`2026-08-08`](runs/2026-08-08/agreement.md) | Second-judge agreement (five-style era) | `agreement.md` |
| [`2026-08-10d`](runs/2026-08-10d/spot-check.md) | Human spot check and the acceptance overrule | `spot-check.md` |

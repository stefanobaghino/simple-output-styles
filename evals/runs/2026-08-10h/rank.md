# Clarity-ranking report

Every contest shows a blind judge the two answers of one prompt,
in both orders, and the judge picks the clearer text. This tool
relaxes one harness invariant on purpose: a clarity contest is a
choice, so a judge call sees both answers of a prompt side by
side. Blindness holds through the absence of labels: no prompt
names a style or an arm, and the position mapping lives only in
the raw rows. The judge model differs from the writer of the
answers. The unstyled answer competes as its own arm and anchors
the strength scale.

Caveats:

- The judge is a proxy reader: the picks state a model preference for clarity, not a measured human outcome.
- The unstyled competitor is ungated: every styled competitor passed its rule gate, and the unstyled answer has no gate.
- A clarity pick can reward the shorter text. The length-confound section states the correlation.

Judge: opus. Judged on 2026-08-10T16:30:36+00:00.

## Matchups

| A | B | Contests | A wins | B wins | Splits | Unscored | Net (A) |
|---|---|---|---|---|---|---|---|
| actionable-clarity | clarity-flow | 30 | 19 | 2 | 9 | 0 | 17 |
| actionable-clarity | classic-concise | 30 | 16 | 5 | 9 | 0 | 11 |
| actionable-clarity | developer-docs | 30 | 14 | 7 | 9 | 0 | 7 |
| actionable-clarity | plain-language | 30 | 13 | 7 | 10 | 0 | 6 |
| actionable-clarity | technical-simplified | 28 | 25 | 1 | 2 | 0 | 24 |
| actionable-clarity | unstyled | 30 | 14 | 8 | 8 | 0 | 6 |
| clarity-flow | classic-concise | 32 | 10 | 12 | 10 | 0 | -2 |
| clarity-flow | developer-docs | 32 | 8 | 11 | 13 | 0 | -3 |
| clarity-flow | plain-language | 32 | 11 | 14 | 7 | 0 | -3 |
| clarity-flow | technical-simplified | 30 | 15 | 5 | 10 | 0 | 10 |
| clarity-flow | unstyled | 32 | 12 | 12 | 8 | 0 | 0 |
| classic-concise | developer-docs | 32 | 7 | 14 | 11 | 0 | -7 |
| classic-concise | plain-language | 32 | 13 | 16 | 3 | 0 | -3 |
| classic-concise | technical-simplified | 30 | 14 | 4 | 12 | 0 | 10 |
| classic-concise | unstyled | 32 | 14 | 10 | 8 | 0 | 4 |
| developer-docs | plain-language | 32 | 14 | 10 | 8 | 0 | 4 |
| developer-docs | technical-simplified | 30 | 19 | 4 | 7 | 0 | 15 |
| developer-docs | unstyled | 32 | 11 | 8 | 13 | 0 | 3 |
| plain-language | technical-simplified | 30 | 18 | 4 | 8 | 0 | 14 |
| plain-language | unstyled | 32 | 11 | 11 | 10 | 0 | 0 |
| technical-simplified | unstyled | 30 | 5 | 18 | 7 | 0 | -13 |

## Win matrix

A cell holds the points of the row competitor against the column
competitor: 1 per decisive win plus 0.5 per split.

| | actionable-clarity | clarity-flow | classic-concise | developer-docs | plain-language | technical-simplified | unstyled |
|---|---|---|---|---|---|---|---|
| actionable-clarity | - | 23.5 | 20.5 | 18.5 | 18.0 | 26.0 | 18.0 |
| clarity-flow | 6.5 | - | 15.0 | 14.5 | 14.5 | 20.0 | 16.0 |
| classic-concise | 9.5 | 17.0 | - | 12.5 | 14.5 | 20.0 | 18.0 |
| developer-docs | 11.5 | 17.5 | 19.5 | - | 18.0 | 22.5 | 17.5 |
| plain-language | 12.0 | 17.5 | 17.5 | 14.0 | - | 22.0 | 16.0 |
| technical-simplified | 2.0 | 10.0 | 10.0 | 7.5 | 8.0 | - | 8.5 |
| unstyled | 12.0 | 16.0 | 14.0 | 14.5 | 16.0 | 21.5 | - |

## Bradley-Terry strengths

The scale is anchored on unstyled at strength 1.0.

The table lists the competitors from the highest strength to the
lowest. A competitor without a finite strength comes last.

| Competitor | Strength | 95% CI |
|---|---|---|
| actionable-clarity | 2.12 | [1.469, 2.955] |
| developer-docs | 1.27 | [0.926, 1.724] |
| plain-language | 1.1 | [0.771, 1.527] |
| unstyled | 1.0 | n/a |
| classic-concise | 0.953 | [0.673, 1.306] |
| clarity-flow | 0.866 | [0.628, 1.181] |
| technical-simplified | 0.394 | [0.269, 0.544] |

The interval comes from 1000 bootstrap resamples of the scored contests (seed 0).

## Position bias

First-pick rate: 0.41 over 1296 usable picks.
Split rate: 0.281 over 648 judged contests.

## Per task type

### code-review

| A | B | Contests | A wins | B wins | Splits | Unscored | Net (A) |
|---|---|---|---|---|---|---|---|
| actionable-clarity | clarity-flow | 7 | 5 | 0 | 2 | 0 | 5 |
| actionable-clarity | classic-concise | 7 | 3 | 1 | 3 | 0 | 2 |
| actionable-clarity | developer-docs | 7 | 5 | 0 | 2 | 0 | 5 |
| actionable-clarity | plain-language | 7 | 4 | 1 | 2 | 0 | 3 |
| actionable-clarity | technical-simplified | 7 | 7 | 0 | 0 | 0 | 7 |
| actionable-clarity | unstyled | 7 | 3 | 1 | 3 | 0 | 2 |
| clarity-flow | classic-concise | 8 | 2 | 2 | 4 | 0 | 0 |
| clarity-flow | developer-docs | 8 | 2 | 2 | 4 | 0 | 0 |
| clarity-flow | plain-language | 8 | 5 | 2 | 1 | 0 | 3 |
| clarity-flow | technical-simplified | 8 | 4 | 1 | 3 | 0 | 3 |
| clarity-flow | unstyled | 8 | 4 | 2 | 2 | 0 | 2 |
| classic-concise | developer-docs | 8 | 2 | 3 | 3 | 0 | -1 |
| classic-concise | plain-language | 8 | 4 | 3 | 1 | 0 | 1 |
| classic-concise | technical-simplified | 8 | 2 | 2 | 4 | 0 | 0 |
| classic-concise | unstyled | 8 | 5 | 2 | 1 | 0 | 3 |
| developer-docs | plain-language | 8 | 4 | 3 | 1 | 0 | 1 |
| developer-docs | technical-simplified | 8 | 5 | 2 | 1 | 0 | 3 |
| developer-docs | unstyled | 8 | 4 | 3 | 1 | 0 | 1 |
| plain-language | technical-simplified | 8 | 2 | 3 | 3 | 0 | -1 |
| plain-language | unstyled | 8 | 1 | 4 | 3 | 0 | -3 |
| technical-simplified | unstyled | 8 | 2 | 2 | 4 | 0 | 0 |

### debugging

| A | B | Contests | A wins | B wins | Splits | Unscored | Net (A) |
|---|---|---|---|---|---|---|---|
| actionable-clarity | clarity-flow | 8 | 4 | 0 | 4 | 0 | 4 |
| actionable-clarity | classic-concise | 8 | 4 | 3 | 1 | 0 | 1 |
| actionable-clarity | developer-docs | 8 | 5 | 3 | 0 | 0 | 2 |
| actionable-clarity | plain-language | 8 | 1 | 3 | 4 | 0 | -2 |
| actionable-clarity | technical-simplified | 7 | 4 | 1 | 2 | 0 | 3 |
| actionable-clarity | unstyled | 8 | 2 | 4 | 2 | 0 | -2 |
| clarity-flow | classic-concise | 8 | 2 | 5 | 1 | 0 | -3 |
| clarity-flow | developer-docs | 8 | 3 | 2 | 3 | 0 | 1 |
| clarity-flow | plain-language | 8 | 3 | 3 | 2 | 0 | 0 |
| clarity-flow | technical-simplified | 7 | 2 | 3 | 2 | 0 | -1 |
| clarity-flow | unstyled | 8 | 1 | 6 | 1 | 0 | -5 |
| classic-concise | developer-docs | 8 | 2 | 3 | 3 | 0 | -1 |
| classic-concise | plain-language | 8 | 4 | 2 | 2 | 0 | 2 |
| classic-concise | technical-simplified | 7 | 4 | 1 | 2 | 0 | 3 |
| classic-concise | unstyled | 8 | 4 | 2 | 2 | 0 | 2 |
| developer-docs | plain-language | 8 | 3 | 1 | 4 | 0 | 2 |
| developer-docs | technical-simplified | 7 | 3 | 1 | 3 | 0 | 2 |
| developer-docs | unstyled | 8 | 1 | 3 | 4 | 0 | -2 |
| plain-language | technical-simplified | 7 | 5 | 0 | 2 | 0 | 5 |
| plain-language | unstyled | 8 | 2 | 4 | 2 | 0 | -2 |
| technical-simplified | unstyled | 7 | 0 | 6 | 1 | 0 | -6 |

### explanation

| A | B | Contests | A wins | B wins | Splits | Unscored | Net (A) |
|---|---|---|---|---|---|---|---|
| actionable-clarity | clarity-flow | 7 | 6 | 0 | 1 | 0 | 6 |
| actionable-clarity | classic-concise | 7 | 4 | 1 | 2 | 0 | 3 |
| actionable-clarity | developer-docs | 7 | 1 | 2 | 4 | 0 | -1 |
| actionable-clarity | plain-language | 7 | 5 | 1 | 1 | 0 | 4 |
| actionable-clarity | technical-simplified | 7 | 7 | 0 | 0 | 0 | 7 |
| actionable-clarity | unstyled | 7 | 4 | 2 | 1 | 0 | 2 |
| clarity-flow | classic-concise | 8 | 2 | 3 | 3 | 0 | -1 |
| clarity-flow | developer-docs | 8 | 0 | 6 | 2 | 0 | -6 |
| clarity-flow | plain-language | 8 | 2 | 5 | 1 | 0 | -3 |
| clarity-flow | technical-simplified | 8 | 4 | 1 | 3 | 0 | 3 |
| clarity-flow | unstyled | 8 | 3 | 4 | 1 | 0 | -1 |
| classic-concise | developer-docs | 8 | 2 | 4 | 2 | 0 | -2 |
| classic-concise | plain-language | 8 | 4 | 4 | 0 | 0 | 0 |
| classic-concise | technical-simplified | 8 | 7 | 1 | 0 | 0 | 6 |
| classic-concise | unstyled | 8 | 3 | 4 | 1 | 0 | -1 |
| developer-docs | plain-language | 8 | 6 | 1 | 1 | 0 | 5 |
| developer-docs | technical-simplified | 8 | 7 | 0 | 1 | 0 | 7 |
| developer-docs | unstyled | 8 | 5 | 1 | 2 | 0 | 4 |
| plain-language | technical-simplified | 8 | 6 | 1 | 1 | 0 | 5 |
| plain-language | unstyled | 8 | 3 | 2 | 3 | 0 | 1 |
| technical-simplified | unstyled | 8 | 1 | 6 | 1 | 0 | -5 |

### summarization

| A | B | Contests | A wins | B wins | Splits | Unscored | Net (A) |
|---|---|---|---|---|---|---|---|
| actionable-clarity | clarity-flow | 8 | 4 | 2 | 2 | 0 | 2 |
| actionable-clarity | classic-concise | 8 | 5 | 0 | 3 | 0 | 5 |
| actionable-clarity | developer-docs | 8 | 3 | 2 | 3 | 0 | 1 |
| actionable-clarity | plain-language | 8 | 3 | 2 | 3 | 0 | 1 |
| actionable-clarity | technical-simplified | 7 | 7 | 0 | 0 | 0 | 7 |
| actionable-clarity | unstyled | 8 | 5 | 1 | 2 | 0 | 4 |
| clarity-flow | classic-concise | 8 | 4 | 2 | 2 | 0 | 2 |
| clarity-flow | developer-docs | 8 | 3 | 1 | 4 | 0 | 2 |
| clarity-flow | plain-language | 8 | 1 | 4 | 3 | 0 | -3 |
| clarity-flow | technical-simplified | 7 | 5 | 0 | 2 | 0 | 5 |
| clarity-flow | unstyled | 8 | 4 | 0 | 4 | 0 | 4 |
| classic-concise | developer-docs | 8 | 1 | 4 | 3 | 0 | -3 |
| classic-concise | plain-language | 8 | 1 | 7 | 0 | 0 | -6 |
| classic-concise | technical-simplified | 7 | 1 | 0 | 6 | 0 | 1 |
| classic-concise | unstyled | 8 | 2 | 2 | 4 | 0 | 0 |
| developer-docs | plain-language | 8 | 1 | 5 | 2 | 0 | -4 |
| developer-docs | technical-simplified | 7 | 4 | 1 | 2 | 0 | 3 |
| developer-docs | unstyled | 8 | 1 | 1 | 6 | 0 | 0 |
| plain-language | technical-simplified | 7 | 5 | 0 | 2 | 0 | 5 |
| plain-language | unstyled | 8 | 5 | 1 | 2 | 0 | 4 |
| technical-simplified | unstyled | 7 | 2 | 4 | 1 | 0 | -2 |

## Length confound

Samples: 644 contests with unequal word counts.
Pearson: 0.11. Spearman: 0.216.
Longer-text win rate: 0.646.

## Call timing

A stored call row holds two times: duration_ms is the model
time that the CLI reports, and wall_ms is the wall clock of
the subprocess. The difference is the startup cost of one CLI
call.

Calls: 362, measured: 362.
Mean duration: 3381 ms. Mean wall: 20576 ms. Mean startup: 17195 ms.

## Harness spend

A stored call row holds the token counts of its call: the
uncached input, cache-write input, cache-read input, and
output tokens. The cache-read share is the cache-read total
over the whole input total.

Calls: 362, measured: 362.
Input tokens: 724 uncached, 781178 cache write, 743186 cache read. Output tokens: 13010.
Cache-read share: 0.487.
Cache writes by lifetime: 781178 at 5 minutes, 0 at 1 hour.

## Reuse

Reused rows: 934, imported from 2026-08-08.
Live calls of this run: 362.

The freshness sample re-ran 6 imported verdicts live; 6 agree.

Clarity picks: 0 of 6 disagree; the tolerance is 5.

A verdict axis compares on exact equality, and one differing
verdict is a warning. The clarity picks carry an aggregate
tolerance instead: the sample warns only when its disagreement
count clears a one-sided binomial tail of 0.05 at the
0.4 cross-judge disagreement rate of the
runs/2026-08-08 second-judge sample. Two judges disagree
with each other at least as often as one judge disagrees with
itself later, so the cross-judge rate bounds the reuse noise
from above.

## Warnings

- technical-simplified/summarization-07: the pair failed the gate, excluded
- technical-simplified/debugging-07: the pair failed the gate, excluded
- actionable-clarity/explanation-08: the pair failed the gate, excluded
- actionable-clarity/code-review-01: the pair failed the gate, excluded

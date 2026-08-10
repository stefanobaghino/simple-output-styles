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

Judge: opus. Judged on 2026-08-10T13:52:53+00:00.

## Matchups

| A | B | Contests | A wins | B wins | Splits | Unscored | Net (A) |
|---|---|---|---|---|---|---|---|
| actionable-clarity | clarity-flow | 32 | 15 | 4 | 12 | 1 | 11 |
| actionable-clarity | classic-concise | 32 | 19 | 7 | 6 | 0 | 12 |
| actionable-clarity | developer-docs | 32 | 13 | 6 | 13 | 0 | 7 |
| actionable-clarity | plain-language | 32 | 13 | 8 | 11 | 0 | 5 |
| actionable-clarity | technical-simplified | 26 | 22 | 0 | 4 | 0 | 22 |
| actionable-clarity | unstyled | 32 | 14 | 7 | 11 | 0 | 7 |
| clarity-flow | classic-concise | 32 | 15 | 6 | 11 | 0 | 9 |
| clarity-flow | developer-docs | 32 | 9 | 15 | 8 | 0 | -6 |
| clarity-flow | plain-language | 32 | 9 | 14 | 9 | 0 | -5 |
| clarity-flow | technical-simplified | 26 | 19 | 3 | 4 | 0 | 16 |
| clarity-flow | unstyled | 32 | 12 | 10 | 10 | 0 | 2 |
| classic-concise | developer-docs | 32 | 8 | 17 | 7 | 0 | -9 |
| classic-concise | plain-language | 32 | 11 | 14 | 7 | 0 | -3 |
| classic-concise | technical-simplified | 26 | 12 | 6 | 8 | 0 | 6 |
| classic-concise | unstyled | 32 | 10 | 11 | 11 | 0 | -1 |
| developer-docs | plain-language | 32 | 12 | 13 | 7 | 0 | -1 |
| developer-docs | technical-simplified | 26 | 15 | 4 | 7 | 0 | 11 |
| developer-docs | unstyled | 32 | 14 | 6 | 12 | 0 | 8 |
| plain-language | technical-simplified | 26 | 18 | 5 | 3 | 0 | 13 |
| plain-language | unstyled | 32 | 13 | 7 | 12 | 0 | 6 |
| technical-simplified | unstyled | 26 | 5 | 13 | 8 | 0 | -8 |

## Win matrix

A cell holds the points of the row competitor against the column
competitor: 1 per decisive win plus 0.5 per split.

| | actionable-clarity | clarity-flow | classic-concise | developer-docs | plain-language | technical-simplified | unstyled |
|---|---|---|---|---|---|---|---|
| actionable-clarity | - | 21.0 | 22.0 | 19.5 | 18.5 | 24.0 | 19.5 |
| clarity-flow | 10.0 | - | 20.5 | 13.0 | 13.5 | 21.0 | 17.0 |
| classic-concise | 10.0 | 11.5 | - | 11.5 | 14.5 | 16.0 | 15.5 |
| developer-docs | 12.5 | 19.0 | 20.5 | - | 15.5 | 18.5 | 20.0 |
| plain-language | 13.5 | 18.5 | 17.5 | 16.5 | - | 19.5 | 19.0 |
| technical-simplified | 2.0 | 5.0 | 10.0 | 7.5 | 6.5 | - | 9.0 |
| unstyled | 12.5 | 15.0 | 16.5 | 12.0 | 13.0 | 17.0 | - |

## Bradley-Terry strengths

The scale is anchored on unstyled at strength 1.0.

The table lists the competitors from the highest strength to the
lowest. A competitor without a finite strength comes last.

| Competitor | Strength | 95% CI |
|---|---|---|
| actionable-clarity | 2.158 | [1.546, 3.024] |
| developer-docs | 1.47 | [1.069, 2.055] |
| plain-language | 1.428 | [1.043, 1.988] |
| clarity-flow | 1.197 | [0.861, 1.64] |
| unstyled | 1.0 | n/a |
| classic-concise | 0.873 | [0.621, 1.192] |
| technical-simplified | 0.438 | [0.298, 0.628] |

The interval comes from 1000 bootstrap resamples of the scored contests (seed 0).

## Position bias

First-pick rate: 0.415 over 1271 usable picks.
Split rate: 0.285 over 635 judged contests.

## Per task type

### code-review

| A | B | Contests | A wins | B wins | Splits | Unscored | Net (A) |
|---|---|---|---|---|---|---|---|
| actionable-clarity | clarity-flow | 8 | 3 | 2 | 3 | 0 | 1 |
| actionable-clarity | classic-concise | 8 | 5 | 2 | 1 | 0 | 3 |
| actionable-clarity | developer-docs | 8 | 5 | 1 | 2 | 0 | 4 |
| actionable-clarity | plain-language | 8 | 5 | 0 | 3 | 0 | 5 |
| actionable-clarity | technical-simplified | 6 | 5 | 0 | 1 | 0 | 5 |
| actionable-clarity | unstyled | 8 | 6 | 1 | 1 | 0 | 5 |
| clarity-flow | classic-concise | 8 | 6 | 0 | 2 | 0 | 6 |
| clarity-flow | developer-docs | 8 | 3 | 3 | 2 | 0 | 0 |
| clarity-flow | plain-language | 8 | 4 | 3 | 1 | 0 | 1 |
| clarity-flow | technical-simplified | 6 | 4 | 1 | 1 | 0 | 3 |
| clarity-flow | unstyled | 8 | 5 | 0 | 3 | 0 | 5 |
| classic-concise | developer-docs | 8 | 2 | 5 | 1 | 0 | -3 |
| classic-concise | plain-language | 8 | 3 | 4 | 1 | 0 | -1 |
| classic-concise | technical-simplified | 6 | 4 | 1 | 1 | 0 | 3 |
| classic-concise | unstyled | 8 | 5 | 1 | 2 | 0 | 4 |
| developer-docs | plain-language | 8 | 4 | 2 | 2 | 0 | 2 |
| developer-docs | technical-simplified | 6 | 4 | 2 | 0 | 0 | 2 |
| developer-docs | unstyled | 8 | 6 | 1 | 1 | 0 | 5 |
| plain-language | technical-simplified | 6 | 2 | 3 | 1 | 0 | -1 |
| plain-language | unstyled | 8 | 5 | 1 | 2 | 0 | 4 |
| technical-simplified | unstyled | 6 | 2 | 2 | 2 | 0 | 0 |

### debugging

| A | B | Contests | A wins | B wins | Splits | Unscored | Net (A) |
|---|---|---|---|---|---|---|---|
| actionable-clarity | clarity-flow | 8 | 6 | 0 | 2 | 0 | 6 |
| actionable-clarity | classic-concise | 8 | 5 | 2 | 1 | 0 | 3 |
| actionable-clarity | developer-docs | 8 | 5 | 1 | 2 | 0 | 4 |
| actionable-clarity | plain-language | 8 | 3 | 4 | 1 | 0 | -1 |
| actionable-clarity | technical-simplified | 6 | 5 | 0 | 1 | 0 | 5 |
| actionable-clarity | unstyled | 8 | 3 | 2 | 3 | 0 | 1 |
| clarity-flow | classic-concise | 8 | 5 | 0 | 3 | 0 | 5 |
| clarity-flow | developer-docs | 8 | 2 | 2 | 4 | 0 | 0 |
| clarity-flow | plain-language | 8 | 1 | 4 | 3 | 0 | -3 |
| clarity-flow | technical-simplified | 6 | 6 | 0 | 0 | 0 | 6 |
| clarity-flow | unstyled | 8 | 1 | 5 | 2 | 0 | -4 |
| classic-concise | developer-docs | 8 | 1 | 6 | 1 | 0 | -5 |
| classic-concise | plain-language | 8 | 1 | 5 | 2 | 0 | -4 |
| classic-concise | technical-simplified | 6 | 1 | 3 | 2 | 0 | -2 |
| classic-concise | unstyled | 8 | 0 | 5 | 3 | 0 | -5 |
| developer-docs | plain-language | 8 | 1 | 6 | 1 | 0 | -5 |
| developer-docs | technical-simplified | 6 | 3 | 1 | 2 | 0 | 2 |
| developer-docs | unstyled | 8 | 2 | 1 | 5 | 0 | 1 |
| plain-language | technical-simplified | 6 | 5 | 1 | 0 | 0 | 4 |
| plain-language | unstyled | 8 | 3 | 2 | 3 | 0 | 1 |
| technical-simplified | unstyled | 6 | 1 | 5 | 0 | 0 | -4 |

### explanation

| A | B | Contests | A wins | B wins | Splits | Unscored | Net (A) |
|---|---|---|---|---|---|---|---|
| actionable-clarity | clarity-flow | 8 | 4 | 1 | 2 | 1 | 3 |
| actionable-clarity | classic-concise | 8 | 4 | 2 | 2 | 0 | 2 |
| actionable-clarity | developer-docs | 8 | 1 | 2 | 5 | 0 | -1 |
| actionable-clarity | plain-language | 8 | 3 | 3 | 2 | 0 | 0 |
| actionable-clarity | technical-simplified | 7 | 6 | 0 | 1 | 0 | 6 |
| actionable-clarity | unstyled | 8 | 3 | 3 | 2 | 0 | 0 |
| clarity-flow | classic-concise | 8 | 1 | 5 | 2 | 0 | -4 |
| clarity-flow | developer-docs | 8 | 0 | 7 | 1 | 0 | -7 |
| clarity-flow | plain-language | 8 | 3 | 4 | 1 | 0 | -1 |
| clarity-flow | technical-simplified | 7 | 5 | 1 | 1 | 0 | 4 |
| clarity-flow | unstyled | 8 | 1 | 4 | 3 | 0 | -3 |
| classic-concise | developer-docs | 8 | 3 | 3 | 2 | 0 | 0 |
| classic-concise | plain-language | 8 | 6 | 2 | 0 | 0 | 4 |
| classic-concise | technical-simplified | 7 | 4 | 1 | 2 | 0 | 3 |
| classic-concise | unstyled | 8 | 2 | 3 | 3 | 0 | -1 |
| developer-docs | plain-language | 8 | 4 | 2 | 2 | 0 | 2 |
| developer-docs | technical-simplified | 7 | 5 | 0 | 2 | 0 | 5 |
| developer-docs | unstyled | 8 | 2 | 2 | 4 | 0 | 0 |
| plain-language | technical-simplified | 7 | 5 | 0 | 2 | 0 | 5 |
| plain-language | unstyled | 8 | 2 | 2 | 4 | 0 | 0 |
| technical-simplified | unstyled | 7 | 0 | 4 | 3 | 0 | -4 |

### summarization

| A | B | Contests | A wins | B wins | Splits | Unscored | Net (A) |
|---|---|---|---|---|---|---|---|
| actionable-clarity | clarity-flow | 8 | 2 | 1 | 5 | 0 | 1 |
| actionable-clarity | classic-concise | 8 | 5 | 1 | 2 | 0 | 4 |
| actionable-clarity | developer-docs | 8 | 2 | 2 | 4 | 0 | 0 |
| actionable-clarity | plain-language | 8 | 2 | 1 | 5 | 0 | 1 |
| actionable-clarity | technical-simplified | 7 | 6 | 0 | 1 | 0 | 6 |
| actionable-clarity | unstyled | 8 | 2 | 1 | 5 | 0 | 1 |
| clarity-flow | classic-concise | 8 | 3 | 1 | 4 | 0 | 2 |
| clarity-flow | developer-docs | 8 | 4 | 3 | 1 | 0 | 1 |
| clarity-flow | plain-language | 8 | 1 | 3 | 4 | 0 | -2 |
| clarity-flow | technical-simplified | 7 | 4 | 1 | 2 | 0 | 3 |
| clarity-flow | unstyled | 8 | 5 | 1 | 2 | 0 | 4 |
| classic-concise | developer-docs | 8 | 2 | 3 | 3 | 0 | -1 |
| classic-concise | plain-language | 8 | 1 | 3 | 4 | 0 | -2 |
| classic-concise | technical-simplified | 7 | 3 | 1 | 3 | 0 | 2 |
| classic-concise | unstyled | 8 | 3 | 2 | 3 | 0 | 1 |
| developer-docs | plain-language | 8 | 3 | 3 | 2 | 0 | 0 |
| developer-docs | technical-simplified | 7 | 3 | 1 | 3 | 0 | 2 |
| developer-docs | unstyled | 8 | 4 | 2 | 2 | 0 | 2 |
| plain-language | technical-simplified | 7 | 6 | 1 | 0 | 0 | 5 |
| plain-language | unstyled | 8 | 3 | 2 | 3 | 0 | 1 |
| technical-simplified | unstyled | 7 | 2 | 2 | 3 | 0 | 0 |

## Length confound

Samples: 631 contests with unequal word counts.
Pearson: 0.166. Spearman: 0.251.
Longer-text win rate: 0.673.

## Call timing

A stored call row holds two times: duration_ms is the model
time that the CLI reports, and wall_ms is the wall clock of
the subprocess. The difference is the startup cost of one CLI
call.

Calls: 378, measured: 378.
Mean duration: 3818 ms. Mean wall: 20431 ms. Mean startup: 16613 ms.

## Harness spend

A stored call row holds the token counts of its call: the
uncached input, cache-write input, cache-read input, and
output tokens. The cache-read share is the cache-read total
over the whole input total.

Calls: 378, measured: 378.
Input tokens: 756 uncached, 810458 cache write, 780827 cache read. Output tokens: 21893.
Cache-read share: 0.49.
Cache writes by lifetime: 810458 at 5 minutes, 0 at 1 hour.

## Reuse

Reused rows: 894, imported from 2026-08-10c.
Live calls of this run: 378.

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

- technical-simplified/explanation-08: the pair failed the gate, excluded
- technical-simplified/code-review-03: the pair failed the gate, excluded
- technical-simplified/code-review-06: the pair failed the gate, excluded
- technical-simplified/summarization-07: the pair failed the gate, excluded
- technical-simplified/debugging-07: the pair failed the gate, excluded
- technical-simplified/debugging-08: the pair failed the gate, excluded
- actionable-clarity vs clarity-flow on explanation-04: the judge gave no usable pick for the order with clarity-flow first, so the contest is unscored
- actionable-clarity vs clarity-flow on explanation-04: an order has no usable pick, so the contest is unscored

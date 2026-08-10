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

Judge: opus. Judged on 2026-08-10T13:44:47+00:00.

## Matchups

| A | B | Contests | A wins | B wins | Splits | Unscored | Net (A) |
|---|---|---|---|---|---|---|---|
| actionable-clarity | clarity-flow | 31 | 17 | 3 | 11 | 0 | 14 |
| actionable-clarity | classic-concise | 31 | 17 | 3 | 11 | 0 | 14 |
| actionable-clarity | developer-docs | 31 | 10 | 8 | 13 | 0 | 2 |
| actionable-clarity | plain-language | 31 | 8 | 9 | 14 | 0 | -1 |
| actionable-clarity | technical-simplified | 28 | 20 | 1 | 7 | 0 | 19 |
| actionable-clarity | unstyled | 31 | 15 | 4 | 11 | 1 | 11 |
| clarity-flow | classic-concise | 32 | 11 | 8 | 13 | 0 | 3 |
| clarity-flow | developer-docs | 32 | 4 | 19 | 9 | 0 | -15 |
| clarity-flow | plain-language | 32 | 5 | 18 | 9 | 0 | -13 |
| clarity-flow | technical-simplified | 29 | 21 | 4 | 4 | 0 | 17 |
| clarity-flow | unstyled | 32 | 5 | 12 | 15 | 0 | -7 |
| classic-concise | developer-docs | 32 | 3 | 22 | 7 | 0 | -19 |
| classic-concise | plain-language | 32 | 4 | 21 | 7 | 0 | -17 |
| classic-concise | technical-simplified | 29 | 10 | 5 | 14 | 0 | 5 |
| classic-concise | unstyled | 32 | 8 | 14 | 10 | 0 | -6 |
| developer-docs | plain-language | 32 | 8 | 15 | 9 | 0 | -7 |
| developer-docs | technical-simplified | 29 | 20 | 3 | 6 | 0 | 17 |
| developer-docs | unstyled | 32 | 16 | 4 | 12 | 0 | 12 |
| plain-language | technical-simplified | 29 | 19 | 1 | 9 | 0 | 18 |
| plain-language | unstyled | 32 | 18 | 4 | 10 | 0 | 14 |
| technical-simplified | unstyled | 29 | 5 | 12 | 12 | 0 | -7 |

## Win matrix

A cell holds the points of the row competitor against the column
competitor: 1 per decisive win plus 0.5 per split.

| | actionable-clarity | clarity-flow | classic-concise | developer-docs | plain-language | technical-simplified | unstyled |
|---|---|---|---|---|---|---|---|
| actionable-clarity | - | 22.5 | 22.5 | 16.5 | 15.0 | 23.5 | 20.5 |
| clarity-flow | 8.5 | - | 17.5 | 8.5 | 9.5 | 23.0 | 12.5 |
| classic-concise | 8.5 | 14.5 | - | 6.5 | 7.5 | 17.0 | 13.0 |
| developer-docs | 14.5 | 23.5 | 25.5 | - | 12.5 | 23.0 | 22.0 |
| plain-language | 16.0 | 22.5 | 24.5 | 19.5 | - | 23.5 | 23.0 |
| technical-simplified | 4.5 | 6.0 | 12.0 | 6.0 | 5.5 | - | 11.0 |
| unstyled | 9.5 | 19.5 | 19.0 | 10.0 | 9.0 | 18.0 | - |

## Bradley-Terry strengths

The scale is anchored on unstyled at strength 1.0.

The table lists the competitors from the highest strength to the
lowest. A competitor without a finite strength comes last.

| Competitor | Strength | 95% CI |
|---|---|---|
| plain-language | 2.426 | [1.777, 3.413] |
| actionable-clarity | 2.211 | [1.617, 3.024] |
| developer-docs | 2.046 | [1.479, 2.769] |
| unstyled | 1.0 | n/a |
| clarity-flow | 0.89 | [0.665, 1.205] |
| classic-concise | 0.689 | [0.491, 0.93] |
| technical-simplified | 0.454 | [0.319, 0.636] |

The interval comes from 1000 bootstrap resamples of the scored contests (seed 0).

## Position bias

First-pick rate: 0.397 over 1295 usable picks.
Split rate: 0.329 over 647 judged contests.

## Per task type

### code-review

| A | B | Contests | A wins | B wins | Splits | Unscored | Net (A) |
|---|---|---|---|---|---|---|---|
| actionable-clarity | clarity-flow | 8 | 3 | 2 | 3 | 0 | 1 |
| actionable-clarity | classic-concise | 8 | 3 | 1 | 4 | 0 | 2 |
| actionable-clarity | developer-docs | 8 | 4 | 1 | 3 | 0 | 3 |
| actionable-clarity | plain-language | 8 | 3 | 3 | 2 | 0 | 0 |
| actionable-clarity | technical-simplified | 8 | 7 | 1 | 0 | 0 | 6 |
| actionable-clarity | unstyled | 8 | 4 | 1 | 3 | 0 | 3 |
| clarity-flow | classic-concise | 8 | 5 | 0 | 3 | 0 | 5 |
| clarity-flow | developer-docs | 8 | 3 | 3 | 2 | 0 | 0 |
| clarity-flow | plain-language | 8 | 3 | 3 | 2 | 0 | 0 |
| clarity-flow | technical-simplified | 8 | 7 | 0 | 1 | 0 | 7 |
| clarity-flow | unstyled | 8 | 1 | 1 | 6 | 0 | 0 |
| classic-concise | developer-docs | 8 | 1 | 6 | 1 | 0 | -5 |
| classic-concise | plain-language | 8 | 1 | 6 | 1 | 0 | -5 |
| classic-concise | technical-simplified | 8 | 3 | 2 | 3 | 0 | 1 |
| classic-concise | unstyled | 8 | 2 | 3 | 3 | 0 | -1 |
| developer-docs | plain-language | 8 | 2 | 6 | 0 | 0 | -4 |
| developer-docs | technical-simplified | 8 | 5 | 1 | 2 | 0 | 4 |
| developer-docs | unstyled | 8 | 3 | 2 | 3 | 0 | 1 |
| plain-language | technical-simplified | 8 | 6 | 1 | 1 | 0 | 5 |
| plain-language | unstyled | 8 | 4 | 2 | 2 | 0 | 2 |
| technical-simplified | unstyled | 8 | 1 | 4 | 3 | 0 | -3 |

### debugging

| A | B | Contests | A wins | B wins | Splits | Unscored | Net (A) |
|---|---|---|---|---|---|---|---|
| actionable-clarity | clarity-flow | 8 | 5 | 1 | 2 | 0 | 4 |
| actionable-clarity | classic-concise | 8 | 6 | 1 | 1 | 0 | 5 |
| actionable-clarity | developer-docs | 8 | 1 | 3 | 4 | 0 | -2 |
| actionable-clarity | plain-language | 8 | 2 | 2 | 4 | 0 | 0 |
| actionable-clarity | technical-simplified | 8 | 5 | 0 | 3 | 0 | 5 |
| actionable-clarity | unstyled | 8 | 4 | 1 | 2 | 1 | 3 |
| clarity-flow | classic-concise | 8 | 2 | 2 | 4 | 0 | 0 |
| clarity-flow | developer-docs | 8 | 0 | 6 | 2 | 0 | -6 |
| clarity-flow | plain-language | 8 | 0 | 5 | 3 | 0 | -5 |
| clarity-flow | technical-simplified | 8 | 3 | 2 | 3 | 0 | 1 |
| clarity-flow | unstyled | 8 | 2 | 4 | 2 | 0 | -2 |
| classic-concise | developer-docs | 8 | 0 | 7 | 1 | 0 | -7 |
| classic-concise | plain-language | 8 | 1 | 5 | 2 | 0 | -4 |
| classic-concise | technical-simplified | 8 | 0 | 2 | 6 | 0 | -2 |
| classic-concise | unstyled | 8 | 1 | 5 | 2 | 0 | -4 |
| developer-docs | plain-language | 8 | 2 | 2 | 4 | 0 | 0 |
| developer-docs | technical-simplified | 8 | 7 | 1 | 0 | 0 | 6 |
| developer-docs | unstyled | 8 | 4 | 0 | 4 | 0 | 4 |
| plain-language | technical-simplified | 8 | 4 | 0 | 4 | 0 | 4 |
| plain-language | unstyled | 8 | 3 | 0 | 5 | 0 | 3 |
| technical-simplified | unstyled | 8 | 2 | 2 | 4 | 0 | 0 |

### explanation

| A | B | Contests | A wins | B wins | Splits | Unscored | Net (A) |
|---|---|---|---|---|---|---|---|
| actionable-clarity | clarity-flow | 7 | 5 | 0 | 2 | 0 | 5 |
| actionable-clarity | classic-concise | 7 | 4 | 1 | 2 | 0 | 3 |
| actionable-clarity | developer-docs | 7 | 2 | 1 | 4 | 0 | 1 |
| actionable-clarity | plain-language | 7 | 3 | 2 | 2 | 0 | 1 |
| actionable-clarity | technical-simplified | 6 | 5 | 0 | 1 | 0 | 5 |
| actionable-clarity | unstyled | 7 | 4 | 2 | 1 | 0 | 2 |
| clarity-flow | classic-concise | 8 | 2 | 5 | 1 | 0 | -3 |
| clarity-flow | developer-docs | 8 | 0 | 7 | 1 | 0 | -7 |
| clarity-flow | plain-language | 8 | 0 | 6 | 2 | 0 | -6 |
| clarity-flow | technical-simplified | 7 | 6 | 1 | 0 | 0 | 5 |
| clarity-flow | unstyled | 8 | 0 | 5 | 3 | 0 | -5 |
| classic-concise | developer-docs | 8 | 2 | 4 | 2 | 0 | -2 |
| classic-concise | plain-language | 8 | 1 | 4 | 3 | 0 | -3 |
| classic-concise | technical-simplified | 7 | 6 | 0 | 1 | 0 | 6 |
| classic-concise | unstyled | 8 | 2 | 3 | 3 | 0 | -1 |
| developer-docs | plain-language | 8 | 2 | 3 | 3 | 0 | -1 |
| developer-docs | technical-simplified | 7 | 5 | 0 | 2 | 0 | 5 |
| developer-docs | unstyled | 8 | 3 | 1 | 4 | 0 | 2 |
| plain-language | technical-simplified | 7 | 6 | 0 | 1 | 0 | 6 |
| plain-language | unstyled | 8 | 3 | 2 | 3 | 0 | 1 |
| technical-simplified | unstyled | 7 | 1 | 4 | 2 | 0 | -3 |

### summarization

| A | B | Contests | A wins | B wins | Splits | Unscored | Net (A) |
|---|---|---|---|---|---|---|---|
| actionable-clarity | clarity-flow | 8 | 4 | 0 | 4 | 0 | 4 |
| actionable-clarity | classic-concise | 8 | 4 | 0 | 4 | 0 | 4 |
| actionable-clarity | developer-docs | 8 | 3 | 3 | 2 | 0 | 0 |
| actionable-clarity | plain-language | 8 | 0 | 2 | 6 | 0 | -2 |
| actionable-clarity | technical-simplified | 6 | 3 | 0 | 3 | 0 | 3 |
| actionable-clarity | unstyled | 8 | 3 | 0 | 5 | 0 | 3 |
| clarity-flow | classic-concise | 8 | 2 | 1 | 5 | 0 | 1 |
| clarity-flow | developer-docs | 8 | 1 | 3 | 4 | 0 | -2 |
| clarity-flow | plain-language | 8 | 2 | 4 | 2 | 0 | -2 |
| clarity-flow | technical-simplified | 6 | 5 | 1 | 0 | 0 | 4 |
| clarity-flow | unstyled | 8 | 2 | 2 | 4 | 0 | 0 |
| classic-concise | developer-docs | 8 | 0 | 5 | 3 | 0 | -5 |
| classic-concise | plain-language | 8 | 1 | 6 | 1 | 0 | -5 |
| classic-concise | technical-simplified | 6 | 1 | 1 | 4 | 0 | 0 |
| classic-concise | unstyled | 8 | 3 | 3 | 2 | 0 | 0 |
| developer-docs | plain-language | 8 | 2 | 4 | 2 | 0 | -2 |
| developer-docs | technical-simplified | 6 | 3 | 1 | 2 | 0 | 2 |
| developer-docs | unstyled | 8 | 6 | 1 | 1 | 0 | 5 |
| plain-language | technical-simplified | 6 | 3 | 0 | 3 | 0 | 3 |
| plain-language | unstyled | 8 | 8 | 0 | 0 | 0 | 8 |
| technical-simplified | unstyled | 6 | 1 | 2 | 3 | 0 | -1 |

## Length confound

Samples: 642 contests with unequal word counts.
Pearson: 0.115. Spearman: 0.173.
Longer-text win rate: 0.628.

## Call timing

A stored call row holds two times: duration_ms is the model
time that the CLI reports, and wall_ms is the wall clock of
the subprocess. The difference is the startup cost of one CLI
call.

Calls: 372, measured: 372.
Mean duration: 4586 ms. Mean wall: 22691 ms. Mean startup: 18105 ms.

## Harness spend

A stored call row holds the token counts of its call: the
uncached input, cache-write input, cache-read input, and
output tokens. The cache-read share is the cache-read total
over the whole input total.

Calls: 372, measured: 372.
Input tokens: 744 uncached, 816484 cache write, 763954 cache read. Output tokens: 22724.
Cache-read share: 0.483.
Cache writes by lifetime: 816484 at 5 minutes, 0 at 1 hour.

## Reuse

Reused rows: 924, imported from 2026-08-10b.
Live calls of this run: 372.

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

- technical-simplified/explanation-01: the pair failed the gate, excluded
- technical-simplified/summarization-06: the pair failed the gate, excluded
- technical-simplified/summarization-08: the pair failed the gate, excluded
- actionable-clarity/explanation-08: the pair failed the gate, excluded
- actionable-clarity vs unstyled on debugging-07: the judge gave no usable pick for the order with actionable-clarity first, so the contest is unscored
- actionable-clarity vs unstyled on debugging-07: an order has no usable pick, so the contest is unscored

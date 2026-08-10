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

Judge: opus. Judged on 2026-08-10T16:22:01+00:00.

## Matchups

| A | B | Contests | A wins | B wins | Splits | Unscored | Net (A) |
|---|---|---|---|---|---|---|---|
| actionable-clarity | clarity-flow | 32 | 19 | 4 | 9 | 0 | 15 |
| actionable-clarity | classic-concise | 32 | 19 | 3 | 10 | 0 | 16 |
| actionable-clarity | developer-docs | 32 | 18 | 6 | 8 | 0 | 12 |
| actionable-clarity | plain-language | 32 | 16 | 8 | 8 | 0 | 8 |
| actionable-clarity | technical-simplified | 26 | 23 | 1 | 2 | 0 | 22 |
| actionable-clarity | unstyled | 32 | 21 | 5 | 6 | 0 | 16 |
| clarity-flow | classic-concise | 32 | 8 | 15 | 9 | 0 | -7 |
| clarity-flow | developer-docs | 32 | 6 | 14 | 12 | 0 | -8 |
| clarity-flow | plain-language | 32 | 7 | 18 | 7 | 0 | -11 |
| clarity-flow | technical-simplified | 26 | 12 | 4 | 10 | 0 | 8 |
| clarity-flow | unstyled | 32 | 9 | 11 | 12 | 0 | -2 |
| classic-concise | developer-docs | 32 | 7 | 14 | 11 | 0 | -7 |
| classic-concise | plain-language | 32 | 8 | 16 | 8 | 0 | -8 |
| classic-concise | technical-simplified | 26 | 13 | 3 | 10 | 0 | 10 |
| classic-concise | unstyled | 32 | 9 | 9 | 14 | 0 | 0 |
| developer-docs | plain-language | 32 | 7 | 12 | 13 | 0 | -5 |
| developer-docs | technical-simplified | 26 | 18 | 4 | 4 | 0 | 14 |
| developer-docs | unstyled | 32 | 16 | 6 | 10 | 0 | 10 |
| plain-language | technical-simplified | 26 | 13 | 6 | 7 | 0 | 7 |
| plain-language | unstyled | 32 | 17 | 9 | 6 | 0 | 8 |
| technical-simplified | unstyled | 26 | 3 | 12 | 11 | 0 | -9 |

## Win matrix

A cell holds the points of the row competitor against the column
competitor: 1 per decisive win plus 0.5 per split.

| | actionable-clarity | clarity-flow | classic-concise | developer-docs | plain-language | technical-simplified | unstyled |
|---|---|---|---|---|---|---|---|
| actionable-clarity | - | 23.5 | 24.0 | 22.0 | 20.0 | 24.0 | 24.0 |
| clarity-flow | 8.5 | - | 12.5 | 12.0 | 10.5 | 17.0 | 15.0 |
| classic-concise | 8.0 | 19.5 | - | 12.5 | 12.0 | 18.0 | 16.0 |
| developer-docs | 10.0 | 20.0 | 19.5 | - | 13.5 | 20.0 | 21.0 |
| plain-language | 12.0 | 21.5 | 20.0 | 18.5 | - | 16.5 | 20.0 |
| technical-simplified | 2.0 | 9.0 | 8.0 | 6.0 | 9.5 | - | 8.5 |
| unstyled | 8.0 | 17.0 | 16.0 | 11.0 | 12.0 | 17.5 | - |

## Bradley-Terry strengths

The scale is anchored on unstyled at strength 1.0.

The table lists the competitors from the highest strength to the
lowest. A competitor without a finite strength comes last.

| Competitor | Strength | 95% CI |
|---|---|---|
| actionable-clarity | 3.144 | [2.222, 4.424] |
| plain-language | 1.698 | [1.203, 2.414] |
| developer-docs | 1.553 | [1.113, 2.14] |
| classic-concise | 1.092 | [0.802, 1.527] |
| unstyled | 1.0 | n/a |
| clarity-flow | 0.888 | [0.657, 1.214] |
| technical-simplified | 0.517 | [0.352, 0.722] |

The interval comes from 1000 bootstrap resamples of the scored contests (seed 0).

## Position bias

First-pick rate: 0.394 over 1272 usable picks.
Split rate: 0.294 over 636 judged contests.

## Per task type

### code-review

| A | B | Contests | A wins | B wins | Splits | Unscored | Net (A) |
|---|---|---|---|---|---|---|---|
| actionable-clarity | clarity-flow | 8 | 5 | 2 | 1 | 0 | 3 |
| actionable-clarity | classic-concise | 8 | 6 | 1 | 1 | 0 | 5 |
| actionable-clarity | developer-docs | 8 | 5 | 1 | 2 | 0 | 4 |
| actionable-clarity | plain-language | 8 | 3 | 1 | 4 | 0 | 2 |
| actionable-clarity | technical-simplified | 6 | 5 | 0 | 1 | 0 | 5 |
| actionable-clarity | unstyled | 8 | 6 | 1 | 1 | 0 | 5 |
| clarity-flow | classic-concise | 8 | 3 | 4 | 1 | 0 | -1 |
| clarity-flow | developer-docs | 8 | 2 | 4 | 2 | 0 | -2 |
| clarity-flow | plain-language | 8 | 2 | 4 | 2 | 0 | -2 |
| clarity-flow | technical-simplified | 6 | 3 | 2 | 1 | 0 | 1 |
| clarity-flow | unstyled | 8 | 3 | 2 | 3 | 0 | 1 |
| classic-concise | developer-docs | 8 | 3 | 2 | 3 | 0 | 1 |
| classic-concise | plain-language | 8 | 2 | 5 | 1 | 0 | -3 |
| classic-concise | technical-simplified | 6 | 2 | 1 | 3 | 0 | 1 |
| classic-concise | unstyled | 8 | 3 | 2 | 3 | 0 | 1 |
| developer-docs | plain-language | 8 | 0 | 5 | 3 | 0 | -5 |
| developer-docs | technical-simplified | 6 | 4 | 2 | 0 | 0 | 2 |
| developer-docs | unstyled | 8 | 3 | 2 | 3 | 0 | 1 |
| plain-language | technical-simplified | 6 | 3 | 1 | 2 | 0 | 2 |
| plain-language | unstyled | 8 | 4 | 2 | 2 | 0 | 2 |
| technical-simplified | unstyled | 6 | 3 | 2 | 1 | 0 | 1 |

### debugging

| A | B | Contests | A wins | B wins | Splits | Unscored | Net (A) |
|---|---|---|---|---|---|---|---|
| actionable-clarity | clarity-flow | 8 | 5 | 0 | 3 | 0 | 5 |
| actionable-clarity | classic-concise | 8 | 5 | 0 | 3 | 0 | 5 |
| actionable-clarity | developer-docs | 8 | 4 | 2 | 2 | 0 | 2 |
| actionable-clarity | plain-language | 8 | 5 | 3 | 0 | 0 | 2 |
| actionable-clarity | technical-simplified | 7 | 7 | 0 | 0 | 0 | 7 |
| actionable-clarity | unstyled | 8 | 5 | 1 | 2 | 0 | 4 |
| clarity-flow | classic-concise | 8 | 2 | 3 | 3 | 0 | -1 |
| clarity-flow | developer-docs | 8 | 1 | 3 | 4 | 0 | -2 |
| clarity-flow | plain-language | 8 | 2 | 4 | 2 | 0 | -2 |
| clarity-flow | technical-simplified | 7 | 2 | 1 | 4 | 0 | 1 |
| clarity-flow | unstyled | 8 | 2 | 4 | 2 | 0 | -2 |
| classic-concise | developer-docs | 8 | 3 | 4 | 1 | 0 | -1 |
| classic-concise | plain-language | 8 | 3 | 4 | 1 | 0 | -1 |
| classic-concise | technical-simplified | 7 | 3 | 1 | 3 | 0 | 2 |
| classic-concise | unstyled | 8 | 1 | 3 | 4 | 0 | -2 |
| developer-docs | plain-language | 8 | 1 | 4 | 3 | 0 | -3 |
| developer-docs | technical-simplified | 7 | 5 | 2 | 0 | 0 | 3 |
| developer-docs | unstyled | 8 | 6 | 0 | 2 | 0 | 6 |
| plain-language | technical-simplified | 7 | 3 | 3 | 1 | 0 | 0 |
| plain-language | unstyled | 8 | 4 | 3 | 1 | 0 | 1 |
| technical-simplified | unstyled | 7 | 0 | 3 | 4 | 0 | -3 |

### explanation

| A | B | Contests | A wins | B wins | Splits | Unscored | Net (A) |
|---|---|---|---|---|---|---|---|
| actionable-clarity | clarity-flow | 8 | 4 | 1 | 3 | 0 | 3 |
| actionable-clarity | classic-concise | 8 | 3 | 2 | 3 | 0 | 1 |
| actionable-clarity | developer-docs | 8 | 5 | 2 | 1 | 0 | 3 |
| actionable-clarity | plain-language | 8 | 3 | 2 | 3 | 0 | 1 |
| actionable-clarity | technical-simplified | 7 | 7 | 0 | 0 | 0 | 7 |
| actionable-clarity | unstyled | 8 | 5 | 1 | 2 | 0 | 4 |
| clarity-flow | classic-concise | 8 | 2 | 4 | 2 | 0 | -2 |
| clarity-flow | developer-docs | 8 | 2 | 4 | 2 | 0 | -2 |
| clarity-flow | plain-language | 8 | 0 | 7 | 1 | 0 | -7 |
| clarity-flow | technical-simplified | 7 | 5 | 1 | 1 | 0 | 4 |
| clarity-flow | unstyled | 8 | 1 | 4 | 3 | 0 | -3 |
| classic-concise | developer-docs | 8 | 0 | 4 | 4 | 0 | -4 |
| classic-concise | plain-language | 8 | 1 | 4 | 3 | 0 | -3 |
| classic-concise | technical-simplified | 7 | 6 | 0 | 1 | 0 | 6 |
| classic-concise | unstyled | 8 | 2 | 3 | 3 | 0 | -1 |
| developer-docs | plain-language | 8 | 1 | 2 | 5 | 0 | -1 |
| developer-docs | technical-simplified | 7 | 7 | 0 | 0 | 0 | 7 |
| developer-docs | unstyled | 8 | 2 | 3 | 3 | 0 | -1 |
| plain-language | technical-simplified | 7 | 6 | 1 | 0 | 0 | 5 |
| plain-language | unstyled | 8 | 5 | 2 | 1 | 0 | 3 |
| technical-simplified | unstyled | 7 | 0 | 6 | 1 | 0 | -6 |

### summarization

| A | B | Contests | A wins | B wins | Splits | Unscored | Net (A) |
|---|---|---|---|---|---|---|---|
| actionable-clarity | clarity-flow | 8 | 5 | 1 | 2 | 0 | 4 |
| actionable-clarity | classic-concise | 8 | 5 | 0 | 3 | 0 | 5 |
| actionable-clarity | developer-docs | 8 | 4 | 1 | 3 | 0 | 3 |
| actionable-clarity | plain-language | 8 | 5 | 2 | 1 | 0 | 3 |
| actionable-clarity | technical-simplified | 6 | 4 | 1 | 1 | 0 | 3 |
| actionable-clarity | unstyled | 8 | 5 | 2 | 1 | 0 | 3 |
| clarity-flow | classic-concise | 8 | 1 | 4 | 3 | 0 | -3 |
| clarity-flow | developer-docs | 8 | 1 | 3 | 4 | 0 | -2 |
| clarity-flow | plain-language | 8 | 3 | 3 | 2 | 0 | 0 |
| clarity-flow | technical-simplified | 6 | 2 | 0 | 4 | 0 | 2 |
| clarity-flow | unstyled | 8 | 3 | 1 | 4 | 0 | 2 |
| classic-concise | developer-docs | 8 | 1 | 4 | 3 | 0 | -3 |
| classic-concise | plain-language | 8 | 2 | 3 | 3 | 0 | -1 |
| classic-concise | technical-simplified | 6 | 2 | 1 | 3 | 0 | 1 |
| classic-concise | unstyled | 8 | 3 | 1 | 4 | 0 | 2 |
| developer-docs | plain-language | 8 | 5 | 1 | 2 | 0 | 4 |
| developer-docs | technical-simplified | 6 | 2 | 0 | 4 | 0 | 2 |
| developer-docs | unstyled | 8 | 5 | 1 | 2 | 0 | 4 |
| plain-language | technical-simplified | 6 | 1 | 1 | 4 | 0 | 0 |
| plain-language | unstyled | 8 | 4 | 2 | 2 | 0 | 2 |
| technical-simplified | unstyled | 6 | 0 | 1 | 5 | 0 | -1 |

## Length confound

Samples: 626 contests with unequal word counts.
Pearson: 0.173. Spearman: 0.229.
Longer-text win rate: 0.654.

## Call timing

A stored call row holds two times: duration_ms is the model
time that the CLI reports, and wall_ms is the wall clock of
the subprocess. The difference is the startup cost of one CLI
call.

Calls: 378, measured: 378.
Mean duration: 3754 ms. Mean wall: 26672 ms. Mean startup: 22918 ms.

## Harness spend

A stored call row holds the token counts of its call: the
uncached input, cache-write input, cache-read input, and
output tokens. The cache-read share is the cache-read total
over the whole input total.

Calls: 378, measured: 378.
Input tokens: 756 uncached, 830402 cache write, 767822 cache read. Output tokens: 22921.
Cache-read share: 0.48.
Cache writes by lifetime: 830402 at 5 minutes, 0 at 1 hour.

## Reuse

Reused rows: 894, imported from 2026-08-07.
Live calls of this run: 378.

The freshness sample re-ran 6 imported verdicts live; 5 agree.
- clarity:code-review-01:077715be98fbe105444d1082c36788610e15dd360c3040094a8fb03b7f0252a0:db7c669a89b5da3f804318f3a7900eaa3a4dcc7330cdfb16dfa3fabcb4dcd835: the verdicts differ.

Clarity picks: 1 of 6 disagree; the tolerance is 5.

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
- technical-simplified/code-review-07: the pair failed the gate, excluded
- technical-simplified/code-review-08: the pair failed the gate, excluded
- technical-simplified/summarization-06: the pair failed the gate, excluded
- technical-simplified/summarization-07: the pair failed the gate, excluded
- technical-simplified/debugging-07: the pair failed the gate, excluded

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

Judge: opus. Judged on 2026-08-10T13:33:41+00:00.

## Matchups

| A | B | Contests | A wins | B wins | Splits | Unscored | Net (A) |
|---|---|---|---|---|---|---|---|
| actionable-clarity | clarity-flow | 32 | 21 | 3 | 8 | 0 | 18 |
| actionable-clarity | classic-concise | 32 | 20 | 3 | 9 | 0 | 17 |
| actionable-clarity | developer-docs | 32 | 18 | 5 | 9 | 0 | 13 |
| actionable-clarity | plain-language | 32 | 19 | 4 | 9 | 0 | 15 |
| actionable-clarity | technical-simplified | 27 | 18 | 1 | 8 | 0 | 17 |
| actionable-clarity | unstyled | 32 | 22 | 4 | 6 | 0 | 18 |
| clarity-flow | classic-concise | 32 | 13 | 11 | 8 | 0 | 2 |
| clarity-flow | developer-docs | 32 | 5 | 14 | 13 | 0 | -9 |
| clarity-flow | plain-language | 32 | 10 | 15 | 7 | 0 | -5 |
| clarity-flow | technical-simplified | 27 | 10 | 9 | 8 | 0 | 1 |
| clarity-flow | unstyled | 32 | 8 | 13 | 11 | 0 | -5 |
| classic-concise | developer-docs | 32 | 7 | 18 | 7 | 0 | -11 |
| classic-concise | plain-language | 32 | 6 | 14 | 12 | 0 | -8 |
| classic-concise | technical-simplified | 27 | 9 | 7 | 11 | 0 | 2 |
| classic-concise | unstyled | 32 | 7 | 16 | 9 | 0 | -9 |
| developer-docs | plain-language | 32 | 10 | 10 | 12 | 0 | 0 |
| developer-docs | technical-simplified | 27 | 18 | 3 | 6 | 0 | 15 |
| developer-docs | unstyled | 32 | 17 | 6 | 9 | 0 | 11 |
| plain-language | technical-simplified | 27 | 17 | 6 | 4 | 0 | 11 |
| plain-language | unstyled | 32 | 14 | 11 | 7 | 0 | 3 |
| technical-simplified | unstyled | 27 | 4 | 17 | 6 | 0 | -13 |

## Win matrix

A cell holds the points of the row competitor against the column
competitor: 1 per decisive win plus 0.5 per split.

| | actionable-clarity | clarity-flow | classic-concise | developer-docs | plain-language | technical-simplified | unstyled |
|---|---|---|---|---|---|---|---|
| actionable-clarity | - | 25.0 | 24.5 | 22.5 | 23.5 | 22.0 | 25.0 |
| clarity-flow | 7.0 | - | 17.0 | 11.5 | 13.5 | 14.0 | 13.5 |
| classic-concise | 7.5 | 15.0 | - | 10.5 | 12.0 | 14.5 | 11.5 |
| developer-docs | 9.5 | 20.5 | 21.5 | - | 16.0 | 21.0 | 21.5 |
| plain-language | 8.5 | 18.5 | 20.0 | 16.0 | - | 19.0 | 17.5 |
| technical-simplified | 5.0 | 13.0 | 12.5 | 6.0 | 8.0 | - | 7.0 |
| unstyled | 7.0 | 18.5 | 20.5 | 10.5 | 14.5 | 20.0 | - |

## Bradley-Terry strengths

The scale is anchored on unstyled at strength 1.0.

The table lists the competitors from the highest strength to the
lowest. A competitor without a finite strength comes last.

| Competitor | Strength | 95% CI |
|---|---|---|
| actionable-clarity | 2.933 | [2.076, 4.111] |
| developer-docs | 1.452 | [1.04, 2.022] |
| plain-language | 1.18 | [0.872, 1.672] |
| unstyled | 1.0 | n/a |
| clarity-flow | 0.753 | [0.538, 1.015] |
| classic-concise | 0.674 | [0.477, 0.939] |
| technical-simplified | 0.52 | [0.362, 0.718] |

The interval comes from 1000 bootstrap resamples of the scored contests (seed 0).

## Position bias

First-pick rate: 0.414 over 1284 usable picks.
Split rate: 0.279 over 642 judged contests.

## Per task type

### code-review

| A | B | Contests | A wins | B wins | Splits | Unscored | Net (A) |
|---|---|---|---|---|---|---|---|
| actionable-clarity | clarity-flow | 8 | 3 | 1 | 4 | 0 | 2 |
| actionable-clarity | classic-concise | 8 | 5 | 1 | 2 | 0 | 4 |
| actionable-clarity | developer-docs | 8 | 5 | 1 | 2 | 0 | 4 |
| actionable-clarity | plain-language | 8 | 4 | 2 | 2 | 0 | 2 |
| actionable-clarity | technical-simplified | 7 | 4 | 0 | 3 | 0 | 4 |
| actionable-clarity | unstyled | 8 | 6 | 2 | 0 | 0 | 4 |
| clarity-flow | classic-concise | 8 | 3 | 4 | 1 | 0 | -1 |
| clarity-flow | developer-docs | 8 | 1 | 3 | 4 | 0 | -2 |
| clarity-flow | plain-language | 8 | 4 | 3 | 1 | 0 | 1 |
| clarity-flow | technical-simplified | 7 | 5 | 1 | 1 | 0 | 4 |
| clarity-flow | unstyled | 8 | 3 | 1 | 4 | 0 | 2 |
| classic-concise | developer-docs | 8 | 2 | 5 | 1 | 0 | -3 |
| classic-concise | plain-language | 8 | 2 | 3 | 3 | 0 | -1 |
| classic-concise | technical-simplified | 7 | 5 | 1 | 1 | 0 | 4 |
| classic-concise | unstyled | 8 | 0 | 3 | 5 | 0 | -3 |
| developer-docs | plain-language | 8 | 3 | 4 | 1 | 0 | -1 |
| developer-docs | technical-simplified | 7 | 5 | 0 | 2 | 0 | 5 |
| developer-docs | unstyled | 8 | 5 | 1 | 2 | 0 | 4 |
| plain-language | technical-simplified | 7 | 5 | 1 | 1 | 0 | 4 |
| plain-language | unstyled | 8 | 4 | 4 | 0 | 0 | 0 |
| technical-simplified | unstyled | 7 | 1 | 5 | 1 | 0 | -4 |

### debugging

| A | B | Contests | A wins | B wins | Splits | Unscored | Net (A) |
|---|---|---|---|---|---|---|---|
| actionable-clarity | clarity-flow | 8 | 5 | 0 | 3 | 0 | 5 |
| actionable-clarity | classic-concise | 8 | 5 | 1 | 2 | 0 | 4 |
| actionable-clarity | developer-docs | 8 | 3 | 1 | 4 | 0 | 2 |
| actionable-clarity | plain-language | 8 | 3 | 2 | 3 | 0 | 1 |
| actionable-clarity | technical-simplified | 6 | 5 | 0 | 1 | 0 | 5 |
| actionable-clarity | unstyled | 8 | 6 | 2 | 0 | 0 | 4 |
| clarity-flow | classic-concise | 8 | 6 | 2 | 0 | 0 | 4 |
| clarity-flow | developer-docs | 8 | 2 | 3 | 3 | 0 | -1 |
| clarity-flow | plain-language | 8 | 2 | 5 | 1 | 0 | -3 |
| clarity-flow | technical-simplified | 6 | 1 | 2 | 3 | 0 | -1 |
| clarity-flow | unstyled | 8 | 2 | 5 | 1 | 0 | -3 |
| classic-concise | developer-docs | 8 | 1 | 3 | 4 | 0 | -2 |
| classic-concise | plain-language | 8 | 0 | 4 | 4 | 0 | -4 |
| classic-concise | technical-simplified | 6 | 0 | 3 | 3 | 0 | -3 |
| classic-concise | unstyled | 8 | 2 | 4 | 2 | 0 | -2 |
| developer-docs | plain-language | 8 | 2 | 3 | 3 | 0 | -1 |
| developer-docs | technical-simplified | 6 | 5 | 1 | 0 | 0 | 4 |
| developer-docs | unstyled | 8 | 4 | 3 | 1 | 0 | 1 |
| plain-language | technical-simplified | 6 | 5 | 0 | 1 | 0 | 5 |
| plain-language | unstyled | 8 | 5 | 2 | 1 | 0 | 3 |
| technical-simplified | unstyled | 6 | 1 | 5 | 0 | 0 | -4 |

### explanation

| A | B | Contests | A wins | B wins | Splits | Unscored | Net (A) |
|---|---|---|---|---|---|---|---|
| actionable-clarity | clarity-flow | 8 | 7 | 1 | 0 | 0 | 6 |
| actionable-clarity | classic-concise | 8 | 3 | 1 | 4 | 0 | 2 |
| actionable-clarity | developer-docs | 8 | 6 | 2 | 0 | 0 | 4 |
| actionable-clarity | plain-language | 8 | 6 | 0 | 2 | 0 | 6 |
| actionable-clarity | technical-simplified | 8 | 6 | 0 | 2 | 0 | 6 |
| actionable-clarity | unstyled | 8 | 4 | 0 | 4 | 0 | 4 |
| clarity-flow | classic-concise | 8 | 2 | 3 | 3 | 0 | -1 |
| clarity-flow | developer-docs | 8 | 1 | 5 | 2 | 0 | -4 |
| clarity-flow | plain-language | 8 | 2 | 3 | 3 | 0 | -1 |
| clarity-flow | technical-simplified | 8 | 4 | 3 | 1 | 0 | 1 |
| clarity-flow | unstyled | 8 | 2 | 4 | 2 | 0 | -2 |
| classic-concise | developer-docs | 8 | 2 | 6 | 0 | 0 | -4 |
| classic-concise | plain-language | 8 | 2 | 3 | 3 | 0 | -1 |
| classic-concise | technical-simplified | 8 | 3 | 2 | 3 | 0 | 1 |
| classic-concise | unstyled | 8 | 3 | 4 | 1 | 0 | -1 |
| developer-docs | plain-language | 8 | 3 | 1 | 4 | 0 | 2 |
| developer-docs | technical-simplified | 8 | 6 | 0 | 2 | 0 | 6 |
| developer-docs | unstyled | 8 | 4 | 1 | 3 | 0 | 3 |
| plain-language | technical-simplified | 8 | 4 | 3 | 1 | 0 | 1 |
| plain-language | unstyled | 8 | 2 | 3 | 3 | 0 | -1 |
| technical-simplified | unstyled | 8 | 1 | 5 | 2 | 0 | -4 |

### summarization

| A | B | Contests | A wins | B wins | Splits | Unscored | Net (A) |
|---|---|---|---|---|---|---|---|
| actionable-clarity | clarity-flow | 8 | 6 | 1 | 1 | 0 | 5 |
| actionable-clarity | classic-concise | 8 | 7 | 0 | 1 | 0 | 7 |
| actionable-clarity | developer-docs | 8 | 4 | 1 | 3 | 0 | 3 |
| actionable-clarity | plain-language | 8 | 6 | 0 | 2 | 0 | 6 |
| actionable-clarity | technical-simplified | 6 | 3 | 1 | 2 | 0 | 2 |
| actionable-clarity | unstyled | 8 | 6 | 0 | 2 | 0 | 6 |
| clarity-flow | classic-concise | 8 | 2 | 2 | 4 | 0 | 0 |
| clarity-flow | developer-docs | 8 | 1 | 3 | 4 | 0 | -2 |
| clarity-flow | plain-language | 8 | 2 | 4 | 2 | 0 | -2 |
| clarity-flow | technical-simplified | 6 | 0 | 3 | 3 | 0 | -3 |
| clarity-flow | unstyled | 8 | 1 | 3 | 4 | 0 | -2 |
| classic-concise | developer-docs | 8 | 2 | 4 | 2 | 0 | -2 |
| classic-concise | plain-language | 8 | 2 | 4 | 2 | 0 | -2 |
| classic-concise | technical-simplified | 6 | 1 | 1 | 4 | 0 | 0 |
| classic-concise | unstyled | 8 | 2 | 5 | 1 | 0 | -3 |
| developer-docs | plain-language | 8 | 2 | 2 | 4 | 0 | 0 |
| developer-docs | technical-simplified | 6 | 2 | 2 | 2 | 0 | 0 |
| developer-docs | unstyled | 8 | 4 | 1 | 3 | 0 | 3 |
| plain-language | technical-simplified | 6 | 3 | 2 | 1 | 0 | 1 |
| plain-language | unstyled | 8 | 3 | 2 | 3 | 0 | 1 |
| technical-simplified | unstyled | 6 | 1 | 2 | 3 | 0 | -1 |

## Length confound

Samples: 634 contests with unequal word counts.
Pearson: 0.118. Spearman: 0.172.
Longer-text win rate: 0.652.

## Call timing

A stored call row holds two times: duration_ms is the model
time that the CLI reports, and wall_ms is the wall clock of
the subprocess. The difference is the startup cost of one CLI
call.

Calls: 380, measured: 380.
Mean duration: 5219 ms. Mean wall: 27252 ms. Mean startup: 22034 ms.

## Harness spend

A stored call row holds the token counts of its call: the
uncached input, cache-write input, cache-read input, and
output tokens. The cache-read share is the cache-read total
over the whole input total.

Calls: 380, measured: 380.
Input tokens: 760 uncached, 819146 cache write, 776115 cache read. Output tokens: 22507.
Cache-read share: 0.486.
Cache writes by lifetime: 819146 at 5 minutes, 0 at 1 hour.

## Reuse

Reused rows: 904, imported from 2026-08-10.
Live calls of this run: 380.

The freshness sample re-ran 6 imported verdicts live; 4 agree.
- clarity:code-review-01:0a1c7a01587f0df0441e4eb484dfcf5f6c210f628da21997e31e4577b34e6da0:b272480f9d374dfeb0f425e1889d61f55ea22a6dd3129e06cf1a3ff0271ef64b: the verdicts differ.
- clarity:code-review-01:34a3e0abf162a2a74972e0fb8da5d220600720d01dd1484f0001013dd86f5506:0a1c7a01587f0df0441e4eb484dfcf5f6c210f628da21997e31e4577b34e6da0: the verdicts differ.

Clarity picks: 2 of 6 disagree; the tolerance is 5.

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

- technical-simplified/code-review-06: the pair failed the gate, excluded
- technical-simplified/summarization-06: the pair failed the gate, excluded
- technical-simplified/summarization-08: the pair failed the gate, excluded
- technical-simplified/debugging-07: the pair failed the gate, excluded
- technical-simplified/debugging-08: the pair failed the gate, excluded

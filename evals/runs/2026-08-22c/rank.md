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

Judge: opus. Judged on 2026-08-22T12:09:29+00:00.

## Matchups

| A | B | Contests | A wins | B wins | Splits | Unscored | Net (A) |
|---|---|---|---|---|---|---|---|
| actionable-clarity | clarity-flow | 32 | 25 | 4 | 3 | 0 | 21 |
| actionable-clarity | classic-concise | 32 | 20 | 4 | 8 | 0 | 16 |
| actionable-clarity | concise | 32 | 25 | 2 | 5 | 0 | 23 |
| actionable-clarity | developer-docs | 32 | 17 | 7 | 8 | 0 | 10 |
| actionable-clarity | plain-language | 32 | 19 | 2 | 11 | 0 | 17 |
| actionable-clarity | technical-simplified | 26 | 20 | 2 | 4 | 0 | 18 |
| actionable-clarity | unstyled | 32 | 16 | 6 | 10 | 0 | 10 |
| clarity-flow | classic-concise | 32 | 10 | 10 | 12 | 0 | 0 |
| clarity-flow | concise | 32 | 19 | 7 | 6 | 0 | 12 |
| clarity-flow | developer-docs | 32 | 4 | 21 | 7 | 0 | -17 |
| clarity-flow | plain-language | 32 | 7 | 16 | 9 | 0 | -9 |
| clarity-flow | technical-simplified | 26 | 11 | 4 | 11 | 0 | 7 |
| clarity-flow | unstyled | 32 | 9 | 13 | 10 | 0 | -4 |
| classic-concise | concise | 32 | 15 | 4 | 13 | 0 | 11 |
| classic-concise | developer-docs | 32 | 3 | 22 | 7 | 0 | -19 |
| classic-concise | plain-language | 32 | 5 | 14 | 13 | 0 | -9 |
| classic-concise | technical-simplified | 26 | 11 | 6 | 9 | 0 | 5 |
| classic-concise | unstyled | 32 | 11 | 10 | 11 | 0 | 1 |
| concise | developer-docs | 32 | 2 | 26 | 4 | 0 | -24 |
| concise | plain-language | 32 | 5 | 23 | 4 | 0 | -18 |
| concise | technical-simplified | 26 | 6 | 12 | 8 | 0 | -6 |
| concise | unstyled | 32 | 6 | 18 | 8 | 0 | -12 |
| developer-docs | plain-language | 32 | 16 | 9 | 7 | 0 | 7 |
| developer-docs | technical-simplified | 26 | 22 | 0 | 4 | 0 | 22 |
| developer-docs | unstyled | 32 | 18 | 8 | 6 | 0 | 10 |
| plain-language | technical-simplified | 26 | 18 | 3 | 5 | 0 | 15 |
| plain-language | unstyled | 32 | 14 | 11 | 7 | 0 | 3 |
| technical-simplified | unstyled | 26 | 5 | 15 | 6 | 0 | -10 |

## Win matrix

A cell holds the points of the row competitor against the column
competitor: 1 per decisive win plus 0.5 per split.

| | actionable-clarity | clarity-flow | classic-concise | concise | developer-docs | plain-language | technical-simplified | unstyled |
|---|---|---|---|---|---|---|---|---|
| actionable-clarity | - | 26.5 | 24.0 | 27.5 | 21.0 | 24.5 | 22.0 | 21.0 |
| clarity-flow | 5.5 | - | 16.0 | 22.0 | 7.5 | 11.5 | 16.5 | 14.0 |
| classic-concise | 8.0 | 16.0 | - | 21.5 | 6.5 | 11.5 | 15.5 | 16.5 |
| concise | 4.5 | 10.0 | 10.5 | - | 4.0 | 7.0 | 10.0 | 10.0 |
| developer-docs | 11.0 | 24.5 | 25.5 | 28.0 | - | 19.5 | 24.0 | 21.0 |
| plain-language | 7.5 | 20.5 | 20.5 | 25.0 | 12.5 | - | 20.5 | 17.5 |
| technical-simplified | 4.0 | 9.5 | 10.5 | 16.0 | 2.0 | 5.5 | - | 8.0 |
| unstyled | 11.0 | 18.0 | 15.5 | 22.0 | 11.0 | 14.5 | 18.0 | - |

## Bradley-Terry strengths

The scale is anchored on unstyled at strength 1.0.

The table lists the competitors from the highest strength to the
lowest. A competitor without a finite strength comes last.

| Competitor | Strength | 95% CI |
|---|---|---|
| actionable-clarity | 2.953 | [2.083, 4.318] |
| developer-docs | 2.244 | [1.631, 3.106] |
| plain-language | 1.285 | [0.949, 1.738] |
| unstyled | 1.0 | n/a |
| classic-concise | 0.772 | [0.557, 1.049] |
| clarity-flow | 0.738 | [0.544, 1.023] |
| technical-simplified | 0.438 | [0.305, 0.608] |
| concise | 0.362 | [0.255, 0.515] |

The interval comes from 1000 bootstrap resamples of the scored contests (seed 0).

## Position bias

First-pick rate: 0.396 over 1708 usable picks.
Split rate: 0.253 over 854 judged contests.

## Per task type

### code-review

| A | B | Contests | A wins | B wins | Splits | Unscored | Net (A) |
|---|---|---|---|---|---|---|---|
| actionable-clarity | clarity-flow | 8 | 7 | 0 | 1 | 0 | 7 |
| actionable-clarity | classic-concise | 8 | 7 | 0 | 1 | 0 | 7 |
| actionable-clarity | concise | 8 | 7 | 0 | 1 | 0 | 7 |
| actionable-clarity | developer-docs | 8 | 6 | 1 | 1 | 0 | 5 |
| actionable-clarity | plain-language | 8 | 6 | 0 | 2 | 0 | 6 |
| actionable-clarity | technical-simplified | 7 | 5 | 0 | 2 | 0 | 5 |
| actionable-clarity | unstyled | 8 | 6 | 0 | 2 | 0 | 6 |
| clarity-flow | classic-concise | 8 | 4 | 3 | 1 | 0 | 1 |
| clarity-flow | concise | 8 | 6 | 1 | 1 | 0 | 5 |
| clarity-flow | developer-docs | 8 | 2 | 4 | 2 | 0 | -2 |
| clarity-flow | plain-language | 8 | 3 | 2 | 3 | 0 | 1 |
| clarity-flow | technical-simplified | 7 | 3 | 1 | 3 | 0 | 2 |
| clarity-flow | unstyled | 8 | 3 | 3 | 2 | 0 | 0 |
| classic-concise | concise | 8 | 5 | 0 | 3 | 0 | 5 |
| classic-concise | developer-docs | 8 | 2 | 5 | 1 | 0 | -3 |
| classic-concise | plain-language | 8 | 1 | 3 | 4 | 0 | -2 |
| classic-concise | technical-simplified | 7 | 5 | 2 | 0 | 0 | 3 |
| classic-concise | unstyled | 8 | 2 | 3 | 3 | 0 | -1 |
| concise | developer-docs | 8 | 1 | 5 | 2 | 0 | -4 |
| concise | plain-language | 8 | 1 | 6 | 1 | 0 | -5 |
| concise | technical-simplified | 7 | 2 | 3 | 2 | 0 | -1 |
| concise | unstyled | 8 | 1 | 5 | 2 | 0 | -4 |
| developer-docs | plain-language | 8 | 3 | 4 | 1 | 0 | -1 |
| developer-docs | technical-simplified | 7 | 6 | 0 | 1 | 0 | 6 |
| developer-docs | unstyled | 8 | 3 | 4 | 1 | 0 | -1 |
| plain-language | technical-simplified | 7 | 4 | 2 | 1 | 0 | 2 |
| plain-language | unstyled | 8 | 3 | 4 | 1 | 0 | -1 |
| technical-simplified | unstyled | 7 | 1 | 4 | 2 | 0 | -3 |

### debugging

| A | B | Contests | A wins | B wins | Splits | Unscored | Net (A) |
|---|---|---|---|---|---|---|---|
| actionable-clarity | clarity-flow | 8 | 6 | 2 | 0 | 0 | 4 |
| actionable-clarity | classic-concise | 8 | 3 | 2 | 3 | 0 | 1 |
| actionable-clarity | concise | 8 | 7 | 1 | 0 | 0 | 6 |
| actionable-clarity | developer-docs | 8 | 2 | 4 | 2 | 0 | -2 |
| actionable-clarity | plain-language | 8 | 4 | 2 | 2 | 0 | 2 |
| actionable-clarity | technical-simplified | 7 | 6 | 0 | 1 | 0 | 6 |
| actionable-clarity | unstyled | 8 | 2 | 2 | 4 | 0 | 0 |
| clarity-flow | classic-concise | 8 | 3 | 2 | 3 | 0 | 1 |
| clarity-flow | concise | 8 | 7 | 0 | 1 | 0 | 7 |
| clarity-flow | developer-docs | 8 | 1 | 5 | 2 | 0 | -4 |
| clarity-flow | plain-language | 8 | 1 | 5 | 2 | 0 | -4 |
| clarity-flow | technical-simplified | 7 | 3 | 0 | 4 | 0 | 3 |
| clarity-flow | unstyled | 8 | 3 | 4 | 1 | 0 | -1 |
| classic-concise | concise | 8 | 6 | 2 | 0 | 0 | 4 |
| classic-concise | developer-docs | 8 | 0 | 7 | 1 | 0 | -7 |
| classic-concise | plain-language | 8 | 0 | 4 | 4 | 0 | -4 |
| classic-concise | technical-simplified | 7 | 2 | 2 | 3 | 0 | 0 |
| classic-concise | unstyled | 8 | 2 | 2 | 4 | 0 | 0 |
| concise | developer-docs | 8 | 0 | 8 | 0 | 0 | -8 |
| concise | plain-language | 8 | 0 | 8 | 0 | 0 | -8 |
| concise | technical-simplified | 7 | 0 | 5 | 2 | 0 | -5 |
| concise | unstyled | 8 | 2 | 6 | 0 | 0 | -4 |
| developer-docs | plain-language | 8 | 4 | 1 | 3 | 0 | 3 |
| developer-docs | technical-simplified | 7 | 5 | 0 | 2 | 0 | 5 |
| developer-docs | unstyled | 8 | 5 | 1 | 2 | 0 | 4 |
| plain-language | technical-simplified | 7 | 5 | 0 | 2 | 0 | 5 |
| plain-language | unstyled | 8 | 5 | 2 | 1 | 0 | 3 |
| technical-simplified | unstyled | 7 | 2 | 4 | 1 | 0 | -2 |

### explanation

| A | B | Contests | A wins | B wins | Splits | Unscored | Net (A) |
|---|---|---|---|---|---|---|---|
| actionable-clarity | clarity-flow | 8 | 7 | 1 | 0 | 0 | 6 |
| actionable-clarity | classic-concise | 8 | 5 | 1 | 2 | 0 | 4 |
| actionable-clarity | concise | 8 | 6 | 0 | 2 | 0 | 6 |
| actionable-clarity | developer-docs | 8 | 4 | 1 | 3 | 0 | 3 |
| actionable-clarity | plain-language | 8 | 5 | 0 | 3 | 0 | 5 |
| actionable-clarity | technical-simplified | 7 | 6 | 1 | 0 | 0 | 5 |
| actionable-clarity | unstyled | 8 | 4 | 3 | 1 | 0 | 1 |
| clarity-flow | classic-concise | 8 | 0 | 4 | 4 | 0 | -4 |
| clarity-flow | concise | 8 | 3 | 3 | 2 | 0 | 0 |
| clarity-flow | developer-docs | 8 | 0 | 7 | 1 | 0 | -7 |
| clarity-flow | plain-language | 8 | 2 | 5 | 1 | 0 | -3 |
| clarity-flow | technical-simplified | 7 | 4 | 1 | 2 | 0 | 3 |
| clarity-flow | unstyled | 8 | 1 | 4 | 3 | 0 | -3 |
| classic-concise | concise | 8 | 4 | 0 | 4 | 0 | 4 |
| classic-concise | developer-docs | 8 | 1 | 5 | 2 | 0 | -4 |
| classic-concise | plain-language | 8 | 3 | 3 | 2 | 0 | 0 |
| classic-concise | technical-simplified | 7 | 4 | 1 | 2 | 0 | 3 |
| classic-concise | unstyled | 8 | 5 | 3 | 0 | 0 | 2 |
| concise | developer-docs | 8 | 0 | 7 | 1 | 0 | -7 |
| concise | plain-language | 8 | 2 | 4 | 2 | 0 | -2 |
| concise | technical-simplified | 7 | 3 | 2 | 2 | 0 | 1 |
| concise | unstyled | 8 | 1 | 5 | 2 | 0 | -4 |
| developer-docs | plain-language | 8 | 6 | 2 | 0 | 0 | 4 |
| developer-docs | technical-simplified | 7 | 7 | 0 | 0 | 0 | 7 |
| developer-docs | unstyled | 8 | 5 | 3 | 0 | 0 | 2 |
| plain-language | technical-simplified | 7 | 6 | 0 | 1 | 0 | 6 |
| plain-language | unstyled | 8 | 3 | 4 | 1 | 0 | -1 |
| technical-simplified | unstyled | 7 | 0 | 5 | 2 | 0 | -5 |

### summarization

| A | B | Contests | A wins | B wins | Splits | Unscored | Net (A) |
|---|---|---|---|---|---|---|---|
| actionable-clarity | clarity-flow | 8 | 5 | 1 | 2 | 0 | 4 |
| actionable-clarity | classic-concise | 8 | 5 | 1 | 2 | 0 | 4 |
| actionable-clarity | concise | 8 | 5 | 1 | 2 | 0 | 4 |
| actionable-clarity | developer-docs | 8 | 5 | 1 | 2 | 0 | 4 |
| actionable-clarity | plain-language | 8 | 4 | 0 | 4 | 0 | 4 |
| actionable-clarity | technical-simplified | 5 | 3 | 1 | 1 | 0 | 2 |
| actionable-clarity | unstyled | 8 | 4 | 1 | 3 | 0 | 3 |
| clarity-flow | classic-concise | 8 | 3 | 1 | 4 | 0 | 2 |
| clarity-flow | concise | 8 | 3 | 3 | 2 | 0 | 0 |
| clarity-flow | developer-docs | 8 | 1 | 5 | 2 | 0 | -4 |
| clarity-flow | plain-language | 8 | 1 | 4 | 3 | 0 | -3 |
| clarity-flow | technical-simplified | 5 | 1 | 2 | 2 | 0 | -1 |
| clarity-flow | unstyled | 8 | 2 | 2 | 4 | 0 | 0 |
| classic-concise | concise | 8 | 0 | 2 | 6 | 0 | -2 |
| classic-concise | developer-docs | 8 | 0 | 5 | 3 | 0 | -5 |
| classic-concise | plain-language | 8 | 1 | 4 | 3 | 0 | -3 |
| classic-concise | technical-simplified | 5 | 0 | 1 | 4 | 0 | -1 |
| classic-concise | unstyled | 8 | 2 | 2 | 4 | 0 | 0 |
| concise | developer-docs | 8 | 1 | 6 | 1 | 0 | -5 |
| concise | plain-language | 8 | 2 | 5 | 1 | 0 | -3 |
| concise | technical-simplified | 5 | 1 | 2 | 2 | 0 | -1 |
| concise | unstyled | 8 | 2 | 2 | 4 | 0 | 0 |
| developer-docs | plain-language | 8 | 3 | 2 | 3 | 0 | 1 |
| developer-docs | technical-simplified | 5 | 4 | 0 | 1 | 0 | 4 |
| developer-docs | unstyled | 8 | 5 | 0 | 3 | 0 | 5 |
| plain-language | technical-simplified | 5 | 3 | 1 | 1 | 0 | 2 |
| plain-language | unstyled | 8 | 3 | 1 | 4 | 0 | 2 |
| technical-simplified | unstyled | 5 | 2 | 2 | 1 | 0 | 0 |

## Length confound

Samples: 847 contests with unequal word counts.
Pearson: 0.129. Spearman: 0.298.
Longer-text win rate: 0.691.

## Call timing

A stored call row holds two times: duration_ms is the model
time that the CLI reports, and wall_ms is the wall clock of
the subprocess. The difference is the startup cost of one CLI
call.

Calls: 1708, measured: 1708.
Mean duration: 2365 ms. Mean wall: 90832 ms. Mean startup: 88466 ms.

## Harness spend

A stored call row holds the token counts of its call: the
uncached input, cache-write input, cache-read input, and
output tokens. The cache-read share is the cache-read total
over the whole input total.

Calls: 1708, measured: 1708.
Input tokens: 3416 uncached, 3482986 cache write, 3545808 cache read. Output tokens: 73201.
Cache-read share: 0.504.
Cache writes by lifetime: 3482986 at 5 minutes, 0 at 1 hour.

## Warnings

- technical-simplified/explanation-08: the pair failed the gate, excluded
- technical-simplified/code-review-08: the pair failed the gate, excluded
- technical-simplified/summarization-06: the pair failed the gate, excluded
- technical-simplified/summarization-07: the pair failed the gate, excluded
- technical-simplified/summarization-08: the pair failed the gate, excluded
- technical-simplified/debugging-06: the pair failed the gate, excluded

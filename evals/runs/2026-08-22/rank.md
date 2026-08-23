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

Judge: opus. Judged on 2026-08-22T09:32:02+00:00.

## Matchups

| A | B | Contests | A wins | B wins | Splits | Unscored | Net (A) |
|---|---|---|---|---|---|---|---|
| actionable-clarity | clarity-flow | 32 | 23 | 3 | 6 | 0 | 20 |
| actionable-clarity | classic-concise | 32 | 18 | 7 | 7 | 0 | 11 |
| actionable-clarity | concise | 32 | 21 | 2 | 9 | 0 | 19 |
| actionable-clarity | developer-docs | 32 | 18 | 4 | 10 | 0 | 14 |
| actionable-clarity | plain-language | 32 | 17 | 6 | 9 | 0 | 11 |
| actionable-clarity | technical-simplified | 26 | 22 | 1 | 3 | 0 | 21 |
| actionable-clarity | unstyled | 32 | 12 | 7 | 13 | 0 | 5 |
| clarity-flow | classic-concise | 32 | 8 | 12 | 12 | 0 | -4 |
| clarity-flow | concise | 32 | 11 | 4 | 17 | 0 | 7 |
| clarity-flow | developer-docs | 32 | 6 | 21 | 5 | 0 | -15 |
| clarity-flow | plain-language | 32 | 7 | 23 | 2 | 0 | -16 |
| clarity-flow | technical-simplified | 26 | 8 | 10 | 8 | 0 | -2 |
| clarity-flow | unstyled | 32 | 7 | 19 | 6 | 0 | -12 |
| classic-concise | concise | 32 | 17 | 5 | 10 | 0 | 12 |
| classic-concise | developer-docs | 32 | 5 | 15 | 12 | 0 | -10 |
| classic-concise | plain-language | 32 | 7 | 13 | 12 | 0 | -6 |
| classic-concise | technical-simplified | 26 | 12 | 8 | 6 | 0 | 4 |
| classic-concise | unstyled | 32 | 7 | 13 | 12 | 0 | -6 |
| concise | developer-docs | 32 | 1 | 21 | 10 | 0 | -20 |
| concise | plain-language | 32 | 2 | 24 | 6 | 0 | -22 |
| concise | technical-simplified | 26 | 4 | 11 | 11 | 0 | -7 |
| concise | unstyled | 32 | 4 | 18 | 10 | 0 | -14 |
| developer-docs | plain-language | 32 | 9 | 9 | 14 | 0 | 0 |
| developer-docs | technical-simplified | 26 | 19 | 1 | 6 | 0 | 18 |
| developer-docs | unstyled | 32 | 10 | 8 | 14 | 0 | 2 |
| plain-language | technical-simplified | 26 | 15 | 2 | 9 | 0 | 13 |
| plain-language | unstyled | 32 | 12 | 8 | 12 | 0 | 4 |
| technical-simplified | unstyled | 26 | 6 | 16 | 4 | 0 | -10 |

## Win matrix

A cell holds the points of the row competitor against the column
competitor: 1 per decisive win plus 0.5 per split.

| | actionable-clarity | clarity-flow | classic-concise | concise | developer-docs | plain-language | technical-simplified | unstyled |
|---|---|---|---|---|---|---|---|---|
| actionable-clarity | - | 26.0 | 21.5 | 25.5 | 23.0 | 21.5 | 23.5 | 18.5 |
| clarity-flow | 6.0 | - | 14.0 | 19.5 | 8.5 | 8.0 | 12.0 | 10.0 |
| classic-concise | 10.5 | 18.0 | - | 22.0 | 11.0 | 13.0 | 15.0 | 13.0 |
| concise | 6.5 | 12.5 | 10.0 | - | 6.0 | 5.0 | 9.5 | 9.0 |
| developer-docs | 9.0 | 23.5 | 21.0 | 26.0 | - | 16.0 | 22.0 | 17.0 |
| plain-language | 10.5 | 24.0 | 19.0 | 27.0 | 16.0 | - | 19.5 | 18.0 |
| technical-simplified | 2.5 | 14.0 | 11.0 | 16.5 | 4.0 | 6.5 | - | 8.0 |
| unstyled | 13.5 | 22.0 | 19.0 | 23.0 | 15.0 | 14.0 | 18.0 | - |

## Bradley-Terry strengths

The scale is anchored on unstyled at strength 1.0.

The table lists the competitors from the highest strength to the
lowest. A competitor without a finite strength comes last.

| Competitor | Strength | 95% CI |
|---|---|---|
| actionable-clarity | 1.928 | [1.411, 2.647] |
| developer-docs | 1.196 | [0.892, 1.585] |
| plain-language | 1.185 | [0.86, 1.611] |
| unstyled | 1.0 | n/a |
| classic-concise | 0.681 | [0.5, 0.899] |
| clarity-flow | 0.439 | [0.317, 0.606] |
| technical-simplified | 0.407 | [0.295, 0.55] |
| concise | 0.301 | [0.221, 0.404] |

The interval comes from 1000 bootstrap resamples of the scored contests (seed 0).

## Position bias

First-pick rate: 0.369 over 1708 usable picks.
Split rate: 0.299 over 854 judged contests.

## Per task type

### code-review

| A | B | Contests | A wins | B wins | Splits | Unscored | Net (A) |
|---|---|---|---|---|---|---|---|
| actionable-clarity | clarity-flow | 8 | 5 | 1 | 2 | 0 | 4 |
| actionable-clarity | classic-concise | 8 | 3 | 3 | 2 | 0 | 0 |
| actionable-clarity | concise | 8 | 6 | 0 | 2 | 0 | 6 |
| actionable-clarity | developer-docs | 8 | 5 | 0 | 3 | 0 | 5 |
| actionable-clarity | plain-language | 8 | 4 | 1 | 3 | 0 | 3 |
| actionable-clarity | technical-simplified | 7 | 7 | 0 | 0 | 0 | 7 |
| actionable-clarity | unstyled | 8 | 4 | 2 | 2 | 0 | 2 |
| clarity-flow | classic-concise | 8 | 1 | 5 | 2 | 0 | -4 |
| clarity-flow | concise | 8 | 4 | 1 | 3 | 0 | 3 |
| clarity-flow | developer-docs | 8 | 3 | 3 | 2 | 0 | 0 |
| clarity-flow | plain-language | 8 | 2 | 5 | 1 | 0 | -3 |
| clarity-flow | technical-simplified | 7 | 4 | 1 | 2 | 0 | 3 |
| clarity-flow | unstyled | 8 | 3 | 4 | 1 | 0 | -1 |
| classic-concise | concise | 8 | 5 | 1 | 2 | 0 | 4 |
| classic-concise | developer-docs | 8 | 2 | 2 | 4 | 0 | 0 |
| classic-concise | plain-language | 8 | 2 | 2 | 4 | 0 | 0 |
| classic-concise | technical-simplified | 7 | 5 | 1 | 1 | 0 | 4 |
| classic-concise | unstyled | 8 | 3 | 3 | 2 | 0 | 0 |
| concise | developer-docs | 8 | 0 | 5 | 3 | 0 | -5 |
| concise | plain-language | 8 | 0 | 6 | 2 | 0 | -6 |
| concise | technical-simplified | 7 | 2 | 3 | 2 | 0 | -1 |
| concise | unstyled | 8 | 3 | 3 | 2 | 0 | 0 |
| developer-docs | plain-language | 8 | 2 | 2 | 4 | 0 | 0 |
| developer-docs | technical-simplified | 7 | 7 | 0 | 0 | 0 | 7 |
| developer-docs | unstyled | 8 | 2 | 2 | 4 | 0 | 0 |
| plain-language | technical-simplified | 7 | 3 | 1 | 3 | 0 | 2 |
| plain-language | unstyled | 8 | 3 | 2 | 3 | 0 | 1 |
| technical-simplified | unstyled | 7 | 2 | 4 | 1 | 0 | -2 |

### debugging

| A | B | Contests | A wins | B wins | Splits | Unscored | Net (A) |
|---|---|---|---|---|---|---|---|
| actionable-clarity | clarity-flow | 8 | 6 | 0 | 2 | 0 | 6 |
| actionable-clarity | classic-concise | 8 | 6 | 1 | 1 | 0 | 5 |
| actionable-clarity | concise | 8 | 6 | 0 | 2 | 0 | 6 |
| actionable-clarity | developer-docs | 8 | 4 | 2 | 2 | 0 | 2 |
| actionable-clarity | plain-language | 8 | 4 | 1 | 3 | 0 | 3 |
| actionable-clarity | technical-simplified | 7 | 6 | 0 | 1 | 0 | 6 |
| actionable-clarity | unstyled | 8 | 1 | 3 | 4 | 0 | -2 |
| clarity-flow | classic-concise | 8 | 4 | 1 | 3 | 0 | 3 |
| clarity-flow | concise | 8 | 4 | 0 | 4 | 0 | 4 |
| clarity-flow | developer-docs | 8 | 1 | 5 | 2 | 0 | -4 |
| clarity-flow | plain-language | 8 | 2 | 5 | 1 | 0 | -3 |
| clarity-flow | technical-simplified | 7 | 2 | 3 | 2 | 0 | -1 |
| clarity-flow | unstyled | 8 | 0 | 6 | 2 | 0 | -6 |
| classic-concise | concise | 8 | 3 | 1 | 4 | 0 | 2 |
| classic-concise | developer-docs | 8 | 1 | 5 | 2 | 0 | -4 |
| classic-concise | plain-language | 8 | 0 | 4 | 4 | 0 | -4 |
| classic-concise | technical-simplified | 7 | 3 | 3 | 1 | 0 | 0 |
| classic-concise | unstyled | 8 | 1 | 4 | 3 | 0 | -3 |
| concise | developer-docs | 8 | 0 | 6 | 2 | 0 | -6 |
| concise | plain-language | 8 | 0 | 6 | 2 | 0 | -6 |
| concise | technical-simplified | 7 | 0 | 3 | 4 | 0 | -3 |
| concise | unstyled | 8 | 0 | 8 | 0 | 0 | -8 |
| developer-docs | plain-language | 8 | 1 | 3 | 4 | 0 | -2 |
| developer-docs | technical-simplified | 7 | 3 | 0 | 4 | 0 | 3 |
| developer-docs | unstyled | 8 | 0 | 3 | 5 | 0 | -3 |
| plain-language | technical-simplified | 7 | 5 | 1 | 1 | 0 | 4 |
| plain-language | unstyled | 8 | 1 | 3 | 4 | 0 | -2 |
| technical-simplified | unstyled | 7 | 1 | 6 | 0 | 0 | -5 |

### explanation

| A | B | Contests | A wins | B wins | Splits | Unscored | Net (A) |
|---|---|---|---|---|---|---|---|
| actionable-clarity | clarity-flow | 8 | 6 | 0 | 2 | 0 | 6 |
| actionable-clarity | classic-concise | 8 | 4 | 1 | 3 | 0 | 3 |
| actionable-clarity | concise | 8 | 5 | 1 | 2 | 0 | 4 |
| actionable-clarity | developer-docs | 8 | 4 | 2 | 2 | 0 | 2 |
| actionable-clarity | plain-language | 8 | 4 | 3 | 1 | 0 | 1 |
| actionable-clarity | technical-simplified | 7 | 5 | 0 | 2 | 0 | 5 |
| actionable-clarity | unstyled | 8 | 1 | 2 | 5 | 0 | -1 |
| clarity-flow | classic-concise | 8 | 1 | 4 | 3 | 0 | -3 |
| clarity-flow | concise | 8 | 2 | 2 | 4 | 0 | 0 |
| clarity-flow | developer-docs | 8 | 1 | 7 | 0 | 0 | -6 |
| clarity-flow | plain-language | 8 | 1 | 7 | 0 | 0 | -6 |
| clarity-flow | technical-simplified | 7 | 2 | 2 | 3 | 0 | 0 |
| clarity-flow | unstyled | 8 | 0 | 7 | 1 | 0 | -7 |
| classic-concise | concise | 8 | 6 | 0 | 2 | 0 | 6 |
| classic-concise | developer-docs | 8 | 1 | 5 | 2 | 0 | -4 |
| classic-concise | plain-language | 8 | 2 | 4 | 2 | 0 | -2 |
| classic-concise | technical-simplified | 7 | 4 | 1 | 2 | 0 | 3 |
| classic-concise | unstyled | 8 | 0 | 4 | 4 | 0 | -4 |
| concise | developer-docs | 8 | 0 | 7 | 1 | 0 | -7 |
| concise | plain-language | 8 | 0 | 7 | 1 | 0 | -7 |
| concise | technical-simplified | 7 | 2 | 1 | 4 | 0 | 1 |
| concise | unstyled | 8 | 0 | 5 | 3 | 0 | -5 |
| developer-docs | plain-language | 8 | 3 | 2 | 3 | 0 | 1 |
| developer-docs | technical-simplified | 7 | 6 | 1 | 0 | 0 | 5 |
| developer-docs | unstyled | 8 | 2 | 3 | 3 | 0 | -1 |
| plain-language | technical-simplified | 7 | 5 | 0 | 2 | 0 | 5 |
| plain-language | unstyled | 8 | 4 | 2 | 2 | 0 | 2 |
| technical-simplified | unstyled | 7 | 0 | 5 | 2 | 0 | -5 |

### summarization

| A | B | Contests | A wins | B wins | Splits | Unscored | Net (A) |
|---|---|---|---|---|---|---|---|
| actionable-clarity | clarity-flow | 8 | 6 | 2 | 0 | 0 | 4 |
| actionable-clarity | classic-concise | 8 | 5 | 2 | 1 | 0 | 3 |
| actionable-clarity | concise | 8 | 4 | 1 | 3 | 0 | 3 |
| actionable-clarity | developer-docs | 8 | 5 | 0 | 3 | 0 | 5 |
| actionable-clarity | plain-language | 8 | 5 | 1 | 2 | 0 | 4 |
| actionable-clarity | technical-simplified | 5 | 4 | 1 | 0 | 0 | 3 |
| actionable-clarity | unstyled | 8 | 6 | 0 | 2 | 0 | 6 |
| clarity-flow | classic-concise | 8 | 2 | 2 | 4 | 0 | 0 |
| clarity-flow | concise | 8 | 1 | 1 | 6 | 0 | 0 |
| clarity-flow | developer-docs | 8 | 1 | 6 | 1 | 0 | -5 |
| clarity-flow | plain-language | 8 | 2 | 6 | 0 | 0 | -4 |
| clarity-flow | technical-simplified | 5 | 0 | 4 | 1 | 0 | -4 |
| clarity-flow | unstyled | 8 | 4 | 2 | 2 | 0 | 2 |
| classic-concise | concise | 8 | 3 | 3 | 2 | 0 | 0 |
| classic-concise | developer-docs | 8 | 1 | 3 | 4 | 0 | -2 |
| classic-concise | plain-language | 8 | 3 | 3 | 2 | 0 | 0 |
| classic-concise | technical-simplified | 5 | 0 | 3 | 2 | 0 | -3 |
| classic-concise | unstyled | 8 | 3 | 2 | 3 | 0 | 1 |
| concise | developer-docs | 8 | 1 | 3 | 4 | 0 | -2 |
| concise | plain-language | 8 | 2 | 5 | 1 | 0 | -3 |
| concise | technical-simplified | 5 | 0 | 4 | 1 | 0 | -4 |
| concise | unstyled | 8 | 1 | 2 | 5 | 0 | -1 |
| developer-docs | plain-language | 8 | 3 | 2 | 3 | 0 | 1 |
| developer-docs | technical-simplified | 5 | 3 | 0 | 2 | 0 | 3 |
| developer-docs | unstyled | 8 | 6 | 0 | 2 | 0 | 6 |
| plain-language | technical-simplified | 5 | 2 | 0 | 3 | 0 | 2 |
| plain-language | unstyled | 8 | 4 | 1 | 3 | 0 | 3 |
| technical-simplified | unstyled | 5 | 3 | 1 | 1 | 0 | 2 |

## Length confound

Samples: 849 contests with unequal word counts.
Pearson: 0.149. Spearman: 0.212.
Longer-text win rate: 0.67.

## Call timing

A stored call row holds two times: duration_ms is the model
time that the CLI reports, and wall_ms is the wall clock of
the subprocess. The difference is the startup cost of one CLI
call.

Calls: 1708, measured: 1708.
Mean duration: 2330 ms. Mean wall: 90821 ms. Mean startup: 88491 ms.

## Harness spend

A stored call row holds the token counts of its call: the
uncached input, cache-write input, cache-read input, and
output tokens. The cache-read share is the cache-read total
over the whole input total.

Calls: 1708, measured: 1708.
Input tokens: 3416 uncached, 3606138 cache write, 3545808 cache read. Output tokens: 62886.
Cache-read share: 0.496.
Cache writes by lifetime: 3606138 at 5 minutes, 0 at 1 hour.

## Warnings

- technical-simplified/explanation-08: the pair failed the gate, excluded
- technical-simplified/code-review-07: the pair failed the gate, excluded
- technical-simplified/summarization-06: the pair failed the gate, excluded
- technical-simplified/summarization-07: the pair failed the gate, excluded
- technical-simplified/summarization-08: the pair failed the gate, excluded
- technical-simplified/debugging-07: the pair failed the gate, excluded

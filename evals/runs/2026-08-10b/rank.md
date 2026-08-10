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

Judge: opus. Judged on 2026-08-10T07:47:44+00:00.

## Matchups

| A | B | Contests | A wins | B wins | Splits | Unscored | Net (A) |
|---|---|---|---|---|---|---|---|
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

| | clarity-flow | classic-concise | developer-docs | plain-language | technical-simplified | unstyled |
|---|---|---|---|---|---|---|
| clarity-flow | - | 17.5 | 8.5 | 9.5 | 23.0 | 12.5 |
| classic-concise | 14.5 | - | 6.5 | 7.5 | 17.0 | 13.0 |
| developer-docs | 23.5 | 25.5 | - | 12.5 | 23.0 | 22.0 |
| plain-language | 22.5 | 24.5 | 19.5 | - | 23.5 | 23.0 |
| technical-simplified | 6.0 | 12.0 | 6.0 | 5.5 | - | 11.0 |
| unstyled | 19.5 | 19.0 | 10.0 | 9.0 | 18.0 | - |

## Bradley-Terry strengths

The scale is anchored on unstyled at strength 1.0.

The table lists the competitors from the highest strength to the
lowest. A competitor without a finite strength comes last.

| Competitor | Strength | 95% CI |
|---|---|---|
| plain-language | 2.453 | [1.73, 3.602] |
| developer-docs | 2.077 | [1.534, 3.054] |
| unstyled | 1.0 | n/a |
| clarity-flow | 0.902 | [0.664, 1.265] |
| classic-concise | 0.673 | [0.48, 0.929] |
| technical-simplified | 0.459 | [0.322, 0.64] |

The interval comes from 1000 bootstrap resamples of the scored contests (seed 0).

## Position bias

First-pick rate: 0.399 over 930 usable picks.
Split rate: 0.314 over 465 judged contests.

## Per task type

### code-review

| A | B | Contests | A wins | B wins | Splits | Unscored | Net (A) |
|---|---|---|---|---|---|---|---|
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

Samples: 462 contests with unequal word counts.
Pearson: 0.134. Spearman: 0.216.
Longer-text win rate: 0.623.

## Call timing

A stored call row holds two times: duration_ms is the model
time that the CLI reports, and wall_ms is the wall clock of
the subprocess. The difference is the startup cost of one CLI
call.

Calls: 930, measured: 930.
Mean duration: 3717 ms. Mean wall: 128396 ms. Mean startup: 124680 ms.

## Harness spend

A stored call row holds the token counts of its call: the
uncached input, cache-write input, cache-read input, and
output tokens. The cache-read share is the cache-read total
over the whole input total.

Calls: 930, measured: 930.
Input tokens: 1860 uncached, 1929624 cache write, 1909290 cache read. Output tokens: 36201.
Cache-read share: 0.497.
Cache writes by lifetime: 1929624 at 5 minutes, 0 at 1 hour.

## Warnings

- technical-simplified/explanation-01: the pair failed the gate, excluded
- technical-simplified/summarization-06: the pair failed the gate, excluded
- technical-simplified/summarization-08: the pair failed the gate, excluded

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

Judge: opus. Judged on 2026-08-08T08:26:14+00:00.

## Matchups

| A | B | Contests | A wins | B wins | Splits | Unscored | Net (A) |
|---|---|---|---|---|---|---|---|
| clarity-flow | classic-concise | 32 | 16 | 9 | 7 | 0 | 7 |
| clarity-flow | developer-docs | 32 | 8 | 13 | 11 | 0 | -5 |
| clarity-flow | plain-language | 32 | 8 | 17 | 7 | 0 | -9 |
| clarity-flow | technical-simplified | 27 | 15 | 5 | 7 | 0 | 10 |
| clarity-flow | unstyled | 32 | 12 | 10 | 10 | 0 | 2 |
| classic-concise | developer-docs | 32 | 7 | 17 | 8 | 0 | -10 |
| classic-concise | plain-language | 32 | 4 | 14 | 14 | 0 | -10 |
| classic-concise | technical-simplified | 27 | 8 | 6 | 13 | 0 | 2 |
| classic-concise | unstyled | 32 | 4 | 15 | 13 | 0 | -11 |
| developer-docs | plain-language | 32 | 9 | 11 | 12 | 0 | -2 |
| developer-docs | technical-simplified | 27 | 15 | 5 | 7 | 0 | 10 |
| developer-docs | unstyled | 32 | 14 | 11 | 7 | 0 | 3 |
| plain-language | technical-simplified | 27 | 18 | 1 | 8 | 0 | 17 |
| plain-language | unstyled | 32 | 14 | 8 | 10 | 0 | 6 |
| technical-simplified | unstyled | 27 | 4 | 14 | 9 | 0 | -10 |

## Win matrix

A cell holds the points of the row competitor against the column
competitor: 1 per decisive win plus 0.5 per split.

| | clarity-flow | classic-concise | developer-docs | plain-language | technical-simplified | unstyled |
|---|---|---|---|---|---|---|
| clarity-flow | - | 19.5 | 13.5 | 11.5 | 18.5 | 17.0 |
| classic-concise | 12.5 | - | 11.0 | 11.0 | 14.5 | 10.5 |
| developer-docs | 18.5 | 21.0 | - | 15.0 | 18.5 | 17.5 |
| plain-language | 20.5 | 21.0 | 17.0 | - | 22.0 | 19.0 |
| technical-simplified | 8.5 | 12.5 | 8.5 | 5.0 | - | 8.5 |
| unstyled | 15.0 | 21.5 | 14.5 | 13.0 | 18.5 | - |

## Bradley-Terry strengths

The scale is anchored on unstyled at strength 1.0.

The table lists the competitors from the highest strength to the
lowest. A competitor without a finite strength comes last.

| Competitor | Strength | 95% CI |
|---|---|---|
| plain-language | 1.471 | [1.022, 2.088] |
| developer-docs | 1.196 | [0.853, 1.71] |
| unstyled | 1.0 | n/a |
| clarity-flow | 0.946 | [0.655, 1.328] |
| classic-concise | 0.597 | [0.414, 0.834] |
| technical-simplified | 0.46 | [0.314, 0.658] |

The interval comes from 1000 bootstrap resamples of the scored contests (seed 0).

## Position bias

First-pick rate: 0.391 over 910 usable picks.
Split rate: 0.314 over 455 judged contests.

## Per task type

### code-review

| A | B | Contests | A wins | B wins | Splits | Unscored | Net (A) |
|---|---|---|---|---|---|---|---|
| clarity-flow | classic-concise | 8 | 4 | 3 | 1 | 0 | 1 |
| clarity-flow | developer-docs | 8 | 0 | 4 | 4 | 0 | -4 |
| clarity-flow | plain-language | 8 | 1 | 5 | 2 | 0 | -4 |
| clarity-flow | technical-simplified | 8 | 6 | 1 | 1 | 0 | 5 |
| clarity-flow | unstyled | 8 | 3 | 2 | 3 | 0 | 1 |
| classic-concise | developer-docs | 8 | 1 | 5 | 2 | 0 | -4 |
| classic-concise | plain-language | 8 | 1 | 5 | 2 | 0 | -4 |
| classic-concise | technical-simplified | 8 | 2 | 2 | 4 | 0 | 0 |
| classic-concise | unstyled | 8 | 2 | 2 | 4 | 0 | 0 |
| developer-docs | plain-language | 8 | 3 | 2 | 3 | 0 | 1 |
| developer-docs | technical-simplified | 8 | 5 | 0 | 3 | 0 | 5 |
| developer-docs | unstyled | 8 | 4 | 1 | 3 | 0 | 3 |
| plain-language | technical-simplified | 8 | 5 | 1 | 2 | 0 | 4 |
| plain-language | unstyled | 8 | 3 | 2 | 3 | 0 | 1 |
| technical-simplified | unstyled | 8 | 1 | 5 | 2 | 0 | -4 |

### debugging

| A | B | Contests | A wins | B wins | Splits | Unscored | Net (A) |
|---|---|---|---|---|---|---|---|
| clarity-flow | classic-concise | 8 | 6 | 0 | 2 | 0 | 6 |
| clarity-flow | developer-docs | 8 | 2 | 3 | 3 | 0 | -1 |
| clarity-flow | plain-language | 8 | 2 | 5 | 1 | 0 | -3 |
| clarity-flow | technical-simplified | 6 | 3 | 1 | 2 | 0 | 2 |
| clarity-flow | unstyled | 8 | 3 | 3 | 2 | 0 | 0 |
| classic-concise | developer-docs | 8 | 1 | 5 | 2 | 0 | -4 |
| classic-concise | plain-language | 8 | 0 | 3 | 5 | 0 | -3 |
| classic-concise | technical-simplified | 6 | 2 | 2 | 2 | 0 | 0 |
| classic-concise | unstyled | 8 | 0 | 5 | 3 | 0 | -5 |
| developer-docs | plain-language | 8 | 2 | 4 | 2 | 0 | -2 |
| developer-docs | technical-simplified | 6 | 3 | 2 | 1 | 0 | 1 |
| developer-docs | unstyled | 8 | 4 | 4 | 0 | 0 | 0 |
| plain-language | technical-simplified | 6 | 5 | 0 | 1 | 0 | 5 |
| plain-language | unstyled | 8 | 4 | 2 | 2 | 0 | 2 |
| technical-simplified | unstyled | 6 | 2 | 3 | 1 | 0 | -1 |

### explanation

| A | B | Contests | A wins | B wins | Splits | Unscored | Net (A) |
|---|---|---|---|---|---|---|---|
| clarity-flow | classic-concise | 8 | 2 | 4 | 2 | 0 | -2 |
| clarity-flow | developer-docs | 8 | 3 | 3 | 2 | 0 | 0 |
| clarity-flow | plain-language | 8 | 2 | 5 | 1 | 0 | -3 |
| clarity-flow | technical-simplified | 7 | 4 | 1 | 2 | 0 | 3 |
| clarity-flow | unstyled | 8 | 2 | 3 | 3 | 0 | -1 |
| classic-concise | developer-docs | 8 | 2 | 4 | 2 | 0 | -2 |
| classic-concise | plain-language | 8 | 0 | 3 | 5 | 0 | -3 |
| classic-concise | technical-simplified | 7 | 3 | 0 | 4 | 0 | 3 |
| classic-concise | unstyled | 8 | 1 | 3 | 4 | 0 | -2 |
| developer-docs | plain-language | 8 | 2 | 3 | 3 | 0 | -1 |
| developer-docs | technical-simplified | 7 | 4 | 1 | 2 | 0 | 3 |
| developer-docs | unstyled | 8 | 2 | 4 | 2 | 0 | -2 |
| plain-language | technical-simplified | 7 | 5 | 0 | 2 | 0 | 5 |
| plain-language | unstyled | 8 | 4 | 2 | 2 | 0 | 2 |
| technical-simplified | unstyled | 7 | 0 | 4 | 3 | 0 | -4 |

### summarization

| A | B | Contests | A wins | B wins | Splits | Unscored | Net (A) |
|---|---|---|---|---|---|---|---|
| clarity-flow | classic-concise | 8 | 4 | 2 | 2 | 0 | 2 |
| clarity-flow | developer-docs | 8 | 3 | 3 | 2 | 0 | 0 |
| clarity-flow | plain-language | 8 | 3 | 2 | 3 | 0 | 1 |
| clarity-flow | technical-simplified | 6 | 2 | 2 | 2 | 0 | 0 |
| clarity-flow | unstyled | 8 | 4 | 2 | 2 | 0 | 2 |
| classic-concise | developer-docs | 8 | 3 | 3 | 2 | 0 | 0 |
| classic-concise | plain-language | 8 | 3 | 3 | 2 | 0 | 0 |
| classic-concise | technical-simplified | 6 | 1 | 2 | 3 | 0 | -1 |
| classic-concise | unstyled | 8 | 1 | 5 | 2 | 0 | -4 |
| developer-docs | plain-language | 8 | 2 | 2 | 4 | 0 | 0 |
| developer-docs | technical-simplified | 6 | 3 | 2 | 1 | 0 | 1 |
| developer-docs | unstyled | 8 | 4 | 2 | 2 | 0 | 2 |
| plain-language | technical-simplified | 6 | 3 | 0 | 3 | 0 | 3 |
| plain-language | unstyled | 8 | 3 | 2 | 3 | 0 | 1 |
| technical-simplified | unstyled | 6 | 1 | 2 | 3 | 0 | -1 |

## Length confound

Samples: 450 contests with unequal word counts.
Pearson: 0.118. Spearman: 0.166.
Longer-text win rate: 0.633.

## Call timing

A stored call row holds two times: duration_ms is the model
time that the CLI reports, and wall_ms is the wall clock of
the subprocess. The difference is the startup cost of one CLI
call.

Calls: 910, measured: 910.
Mean duration: 2833 ms. Mean wall: 70824 ms. Mean startup: 67992 ms.

## Harness spend

A stored call row holds the token counts of its call: the
uncached input, cache-write input, cache-read input, and
output tokens. The cache-read share is the cache-read total
over the whole input total.

Calls: 910, measured: 910.
Input tokens: 1820 uncached, 1887640 cache write, 1868230 cache read. Output tokens: 42688.
Cache-read share: 0.497.

## Warnings

- technical-simplified/explanation-01: the pair failed the gate, excluded
- technical-simplified/summarization-06: the pair failed the gate, excluded
- technical-simplified/summarization-08: the pair failed the gate, excluded
- technical-simplified/debugging-04: the pair failed the gate, excluded
- technical-simplified/debugging-07: the pair failed the gate, excluded

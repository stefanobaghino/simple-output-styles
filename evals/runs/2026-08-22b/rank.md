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

Judge: opus. Judged on 2026-08-22T10:58:54+00:00.

## Matchups

| A | B | Contests | A wins | B wins | Splits | Unscored | Net (A) |
|---|---|---|---|---|---|---|---|
| actionable-clarity | clarity-flow | 32 | 20 | 6 | 6 | 0 | 14 |
| actionable-clarity | classic-concise | 32 | 19 | 3 | 10 | 0 | 16 |
| actionable-clarity | concise | 32 | 26 | 2 | 4 | 0 | 24 |
| actionable-clarity | developer-docs | 32 | 11 | 8 | 13 | 0 | 3 |
| actionable-clarity | plain-language | 32 | 13 | 10 | 9 | 0 | 3 |
| actionable-clarity | technical-simplified | 28 | 19 | 3 | 6 | 0 | 16 |
| actionable-clarity | unstyled | 32 | 14 | 7 | 11 | 0 | 7 |
| clarity-flow | classic-concise | 32 | 12 | 6 | 14 | 0 | 6 |
| clarity-flow | concise | 32 | 17 | 5 | 10 | 0 | 12 |
| clarity-flow | developer-docs | 32 | 3 | 16 | 13 | 0 | -13 |
| clarity-flow | plain-language | 32 | 8 | 16 | 8 | 0 | -8 |
| clarity-flow | technical-simplified | 28 | 12 | 10 | 6 | 0 | 2 |
| clarity-flow | unstyled | 32 | 9 | 12 | 11 | 0 | -3 |
| classic-concise | concise | 32 | 14 | 8 | 10 | 0 | 6 |
| classic-concise | developer-docs | 32 | 3 | 18 | 11 | 0 | -15 |
| classic-concise | plain-language | 32 | 5 | 13 | 14 | 0 | -8 |
| classic-concise | technical-simplified | 28 | 14 | 7 | 7 | 0 | 7 |
| classic-concise | unstyled | 32 | 7 | 14 | 11 | 0 | -7 |
| concise | developer-docs | 32 | 0 | 22 | 10 | 0 | -22 |
| concise | plain-language | 32 | 5 | 20 | 7 | 0 | -15 |
| concise | technical-simplified | 28 | 6 | 13 | 9 | 0 | -7 |
| concise | unstyled | 32 | 4 | 21 | 7 | 0 | -17 |
| developer-docs | plain-language | 32 | 11 | 6 | 15 | 0 | 5 |
| developer-docs | technical-simplified | 28 | 17 | 4 | 7 | 0 | 13 |
| developer-docs | unstyled | 32 | 16 | 5 | 11 | 0 | 11 |
| plain-language | technical-simplified | 28 | 17 | 4 | 7 | 0 | 13 |
| plain-language | unstyled | 32 | 17 | 7 | 8 | 0 | 10 |
| technical-simplified | unstyled | 28 | 8 | 14 | 6 | 0 | -6 |

## Win matrix

A cell holds the points of the row competitor against the column
competitor: 1 per decisive win plus 0.5 per split.

| | actionable-clarity | clarity-flow | classic-concise | concise | developer-docs | plain-language | technical-simplified | unstyled |
|---|---|---|---|---|---|---|---|---|
| actionable-clarity | - | 23.0 | 24.0 | 28.0 | 17.5 | 17.5 | 22.0 | 19.5 |
| clarity-flow | 9.0 | - | 19.0 | 22.0 | 9.5 | 12.0 | 15.0 | 14.5 |
| classic-concise | 8.0 | 13.0 | - | 19.0 | 8.5 | 12.0 | 17.5 | 12.5 |
| concise | 4.0 | 10.0 | 13.0 | - | 5.0 | 8.5 | 10.5 | 7.5 |
| developer-docs | 14.5 | 22.5 | 23.5 | 27.0 | - | 18.5 | 20.5 | 21.5 |
| plain-language | 14.5 | 20.0 | 20.0 | 23.5 | 13.5 | - | 20.5 | 21.0 |
| technical-simplified | 6.0 | 13.0 | 10.5 | 17.5 | 7.5 | 7.5 | - | 11.0 |
| unstyled | 12.5 | 17.5 | 19.5 | 24.5 | 10.5 | 11.0 | 17.0 | - |

## Bradley-Terry strengths

The scale is anchored on unstyled at strength 1.0.

The table lists the competitors from the highest strength to the
lowest. A competitor without a finite strength comes last.

| Competitor | Strength | 95% CI |
|---|---|---|
| actionable-clarity | 1.992 | [1.461, 2.75] |
| developer-docs | 1.866 | [1.433, 2.459] |
| plain-language | 1.424 | [1.062, 1.89] |
| unstyled | 1.0 | n/a |
| clarity-flow | 0.822 | [0.611, 1.101] |
| classic-concise | 0.686 | [0.504, 0.921] |
| technical-simplified | 0.584 | [0.421, 0.795] |
| concise | 0.379 | [0.276, 0.51] |

The interval comes from 1000 bootstrap resamples of the scored contests (seed 0).

## Position bias

First-pick rate: 0.375 over 1736 usable picks.
Split rate: 0.301 over 868 judged contests.

## Per task type

### code-review

| A | B | Contests | A wins | B wins | Splits | Unscored | Net (A) |
|---|---|---|---|---|---|---|---|
| actionable-clarity | clarity-flow | 8 | 6 | 2 | 0 | 0 | 4 |
| actionable-clarity | classic-concise | 8 | 6 | 0 | 2 | 0 | 6 |
| actionable-clarity | concise | 8 | 8 | 0 | 0 | 0 | 8 |
| actionable-clarity | developer-docs | 8 | 3 | 1 | 4 | 0 | 2 |
| actionable-clarity | plain-language | 8 | 3 | 3 | 2 | 0 | 0 |
| actionable-clarity | technical-simplified | 8 | 5 | 0 | 3 | 0 | 5 |
| actionable-clarity | unstyled | 8 | 4 | 0 | 4 | 0 | 4 |
| clarity-flow | classic-concise | 8 | 4 | 2 | 2 | 0 | 2 |
| clarity-flow | concise | 8 | 6 | 0 | 2 | 0 | 6 |
| clarity-flow | developer-docs | 8 | 1 | 2 | 5 | 0 | -1 |
| clarity-flow | plain-language | 8 | 2 | 4 | 2 | 0 | -2 |
| clarity-flow | technical-simplified | 8 | 4 | 3 | 1 | 0 | 1 |
| clarity-flow | unstyled | 8 | 5 | 1 | 2 | 0 | 4 |
| classic-concise | concise | 8 | 5 | 2 | 1 | 0 | 3 |
| classic-concise | developer-docs | 8 | 0 | 5 | 3 | 0 | -5 |
| classic-concise | plain-language | 8 | 1 | 4 | 3 | 0 | -3 |
| classic-concise | technical-simplified | 8 | 3 | 2 | 3 | 0 | 1 |
| classic-concise | unstyled | 8 | 2 | 4 | 2 | 0 | -2 |
| concise | developer-docs | 8 | 0 | 7 | 1 | 0 | -7 |
| concise | plain-language | 8 | 1 | 7 | 0 | 0 | -6 |
| concise | technical-simplified | 8 | 3 | 4 | 1 | 0 | -1 |
| concise | unstyled | 8 | 0 | 7 | 1 | 0 | -7 |
| developer-docs | plain-language | 8 | 3 | 2 | 3 | 0 | 1 |
| developer-docs | technical-simplified | 8 | 4 | 3 | 1 | 0 | 1 |
| developer-docs | unstyled | 8 | 4 | 0 | 4 | 0 | 4 |
| plain-language | technical-simplified | 8 | 5 | 1 | 2 | 0 | 4 |
| plain-language | unstyled | 8 | 7 | 1 | 0 | 0 | 6 |
| technical-simplified | unstyled | 8 | 2 | 4 | 2 | 0 | -2 |

### debugging

| A | B | Contests | A wins | B wins | Splits | Unscored | Net (A) |
|---|---|---|---|---|---|---|---|
| actionable-clarity | clarity-flow | 8 | 3 | 4 | 1 | 0 | -1 |
| actionable-clarity | classic-concise | 8 | 3 | 2 | 3 | 0 | 1 |
| actionable-clarity | concise | 8 | 6 | 1 | 1 | 0 | 5 |
| actionable-clarity | developer-docs | 8 | 1 | 3 | 4 | 0 | -2 |
| actionable-clarity | plain-language | 8 | 0 | 6 | 2 | 0 | -6 |
| actionable-clarity | technical-simplified | 6 | 2 | 3 | 1 | 0 | -1 |
| actionable-clarity | unstyled | 8 | 0 | 6 | 2 | 0 | -6 |
| clarity-flow | classic-concise | 8 | 5 | 0 | 3 | 0 | 5 |
| clarity-flow | concise | 8 | 5 | 1 | 2 | 0 | 4 |
| clarity-flow | developer-docs | 8 | 1 | 3 | 4 | 0 | -2 |
| clarity-flow | plain-language | 8 | 1 | 4 | 3 | 0 | -3 |
| clarity-flow | technical-simplified | 6 | 1 | 3 | 2 | 0 | -2 |
| clarity-flow | unstyled | 8 | 1 | 4 | 3 | 0 | -3 |
| classic-concise | concise | 8 | 3 | 3 | 2 | 0 | 0 |
| classic-concise | developer-docs | 8 | 1 | 4 | 3 | 0 | -3 |
| classic-concise | plain-language | 8 | 1 | 3 | 4 | 0 | -2 |
| classic-concise | technical-simplified | 6 | 2 | 4 | 0 | 0 | -2 |
| classic-concise | unstyled | 8 | 0 | 5 | 3 | 0 | -5 |
| concise | developer-docs | 8 | 0 | 5 | 3 | 0 | -5 |
| concise | plain-language | 8 | 0 | 5 | 3 | 0 | -5 |
| concise | technical-simplified | 6 | 0 | 4 | 2 | 0 | -4 |
| concise | unstyled | 8 | 1 | 6 | 1 | 0 | -5 |
| developer-docs | plain-language | 8 | 0 | 3 | 5 | 0 | -3 |
| developer-docs | technical-simplified | 6 | 4 | 1 | 1 | 0 | 3 |
| developer-docs | unstyled | 8 | 3 | 3 | 2 | 0 | 0 |
| plain-language | technical-simplified | 6 | 3 | 1 | 2 | 0 | 2 |
| plain-language | unstyled | 8 | 3 | 2 | 3 | 0 | 1 |
| technical-simplified | unstyled | 6 | 2 | 3 | 1 | 0 | -1 |

### explanation

| A | B | Contests | A wins | B wins | Splits | Unscored | Net (A) |
|---|---|---|---|---|---|---|---|
| actionable-clarity | clarity-flow | 8 | 5 | 0 | 3 | 0 | 5 |
| actionable-clarity | classic-concise | 8 | 4 | 1 | 3 | 0 | 3 |
| actionable-clarity | concise | 8 | 5 | 1 | 2 | 0 | 4 |
| actionable-clarity | developer-docs | 8 | 3 | 3 | 2 | 0 | 0 |
| actionable-clarity | plain-language | 8 | 3 | 0 | 5 | 0 | 3 |
| actionable-clarity | technical-simplified | 8 | 7 | 0 | 1 | 0 | 7 |
| actionable-clarity | unstyled | 8 | 4 | 0 | 4 | 0 | 4 |
| clarity-flow | classic-concise | 8 | 1 | 2 | 5 | 0 | -1 |
| clarity-flow | concise | 8 | 3 | 2 | 3 | 0 | 1 |
| clarity-flow | developer-docs | 8 | 1 | 6 | 1 | 0 | -5 |
| clarity-flow | plain-language | 8 | 3 | 3 | 2 | 0 | 0 |
| clarity-flow | technical-simplified | 8 | 3 | 2 | 3 | 0 | 1 |
| clarity-flow | unstyled | 8 | 1 | 4 | 3 | 0 | -3 |
| classic-concise | concise | 8 | 3 | 2 | 3 | 0 | 1 |
| classic-concise | developer-docs | 8 | 1 | 4 | 3 | 0 | -3 |
| classic-concise | plain-language | 8 | 2 | 2 | 4 | 0 | 0 |
| classic-concise | technical-simplified | 8 | 6 | 1 | 1 | 0 | 5 |
| classic-concise | unstyled | 8 | 1 | 3 | 4 | 0 | -2 |
| concise | developer-docs | 8 | 0 | 4 | 4 | 0 | -4 |
| concise | plain-language | 8 | 3 | 4 | 1 | 0 | -1 |
| concise | technical-simplified | 8 | 2 | 3 | 3 | 0 | -1 |
| concise | unstyled | 8 | 1 | 5 | 2 | 0 | -4 |
| developer-docs | plain-language | 8 | 4 | 1 | 3 | 0 | 3 |
| developer-docs | technical-simplified | 8 | 4 | 0 | 4 | 0 | 4 |
| developer-docs | unstyled | 8 | 4 | 2 | 2 | 0 | 2 |
| plain-language | technical-simplified | 8 | 5 | 2 | 1 | 0 | 3 |
| plain-language | unstyled | 8 | 3 | 3 | 2 | 0 | 0 |
| technical-simplified | unstyled | 8 | 1 | 5 | 2 | 0 | -4 |

### summarization

| A | B | Contests | A wins | B wins | Splits | Unscored | Net (A) |
|---|---|---|---|---|---|---|---|
| actionable-clarity | clarity-flow | 8 | 6 | 0 | 2 | 0 | 6 |
| actionable-clarity | classic-concise | 8 | 6 | 0 | 2 | 0 | 6 |
| actionable-clarity | concise | 8 | 7 | 0 | 1 | 0 | 7 |
| actionable-clarity | developer-docs | 8 | 4 | 1 | 3 | 0 | 3 |
| actionable-clarity | plain-language | 8 | 7 | 1 | 0 | 0 | 6 |
| actionable-clarity | technical-simplified | 6 | 5 | 0 | 1 | 0 | 5 |
| actionable-clarity | unstyled | 8 | 6 | 1 | 1 | 0 | 5 |
| clarity-flow | classic-concise | 8 | 2 | 2 | 4 | 0 | 0 |
| clarity-flow | concise | 8 | 3 | 2 | 3 | 0 | 1 |
| clarity-flow | developer-docs | 8 | 0 | 5 | 3 | 0 | -5 |
| clarity-flow | plain-language | 8 | 2 | 5 | 1 | 0 | -3 |
| clarity-flow | technical-simplified | 6 | 4 | 2 | 0 | 0 | 2 |
| clarity-flow | unstyled | 8 | 2 | 3 | 3 | 0 | -1 |
| classic-concise | concise | 8 | 3 | 1 | 4 | 0 | 2 |
| classic-concise | developer-docs | 8 | 1 | 5 | 2 | 0 | -4 |
| classic-concise | plain-language | 8 | 1 | 4 | 3 | 0 | -3 |
| classic-concise | technical-simplified | 6 | 3 | 0 | 3 | 0 | 3 |
| classic-concise | unstyled | 8 | 4 | 2 | 2 | 0 | 2 |
| concise | developer-docs | 8 | 0 | 6 | 2 | 0 | -6 |
| concise | plain-language | 8 | 1 | 4 | 3 | 0 | -3 |
| concise | technical-simplified | 6 | 1 | 2 | 3 | 0 | -1 |
| concise | unstyled | 8 | 2 | 3 | 3 | 0 | -1 |
| developer-docs | plain-language | 8 | 4 | 0 | 4 | 0 | 4 |
| developer-docs | technical-simplified | 6 | 5 | 0 | 1 | 0 | 5 |
| developer-docs | unstyled | 8 | 5 | 0 | 3 | 0 | 5 |
| plain-language | technical-simplified | 6 | 4 | 0 | 2 | 0 | 4 |
| plain-language | unstyled | 8 | 4 | 1 | 3 | 0 | 3 |
| technical-simplified | unstyled | 6 | 3 | 2 | 1 | 0 | 1 |

## Length confound

Samples: 861 contests with unequal word counts.
Pearson: 0.118. Spearman: 0.238.
Longer-text win rate: 0.688.

## Call timing

A stored call row holds two times: duration_ms is the model
time that the CLI reports, and wall_ms is the wall clock of
the subprocess. The difference is the startup cost of one CLI
call.

Calls: 1736, measured: 1736.
Mean duration: 2394 ms. Mean wall: 89478 ms. Mean startup: 87084 ms.

## Harness spend

A stored call row holds the token counts of its call: the
uncached input, cache-write input, cache-read input, and
output tokens. The cache-read share is the cache-read total
over the whole input total.

Calls: 1736, measured: 1736.
Input tokens: 3472 uncached, 3613294 cache write, 3603936 cache read. Output tokens: 74638.
Cache-read share: 0.499.
Cache writes by lifetime: 3613294 at 5 minutes, 0 at 1 hour.

## Warnings

- technical-simplified/summarization-02: the pair failed the gate, excluded
- technical-simplified/summarization-06: the pair failed the gate, excluded
- technical-simplified/debugging-06: the pair failed the gate, excluded
- technical-simplified/debugging-08: the pair failed the gate, excluded

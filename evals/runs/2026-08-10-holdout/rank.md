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

Judge: opus. Judged on 2026-08-10T14:32:55+00:00.

## Matchups

| A | B | Contests | A wins | B wins | Splits | Unscored | Net (A) |
|---|---|---|---|---|---|---|---|
| actionable-clarity | clarity-flow | 23 | 8 | 5 | 9 | 1 | 3 |
| actionable-clarity | classic-concise | 23 | 13 | 5 | 4 | 1 | 8 |
| actionable-clarity | developer-docs | 23 | 12 | 5 | 6 | 0 | 7 |
| actionable-clarity | plain-language | 23 | 8 | 12 | 3 | 0 | -4 |
| actionable-clarity | technical-simplified | 21 | 13 | 6 | 2 | 0 | 7 |
| actionable-clarity | unstyled | 23 | 11 | 6 | 6 | 0 | 5 |
| clarity-flow | classic-concise | 24 | 10 | 7 | 7 | 0 | 3 |
| clarity-flow | developer-docs | 24 | 9 | 7 | 8 | 0 | 2 |
| clarity-flow | plain-language | 24 | 4 | 12 | 6 | 2 | -8 |
| clarity-flow | technical-simplified | 21 | 10 | 3 | 8 | 0 | 7 |
| clarity-flow | unstyled | 24 | 11 | 9 | 4 | 0 | 2 |
| classic-concise | developer-docs | 24 | 8 | 7 | 9 | 0 | 1 |
| classic-concise | plain-language | 24 | 4 | 15 | 5 | 0 | -11 |
| classic-concise | technical-simplified | 21 | 10 | 5 | 6 | 0 | 5 |
| classic-concise | unstyled | 24 | 8 | 8 | 8 | 0 | 0 |
| developer-docs | plain-language | 24 | 4 | 16 | 3 | 1 | -12 |
| developer-docs | technical-simplified | 21 | 14 | 3 | 4 | 0 | 11 |
| developer-docs | unstyled | 24 | 12 | 7 | 5 | 0 | 5 |
| plain-language | technical-simplified | 21 | 16 | 3 | 2 | 0 | 13 |
| plain-language | unstyled | 24 | 15 | 3 | 5 | 1 | 12 |
| technical-simplified | unstyled | 21 | 8 | 8 | 5 | 0 | 0 |

## Win matrix

A cell holds the points of the row competitor against the column
competitor: 1 per decisive win plus 0.5 per split.

| | actionable-clarity | clarity-flow | classic-concise | developer-docs | plain-language | technical-simplified | unstyled |
|---|---|---|---|---|---|---|---|
| actionable-clarity | - | 12.5 | 15.0 | 15.0 | 9.5 | 14.0 | 14.0 |
| clarity-flow | 9.5 | - | 13.5 | 13.0 | 7.0 | 14.0 | 13.0 |
| classic-concise | 7.0 | 10.5 | - | 12.5 | 6.5 | 13.0 | 12.0 |
| developer-docs | 8.0 | 11.0 | 11.5 | - | 5.5 | 16.0 | 14.5 |
| plain-language | 13.5 | 15.0 | 17.5 | 17.5 | - | 17.0 | 17.5 |
| technical-simplified | 7.0 | 7.0 | 8.0 | 5.0 | 4.0 | - | 10.5 |
| unstyled | 9.0 | 11.0 | 12.0 | 9.5 | 5.5 | 10.5 | - |

## Bradley-Terry strengths

The scale is anchored on unstyled at strength 1.0.

The table lists the competitors from the highest strength to the
lowest. A competitor without a finite strength comes last.

| Competitor | Strength | 95% CI |
|---|---|---|
| plain-language | 3.136 | [2.06, 4.905] |
| actionable-clarity | 1.944 | [1.293, 2.995] |
| clarity-flow | 1.407 | [0.95, 2.166] |
| developer-docs | 1.262 | [0.842, 1.836] |
| classic-concise | 1.113 | [0.741, 1.659] |
| unstyled | 1.0 | n/a |
| technical-simplified | 0.723 | [0.468, 1.1] |

The interval comes from 1000 bootstrap resamples of the scored contests (seed 0).

## Position bias

First-pick rate: 0.421 over 956 usable picks.
Split rate: 0.242 over 475 judged contests.

## Per task type

### code-review

| A | B | Contests | A wins | B wins | Splits | Unscored | Net (A) |
|---|---|---|---|---|---|---|---|
| actionable-clarity | clarity-flow | 5 | 1 | 2 | 1 | 1 | -1 |
| actionable-clarity | classic-concise | 5 | 2 | 1 | 1 | 1 | 1 |
| actionable-clarity | developer-docs | 5 | 3 | 2 | 0 | 0 | 1 |
| actionable-clarity | plain-language | 5 | 3 | 2 | 0 | 0 | 1 |
| actionable-clarity | technical-simplified | 5 | 1 | 3 | 1 | 0 | -2 |
| actionable-clarity | unstyled | 5 | 2 | 2 | 1 | 0 | 0 |
| clarity-flow | classic-concise | 6 | 3 | 3 | 0 | 0 | 0 |
| clarity-flow | developer-docs | 6 | 4 | 1 | 1 | 0 | 3 |
| clarity-flow | plain-language | 6 | 0 | 2 | 2 | 2 | -2 |
| clarity-flow | technical-simplified | 5 | 4 | 0 | 1 | 0 | 4 |
| clarity-flow | unstyled | 6 | 3 | 1 | 2 | 0 | 2 |
| classic-concise | developer-docs | 6 | 2 | 1 | 3 | 0 | 1 |
| classic-concise | plain-language | 6 | 2 | 3 | 1 | 0 | -1 |
| classic-concise | technical-simplified | 5 | 3 | 0 | 2 | 0 | 3 |
| classic-concise | unstyled | 6 | 2 | 2 | 2 | 0 | 0 |
| developer-docs | plain-language | 6 | 0 | 5 | 0 | 1 | -5 |
| developer-docs | technical-simplified | 5 | 3 | 1 | 1 | 0 | 2 |
| developer-docs | unstyled | 6 | 2 | 2 | 2 | 0 | 0 |
| plain-language | technical-simplified | 5 | 4 | 1 | 0 | 0 | 3 |
| plain-language | unstyled | 6 | 3 | 0 | 2 | 1 | 3 |
| technical-simplified | unstyled | 5 | 2 | 2 | 1 | 0 | 0 |

### debugging

| A | B | Contests | A wins | B wins | Splits | Unscored | Net (A) |
|---|---|---|---|---|---|---|---|
| actionable-clarity | clarity-flow | 6 | 3 | 2 | 1 | 0 | 1 |
| actionable-clarity | classic-concise | 6 | 4 | 1 | 1 | 0 | 3 |
| actionable-clarity | developer-docs | 6 | 2 | 2 | 2 | 0 | 0 |
| actionable-clarity | plain-language | 6 | 1 | 4 | 1 | 0 | -3 |
| actionable-clarity | technical-simplified | 6 | 2 | 3 | 1 | 0 | -1 |
| actionable-clarity | unstyled | 6 | 2 | 2 | 2 | 0 | 0 |
| clarity-flow | classic-concise | 6 | 4 | 1 | 1 | 0 | 3 |
| clarity-flow | developer-docs | 6 | 1 | 2 | 3 | 0 | -1 |
| clarity-flow | plain-language | 6 | 2 | 3 | 1 | 0 | -1 |
| clarity-flow | technical-simplified | 6 | 2 | 2 | 2 | 0 | 0 |
| clarity-flow | unstyled | 6 | 3 | 3 | 0 | 0 | 0 |
| classic-concise | developer-docs | 6 | 1 | 3 | 2 | 0 | -2 |
| classic-concise | plain-language | 6 | 1 | 3 | 2 | 0 | -2 |
| classic-concise | technical-simplified | 6 | 1 | 4 | 1 | 0 | -3 |
| classic-concise | unstyled | 6 | 1 | 2 | 3 | 0 | -1 |
| developer-docs | plain-language | 6 | 2 | 4 | 0 | 0 | -2 |
| developer-docs | technical-simplified | 6 | 3 | 2 | 1 | 0 | 1 |
| developer-docs | unstyled | 6 | 3 | 2 | 1 | 0 | 1 |
| plain-language | technical-simplified | 6 | 3 | 1 | 2 | 0 | 2 |
| plain-language | unstyled | 6 | 4 | 2 | 0 | 0 | 2 |
| technical-simplified | unstyled | 6 | 3 | 1 | 2 | 0 | 2 |

### explanation

| A | B | Contests | A wins | B wins | Splits | Unscored | Net (A) |
|---|---|---|---|---|---|---|---|
| actionable-clarity | clarity-flow | 6 | 2 | 1 | 3 | 0 | 1 |
| actionable-clarity | classic-concise | 6 | 2 | 3 | 1 | 0 | -1 |
| actionable-clarity | developer-docs | 6 | 4 | 1 | 1 | 0 | 3 |
| actionable-clarity | plain-language | 6 | 2 | 4 | 0 | 0 | -2 |
| actionable-clarity | technical-simplified | 6 | 6 | 0 | 0 | 0 | 6 |
| actionable-clarity | unstyled | 6 | 3 | 2 | 1 | 0 | 1 |
| clarity-flow | classic-concise | 6 | 1 | 3 | 2 | 0 | -2 |
| clarity-flow | developer-docs | 6 | 2 | 2 | 2 | 0 | 0 |
| clarity-flow | plain-language | 6 | 0 | 4 | 2 | 0 | -4 |
| clarity-flow | technical-simplified | 6 | 3 | 1 | 2 | 0 | 2 |
| clarity-flow | unstyled | 6 | 3 | 2 | 1 | 0 | 1 |
| classic-concise | developer-docs | 6 | 3 | 0 | 3 | 0 | 3 |
| classic-concise | plain-language | 6 | 0 | 4 | 2 | 0 | -4 |
| classic-concise | technical-simplified | 6 | 3 | 1 | 2 | 0 | 2 |
| classic-concise | unstyled | 6 | 3 | 1 | 2 | 0 | 2 |
| developer-docs | plain-language | 6 | 0 | 4 | 2 | 0 | -4 |
| developer-docs | technical-simplified | 6 | 5 | 0 | 1 | 0 | 5 |
| developer-docs | unstyled | 6 | 5 | 1 | 0 | 0 | 4 |
| plain-language | technical-simplified | 6 | 6 | 0 | 0 | 0 | 6 |
| plain-language | unstyled | 6 | 4 | 0 | 2 | 0 | 4 |
| technical-simplified | unstyled | 6 | 2 | 3 | 1 | 0 | -1 |

### summarization

| A | B | Contests | A wins | B wins | Splits | Unscored | Net (A) |
|---|---|---|---|---|---|---|---|
| actionable-clarity | clarity-flow | 6 | 2 | 0 | 4 | 0 | 2 |
| actionable-clarity | classic-concise | 6 | 5 | 0 | 1 | 0 | 5 |
| actionable-clarity | developer-docs | 6 | 3 | 0 | 3 | 0 | 3 |
| actionable-clarity | plain-language | 6 | 2 | 2 | 2 | 0 | 0 |
| actionable-clarity | technical-simplified | 4 | 4 | 0 | 0 | 0 | 4 |
| actionable-clarity | unstyled | 6 | 4 | 0 | 2 | 0 | 4 |
| clarity-flow | classic-concise | 6 | 2 | 0 | 4 | 0 | 2 |
| clarity-flow | developer-docs | 6 | 2 | 2 | 2 | 0 | 0 |
| clarity-flow | plain-language | 6 | 2 | 3 | 1 | 0 | -1 |
| clarity-flow | technical-simplified | 4 | 1 | 0 | 3 | 0 | 1 |
| clarity-flow | unstyled | 6 | 2 | 3 | 1 | 0 | -1 |
| classic-concise | developer-docs | 6 | 2 | 3 | 1 | 0 | -1 |
| classic-concise | plain-language | 6 | 1 | 5 | 0 | 0 | -4 |
| classic-concise | technical-simplified | 4 | 3 | 0 | 1 | 0 | 3 |
| classic-concise | unstyled | 6 | 2 | 3 | 1 | 0 | -1 |
| developer-docs | plain-language | 6 | 2 | 3 | 1 | 0 | -1 |
| developer-docs | technical-simplified | 4 | 3 | 0 | 1 | 0 | 3 |
| developer-docs | unstyled | 6 | 2 | 2 | 2 | 0 | 0 |
| plain-language | technical-simplified | 4 | 3 | 1 | 0 | 0 | 2 |
| plain-language | unstyled | 6 | 4 | 1 | 1 | 0 | 3 |
| technical-simplified | unstyled | 4 | 1 | 2 | 1 | 0 | -1 |

## Length confound

Samples: 471 contests with unequal word counts.
Pearson: 0.169. Spearman: 0.226.
Longer-text win rate: 0.683.

## Call timing

A stored call row holds two times: duration_ms is the model
time that the CLI reports, and wall_ms is the wall clock of
the subprocess. The difference is the startup cost of one CLI
call.

Calls: 962, measured: 962.
Mean duration: 3887 ms. Mean wall: 49643 ms. Mean startup: 45756 ms.

## Harness spend

A stored call row holds the token counts of its call: the
uncached input, cache-write input, cache-read input, and
output tokens. The cache-read share is the cache-read total
over the whole input total.

Calls: 962, measured: 962.
Input tokens: 1926 uncached, 2037662 cache write, 1985447 cache read. Output tokens: 55768.
Cache-read share: 0.493.
Cache writes by lifetime: 2037662 at 5 minutes, 0 at 1 hour.

## Warnings

- actionable-clarity/code-review-h06: the pair failed the gate, excluded
- technical-simplified/summarization-h03: the pair failed the gate, excluded
- technical-simplified/code-review-h06: the pair failed the gate, excluded
- technical-simplified/summarization-h06: the pair failed the gate, excluded
- actionable-clarity vs clarity-flow on code-review-h01: the judge gave no usable pick for the order with clarity-flow first, so the contest is unscored
- actionable-clarity vs classic-concise on code-review-h01: the judge gave no usable pick for the order with classic-concise first, so the contest is unscored
- clarity-flow vs plain-language on code-review-h05: the judge gave no usable pick for the order with clarity-flow first, so the contest is unscored
- clarity-flow vs plain-language on code-review-h06: the judge gave no usable pick for the order with clarity-flow first, so the contest is unscored
- developer-docs vs plain-language on code-review-h05: the judge gave no usable pick for the order with developer-docs first, so the contest is unscored
- plain-language vs unstyled on code-review-h06: the judge gave no usable pick for the order with unstyled first, so the contest is unscored
- actionable-clarity vs clarity-flow on code-review-h01: an order has no usable pick, so the contest is unscored
- actionable-clarity vs classic-concise on code-review-h01: an order has no usable pick, so the contest is unscored
- clarity-flow vs plain-language on code-review-h05: an order has no usable pick, so the contest is unscored
- clarity-flow vs plain-language on code-review-h06: an order has no usable pick, so the contest is unscored
- developer-docs vs plain-language on code-review-h05: an order has no usable pick, so the contest is unscored
- plain-language vs unstyled on code-review-h06: an order has no usable pick, so the contest is unscored

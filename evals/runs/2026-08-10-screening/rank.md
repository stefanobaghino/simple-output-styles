# Clarity-ranking report

**Screening run.** This run covers 8 of 32 prompts, as one
run instead of 3. By design, the generation calls are about
8% of a full campaign, and the judge calls are about 25%
of one full run.
The subset holds 2 hedge-rich prompts, mirroring the
hedge-rich share of the full set.
Measured against the baseline campaign
(runs/2026-08-08 and runs/2026-08-08b), a screening run holds about
25% of the calls and about 25% of the
weighted input tokens of one full run, plus the full cost
probe, which is per style and does not shrink.
The error bars are wider than in a full run,
because fewer contests feed the bootstrap intervals.
`style-compare` rejects a comparison of this run with a full run.

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

Judge: opus. Judged on 2026-08-10T10:54:44+00:00.

## Matchups

| A | B | Contests | A wins | B wins | Splits | Unscored | Net (A) |
|---|---|---|---|---|---|---|---|
| actionable-clarity | clarity-flow | 8 | 5 | 0 | 3 | 0 | 5 |
| actionable-clarity | classic-concise | 8 | 5 | 1 | 2 | 0 | 4 |
| actionable-clarity | developer-docs | 8 | 4 | 1 | 3 | 0 | 3 |
| actionable-clarity | plain-complete | 8 | 7 | 0 | 1 | 0 | 7 |
| actionable-clarity | plain-language | 8 | 6 | 2 | 0 | 0 | 4 |
| actionable-clarity | technical-simplified | 6 | 4 | 1 | 1 | 0 | 3 |
| actionable-clarity | unstyled | 8 | 6 | 0 | 2 | 0 | 6 |
| clarity-flow | classic-concise | 8 | 4 | 2 | 2 | 0 | 2 |
| clarity-flow | developer-docs | 8 | 3 | 2 | 3 | 0 | 1 |
| clarity-flow | plain-complete | 8 | 3 | 4 | 1 | 0 | -1 |
| clarity-flow | plain-language | 8 | 1 | 5 | 2 | 0 | -4 |
| clarity-flow | technical-simplified | 6 | 3 | 0 | 3 | 0 | 3 |
| clarity-flow | unstyled | 8 | 2 | 2 | 4 | 0 | 0 |
| classic-concise | developer-docs | 8 | 2 | 5 | 1 | 0 | -3 |
| classic-concise | plain-complete | 8 | 2 | 5 | 1 | 0 | -3 |
| classic-concise | plain-language | 8 | 0 | 5 | 3 | 0 | -5 |
| classic-concise | technical-simplified | 6 | 3 | 1 | 2 | 0 | 2 |
| classic-concise | unstyled | 8 | 0 | 4 | 4 | 0 | -4 |
| developer-docs | plain-complete | 8 | 3 | 2 | 3 | 0 | 1 |
| developer-docs | plain-language | 8 | 3 | 2 | 3 | 0 | 1 |
| developer-docs | technical-simplified | 6 | 4 | 1 | 1 | 0 | 3 |
| developer-docs | unstyled | 8 | 3 | 1 | 4 | 0 | 2 |
| plain-complete | plain-language | 8 | 0 | 2 | 6 | 0 | -2 |
| plain-complete | technical-simplified | 6 | 5 | 0 | 1 | 0 | 5 |
| plain-complete | unstyled | 8 | 4 | 1 | 3 | 0 | 3 |
| plain-language | technical-simplified | 6 | 5 | 0 | 1 | 0 | 5 |
| plain-language | unstyled | 8 | 5 | 0 | 3 | 0 | 5 |
| technical-simplified | unstyled | 6 | 0 | 4 | 2 | 0 | -4 |

## Win matrix

A cell holds the points of the row competitor against the column
competitor: 1 per decisive win plus 0.5 per split.

| | actionable-clarity | clarity-flow | classic-concise | developer-docs | plain-complete | plain-language | technical-simplified | unstyled |
|---|---|---|---|---|---|---|---|---|
| actionable-clarity | - | 6.5 | 6.0 | 5.5 | 7.5 | 6.0 | 4.5 | 7.0 |
| clarity-flow | 1.5 | - | 5.0 | 4.5 | 3.5 | 2.0 | 4.5 | 4.0 |
| classic-concise | 2.0 | 3.0 | - | 2.5 | 2.5 | 1.5 | 4.0 | 2.0 |
| developer-docs | 2.5 | 3.5 | 5.5 | - | 4.5 | 4.5 | 4.5 | 5.0 |
| plain-complete | 0.5 | 4.5 | 5.5 | 3.5 | - | 3.0 | 5.5 | 5.5 |
| plain-language | 2.0 | 6.0 | 6.5 | 3.5 | 5.0 | - | 5.5 | 6.5 |
| technical-simplified | 1.5 | 1.5 | 2.0 | 1.5 | 0.5 | 0.5 | - | 1.0 |
| unstyled | 1.0 | 4.0 | 6.0 | 3.0 | 2.5 | 1.5 | 5.0 | - |

## Bradley-Terry strengths

The scale is anchored on unstyled at strength 1.0.

The table lists the competitors from the highest strength to the
lowest. A competitor without a finite strength comes last.

| Competitor | Strength | 95% CI |
|---|---|---|
| actionable-clarity | 4.73 | [2.612, 9.847] |
| plain-language | 2.405 | [1.429, 4.451] |
| developer-docs | 1.658 | [0.995, 3.026] |
| plain-complete | 1.435 | [0.875, 2.515] |
| clarity-flow | 1.156 | [0.693, 2.031] |
| unstyled | 1.0 | n/a |
| classic-concise | 0.66 | [0.374, 1.209] |
| technical-simplified | 0.354 | [0.166, 0.685] |

The interval comes from 1000 bootstrap resamples of the scored contests (seed 0).

## Position bias

First-pick rate: 0.374 over 420 usable picks.
Split rate: 0.31 over 210 judged contests.

## Per task type

### code-review

| A | B | Contests | A wins | B wins | Splits | Unscored | Net (A) |
|---|---|---|---|---|---|---|---|
| actionable-clarity | clarity-flow | 2 | 2 | 0 | 0 | 0 | 2 |
| actionable-clarity | classic-concise | 2 | 2 | 0 | 0 | 0 | 2 |
| actionable-clarity | developer-docs | 2 | 2 | 0 | 0 | 0 | 2 |
| actionable-clarity | plain-complete | 2 | 2 | 0 | 0 | 0 | 2 |
| actionable-clarity | plain-language | 2 | 2 | 0 | 0 | 0 | 2 |
| actionable-clarity | technical-simplified | 2 | 2 | 0 | 0 | 0 | 2 |
| actionable-clarity | unstyled | 2 | 2 | 0 | 0 | 0 | 2 |
| clarity-flow | classic-concise | 2 | 1 | 0 | 1 | 0 | 1 |
| clarity-flow | developer-docs | 2 | 1 | 0 | 1 | 0 | 1 |
| clarity-flow | plain-complete | 2 | 1 | 1 | 0 | 0 | 0 |
| clarity-flow | plain-language | 2 | 0 | 2 | 0 | 0 | -2 |
| clarity-flow | technical-simplified | 2 | 2 | 0 | 0 | 0 | 2 |
| clarity-flow | unstyled | 2 | 0 | 0 | 2 | 0 | 0 |
| classic-concise | developer-docs | 2 | 0 | 2 | 0 | 0 | -2 |
| classic-concise | plain-complete | 2 | 0 | 1 | 1 | 0 | -1 |
| classic-concise | plain-language | 2 | 0 | 1 | 1 | 0 | -1 |
| classic-concise | technical-simplified | 2 | 1 | 1 | 0 | 0 | 0 |
| classic-concise | unstyled | 2 | 0 | 1 | 1 | 0 | -1 |
| developer-docs | plain-complete | 2 | 0 | 0 | 2 | 0 | 0 |
| developer-docs | plain-language | 2 | 1 | 0 | 1 | 0 | 1 |
| developer-docs | technical-simplified | 2 | 2 | 0 | 0 | 0 | 2 |
| developer-docs | unstyled | 2 | 1 | 0 | 1 | 0 | 1 |
| plain-complete | plain-language | 2 | 0 | 0 | 2 | 0 | 0 |
| plain-complete | technical-simplified | 2 | 2 | 0 | 0 | 0 | 2 |
| plain-complete | unstyled | 2 | 2 | 0 | 0 | 0 | 2 |
| plain-language | technical-simplified | 2 | 2 | 0 | 0 | 0 | 2 |
| plain-language | unstyled | 2 | 1 | 0 | 1 | 0 | 1 |
| technical-simplified | unstyled | 2 | 0 | 2 | 0 | 0 | -2 |

### debugging

| A | B | Contests | A wins | B wins | Splits | Unscored | Net (A) |
|---|---|---|---|---|---|---|---|
| actionable-clarity | clarity-flow | 2 | 1 | 0 | 1 | 0 | 1 |
| actionable-clarity | classic-concise | 2 | 0 | 0 | 2 | 0 | 0 |
| actionable-clarity | developer-docs | 2 | 1 | 0 | 1 | 0 | 1 |
| actionable-clarity | plain-complete | 2 | 2 | 0 | 0 | 0 | 2 |
| actionable-clarity | plain-language | 2 | 1 | 1 | 0 | 0 | 0 |
| actionable-clarity | technical-simplified | 2 | 1 | 0 | 1 | 0 | 1 |
| actionable-clarity | unstyled | 2 | 2 | 0 | 0 | 0 | 2 |
| clarity-flow | classic-concise | 2 | 1 | 1 | 0 | 0 | 0 |
| clarity-flow | developer-docs | 2 | 1 | 0 | 1 | 0 | 1 |
| clarity-flow | plain-complete | 2 | 1 | 0 | 1 | 0 | 1 |
| clarity-flow | plain-language | 2 | 0 | 1 | 1 | 0 | -1 |
| clarity-flow | technical-simplified | 2 | 1 | 0 | 1 | 0 | 1 |
| clarity-flow | unstyled | 2 | 1 | 0 | 1 | 0 | 1 |
| classic-concise | developer-docs | 2 | 1 | 0 | 1 | 0 | 1 |
| classic-concise | plain-complete | 2 | 2 | 0 | 0 | 0 | 2 |
| classic-concise | plain-language | 2 | 0 | 1 | 1 | 0 | -1 |
| classic-concise | technical-simplified | 2 | 1 | 0 | 1 | 0 | 1 |
| classic-concise | unstyled | 2 | 0 | 1 | 1 | 0 | -1 |
| developer-docs | plain-complete | 2 | 0 | 1 | 1 | 0 | -1 |
| developer-docs | plain-language | 2 | 0 | 1 | 1 | 0 | -1 |
| developer-docs | technical-simplified | 2 | 0 | 1 | 1 | 0 | -1 |
| developer-docs | unstyled | 2 | 0 | 0 | 2 | 0 | 0 |
| plain-complete | plain-language | 2 | 0 | 1 | 1 | 0 | -1 |
| plain-complete | technical-simplified | 2 | 2 | 0 | 0 | 0 | 2 |
| plain-complete | unstyled | 2 | 0 | 1 | 1 | 0 | -1 |
| plain-language | technical-simplified | 2 | 1 | 0 | 1 | 0 | 1 |
| plain-language | unstyled | 2 | 2 | 0 | 0 | 0 | 2 |
| technical-simplified | unstyled | 2 | 0 | 1 | 1 | 0 | -1 |

### explanation

| A | B | Contests | A wins | B wins | Splits | Unscored | Net (A) |
|---|---|---|---|---|---|---|---|
| actionable-clarity | clarity-flow | 2 | 2 | 0 | 0 | 0 | 2 |
| actionable-clarity | classic-concise | 2 | 2 | 0 | 0 | 0 | 2 |
| actionable-clarity | developer-docs | 2 | 0 | 0 | 2 | 0 | 0 |
| actionable-clarity | plain-complete | 2 | 2 | 0 | 0 | 0 | 2 |
| actionable-clarity | plain-language | 2 | 2 | 0 | 0 | 0 | 2 |
| actionable-clarity | technical-simplified | 1 | 1 | 0 | 0 | 0 | 1 |
| actionable-clarity | unstyled | 2 | 1 | 0 | 1 | 0 | 1 |
| clarity-flow | classic-concise | 2 | 0 | 1 | 1 | 0 | -1 |
| clarity-flow | developer-docs | 2 | 0 | 2 | 0 | 0 | -2 |
| clarity-flow | plain-complete | 2 | 0 | 2 | 0 | 0 | -2 |
| clarity-flow | plain-language | 2 | 0 | 2 | 0 | 0 | -2 |
| clarity-flow | technical-simplified | 1 | 0 | 0 | 1 | 0 | 0 |
| clarity-flow | unstyled | 2 | 0 | 2 | 0 | 0 | -2 |
| classic-concise | developer-docs | 2 | 0 | 2 | 0 | 0 | -2 |
| classic-concise | plain-complete | 2 | 0 | 2 | 0 | 0 | -2 |
| classic-concise | plain-language | 2 | 0 | 1 | 1 | 0 | -1 |
| classic-concise | technical-simplified | 1 | 1 | 0 | 0 | 0 | 1 |
| classic-concise | unstyled | 2 | 0 | 2 | 0 | 0 | -2 |
| developer-docs | plain-complete | 2 | 2 | 0 | 0 | 0 | 2 |
| developer-docs | plain-language | 2 | 2 | 0 | 0 | 0 | 2 |
| developer-docs | technical-simplified | 1 | 1 | 0 | 0 | 0 | 1 |
| developer-docs | unstyled | 2 | 1 | 0 | 1 | 0 | 1 |
| plain-complete | plain-language | 2 | 0 | 0 | 2 | 0 | 0 |
| plain-complete | technical-simplified | 1 | 0 | 0 | 1 | 0 | 0 |
| plain-complete | unstyled | 2 | 0 | 0 | 2 | 0 | 0 |
| plain-language | technical-simplified | 1 | 1 | 0 | 0 | 0 | 1 |
| plain-language | unstyled | 2 | 0 | 0 | 2 | 0 | 0 |
| technical-simplified | unstyled | 1 | 0 | 1 | 0 | 0 | -1 |

### summarization

| A | B | Contests | A wins | B wins | Splits | Unscored | Net (A) |
|---|---|---|---|---|---|---|---|
| actionable-clarity | clarity-flow | 2 | 0 | 0 | 2 | 0 | 0 |
| actionable-clarity | classic-concise | 2 | 1 | 1 | 0 | 0 | 0 |
| actionable-clarity | developer-docs | 2 | 1 | 1 | 0 | 0 | 0 |
| actionable-clarity | plain-complete | 2 | 1 | 0 | 1 | 0 | 1 |
| actionable-clarity | plain-language | 2 | 1 | 1 | 0 | 0 | 0 |
| actionable-clarity | technical-simplified | 1 | 0 | 1 | 0 | 0 | -1 |
| actionable-clarity | unstyled | 2 | 1 | 0 | 1 | 0 | 1 |
| clarity-flow | classic-concise | 2 | 2 | 0 | 0 | 0 | 2 |
| clarity-flow | developer-docs | 2 | 1 | 0 | 1 | 0 | 1 |
| clarity-flow | plain-complete | 2 | 1 | 1 | 0 | 0 | 0 |
| clarity-flow | plain-language | 2 | 1 | 0 | 1 | 0 | 1 |
| clarity-flow | technical-simplified | 1 | 0 | 0 | 1 | 0 | 0 |
| clarity-flow | unstyled | 2 | 1 | 0 | 1 | 0 | 1 |
| classic-concise | developer-docs | 2 | 1 | 1 | 0 | 0 | 0 |
| classic-concise | plain-complete | 2 | 0 | 2 | 0 | 0 | -2 |
| classic-concise | plain-language | 2 | 0 | 2 | 0 | 0 | -2 |
| classic-concise | technical-simplified | 1 | 0 | 0 | 1 | 0 | 0 |
| classic-concise | unstyled | 2 | 0 | 0 | 2 | 0 | 0 |
| developer-docs | plain-complete | 2 | 1 | 1 | 0 | 0 | 0 |
| developer-docs | plain-language | 2 | 0 | 1 | 1 | 0 | -1 |
| developer-docs | technical-simplified | 1 | 1 | 0 | 0 | 0 | 1 |
| developer-docs | unstyled | 2 | 1 | 1 | 0 | 0 | 0 |
| plain-complete | plain-language | 2 | 0 | 1 | 1 | 0 | -1 |
| plain-complete | technical-simplified | 1 | 1 | 0 | 0 | 0 | 1 |
| plain-complete | unstyled | 2 | 2 | 0 | 0 | 0 | 2 |
| plain-language | technical-simplified | 1 | 1 | 0 | 0 | 0 | 1 |
| plain-language | unstyled | 2 | 2 | 0 | 0 | 0 | 2 |
| technical-simplified | unstyled | 1 | 0 | 0 | 1 | 0 | 0 |

## Length confound

Samples: 210 contests with unequal word counts.
Pearson: 0.05. Spearman: 0.254.
Longer-text win rate: 0.683.

## Call timing

A stored call row holds two times: duration_ms is the model
time that the CLI reports, and wall_ms is the wall clock of
the subprocess. The difference is the startup cost of one CLI
call.

Calls: 420, measured: 420.
Mean duration: 3721 ms. Mean wall: 38020 ms. Mean startup: 34299 ms.

## Harness spend

A stored call row holds the token counts of its call: the
uncached input, cache-write input, cache-read input, and
output tokens. The cache-read share is the cache-read total
over the whole input total.

Calls: 420, measured: 420.
Input tokens: 840 uncached, 912186 cache write, 862260 cache read. Output tokens: 24311.
Cache-read share: 0.486.
Cache writes by lifetime: 912186 at 5 minutes, 0 at 1 hour.

## Warnings

- technical-simplified/summarization-08: the pair failed the gate, excluded
- technical-simplified/explanation-03: the pair failed the gate, excluded

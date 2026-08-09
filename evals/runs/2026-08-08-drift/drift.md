# Drift report

Run: 2026-08-08-drift

The report measures rule obedience across long sessions. A session is
15 scripted turns in one Claude Code session, with the style
active. Each turn resumes the session of the previous turn, so the
context grows. Each session runs 3 time(s), and each repeat
rotates the prompt order, so a hard prompt does not always sit at the
same turn position. The linter checks each answer with the rule set
of the style. The rate of a turn position pools the complete
sessions: 100 times the violations at that position over the
sentences at that position. Thus a short answer weighs by its
sentence count and cannot dominate the series. The verdict compares
the slope of the pooled series against a per-style threshold:
"growing" when the slope is larger, else "flat". The threshold comes
from a permutation null: the turn order of each session shuffles,
the pooled slope refits, and the threshold is a nearest-rank
quantile of the shuffled slopes. The section of each style states
the quantile, the permutation count, and the seed. The
`--slope-threshold` flag replaces the derived threshold, and the
section then states both values.

## clarity-flow

- Sessions: 3/3 complete
- Slope of the pooled series: 0.0 violations per 100 sentences per turn
- Slope threshold: 0.0 (the 0.95 quantile of 1000 shuffled slopes, seed 0)
- Verdict: flat

| Turn | Pooled rate | Repeat 1 | Repeat 2 | Repeat 3 |
|---|---|---|---|---|
| 1 | 0.00 | 0.00 | 0.00 | 0.00 |
| 2 | 0.00 | 0.00 | 0.00 | 0.00 |
| 3 | 0.00 | 0.00 | 0.00 | 0.00 |
| 4 | 0.00 | 0.00 | 0.00 | 0.00 |
| 5 | 0.00 | 0.00 | 0.00 | 0.00 |
| 6 | 0.00 | 0.00 | 0.00 | 0.00 |
| 7 | 0.00 | 0.00 | 0.00 | 0.00 |
| 8 | 0.00 | 0.00 | 0.00 | 0.00 |
| 9 | 0.00 | 0.00 | 0.00 | 0.00 |
| 10 | 0.00 | 0.00 | 0.00 | 0.00 |
| 11 | 0.00 | 0.00 | 0.00 | 0.00 |
| 12 | 0.00 | 0.00 | 0.00 | 0.00 |
| 13 | 0.00 | 0.00 | 0.00 | 0.00 |
| 14 | 0.00 | 0.00 | 0.00 | 0.00 |
| 15 | 0.00 | 0.00 | 0.00 | 0.00 |

## classic-concise

- Sessions: 3/3 complete
- Slope of the pooled series: 0.0 violations per 100 sentences per turn
- Slope threshold: 0.0 (the 0.95 quantile of 1000 shuffled slopes, seed 0)
- Verdict: flat

| Turn | Pooled rate | Repeat 1 | Repeat 2 | Repeat 3 |
|---|---|---|---|---|
| 1 | 0.00 | 0.00 | 0.00 | 0.00 |
| 2 | 0.00 | 0.00 | 0.00 | 0.00 |
| 3 | 0.00 | 0.00 | 0.00 | 0.00 |
| 4 | 0.00 | 0.00 | 0.00 | 0.00 |
| 5 | 0.00 | 0.00 | 0.00 | 0.00 |
| 6 | 0.00 | 0.00 | 0.00 | 0.00 |
| 7 | 0.00 | 0.00 | 0.00 | 0.00 |
| 8 | 0.00 | 0.00 | 0.00 | 0.00 |
| 9 | 0.00 | 0.00 | 0.00 | 0.00 |
| 10 | 0.00 | 0.00 | 0.00 | 0.00 |
| 11 | 0.00 | 0.00 | 0.00 | 0.00 |
| 12 | 0.00 | 0.00 | 0.00 | 0.00 |
| 13 | 0.00 | 0.00 | 0.00 | 0.00 |
| 14 | 0.00 | 0.00 | 0.00 | 0.00 |
| 15 | 0.00 | 0.00 | 0.00 | 0.00 |

## developer-docs

- Sessions: 3/3 complete
- Slope of the pooled series: 0.094 violations per 100 sentences per turn
- Slope threshold: 0.078 (the 0.95 quantile of 1000 shuffled slopes, seed 0)
- Verdict: growing

| Turn | Pooled rate | Repeat 1 | Repeat 2 | Repeat 3 |
|---|---|---|---|---|
| 1 | 0.00 | 0.00 | 0.00 | 0.00 |
| 2 | 0.00 | 0.00 | 0.00 | 0.00 |
| 3 | 0.00 | 0.00 | 0.00 | 0.00 |
| 4 | 0.00 | 0.00 | 0.00 | 0.00 |
| 5 | 0.00 | 0.00 | 0.00 | 0.00 |
| 6 | 0.00 | 0.00 | 0.00 | 0.00 |
| 7 | 0.00 | 0.00 | 0.00 | 0.00 |
| 8 | 0.00 | 0.00 | 0.00 | 0.00 |
| 9 | 0.00 | 0.00 | 0.00 | 0.00 |
| 10 | 0.00 | 0.00 | 0.00 | 0.00 |
| 11 | 0.00 | 0.00 | 0.00 | 0.00 |
| 12 | 2.44 | 0.00 | 3.57 | 0.00 |
| 13 | 0.00 | 0.00 | 0.00 | 0.00 |
| 14 | 2.78 | 0.00 | 0.00 | 5.88 |
| 15 | 0.00 | 0.00 | 0.00 | 0.00 |

## plain-language

- Sessions: 3/3 complete
- Slope of the pooled series: 0.0 violations per 100 sentences per turn
- Slope threshold: 0.0 (the 0.95 quantile of 1000 shuffled slopes, seed 0)
- Verdict: flat

| Turn | Pooled rate | Repeat 1 | Repeat 2 | Repeat 3 |
|---|---|---|---|---|
| 1 | 0.00 | 0.00 | 0.00 | 0.00 |
| 2 | 0.00 | 0.00 | 0.00 | 0.00 |
| 3 | 0.00 | 0.00 | 0.00 | 0.00 |
| 4 | 0.00 | 0.00 | 0.00 | 0.00 |
| 5 | 0.00 | 0.00 | 0.00 | 0.00 |
| 6 | 0.00 | 0.00 | 0.00 | 0.00 |
| 7 | 0.00 | 0.00 | 0.00 | 0.00 |
| 8 | 0.00 | 0.00 | 0.00 | 0.00 |
| 9 | 0.00 | 0.00 | 0.00 | 0.00 |
| 10 | 0.00 | 0.00 | 0.00 | 0.00 |
| 11 | 0.00 | 0.00 | 0.00 | 0.00 |
| 12 | 0.00 | 0.00 | 0.00 | 0.00 |
| 13 | 0.00 | 0.00 | 0.00 | 0.00 |
| 14 | 0.00 | 0.00 | 0.00 | 0.00 |
| 15 | 0.00 | 0.00 | 0.00 | 0.00 |

## technical-simplified

- Sessions: 3/3 complete
- Slope of the pooled series: 0.663 violations per 100 sentences per turn
- Slope threshold: 0.634 (the 0.95 quantile of 1000 shuffled slopes, seed 0)
- Verdict: growing

| Turn | Pooled rate | Repeat 1 | Repeat 2 | Repeat 3 |
|---|---|---|---|---|
| 1 | 7.41 | 14.29 | 0.00 | 11.11 |
| 2 | 2.08 | 3.57 | 0.00 | 0.00 |
| 3 | 2.56 | 0.00 | 0.00 | 5.56 |
| 4 | 13.04 | 0.00 | 27.27 | 0.00 |
| 5 | 0.00 | 0.00 | 0.00 | 0.00 |
| 6 | 3.92 | 4.55 | 0.00 | 4.55 |
| 7 | 2.27 | 0.00 | 9.09 | 0.00 |
| 8 | 4.55 | 0.00 | 7.69 | 0.00 |
| 9 | 7.84 | 12.50 | 4.76 | 0.00 |
| 10 | 7.27 | 4.76 | 0.00 | 15.79 |
| 11 | 18.75 | 40.00 | 25.00 | 5.26 |
| 12 | 6.82 | 11.11 | 3.70 | 12.50 |
| 13 | 7.14 | 13.64 | 0.00 | 0.00 |
| 14 | 20.51 | 5.56 | 0.00 | 50.00 |
| 15 | 8.62 | 0.00 | 20.00 | 0.00 |

## Harness spend

A stored call row holds the token counts of its call: the
uncached input, cache-write input, cache-read input, and
output tokens. The cache-read share is the cache-read total
over the whole input total.

Calls: 225, measured: 225.
Input tokens: 225 uncached, 140952 cache write, 3133100 cache read. Output tokens: 113913.
Cache-read share: 0.957.

## Warnings

- none

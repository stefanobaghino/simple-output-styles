# Drift report

Run: 2026-08-10-drift

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
quantile of the shuffled slopes. The same null yields a one-sided
p-value — the share of shuffled slopes at or above the observed
slope — stated for information; the verdict rests on the threshold
alone. The section of each style states
the quantile, the permutation count, and the seed. The
`--slope-threshold` flag replaces the derived threshold, and the
section then states both values.

Each style section states the final context depth of its sessions — the uncached input, the cache-write, and the cache-read tokens of a call, summed — against the 200,000-token context window (`--context-window`).

## actionable-clarity

- Sessions: 3/3 complete
- Slope of the pooled series: 0.0 violations per 100 sentences per turn
- Slope threshold: 0.0 (the 0.95 quantile of 10000 shuffled slopes, seed 0)
- Null p-value: 1.0 (the share of shuffled slopes at or above the slope)
- Verdict: flat
- Final depth: mean 21,089 tokens, 10.5 percent of the 200,000-token window (repeats 20,727 / 21,354 / 21,186)

| Turn | Pooled rate | Mean depth | Repeat 1 | Repeat 2 | Repeat 3 |
|---|---|---|---|---|---|
| 1 | 0.00 | 10,644 | 0.00 | 0.00 | 0.00 |
| 2 | 0.00 | 11,302 | 0.00 | 0.00 | 0.00 |
| 3 | 0.00 | 12,018 | 0.00 | 0.00 | 0.00 |
| 4 | 0.00 | 12,586 | 0.00 | 0.00 | 0.00 |
| 5 | 0.00 | 13,370 | 0.00 | 0.00 | 0.00 |
| 6 | 0.00 | 14,093 | 0.00 | 0.00 | 0.00 |
| 7 | 0.00 | 14,834 | 0.00 | 0.00 | 0.00 |
| 8 | 0.00 | 15,674 | 0.00 | 0.00 | 0.00 |
| 9 | 0.00 | 16,327 | 0.00 | 0.00 | 0.00 |
| 10 | 0.00 | 17,044 | 0.00 | 0.00 | 0.00 |
| 11 | 0.00 | 17,836 | 0.00 | 0.00 | 0.00 |
| 12 | 0.00 | 18,806 | 0.00 | 0.00 | 0.00 |
| 13 | 0.00 | 19,618 | 0.00 | 0.00 | 0.00 |
| 14 | 0.00 | 20,261 | 0.00 | 0.00 | 0.00 |
| 15 | 0.00 | 21,089 | 0.00 | 0.00 | 0.00 |

## clarity-flow

- Sessions: 3/3 complete
- Slope of the pooled series: 0.0 violations per 100 sentences per turn
- Slope threshold: 0.0 (the 0.95 quantile of 10000 shuffled slopes, seed 0)
- Null p-value: 1.0 (the share of shuffled slopes at or above the slope)
- Verdict: flat
- Final depth: mean 18,350 tokens, 9.2 percent of the 200,000-token window (repeats 19,871 / 18,792 / 16,388)

| Turn | Pooled rate | Mean depth | Repeat 1 | Repeat 2 | Repeat 3 |
|---|---|---|---|---|---|
| 1 | 0.00 | 9,821 | 0.00 | 0.00 | 0.00 |
| 2 | 0.00 | 10,490 | 0.00 | 0.00 | 0.00 |
| 3 | 0.00 | 10,994 | 0.00 | 0.00 | 0.00 |
| 4 | 0.00 | 11,392 | 0.00 | 0.00 | 0.00 |
| 5 | 0.00 | 11,913 | 0.00 | 0.00 | 0.00 |
| 6 | 0.00 | 12,446 | 0.00 | 0.00 | 0.00 |
| 7 | 0.00 | 13,085 | 0.00 | 0.00 | 0.00 |
| 8 | 0.00 | 13,763 | 0.00 | 0.00 | 0.00 |
| 9 | 0.00 | 14,912 | 0.00 | 0.00 | 0.00 |
| 10 | 0.00 | 15,487 | 0.00 | 0.00 | 0.00 |
| 11 | 0.00 | 16,077 | 0.00 | 0.00 | 0.00 |
| 12 | 0.00 | 16,811 | 0.00 | 0.00 | 0.00 |
| 13 | 0.00 | 17,434 | 0.00 | 0.00 | 0.00 |
| 14 | 0.00 | 17,866 | 0.00 | 0.00 | 0.00 |
| 15 | 0.00 | 18,350 | 0.00 | 0.00 | 0.00 |

## classic-concise

- Sessions: 3/3 complete
- Slope of the pooled series: -0.024 violations per 100 sentences per turn
- Slope threshold: 0.094 (the 0.95 quantile of 10000 shuffled slopes, seed 0)
- Null p-value: 0.6289 (the share of shuffled slopes at or above the slope)
- Verdict: flat
- Final depth: mean 16,772 tokens, 8.4 percent of the 200,000-token window (repeats 17,439 / 17,641 / 15,235)

| Turn | Pooled rate | Mean depth | Repeat 1 | Repeat 2 | Repeat 3 |
|---|---|---|---|---|---|
| 1 | 0.00 | 9,885 | 0.00 | 0.00 | 0.00 |
| 2 | 0.00 | 10,480 | 0.00 | 0.00 | 0.00 |
| 3 | 0.00 | 10,941 | 0.00 | 0.00 | 0.00 |
| 4 | 0.00 | 11,291 | 0.00 | 0.00 | 0.00 |
| 5 | 0.00 | 11,744 | 0.00 | 0.00 | 0.00 |
| 6 | 3.33 | 12,293 | 8.33 | 0.00 | 0.00 |
| 7 | 0.00 | 12,781 | 0.00 | 0.00 | 0.00 |
| 8 | 0.00 | 13,250 | 0.00 | 0.00 | 0.00 |
| 9 | 0.00 | 13,719 | 0.00 | 0.00 | 0.00 |
| 10 | 0.00 | 14,274 | 0.00 | 0.00 | 0.00 |
| 11 | 0.00 | 14,789 | 0.00 | 0.00 | 0.00 |
| 12 | 0.00 | 15,370 | 0.00 | 0.00 | 0.00 |
| 13 | 0.00 | 15,937 | 0.00 | 0.00 | 0.00 |
| 14 | 0.00 | 16,360 | 0.00 | 0.00 | 0.00 |
| 15 | 0.00 | 16,772 | 0.00 | 0.00 | 0.00 |

## developer-docs

- Sessions: 3/3 complete
- Slope of the pooled series: -0.046 violations per 100 sentences per turn
- Slope threshold: 0.038 (the 0.95 quantile of 10000 shuffled slopes, seed 0)
- Null p-value: 0.9904 (the share of shuffled slopes at or above the slope)
- Verdict: flat
- Final depth: mean 19,010 tokens, 9.5 percent of the 200,000-token window (repeats 19,713 / 19,328 / 17,989)

| Turn | Pooled rate | Mean depth | Repeat 1 | Repeat 2 | Repeat 3 |
|---|---|---|---|---|---|
| 1 | 1.85 | 9,824 | 2.78 | 0.00 | 0.00 |
| 2 | 0.00 | 10,428 | 0.00 | 0.00 | 0.00 |
| 3 | 0.00 | 11,011 | 0.00 | 0.00 | 0.00 |
| 4 | 0.00 | 11,758 | 0.00 | 0.00 | 0.00 |
| 5 | 0.00 | 12,320 | 0.00 | 0.00 | 0.00 |
| 6 | 0.00 | 12,983 | 0.00 | 0.00 | 0.00 |
| 7 | 0.00 | 13,609 | 0.00 | 0.00 | 0.00 |
| 8 | 0.00 | 14,255 | 0.00 | 0.00 | 0.00 |
| 9 | 0.00 | 14,869 | 0.00 | 0.00 | 0.00 |
| 10 | 0.00 | 15,562 | 0.00 | 0.00 | 0.00 |
| 11 | 0.00 | 16,378 | 0.00 | 0.00 | 0.00 |
| 12 | 0.00 | 17,078 | 0.00 | 0.00 | 0.00 |
| 13 | 0.00 | 17,722 | 0.00 | 0.00 | 0.00 |
| 14 | 0.00 | 18,314 | 0.00 | 0.00 | 0.00 |
| 15 | 0.00 | 19,010 | 0.00 | 0.00 | 0.00 |

## plain-language

- Sessions: 3/3 complete
- Slope of the pooled series: -0.051 violations per 100 sentences per turn
- Slope threshold: 0.052 (the 0.95 quantile of 10000 shuffled slopes, seed 0)
- Null p-value: 0.9535 (the share of shuffled slopes at or above the slope)
- Verdict: flat
- Final depth: mean 19,445 tokens, 9.7 percent of the 200,000-token window (repeats 20,026 / 19,225 / 19,084)

| Turn | Pooled rate | Mean depth | Repeat 1 | Repeat 2 | Repeat 3 |
|---|---|---|---|---|---|
| 1 | 0.00 | 10,043 | 0.00 | 0.00 | 0.00 |
| 2 | 0.00 | 10,756 | 0.00 | 0.00 | 0.00 |
| 3 | 2.86 | 11,469 | 0.00 | 0.00 | 5.56 |
| 4 | 0.00 | 11,954 | 0.00 | 0.00 | 0.00 |
| 5 | 0.00 | 12,572 | 0.00 | 0.00 | 0.00 |
| 6 | 0.00 | 13,225 | 0.00 | 0.00 | 0.00 |
| 7 | 0.00 | 13,931 | 0.00 | 0.00 | 0.00 |
| 8 | 0.00 | 14,719 | 0.00 | 0.00 | 0.00 |
| 9 | 0.00 | 15,298 | 0.00 | 0.00 | 0.00 |
| 10 | 0.00 | 15,893 | 0.00 | 0.00 | 0.00 |
| 11 | 0.00 | 16,623 | 0.00 | 0.00 | 0.00 |
| 12 | 0.00 | 17,443 | 0.00 | 0.00 | 0.00 |
| 13 | 0.00 | 18,181 | 0.00 | 0.00 | 0.00 |
| 14 | 0.00 | 18,778 | 0.00 | 0.00 | 0.00 |
| 15 | 0.00 | 19,445 | 0.00 | 0.00 | 0.00 |

## technical-simplified

- Sessions: 3/3 complete
- Slope of the pooled series: 0.581 violations per 100 sentences per turn
- Slope threshold: 0.826 (the 0.95 quantile of 10000 shuffled slopes, seed 0)
- Null p-value: 0.1321 (the share of shuffled slopes at or above the slope)
- Verdict: flat
- Final depth: mean 19,337 tokens, 9.7 percent of the 200,000-token window (repeats 19,966 / 18,883 / 19,163)

| Turn | Pooled rate | Mean depth | Repeat 1 | Repeat 2 | Repeat 3 |
|---|---|---|---|---|---|
| 1 | 4.35 | 10,571 | 11.11 | 0.00 | 0.00 |
| 2 | 2.27 | 11,688 | 0.00 | 10.00 | 0.00 |
| 3 | 10.53 | 12,247 | 0.00 | 14.29 | 13.04 |
| 4 | 8.16 | 12,743 | 0.00 | 16.67 | 0.00 |
| 5 | 3.64 | 13,298 | 8.33 | 0.00 | 0.00 |
| 6 | 23.91 | 13,837 | 16.67 | 75.00 | 20.83 |
| 7 | 0.00 | 14,410 | 0.00 | 0.00 | 0.00 |
| 8 | 2.33 | 15,117 | 0.00 | 4.00 | 0.00 |
| 9 | 13.04 | 15,613 | 20.83 | 6.25 | 0.00 |
| 10 | 7.69 | 16,182 | 0.00 | 0.00 | 14.81 |
| 11 | 12.73 | 16,748 | 0.00 | 24.00 | 4.35 |
| 12 | 2.00 | 17,523 | 0.00 | 3.85 | 0.00 |
| 13 | 4.44 | 18,221 | 7.14 | 0.00 | 0.00 |
| 14 | 31.71 | 18,748 | 0.00 | 0.00 | 68.42 |
| 15 | 9.09 | 19,337 | 0.00 | 16.00 | 6.25 |

## Harness spend

A stored call row holds the token counts of its call: the
uncached input, cache-write input, cache-read input, and
output tokens. The cache-read share is the cache-read total
over the whole input total.

Calls: 270, measured: 270.
Input tokens: 270 uncached, 180063 cache write, 3743555 cache read. Output tokens: 136793.
Cache-read share: 0.954.
Cache writes by lifetime: 180063 at 5 minutes, 0 at 1 hour.

## Warnings

- none

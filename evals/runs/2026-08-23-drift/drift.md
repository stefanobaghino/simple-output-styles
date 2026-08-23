# Drift report

Run: 2026-08-23-drift

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

## concise

- Sessions: 3/3 complete
- Slope of the pooled series: 0.0 violations per 100 sentences per turn
- Slope threshold: 0.0 (the 0.95 quantile of 10000 shuffled slopes, seed 0)
- Null p-value: 1.0 (the share of shuffled slopes at or above the slope)
- Verdict: flat
- Final depth: mean 17,509 tokens, 8.8 percent of the 200,000-token window (repeats 17,820 / 18,188 / 16,520)

| Turn | Pooled rate | Mean depth | Repeat 1 | Repeat 2 | Repeat 3 |
|---|---|---|---|---|---|
| 1 | 0.00 | 9,149 | 0.00 | 0.00 | 0.00 |
| 2 | 0.00 | 9,779 | 0.00 | 0.00 | 0.00 |
| 3 | 0.00 | 10,271 | 0.00 | 0.00 | 0.00 |
| 4 | 0.00 | 10,691 | 0.00 | 0.00 | 0.00 |
| 5 | 0.00 | 11,278 | 0.00 | 0.00 | 0.00 |
| 6 | 0.00 | 11,894 | 0.00 | 0.00 | 0.00 |
| 7 | 0.00 | 12,589 | 0.00 | 0.00 | 0.00 |
| 8 | 0.00 | 13,138 | 0.00 | 0.00 | 0.00 |
| 9 | 0.00 | 13,738 | 0.00 | 0.00 | 0.00 |
| 10 | 0.00 | 14,342 | 0.00 | 0.00 | 0.00 |
| 11 | 0.00 | 14,999 | 0.00 | 0.00 | 0.00 |
| 12 | 0.00 | 15,785 | 0.00 | 0.00 | 0.00 |
| 13 | 0.00 | 10,950 | 0.00 | 0.00 | 0.00 |
| 14 | 0.00 | 16,870 | 0.00 | 0.00 | 0.00 |
| 15 | 0.00 | 17,509 | 0.00 | 0.00 | 0.00 |

## Harness spend

A stored call row holds the token counts of its call: the
uncached input, cache-write input, cache-read input, and
output tokens. The cache-read share is the cache-read total
over the whole input total.

Calls: 45, measured: 45.
Input tokens: 88 uncached, 35099 cache write, 543757 cache read. Output tokens: 16325.
Cache-read share: 0.939.
Cache writes by lifetime: 35099 at 5 minutes, 0 at 1 hour.

## Warnings

- none

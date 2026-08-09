# Drift report

Run: 2026-08-09-drift-deep

The report measures rule obedience across long sessions. A session is
15 scripted turns in one Claude Code session, with the style
active. Each turn resumes the session of the previous turn, so the
context grows. Each session follows one coherent script with heavy
turn material, and later turns reference earlier material, so the
model must read deep context while it obeys the style. A coherent
script cannot rotate, so the 3 repeat(s) spread over several
different scripts, and the coupling of turn position to content
averages over scripts. The shallow rotated run is the control. The
linter checks each answer with the rule set of the style. The rate
of a turn position pools the complete sessions: 100 times the
violations at that position over the sentences at that position.
Thus a short answer weighs by its sentence count and cannot dominate
the series. The verdict compares the slope of the pooled series
against a per-style threshold: "growing" when the slope is larger,
else "flat". The threshold comes from a permutation null: the turn
order of each session shuffles, the pooled slope refits, and the
threshold is a nearest-rank quantile of the shuffled slopes. The
same null yields a one-sided p-value — the share of shuffled slopes
at or above the observed slope — stated for information; the
verdict rests on the threshold alone. The
section of each style states the quantile, the permutation count,
and the seed. The `--slope-threshold` flag replaces the derived
threshold, and the section then states both values.

- Repeat 1: script `incident-timeline`
- Repeat 2: script `service-review`
- Repeat 3: script `design-doc-series`

Each style section states the final context depth of its sessions — the uncached input, the cache-write, and the cache-read tokens of a call, summed — against the 200,000-token context window (`--context-window`). The depth target is 60 percent of the window: a style whose mean final depth misses the target warns, because a flat verdict at a shallow depth is weak evidence.

## clarity-flow

- Sessions: 3/3 complete
- Slope of the pooled series: 0.0 violations per 100 sentences per turn
- Slope threshold: 0.0 (the 0.95 quantile of 10000 shuffled slopes, seed 0)
- Null p-value: 1.0 (the share of shuffled slopes at or above the slope)
- Verdict: flat
- Final depth: mean 297,325 tokens, 148.7 percent of the 200,000-token window (repeats 311,519 / 418,058 / 162,397)

| Turn | Pooled rate | Mean depth | Repeat 1 | Repeat 2 | Repeat 3 |
|---|---|---|---|---|---|
| 1 | 0.00 | 20,897 | 0.00 | 0.00 | 0.00 |
| 2 | 0.00 | 37,944 | 0.00 | 0.00 | 0.00 |
| 3 | 0.00 | 56,133 | 0.00 | 0.00 | 0.00 |
| 4 | 0.00 | 75,188 | 0.00 | 0.00 | 0.00 |
| 5 | 0.00 | 95,054 | 0.00 | 0.00 | 0.00 |
| 6 | 0.00 | 114,218 | 0.00 | 0.00 | 0.00 |
| 7 | 0.00 | 130,773 | 0.00 | 0.00 | 0.00 |
| 8 | 0.00 | 146,644 | 0.00 | 0.00 | 0.00 |
| 9 | 0.00 | 168,094 | 0.00 | 0.00 | 0.00 |
| 10 | 0.00 | 186,932 | 0.00 | 0.00 | 0.00 |
| 11 | 0.00 | 207,638 | 0.00 | 0.00 | 0.00 |
| 12 | 0.00 | 229,540 | 0.00 | 0.00 | 0.00 |
| 13 | 0.00 | 253,191 | 0.00 | 0.00 | 0.00 |
| 14 | 0.00 | 272,649 | 0.00 | 0.00 | 0.00 |
| 15 | 0.00 | 297,325 | 0.00 | 0.00 | 0.00 |

## Harness spend

A stored call row holds the token counts of its call: the
uncached input, cache-write input, cache-read input, and
output tokens. The cache-read share is the cache-read total
over the whole input total.

Calls: 45, measured: 45.
Input tokens: 45 uncached, 1252871 cache write, 5623742 cache read. Output tokens: 422220.
Cache-read share: 0.818.
Cache writes by lifetime: 1252871 at 5 minutes, 0 at 1 hour.

## Warnings

- none

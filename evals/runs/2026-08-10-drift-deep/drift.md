# Drift report

Run: 2026-08-10-drift-deep

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

## actionable-clarity

- Sessions: 3/3 complete
- Slope of the pooled series: -0.022 violations per 100 sentences per turn
- Slope threshold: 0.069 (the 0.95 quantile of 10000 shuffled slopes, seed 0)
- Null p-value: 0.6979 (the share of shuffled slopes at or above the slope)
- Verdict: flat
- Final depth: mean 304,593 tokens, 152.3 percent of the 200,000-token window (repeats 354,264 / 392,400 / 167,114)

| Turn | Pooled rate | Mean depth | Repeat 1 | Repeat 2 | Repeat 3 |
|---|---|---|---|---|---|
| 1 | 0.00 | 21,721 | 0.00 | 0.00 | 0.00 |
| 2 | 0.00 | 39,209 | 0.00 | 0.00 | 0.00 |
| 3 | 0.85 | 58,274 | 0.00 | 1.64 | 0.00 |
| 4 | 2.02 | 79,750 | 0.00 | 5.13 | 0.00 |
| 5 | 0.00 | 100,224 | 0.00 | 0.00 | 0.00 |
| 6 | 0.75 | 119,860 | 0.00 | 2.27 | 0.00 |
| 7 | 0.00 | 137,400 | 0.00 | 0.00 | 0.00 |
| 8 | 3.70 | 154,754 | 4.76 | 4.44 | 0.00 |
| 9 | 1.22 | 177,416 | 0.00 | 2.50 | 0.00 |
| 10 | 1.04 | 195,834 | 1.03 | 1.45 | 0.00 |
| 11 | 0.00 | 217,665 | 0.00 | 0.00 | 0.00 |
| 12 | 0.00 | 239,838 | 0.00 | 0.00 | 0.00 |
| 13 | 0.48 | 260,475 | 0.00 | 1.15 | 0.00 |
| 14 | 0.35 | 282,383 | 0.00 | 0.92 | 0.00 |
| 15 | 0.00 | 304,593 | 0.00 | 0.00 | 0.00 |

## Harness spend

A stored call row holds the token counts of its call: the
uncached input, cache-write input, cache-read input, and
output tokens. The cache-read share is the cache-read total
over the whole input total.

Calls: 45, measured: 45.
Input tokens: 45 uncached, 893491 cache write, 6274653 cache read. Output tokens: 433758.
Cache-read share: 0.875.
Cache writes by lifetime: 893491 at 5 minutes, 0 at 1 hour.

## Warnings

- none

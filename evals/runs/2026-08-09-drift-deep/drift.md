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

## classic-concise

- Sessions: 3/3 complete
- Slope of the pooled series: -0.007 violations per 100 sentences per turn
- Slope threshold: 0.081 (the 0.95 quantile of 10000 shuffled slopes, seed 0)
- Null p-value: 0.5461 (the share of shuffled slopes at or above the slope)
- Verdict: flat
- Final depth: mean 281,388 tokens, 140.7 percent of the 200,000-token window (repeats 319,464 / 372,171 / 152,529)

| Turn | Pooled rate | Mean depth | Repeat 1 | Repeat 2 | Repeat 3 |
|---|---|---|---|---|---|
| 1 | 0.00 | 20,954 | 0.00 | 0.00 | 0.00 |
| 2 | 0.00 | 37,950 | 0.00 | 0.00 | 0.00 |
| 3 | 1.28 | 55,534 | 0.00 | 1.85 | 0.00 |
| 4 | 0.00 | 73,685 | 0.00 | 0.00 | 0.00 |
| 5 | 1.14 | 93,466 | 0.00 | 1.85 | 0.00 |
| 6 | 0.00 | 110,835 | 0.00 | 0.00 | 0.00 |
| 7 | 0.00 | 126,616 | 0.00 | 0.00 | 0.00 |
| 8 | 1.09 | 142,611 | 0.00 | 1.49 | 0.00 |
| 9 | 0.00 | 162,709 | 0.00 | 0.00 | 0.00 |
| 10 | 2.46 | 178,065 | 0.00 | 5.08 | 0.00 |
| 11 | 0.00 | 197,760 | 0.00 | 0.00 | 0.00 |
| 12 | 0.75 | 218,996 | 0.00 | 3.57 | 0.00 |
| 13 | 0.00 | 239,952 | 0.00 | 0.00 | 0.00 |
| 14 | 0.00 | 259,891 | 0.00 | 0.00 | 0.00 |
| 15 | 0.00 | 281,388 | 0.00 | 0.00 | 0.00 |

## developer-docs

- Sessions: 3/3 complete
- Slope of the pooled series: 0.063 violations per 100 sentences per turn
- Slope threshold: 0.072 (the 0.95 quantile of 10000 shuffled slopes, seed 0)
- Null p-value: 0.0767 (the share of shuffled slopes at or above the slope)
- Verdict: flat
- Final depth: mean 297,218 tokens, 148.6 percent of the 200,000-token window (repeats 330,077 / 407,119 / 154,457)

| Turn | Pooled rate | Mean depth | Repeat 1 | Repeat 2 | Repeat 3 |
|---|---|---|---|---|---|
| 1 | 0.00 | 20,893 | 0.00 | 0.00 | 0.00 |
| 2 | 0.00 | 37,951 | 0.00 | 0.00 | 0.00 |
| 3 | 1.59 | 56,450 | 0.00 | 1.59 | 4.35 |
| 4 | 0.00 | 74,482 | 0.00 | 0.00 | 0.00 |
| 5 | 0.92 | 93,420 | 0.00 | 1.75 | 0.00 |
| 6 | 0.00 | 111,780 | 0.00 | 0.00 | 0.00 |
| 7 | 1.16 | 129,475 | 0.00 | 2.38 | 0.00 |
| 8 | 0.98 | 147,202 | 0.00 | 0.00 | 6.67 |
| 9 | 1.09 | 168,992 | 3.57 | 0.00 | 0.00 |
| 10 | 1.10 | 188,455 | 0.00 | 2.53 | 0.00 |
| 11 | 0.45 | 211,284 | 0.00 | 1.20 | 0.00 |
| 12 | 0.55 | 233,921 | 0.00 | 0.00 | 2.44 |
| 13 | 1.31 | 255,254 | 0.00 | 0.93 | 2.00 |
| 14 | 1.06 | 274,464 | 0.00 | 2.73 | 0.00 |
| 15 | 1.40 | 297,218 | 0.00 | 2.56 | 0.00 |

## plain-language

- Sessions: 3/3 complete
- Slope of the pooled series: -0.028 violations per 100 sentences per turn
- Slope threshold: 0.062 (the 0.95 quantile of 10000 shuffled slopes, seed 0)
- Null p-value: 0.7563 (the share of shuffled slopes at or above the slope)
- Verdict: flat
- Final depth: mean 308,419 tokens, 154.2 percent of the 200,000-token window (repeats 342,385 / 423,433 / 159,438)

| Turn | Pooled rate | Mean depth | Repeat 1 | Repeat 2 | Repeat 3 |
|---|---|---|---|---|---|
| 1 | 0.91 | 21,112 | 0.00 | 1.75 | 0.00 |
| 2 | 0.84 | 38,162 | 3.45 | 0.00 | 0.00 |
| 3 | 0.00 | 57,080 | 0.00 | 0.00 | 0.00 |
| 4 | 0.00 | 78,529 | 0.00 | 0.00 | 0.00 |
| 5 | 0.74 | 98,787 | 0.00 | 1.37 | 0.00 |
| 6 | 1.87 | 118,031 | 3.80 | 1.64 | 0.00 |
| 7 | 0.93 | 134,868 | 2.86 | 0.00 | 0.00 |
| 8 | 0.00 | 152,005 | 0.00 | 0.00 | 0.00 |
| 9 | 0.00 | 174,534 | 0.00 | 0.00 | 0.00 |
| 10 | 0.00 | 191,953 | 0.00 | 0.00 | 0.00 |
| 11 | 1.12 | 213,045 | 3.00 | 0.00 | 0.00 |
| 12 | 0.52 | 238,288 | 0.83 | 0.00 | 0.00 |
| 13 | 0.00 | 262,045 | 0.00 | 0.00 | 0.00 |
| 14 | 0.85 | 283,058 | 1.59 | 0.88 | 0.00 |
| 15 | 0.00 | 308,419 | 0.00 | 0.00 | 0.00 |

## technical-simplified

- Sessions: 3/3 complete
- Slope of the pooled series: 1.884 violations per 100 sentences per turn
- Slope threshold: 1.236 (the 0.95 quantile of 10000 shuffled slopes, seed 0)
- Null p-value: 0.0046 (the share of shuffled slopes at or above the slope)
- Verdict: growing
- Final depth: mean 304,634 tokens, 152.3 percent of the 200,000-token window (repeats 351,867 / 403,826 / 158,209)

| Turn | Pooled rate | Mean depth | Repeat 1 | Repeat 2 | Repeat 3 |
|---|---|---|---|---|---|
| 1 | 3.91 | 21,640 | 3.03 | 4.11 | 4.55 |
| 2 | 31.67 | 37,590 | 30.30 | 0.00 | 34.62 |
| 3 | 27.15 | 56,628 | 13.64 | 36.90 | 17.39 |
| 4 | 33.02 | 77,179 | 15.15 | 56.86 | 4.55 |
| 5 | 46.02 | 96,228 | 16.67 | 75.56 | 50.00 |
| 6 | 47.41 | 114,836 | 30.95 | 69.81 | 23.81 |
| 7 | 51.58 | 132,611 | 47.06 | 78.38 | 16.67 |
| 8 | 60.19 | 148,918 | 37.14 | 86.21 | 13.33 |
| 9 | 47.00 | 171,859 | 40.54 | 60.98 | 31.82 |
| 10 | 43.35 | 190,923 | 21.59 | 81.03 | 33.33 |
| 11 | 36.40 | 212,448 | 59.30 | 39.39 | 14.29 |
| 12 | 56.86 | 235,102 | 56.76 | 86.11 | 38.60 |
| 13 | 49.34 | 257,324 | 70.27 | 61.84 | 34.48 |
| 14 | 39.73 | 279,070 | 36.61 | 50.44 | 27.78 |
| 15 | 48.82 | 304,634 | 66.67 | 83.33 | 17.19 |

## Harness spend

A stored call row holds the token counts of its call: the
uncached input, cache-write input, cache-read input, and
output tokens. The cache-read share is the cache-read total
over the whole input total.

Calls: 225, measured: 225.
Input tokens: 225 uncached, 4729463 cache write, 29772635 cache read. Output tokens: 2085102.
Cache-read share: 0.863.
Cache writes by lifetime: 4729463 at 5 minutes, 0 at 1 hour.

## Warnings

- none

# Token cost report

A style costs tokens in two ways: the style block adds a fixed
quantity of input tokens to every request, and the style changes
the answer length. The report states both numbers per style. The
report reads all pairs of the run, gated or not.

## Input overhead per request

The overhead is the difference in input context tokens between
a styled probe call and an unstyled probe call of the same
repeat. Both probe arms load the plugin, so the difference
isolates the style block. The weighted overhead multiplies each
token count by its price ratio against one uncached input token
(uncached 1.0, cache write 1.25, cache read 0.1), so the unit is
uncached-token equivalents.

| Style | Overhead tokens (mean ± stdev) | Weighted overhead (mean ± stdev) |
|---|---|---|
| actionable-clarity | 2115.0 ± 0.0 | -102.067 ± 543.113 |
| clarity-flow | 1291.0 ± 0.0 | -184.85 ± 543.777 |
| classic-concise | 1354.0 ± 0.0 | -178.933 ± 544.441 |
| concise | 504.0 ± 0.0 | -263.167 ± 543.113 |
| developer-docs | 1293.0 ± 0.0 | -185.033 ± 544.441 |
| plain-language | 1511.0 ± 0.0 | -163.617 ± 545.105 |
| technical-simplified | 2041.0 ± 0.0 | -109.85 ± 543.777 |

Probe: 2026-08-23T11:28:28+00:00, model sonnet, repeats 3.

## Harness spend

A stored call row holds the token counts of its call: the
uncached input, cache-write input, cache-read input, and
output tokens. The cache-read share is the cache-read total
over the whole input total.

Calls: 24, measured: 24.
Input tokens: 48 uncached, 4505 cache write, 230110 cache read. Output tokens: 96.
Cache-read share: 0.981.
Cache writes by lifetime: 4505 at 5 minutes, 0 at 1 hour.

## Answer-length ratio

The ratio of a pair is the output-token count of the styled
answer divided by the output-token count of the unstyled answer
of the same prompt. A ratio below 1 means a shorter styled
answer.

### actionable-clarity

- Pairs: 32
- Output tokens: styled 29331, unstyled 30039, ratio of totals 0.98

| n | min | p25 | median | p75 | max | mean |
|---|---|---|---|---|---|---|
| 32 | 0.58 | 0.82 | 0.97 | 1.18 | 2.49 | 1.04 |

| Task type | n | min | median | mean | max |
|---|---|---|---|---|---|
| code-review | 8 | 0.75 | 0.98 | 1.22 | 2.49 |
| debugging | 8 | 0.58 | 0.88 | 0.87 | 1.17 |
| explanation | 8 | 0.62 | 0.96 | 0.95 | 1.26 |
| summarization | 8 | 0.63 | 1.08 | 1.11 | 1.83 |

### clarity-flow

- Pairs: 32
- Output tokens: styled 25250, unstyled 30039, ratio of totals 0.84

| n | min | p25 | median | p75 | max | mean |
|---|---|---|---|---|---|---|
| 32 | 0.37 | 0.67 | 0.86 | 1.02 | 2.25 | 0.93 |

| Task type | n | min | median | mean | max |
|---|---|---|---|---|---|
| code-review | 8 | 0.68 | 0.92 | 1.1 | 1.87 |
| debugging | 8 | 0.37 | 0.66 | 0.8 | 2.04 |
| explanation | 8 | 0.39 | 0.72 | 0.77 | 1.13 |
| summarization | 8 | 0.65 | 0.87 | 1.04 | 2.25 |

### classic-concise

- Pairs: 32
- Output tokens: styled 15282, unstyled 30039, ratio of totals 0.51

| n | min | p25 | median | p75 | max | mean |
|---|---|---|---|---|---|---|
| 32 | 0.24 | 0.43 | 0.62 | 0.75 | 1.61 | 0.63 |

| Task type | n | min | median | mean | max |
|---|---|---|---|---|---|
| code-review | 8 | 0.24 | 0.49 | 0.64 | 1.61 |
| debugging | 8 | 0.24 | 0.41 | 0.45 | 0.72 |
| explanation | 8 | 0.41 | 0.63 | 0.62 | 0.84 |
| summarization | 8 | 0.42 | 0.84 | 0.8 | 0.99 |

### concise

- Pairs: 32
- Output tokens: styled 16647, unstyled 30039, ratio of totals 0.55

| n | min | p25 | median | p75 | max | mean |
|---|---|---|---|---|---|---|
| 32 | 0.19 | 0.46 | 0.57 | 0.7 | 2.1 | 0.62 |

| Task type | n | min | median | mean | max |
|---|---|---|---|---|---|
| code-review | 8 | 0.21 | 0.56 | 0.53 | 0.67 |
| debugging | 8 | 0.19 | 0.51 | 0.67 | 2.1 |
| explanation | 8 | 0.32 | 0.52 | 0.53 | 0.82 |
| summarization | 8 | 0.37 | 0.82 | 0.75 | 0.87 |

### developer-docs

- Pairs: 32
- Output tokens: styled 27759, unstyled 30039, ratio of totals 0.92

| n | min | p25 | median | p75 | max | mean |
|---|---|---|---|---|---|---|
| 32 | 0.28 | 0.68 | 0.94 | 1.28 | 2.45 | 1.05 |

| Task type | n | min | median | mean | max |
|---|---|---|---|---|---|
| code-review | 8 | 0.48 | 0.87 | 1.07 | 2.23 |
| debugging | 8 | 0.28 | 0.95 | 1.11 | 2.45 |
| explanation | 8 | 0.49 | 0.98 | 0.94 | 1.31 |
| summarization | 8 | 0.55 | 1.01 | 1.1 | 1.98 |

### plain-language

- Pairs: 32
- Output tokens: styled 28648, unstyled 30039, ratio of totals 0.95

| n | min | p25 | median | p75 | max | mean |
|---|---|---|---|---|---|---|
| 32 | 0.31 | 0.76 | 0.96 | 1.31 | 2.38 | 1.06 |

| Task type | n | min | median | mean | max |
|---|---|---|---|---|---|
| code-review | 8 | 0.61 | 0.94 | 1.22 | 2.38 |
| debugging | 8 | 0.31 | 1.0 | 0.93 | 1.47 |
| explanation | 8 | 0.5 | 0.84 | 0.95 | 1.79 |
| summarization | 8 | 0.54 | 1.09 | 1.16 | 2.15 |

### technical-simplified

- Pairs: 32
- Output tokens: styled 25138, unstyled 30039, ratio of totals 0.84

| n | min | p25 | median | p75 | max | mean |
|---|---|---|---|---|---|---|
| 32 | 0.18 | 0.72 | 0.95 | 1.22 | 7.4 | 1.15 |

| Task type | n | min | median | mean | max |
|---|---|---|---|---|---|
| code-review | 8 | 0.18 | 0.91 | 0.81 | 1.22 |
| debugging | 8 | 0.38 | 0.85 | 0.9 | 1.6 |
| explanation | 8 | 0.61 | 0.83 | 0.91 | 1.45 |
| summarization | 8 | 0.75 | 0.98 | 2.0 | 7.4 |

## Reading the ratio

A lower ratio is not by itself a win: fewer tokens with less content is a loss. Issue #7 measures whether the content survives.

## Warnings

- none

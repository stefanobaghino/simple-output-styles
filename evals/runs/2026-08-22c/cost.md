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
| actionable-clarity | 2115.0 ± 0.0 | 3637.35 ± 6346.457 |
| clarity-flow | 1291.0 ± 0.0 | 461.067 ± 1011.18 |
| classic-concise | 1354.0 ± 0.0 | 491.517 ± 1051.901 |
| concise | 504.0 ± 0.0 | 80.683 ± 517.59 |
| developer-docs | 1293.0 ± 0.0 | 462.033 ± 1012.471 |
| plain-language | 1511.0 ± 0.0 | 567.4 ± 1153.727 |
| technical-simplified | 2041.0 ± 0.0 | 823.567 ± 1499.922 |

Probe: 2026-08-23T11:28:29+00:00, model sonnet, repeats 3.

## Harness spend

A stored call row holds the token counts of its call: the
uncached input, cache-write input, cache-read input, and
output tokens. The cache-read share is the cache-read total
over the whole input total.

Calls: 24, measured: 24.
Input tokens: 48 uncached, 27917 cache write, 206746 cache read. Output tokens: 96.
Cache-read share: 0.881.
Cache writes by lifetime: 27917 at 5 minutes, 0 at 1 hour.

## Answer-length ratio

The ratio of a pair is the output-token count of the styled
answer divided by the output-token count of the unstyled answer
of the same prompt. A ratio below 1 means a shorter styled
answer.

### actionable-clarity

- Pairs: 32
- Output tokens: styled 29858, unstyled 24149, ratio of totals 1.24

| n | min | p25 | median | p75 | max | mean |
|---|---|---|---|---|---|---|
| 32 | 0.23 | 0.89 | 1.09 | 1.36 | 16.34 | 1.63 |

| Task type | n | min | median | mean | max |
|---|---|---|---|---|---|
| code-review | 8 | 0.71 | 1.28 | 1.45 | 2.55 |
| debugging | 8 | 0.23 | 1.01 | 2.9 | 16.34 |
| explanation | 8 | 0.67 | 0.96 | 1.03 | 1.53 |
| summarization | 8 | 0.89 | 1.14 | 1.13 | 1.46 |

### clarity-flow

- Pairs: 32
- Output tokens: styled 21930, unstyled 24149, ratio of totals 0.91

| n | min | p25 | median | p75 | max | mean |
|---|---|---|---|---|---|---|
| 32 | 0.18 | 0.59 | 0.86 | 1.08 | 10.8 | 1.32 |

| Task type | n | min | median | mean | max |
|---|---|---|---|---|---|
| code-review | 8 | 0.44 | 0.9 | 1.08 | 2.79 |
| debugging | 8 | 0.18 | 0.84 | 2.56 | 10.8 |
| explanation | 8 | 0.43 | 0.59 | 0.64 | 1.24 |
| summarization | 8 | 0.78 | 0.96 | 1.0 | 1.37 |

### classic-concise

- Pairs: 32
- Output tokens: styled 17763, unstyled 24149, ratio of totals 0.74

| n | min | p25 | median | p75 | max | mean |
|---|---|---|---|---|---|---|
| 32 | 0.13 | 0.55 | 0.63 | 0.87 | 4.94 | 0.94 |

| Task type | n | min | median | mean | max |
|---|---|---|---|---|---|
| code-review | 8 | 0.46 | 0.63 | 0.72 | 1.49 |
| debugging | 8 | 0.13 | 0.74 | 1.65 | 4.94 |
| explanation | 8 | 0.53 | 0.57 | 0.59 | 0.74 |
| summarization | 8 | 0.5 | 0.8 | 0.78 | 1.06 |

### concise

- Pairs: 32
- Output tokens: styled 16010, unstyled 24149, ratio of totals 0.66

| n | min | p25 | median | p75 | max | mean |
|---|---|---|---|---|---|---|
| 32 | 0.14 | 0.55 | 0.61 | 0.9 | 5.99 | 0.97 |

| Task type | n | min | median | mean | max |
|---|---|---|---|---|---|
| code-review | 8 | 0.32 | 0.6 | 0.64 | 1.24 |
| debugging | 8 | 0.14 | 0.64 | 1.85 | 5.99 |
| explanation | 8 | 0.37 | 0.54 | 0.57 | 0.9 |
| summarization | 8 | 0.58 | 0.85 | 0.83 | 1.04 |

### developer-docs

- Pairs: 32
- Output tokens: styled 22828, unstyled 24149, ratio of totals 0.95

| n | min | p25 | median | p75 | max | mean |
|---|---|---|---|---|---|---|
| 32 | 0.43 | 0.76 | 0.86 | 1.11 | 11.78 | 1.46 |

| Task type | n | min | median | mean | max |
|---|---|---|---|---|---|
| code-review | 8 | 0.72 | 0.9 | 1.01 | 2.02 |
| debugging | 8 | 0.43 | 1.13 | 3.04 | 11.78 |
| explanation | 8 | 0.49 | 0.74 | 0.8 | 1.38 |
| summarization | 8 | 0.78 | 0.97 | 0.99 | 1.26 |

### plain-language

- Pairs: 32
- Output tokens: styled 22551, unstyled 24149, ratio of totals 0.93

| n | min | p25 | median | p75 | max | mean |
|---|---|---|---|---|---|---|
| 32 | 0.08 | 0.76 | 0.99 | 1.1 | 11.17 | 1.5 |

| Task type | n | min | median | mean | max |
|---|---|---|---|---|---|
| code-review | 8 | 0.08 | 0.84 | 0.79 | 1.08 |
| debugging | 8 | 0.37 | 1.13 | 3.31 | 11.17 |
| explanation | 8 | 0.53 | 0.93 | 0.91 | 1.31 |
| summarization | 8 | 0.76 | 1.08 | 1.0 | 1.2 |

### technical-simplified

- Pairs: 32
- Output tokens: styled 27750, unstyled 24149, ratio of totals 1.15

| n | min | p25 | median | p75 | max | mean |
|---|---|---|---|---|---|---|
| 32 | 0.09 | 0.71 | 0.96 | 1.29 | 11.86 | 1.61 |

| Task type | n | min | median | mean | max |
|---|---|---|---|---|---|
| code-review | 8 | 0.09 | 1.04 | 1.23 | 3.27 |
| debugging | 8 | 0.24 | 1.04 | 3.09 | 11.86 |
| explanation | 8 | 0.16 | 0.72 | 0.91 | 2.43 |
| summarization | 8 | 0.78 | 0.99 | 1.21 | 2.95 |

## Reading the ratio

A lower ratio is not by itself a win: fewer tokens with less content is a loss. Issue #7 measures whether the content survives.

## Warnings

- none

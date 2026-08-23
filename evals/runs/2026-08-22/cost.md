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
| actionable-clarity | 2115.0 ± 0.0 | 232.2 ± 35.853 |
| clarity-flow | 1291.0 ± 0.0 | 149.417 ± 35.189 |
| classic-concise | 1354.0 ± 0.0 | 155.333 ± 34.526 |
| concise | 504.0 ± 0.0 | 71.1 ± 35.853 |
| developer-docs | 1293.0 ± 0.0 | 149.233 ± 34.526 |
| plain-language | 1511.0 ± 0.0 | 170.65 ± 33.862 |
| technical-simplified | 2041.0 ± 0.0 | 224.417 ± 35.189 |

Probe: 2026-08-23T11:28:34+00:00, model sonnet, repeats 3.

## Harness spend

A stored call row holds the token counts of its call: the
uncached input, cache-write input, cache-read input, and
output tokens. The cache-read share is the cache-read total
over the whole input total.

Calls: 24, measured: 24.
Input tokens: 48 uncached, 3657 cache write, 231030 cache read. Output tokens: 96.
Cache-read share: 0.984.
Cache writes by lifetime: 3657 at 5 minutes, 0 at 1 hour.

## Answer-length ratio

The ratio of a pair is the output-token count of the styled
answer divided by the output-token count of the unstyled answer
of the same prompt. A ratio below 1 means a shorter styled
answer.

### actionable-clarity

- Pairs: 32
- Output tokens: styled 33464, unstyled 34215, ratio of totals 0.98

| n | min | p25 | median | p75 | max | mean |
|---|---|---|---|---|---|---|
| 32 | 0.51 | 0.78 | 1.03 | 1.3 | 2.04 | 1.1 |

| Task type | n | min | median | mean | max |
|---|---|---|---|---|---|
| code-review | 8 | 0.65 | 1.18 | 1.25 | 2.04 |
| debugging | 8 | 0.51 | 0.77 | 0.94 | 1.71 |
| explanation | 8 | 0.68 | 0.89 | 1.03 | 1.95 |
| summarization | 8 | 0.66 | 1.16 | 1.18 | 2.04 |

### clarity-flow

- Pairs: 32
- Output tokens: styled 20711, unstyled 34215, ratio of totals 0.61

| n | min | p25 | median | p75 | max | mean |
|---|---|---|---|---|---|---|
| 32 | 0.21 | 0.51 | 0.72 | 0.96 | 1.91 | 0.78 |

| Task type | n | min | median | mean | max |
|---|---|---|---|---|---|
| code-review | 8 | 0.52 | 0.86 | 0.97 | 1.59 |
| debugging | 8 | 0.21 | 0.43 | 0.54 | 1.24 |
| explanation | 8 | 0.41 | 0.58 | 0.61 | 0.82 |
| summarization | 8 | 0.56 | 0.91 | 1.01 | 1.91 |

### classic-concise

- Pairs: 32
- Output tokens: styled 17552, unstyled 34215, ratio of totals 0.51

| n | min | p25 | median | p75 | max | mean |
|---|---|---|---|---|---|---|
| 32 | 0.14 | 0.43 | 0.57 | 0.73 | 1.33 | 0.63 |

| Task type | n | min | median | mean | max |
|---|---|---|---|---|---|
| code-review | 8 | 0.42 | 0.61 | 0.67 | 1.33 |
| debugging | 8 | 0.14 | 0.4 | 0.49 | 1.04 |
| explanation | 8 | 0.42 | 0.56 | 0.55 | 0.69 |
| summarization | 8 | 0.48 | 0.8 | 0.8 | 1.11 |

### concise

- Pairs: 32
- Output tokens: styled 18152, unstyled 34215, ratio of totals 0.53

| n | min | p25 | median | p75 | max | mean |
|---|---|---|---|---|---|---|
| 32 | 0.26 | 0.49 | 0.56 | 0.73 | 1.12 | 0.62 |

| Task type | n | min | median | mean | max |
|---|---|---|---|---|---|
| code-review | 8 | 0.49 | 0.56 | 0.61 | 0.92 |
| debugging | 8 | 0.26 | 0.5 | 0.5 | 0.73 |
| explanation | 8 | 0.33 | 0.49 | 0.48 | 0.62 |
| summarization | 8 | 0.5 | 0.9 | 0.87 | 1.12 |

### developer-docs

- Pairs: 32
- Output tokens: styled 23352, unstyled 34215, ratio of totals 0.68

| n | min | p25 | median | p75 | max | mean |
|---|---|---|---|---|---|---|
| 32 | 0.35 | 0.63 | 0.77 | 1.09 | 1.59 | 0.85 |

| Task type | n | min | median | mean | max |
|---|---|---|---|---|---|
| code-review | 8 | 0.6 | 0.76 | 0.88 | 1.35 |
| debugging | 8 | 0.35 | 0.66 | 0.76 | 1.59 |
| explanation | 8 | 0.41 | 0.75 | 0.82 | 1.23 |
| summarization | 8 | 0.58 | 1.02 | 0.96 | 1.32 |

### plain-language

- Pairs: 32
- Output tokens: styled 23845, unstyled 34215, ratio of totals 0.7

| n | min | p25 | median | p75 | max | mean |
|---|---|---|---|---|---|---|
| 32 | 0.24 | 0.66 | 0.81 | 1.16 | 2.48 | 0.95 |

| Task type | n | min | median | mean | max |
|---|---|---|---|---|---|
| code-review | 8 | 0.62 | 0.89 | 0.96 | 1.45 |
| debugging | 8 | 0.24 | 0.76 | 0.85 | 1.87 |
| explanation | 8 | 0.51 | 0.73 | 0.85 | 1.23 |
| summarization | 8 | 0.61 | 1.01 | 1.12 | 2.48 |

### technical-simplified

- Pairs: 32
- Output tokens: styled 25265, unstyled 34215, ratio of totals 0.74

| n | min | p25 | median | p75 | max | mean |
|---|---|---|---|---|---|---|
| 32 | 0.25 | 0.54 | 0.78 | 1.01 | 1.85 | 0.8 |

| Task type | n | min | median | mean | max |
|---|---|---|---|---|---|
| code-review | 8 | 0.25 | 0.84 | 0.85 | 1.85 |
| debugging | 8 | 0.25 | 0.6 | 0.81 | 1.66 |
| explanation | 8 | 0.34 | 0.56 | 0.63 | 0.89 |
| summarization | 8 | 0.65 | 0.94 | 0.92 | 1.22 |

## Reading the ratio

A lower ratio is not by itself a win: fewer tokens with less content is a loss. Issue #7 measures whether the content survives.

## Warnings

- none

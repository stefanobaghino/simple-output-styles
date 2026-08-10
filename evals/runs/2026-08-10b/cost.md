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
| clarity-flow | 1238.0 ± 0.0 | -201.65 ± 563.696 |
| classic-concise | 1302.0 ± 0.0 | -195.25 ± 563.696 |
| developer-docs | 1241.0 ± 0.0 | -201.35 ± 563.696 |
| plain-language | 1460.0 ± 0.0 | -179.45 ± 563.696 |
| technical-simplified | 1988.0 ± 0.0 | -126.65 ± 563.696 |

Probe: 2026-08-10T08:46:45+00:00, model sonnet, repeats 3.

## Harness spend

A stored call row holds the token counts of its call: the
uncached input, cache-write input, cache-read input, and
output tokens. The cache-read share is the cache-read total
over the whole input total.

Calls: 18, measured: 18.
Input tokens: 36 uncached, 3087 cache write, 170772 cache read. Output tokens: 72.
Cache-read share: 0.982.
Cache writes by lifetime: 3087 at 5 minutes, 0 at 1 hour.

## Answer-length ratio

The ratio of a pair is the output-token count of the styled
answer divided by the output-token count of the unstyled answer
of the same prompt. A ratio below 1 means a shorter styled
answer.

### clarity-flow

- Pairs: 32
- Output tokens: styled 25177, unstyled 30301, ratio of totals 0.83

| n | min | p25 | median | p75 | max | mean |
|---|---|---|---|---|---|---|
| 32 | 0.21 | 0.64 | 0.84 | 1.27 | 2.49 | 0.93 |

| Task type | n | min | median | mean | max |
|---|---|---|---|---|---|
| code-review | 8 | 0.55 | 0.94 | 1.03 | 1.66 |
| debugging | 8 | 0.21 | 0.69 | 0.86 | 2.49 |
| explanation | 8 | 0.37 | 0.8 | 0.77 | 1.28 |
| summarization | 8 | 0.64 | 1.06 | 1.04 | 1.41 |

### classic-concise

- Pairs: 32
- Output tokens: styled 18795, unstyled 30301, ratio of totals 0.62

| n | min | p25 | median | p75 | max | mean |
|---|---|---|---|---|---|---|
| 32 | 0.23 | 0.55 | 0.68 | 0.88 | 3.52 | 0.79 |

| Task type | n | min | median | mean | max |
|---|---|---|---|---|---|
| code-review | 8 | 0.23 | 0.63 | 0.62 | 0.94 |
| debugging | 8 | 0.43 | 0.77 | 1.03 | 3.52 |
| explanation | 8 | 0.39 | 0.63 | 0.65 | 0.97 |
| summarization | 8 | 0.58 | 0.74 | 0.86 | 1.37 |

### developer-docs

- Pairs: 32
- Output tokens: styled 27369, unstyled 30301, ratio of totals 0.9

| n | min | p25 | median | p75 | max | mean |
|---|---|---|---|---|---|---|
| 32 | 0.42 | 0.78 | 1.02 | 1.28 | 4.57 | 1.13 |

| Task type | n | min | median | mean | max |
|---|---|---|---|---|---|
| code-review | 8 | 0.42 | 0.98 | 0.95 | 1.53 |
| debugging | 8 | 0.44 | 1.18 | 1.49 | 4.57 |
| explanation | 8 | 0.6 | 1.02 | 1.0 | 1.49 |
| summarization | 8 | 0.82 | 1.02 | 1.09 | 1.81 |

### plain-language

- Pairs: 32
- Output tokens: styled 25699, unstyled 30301, ratio of totals 0.85

| n | min | p25 | median | p75 | max | mean |
|---|---|---|---|---|---|---|
| 32 | 0.28 | 0.72 | 1.02 | 1.42 | 2.7 | 1.1 |

| Task type | n | min | median | mean | max |
|---|---|---|---|---|---|
| code-review | 8 | 0.28 | 1.06 | 0.97 | 1.78 |
| debugging | 8 | 0.51 | 1.18 | 1.38 | 2.7 |
| explanation | 8 | 0.54 | 0.92 | 0.99 | 1.6 |
| summarization | 8 | 0.68 | 0.98 | 1.06 | 1.59 |

### technical-simplified

- Pairs: 32
- Output tokens: styled 29368, unstyled 30301, ratio of totals 0.97

| n | min | p25 | median | p75 | max | mean |
|---|---|---|---|---|---|---|
| 32 | 0.38 | 0.7 | 0.87 | 1.2 | 4.06 | 1.14 |

| Task type | n | min | median | mean | max |
|---|---|---|---|---|---|
| code-review | 8 | 0.45 | 0.93 | 0.92 | 1.24 |
| debugging | 8 | 0.38 | 1.06 | 1.53 | 4.06 |
| explanation | 8 | 0.46 | 0.74 | 0.78 | 1.46 |
| summarization | 8 | 0.47 | 1.1 | 1.31 | 3.03 |

## Reading the ratio

A lower ratio is not by itself a win: fewer tokens with less content is a loss. Issue #7 measures whether the content survives.

## Warnings

- none

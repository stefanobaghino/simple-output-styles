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
| actionable-clarity | 2061.0 ± 0.0 | 3626.583 ± 7172.818 |
| clarity-flow | 1238.0 ± 0.0 | 450.783 ± 1913.396 |
| classic-concise | 1302.0 ± 0.0 | 481.717 ± 1952.997 |
| developer-docs | 1241.0 ± 0.0 | 452.233 ± 1915.249 |
| plain-language | 1460.0 ± 0.0 | 558.083 ± 2051.258 |
| technical-simplified | 1988.0 ± 0.0 | 813.283 ± 2383.735 |

Probe: 2026-08-10T14:50:34+00:00, model sonnet, repeats 3.

## Harness spend

A stored call row holds the token counts of its call: the
uncached input, cache-write input, cache-read input, and
output tokens. The cache-read share is the cache-read total
over the whole input total.

Calls: 21, measured: 21.
Input tokens: 42 uncached, 25350 cache write, 179991 cache read. Output tokens: 84.
Cache-read share: 0.876.
Cache writes by lifetime: 25350 at 5 minutes, 0 at 1 hour.

## Answer-length ratio

The ratio of a pair is the output-token count of the styled
answer divided by the output-token count of the unstyled answer
of the same prompt. A ratio below 1 means a shorter styled
answer.

### actionable-clarity

- Pairs: 24
- Output tokens: styled 20009, unstyled 25367, ratio of totals 0.79

| n | min | p25 | median | p75 | max | mean |
|---|---|---|---|---|---|---|
| 24 | 0.12 | 0.74 | 0.98 | 1.35 | 18.57 | 1.88 |

| Task type | n | min | median | mean | max |
|---|---|---|---|---|---|
| code-review | 6 | 0.12 | 0.68 | 3.53 | 18.57 |
| debugging | 6 | 0.46 | 1.22 | 1.16 | 1.74 |
| explanation | 6 | 0.74 | 1.01 | 1.05 | 1.35 |
| summarization | 6 | 0.7 | 1.0 | 1.79 | 4.35 |

### clarity-flow

- Pairs: 24
- Output tokens: styled 22966, unstyled 25367, ratio of totals 0.91

| n | min | p25 | median | p75 | max | mean |
|---|---|---|---|---|---|---|
| 24 | 0.38 | 0.61 | 0.8 | 0.98 | 11.12 | 1.59 |

| Task type | n | min | median | mean | max |
|---|---|---|---|---|---|
| code-review | 6 | 0.38 | 0.84 | 2.43 | 11.12 |
| debugging | 6 | 0.56 | 0.74 | 2.14 | 9.21 |
| explanation | 6 | 0.56 | 0.65 | 0.73 | 1.04 |
| summarization | 6 | 0.58 | 0.97 | 1.07 | 1.97 |

### classic-concise

- Pairs: 24
- Output tokens: styled 18350, unstyled 25367, ratio of totals 0.72

| n | min | p25 | median | p75 | max | mean |
|---|---|---|---|---|---|---|
| 24 | 0.32 | 0.57 | 0.76 | 0.87 | 15.12 | 1.65 |

| Task type | n | min | median | mean | max |
|---|---|---|---|---|---|
| code-review | 6 | 0.32 | 0.58 | 2.97 | 15.12 |
| debugging | 6 | 0.33 | 0.71 | 1.65 | 6.78 |
| explanation | 6 | 0.62 | 0.74 | 0.75 | 0.89 |
| summarization | 6 | 0.57 | 0.88 | 1.22 | 3.21 |

### developer-docs

- Pairs: 24
- Output tokens: styled 23313, unstyled 25367, ratio of totals 0.92

| n | min | p25 | median | p75 | max | mean |
|---|---|---|---|---|---|---|
| 24 | 0.06 | 0.75 | 0.97 | 1.14 | 11.63 | 1.6 |

| Task type | n | min | median | mean | max |
|---|---|---|---|---|---|
| code-review | 6 | 0.06 | 0.94 | 1.52 | 5.47 |
| debugging | 6 | 0.33 | 1.14 | 2.7 | 11.63 |
| explanation | 6 | 0.67 | 0.91 | 1.02 | 1.9 |
| summarization | 6 | 0.61 | 0.98 | 1.14 | 2.39 |

### plain-language

- Pairs: 24
- Output tokens: styled 19415, unstyled 25367, ratio of totals 0.77

| n | min | p25 | median | p75 | max | mean |
|---|---|---|---|---|---|---|
| 24 | 0.05 | 0.84 | 1.03 | 1.45 | 22.37 | 2.31 |

| Task type | n | min | median | mean | max |
|---|---|---|---|---|---|
| code-review | 6 | 0.05 | 0.91 | 4.3 | 22.37 |
| debugging | 6 | 0.09 | 1.49 | 2.52 | 9.08 |
| explanation | 6 | 0.73 | 0.99 | 0.93 | 1.05 |
| summarization | 6 | 0.73 | 1.02 | 1.5 | 3.96 |

### technical-simplified

- Pairs: 24
- Output tokens: styled 37674, unstyled 25367, ratio of totals 1.49

| n | min | p25 | median | p75 | max | mean |
|---|---|---|---|---|---|---|
| 24 | 0.09 | 0.8 | 0.99 | 1.43 | 24.53 | 2.9 |

| Task type | n | min | median | mean | max |
|---|---|---|---|---|---|
| code-review | 6 | 0.43 | 1.26 | 2.65 | 10.53 |
| debugging | 6 | 0.87 | 1.09 | 4.97 | 24.53 |
| explanation | 6 | 0.53 | 0.81 | 0.81 | 1.07 |
| summarization | 6 | 0.09 | 1.2 | 3.15 | 10.55 |

## Reading the ratio

A lower ratio is not by itself a win: fewer tokens with less content is a loss. Issue #7 measures whether the content survives.

## Warnings

- none

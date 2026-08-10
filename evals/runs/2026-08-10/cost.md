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
| clarity-flow | 1238.0 ± 0.0 | 3553.1 ± 6314.847 |
| classic-concise | 1302.0 ± 0.0 | 806.017 ± 1556.874 |
| developer-docs | 1241.0 ± 0.0 | 776.533 ± 1516.769 |
| plain-language | 1460.0 ± 0.0 | 882.383 ± 1660.841 |
| technical-simplified | 1988.0 ± 0.0 | 1137.583 ± 2008.983 |

Probe: 2026-08-10T08:46:35+00:00, model sonnet, repeats 3.

## Harness spend

A stored call row holds the token counts of its call: the
uncached input, cache-write input, cache-read input, and
output tokens. The cache-read share is the cache-read total
over the whole input total.

Calls: 18, measured: 18.
Input tokens: 36 uncached, 21257 cache write, 152602 cache read. Output tokens: 72.
Cache-read share: 0.878.
Cache writes by lifetime: 21257 at 5 minutes, 0 at 1 hour.

## Answer-length ratio

The ratio of a pair is the output-token count of the styled
answer divided by the output-token count of the unstyled answer
of the same prompt. A ratio below 1 means a shorter styled
answer.

### clarity-flow

- Pairs: 32
- Output tokens: styled 24797, unstyled 26634, ratio of totals 0.93

| n | min | p25 | median | p75 | max | mean |
|---|---|---|---|---|---|---|
| 32 | 0.28 | 0.62 | 0.74 | 1.18 | 27.29 | 2.05 |

| Task type | n | min | median | mean | max |
|---|---|---|---|---|---|
| code-review | 8 | 0.28 | 0.7 | 0.87 | 1.96 |
| debugging | 8 | 0.46 | 0.76 | 5.41 | 27.29 |
| explanation | 8 | 0.35 | 0.68 | 0.71 | 1.2 |
| summarization | 8 | 0.62 | 1.09 | 1.2 | 2.74 |

### classic-concise

- Pairs: 32
- Output tokens: styled 22301, unstyled 26634, ratio of totals 0.84

| n | min | p25 | median | p75 | max | mean |
|---|---|---|---|---|---|---|
| 32 | 0.31 | 0.54 | 0.71 | 0.94 | 18.24 | 1.6 |

| Task type | n | min | median | mean | max |
|---|---|---|---|---|---|
| code-review | 8 | 0.31 | 0.67 | 0.69 | 1.08 |
| debugging | 8 | 0.53 | 0.79 | 4.23 | 18.24 |
| explanation | 8 | 0.37 | 0.64 | 0.68 | 1.06 |
| summarization | 8 | 0.54 | 0.78 | 0.8 | 1.14 |

### developer-docs

- Pairs: 32
- Output tokens: styled 32038, unstyled 26634, ratio of totals 1.2

| n | min | p25 | median | p75 | max | mean |
|---|---|---|---|---|---|---|
| 32 | 0.43 | 0.75 | 1.05 | 1.39 | 31.37 | 2.65 |

| Task type | n | min | median | mean | max |
|---|---|---|---|---|---|
| code-review | 8 | 0.43 | 0.88 | 0.91 | 1.44 |
| debugging | 8 | 0.72 | 1.1 | 7.41 | 31.37 |
| explanation | 8 | 0.71 | 0.97 | 1.11 | 2.13 |
| summarization | 8 | 0.76 | 1.14 | 1.19 | 1.72 |

### plain-language

- Pairs: 32
- Output tokens: styled 22455, unstyled 26634, ratio of totals 0.84

| n | min | p25 | median | p75 | max | mean |
|---|---|---|---|---|---|---|
| 32 | 0.05 | 0.74 | 1.03 | 1.15 | 32.57 | 1.94 |

| Task type | n | min | median | mean | max |
|---|---|---|---|---|---|
| code-review | 8 | 0.05 | 0.68 | 0.76 | 2.03 |
| debugging | 8 | 0.76 | 1.14 | 5.17 | 32.57 |
| explanation | 8 | 0.08 | 0.79 | 0.8 | 1.48 |
| summarization | 8 | 0.8 | 1.09 | 1.05 | 1.26 |

### technical-simplified

- Pairs: 32
- Output tokens: styled 32873, unstyled 26634, ratio of totals 1.23

| n | min | p25 | median | p75 | max | mean |
|---|---|---|---|---|---|---|
| 32 | 0.08 | 0.8 | 1.05 | 2.07 | 38.84 | 2.88 |

| Task type | n | min | median | mean | max |
|---|---|---|---|---|---|
| code-review | 8 | 0.08 | 0.73 | 0.85 | 2.18 |
| debugging | 8 | 0.75 | 1.5 | 6.29 | 38.84 |
| explanation | 8 | 0.51 | 1.23 | 1.31 | 2.32 |
| summarization | 8 | 0.69 | 1.05 | 3.05 | 12.95 |

## Reading the ratio

A lower ratio is not by itself a win: fewer tokens with less content is a loss. Issue #7 measures whether the content survives.

## Warnings

- none

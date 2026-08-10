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
| actionable-clarity | 2061.0 ± 0.0 | -119.35 ± 563.696 |
| clarity-flow | 1238.0 ± 0.0 | -201.65 ± 563.696 |
| classic-concise | 1302.0 ± 0.0 | -195.25 ± 563.696 |
| developer-docs | 1241.0 ± 0.0 | -201.35 ± 563.696 |
| plain-language | 1460.0 ± 0.0 | -179.45 ± 563.696 |
| technical-simplified | 1988.0 ± 0.0 | -126.65 ± 563.696 |

Probe: 2026-08-10T13:55:52+00:00, model sonnet, repeats 3.

## Harness spend

A stored call row holds the token counts of its call: the
uncached input, cache-write input, cache-read input, and
output tokens. The cache-read share is the cache-read total
over the whole input total.

Calls: 6, measured: 6.
Input tokens: 12 uncached, 1587 cache write, 55296 cache read. Output tokens: 24.
Cache-read share: 0.972.
Cache writes by lifetime: 1587 at 5 minutes, 0 at 1 hour.

## Reuse

Reused probe arms: 18, imported from 2026-08-10c (probe of 2026-08-10T08:46:43+00:00).
Live probe arms of this run: 6.
Imported styles: clarity-flow, classic-concise, developer-docs, plain-language, technical-simplified.

The probe arms carry no freshness sample: they are token
measurements, not judge scores.

## Answer-length ratio

The ratio of a pair is the output-token count of the styled
answer divided by the output-token count of the unstyled answer
of the same prompt. A ratio below 1 means a shorter styled
answer.

### actionable-clarity

- Pairs: 32
- Output tokens: styled 34507, unstyled 34438, ratio of totals 1.0

| n | min | p25 | median | p75 | max | mean |
|---|---|---|---|---|---|---|
| 32 | 0.4 | 0.84 | 1.07 | 1.31 | 12.67 | 1.78 |

| Task type | n | min | median | mean | max |
|---|---|---|---|---|---|
| code-review | 8 | 0.81 | 1.21 | 2.59 | 12.67 |
| debugging | 8 | 0.4 | 0.88 | 0.89 | 1.2 |
| explanation | 8 | 0.6 | 1.22 | 1.33 | 3.27 |
| summarization | 8 | 0.64 | 1.08 | 2.32 | 10.84 |

### clarity-flow

- Pairs: 32
- Output tokens: styled 28155, unstyled 34438, ratio of totals 0.82

| n | min | p25 | median | p75 | max | mean |
|---|---|---|---|---|---|---|
| 32 | 0.15 | 0.71 | 0.87 | 1.17 | 14.63 | 1.67 |

| Task type | n | min | median | mean | max |
|---|---|---|---|---|---|
| code-review | 8 | 0.72 | 0.9 | 2.65 | 14.63 |
| debugging | 8 | 0.15 | 0.57 | 0.92 | 3.79 |
| explanation | 8 | 0.7 | 0.82 | 0.99 | 1.87 |
| summarization | 8 | 0.67 | 1.07 | 2.13 | 9.6 |

### classic-concise

- Pairs: 32
- Output tokens: styled 22889, unstyled 34438, ratio of totals 0.66

| n | min | p25 | median | p75 | max | mean |
|---|---|---|---|---|---|---|
| 32 | 0.26 | 0.5 | 0.63 | 0.79 | 12.6 | 1.22 |

| Task type | n | min | median | mean | max |
|---|---|---|---|---|---|
| code-review | 8 | 0.43 | 0.64 | 2.14 | 12.6 |
| debugging | 8 | 0.26 | 0.48 | 0.47 | 0.74 |
| explanation | 8 | 0.48 | 0.67 | 0.82 | 1.83 |
| summarization | 8 | 0.37 | 0.79 | 1.43 | 6.44 |

### developer-docs

- Pairs: 32
- Output tokens: styled 25983, unstyled 34438, ratio of totals 0.75

| n | min | p25 | median | p75 | max | mean |
|---|---|---|---|---|---|---|
| 32 | 0.08 | 0.7 | 0.98 | 1.22 | 11.6 | 1.4 |

| Task type | n | min | median | mean | max |
|---|---|---|---|---|---|
| code-review | 8 | 0.52 | 0.97 | 1.39 | 4.46 |
| debugging | 8 | 0.08 | 0.75 | 0.65 | 1.07 |
| explanation | 8 | 0.66 | 1.01 | 1.15 | 2.67 |
| summarization | 8 | 0.56 | 1.18 | 2.4 | 11.6 |

### plain-language

- Pairs: 32
- Output tokens: styled 24045, unstyled 34438, ratio of totals 0.7

| n | min | p25 | median | p75 | max | mean |
|---|---|---|---|---|---|---|
| 32 | 0.03 | 0.73 | 1.02 | 1.26 | 10.52 | 1.29 |

| Task type | n | min | median | mean | max |
|---|---|---|---|---|---|
| code-review | 8 | 0.08 | 0.79 | 0.76 | 1.26 |
| debugging | 8 | 0.03 | 0.84 | 0.99 | 2.01 |
| explanation | 8 | 0.64 | 1.1 | 1.17 | 2.1 |
| summarization | 8 | 0.45 | 1.06 | 2.23 | 10.52 |

### technical-simplified

- Pairs: 32
- Output tokens: styled 29233, unstyled 34438, ratio of totals 0.85

| n | min | p25 | median | p75 | max | mean |
|---|---|---|---|---|---|---|
| 32 | 0.16 | 0.8 | 0.94 | 1.28 | 15.22 | 1.75 |

| Task type | n | min | median | mean | max |
|---|---|---|---|---|---|
| code-review | 8 | 0.51 | 1.11 | 2.81 | 15.22 |
| debugging | 8 | 0.16 | 0.76 | 0.78 | 1.54 |
| explanation | 8 | 0.53 | 0.82 | 1.0 | 2.35 |
| summarization | 8 | 0.8 | 1.29 | 2.41 | 10.4 |

## Reading the ratio

A lower ratio is not by itself a win: fewer tokens with less content is a loss. Issue #7 measures whether the content survives.

## Warnings

- none

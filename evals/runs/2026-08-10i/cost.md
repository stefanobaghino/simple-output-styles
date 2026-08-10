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
| clarity-flow | 1238.0 ± 0.0 | 123.8 ± 0.0 |
| classic-concise | 1302.0 ± 0.0 | 130.2 ± 0.0 |
| developer-docs | 1241.0 ± 0.0 | 124.1 ± 0.0 |
| plain-language | 1460.0 ± 0.0 | 146.0 ± 0.0 |
| technical-simplified | 1988.0 ± 0.0 | 198.8 ± 0.0 |

Probe: 2026-08-10T16:41:27+00:00, model sonnet, repeats 3.

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

Reused probe arms: 18, imported from 2026-08-08b (probe of 2026-08-08T20:39:52+00:00).
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
- Output tokens: styled 40513, unstyled 33676, ratio of totals 1.2

| n | min | p25 | median | p75 | max | mean |
|---|---|---|---|---|---|---|
| 32 | 0.68 | 0.95 | 1.16 | 1.41 | 2.6 | 1.27 |

| Task type | n | min | median | mean | max |
|---|---|---|---|---|---|
| code-review | 8 | 0.84 | 1.32 | 1.4 | 2.33 |
| debugging | 8 | 0.78 | 1.09 | 1.13 | 1.51 |
| explanation | 8 | 0.68 | 0.97 | 1.18 | 2.6 |
| summarization | 8 | 0.8 | 1.24 | 1.37 | 2.44 |

### clarity-flow

- Pairs: 32
- Output tokens: styled 29022, unstyled 33676, ratio of totals 0.86

| n | min | p25 | median | p75 | max | mean |
|---|---|---|---|---|---|---|
| 32 | 0.33 | 0.67 | 0.8 | 1.0 | 1.94 | 0.88 |

| Task type | n | min | median | mean | max |
|---|---|---|---|---|---|
| code-review | 8 | 0.55 | 0.85 | 1.03 | 1.94 |
| debugging | 8 | 0.33 | 0.78 | 0.74 | 1.07 |
| explanation | 8 | 0.42 | 0.72 | 0.8 | 1.23 |
| summarization | 8 | 0.57 | 0.86 | 0.95 | 1.51 |

### classic-concise

- Pairs: 32
- Output tokens: styled 20436, unstyled 33676, ratio of totals 0.61

| n | min | p25 | median | p75 | max | mean |
|---|---|---|---|---|---|---|
| 32 | 0.23 | 0.52 | 0.69 | 0.8 | 1.74 | 0.68 |

| Task type | n | min | median | mean | max |
|---|---|---|---|---|---|
| code-review | 8 | 0.38 | 0.56 | 0.71 | 1.74 |
| debugging | 8 | 0.23 | 0.41 | 0.49 | 0.86 |
| explanation | 8 | 0.44 | 0.75 | 0.75 | 1.02 |
| summarization | 8 | 0.57 | 0.76 | 0.76 | 0.91 |

### developer-docs

- Pairs: 32
- Output tokens: styled 32155, unstyled 33676, ratio of totals 0.95

| n | min | p25 | median | p75 | max | mean |
|---|---|---|---|---|---|---|
| 32 | 0.07 | 0.81 | 0.96 | 1.09 | 3.0 | 1.0 |

| Task type | n | min | median | mean | max |
|---|---|---|---|---|---|
| code-review | 8 | 0.83 | 1.01 | 1.25 | 3.0 |
| debugging | 8 | 0.35 | 0.85 | 0.83 | 1.36 |
| explanation | 8 | 0.07 | 0.94 | 0.81 | 1.15 |
| summarization | 8 | 0.73 | 0.94 | 1.08 | 1.71 |

### plain-language

- Pairs: 32
- Output tokens: styled 31966, unstyled 33676, ratio of totals 0.95

| n | min | p25 | median | p75 | max | mean |
|---|---|---|---|---|---|---|
| 32 | 0.29 | 0.83 | 0.99 | 1.25 | 2.2 | 1.05 |

| Task type | n | min | median | mean | max |
|---|---|---|---|---|---|
| code-review | 8 | 0.33 | 0.95 | 1.06 | 2.2 |
| debugging | 8 | 0.29 | 1.07 | 0.95 | 1.59 |
| explanation | 8 | 0.51 | 0.94 | 1.01 | 1.61 |
| summarization | 8 | 0.77 | 1.06 | 1.19 | 1.86 |

### technical-simplified

- Pairs: 32
- Output tokens: styled 23762, unstyled 33676, ratio of totals 0.71

| n | min | p25 | median | p75 | max | mean |
|---|---|---|---|---|---|---|
| 32 | 0.09 | 0.69 | 0.83 | 1.02 | 3.18 | 0.97 |

| Task type | n | min | median | mean | max |
|---|---|---|---|---|---|
| code-review | 8 | 0.19 | 0.71 | 0.65 | 0.96 |
| debugging | 8 | 0.09 | 0.91 | 0.82 | 1.79 |
| explanation | 8 | 0.44 | 0.82 | 0.91 | 1.91 |
| summarization | 8 | 0.72 | 1.37 | 1.5 | 3.18 |

## Reading the ratio

A lower ratio is not by itself a win: fewer tokens with less content is a loss. Issue #7 measures whether the content survives.

## Warnings

- none

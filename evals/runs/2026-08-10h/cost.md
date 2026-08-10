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
| actionable-clarity | 2061.0 ± 0.0 | 206.1 ± 0.0 |
| clarity-flow | 1238.0 ± 0.0 | 3370.633 ± 5623.68 |
| classic-concise | 1302.0 ± 0.0 | 623.55 ± 854.507 |
| developer-docs | 1241.0 ± 0.0 | 594.067 ± 814.006 |
| plain-language | 1460.0 ± 0.0 | 699.917 ± 959.412 |
| technical-simplified | 1988.0 ± 0.0 | 955.117 ± 1309.979 |

Probe: 2026-08-10T16:33:26+00:00, model sonnet, repeats 3.

## Harness spend

A stored call row holds the token counts of its call: the
uncached input, cache-write input, cache-read input, and
output tokens. The cache-read share is the cache-read total
over the whole input total.

Calls: 6, measured: 6.
Input tokens: 12 uncached, 742 cache write, 56153 cache read. Output tokens: 24.
Cache-read share: 0.987.
Cache writes by lifetime: 742 at 5 minutes, 0 at 1 hour.

## Reuse

Reused probe arms: 18, imported from 2026-08-08 (probe of 2026-08-08T20:39:50+00:00).
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
- Output tokens: styled 33883, unstyled 33620, ratio of totals 1.01

| n | min | p25 | median | p75 | max | mean |
|---|---|---|---|---|---|---|
| 32 | 0.27 | 0.89 | 1.02 | 1.27 | 3.17 | 1.17 |

| Task type | n | min | median | mean | max |
|---|---|---|---|---|---|
| code-review | 8 | 0.76 | 1.01 | 1.17 | 2.04 |
| debugging | 8 | 0.27 | 1.1 | 1.11 | 2.16 |
| explanation | 8 | 0.58 | 1.09 | 1.41 | 3.17 |
| summarization | 8 | 0.72 | 1.03 | 1.0 | 1.12 |

### clarity-flow

- Pairs: 32
- Output tokens: styled 20021, unstyled 33620, ratio of totals 0.6

| n | min | p25 | median | p75 | max | mean |
|---|---|---|---|---|---|---|
| 32 | 0.24 | 0.54 | 0.79 | 1.0 | 1.71 | 0.83 |

| Task type | n | min | median | mean | max |
|---|---|---|---|---|---|
| code-review | 8 | 0.32 | 0.67 | 0.69 | 1.39 |
| debugging | 8 | 0.24 | 0.94 | 0.76 | 1.37 |
| explanation | 8 | 0.47 | 0.68 | 0.89 | 1.71 |
| summarization | 8 | 0.71 | 0.87 | 0.98 | 1.5 |

### classic-concise

- Pairs: 32
- Output tokens: styled 23123, unstyled 33620, ratio of totals 0.69

| n | min | p25 | median | p75 | max | mean |
|---|---|---|---|---|---|---|
| 32 | 0.33 | 0.57 | 0.71 | 0.88 | 1.58 | 0.75 |

| Task type | n | min | median | mean | max |
|---|---|---|---|---|---|
| code-review | 8 | 0.39 | 0.78 | 0.76 | 1.13 |
| debugging | 8 | 0.33 | 0.62 | 0.69 | 1.02 |
| explanation | 8 | 0.41 | 0.68 | 0.79 | 1.58 |
| summarization | 8 | 0.6 | 0.73 | 0.75 | 1.02 |

### developer-docs

- Pairs: 32
- Output tokens: styled 30965, unstyled 33620, ratio of totals 0.92

| n | min | p25 | median | p75 | max | mean |
|---|---|---|---|---|---|---|
| 32 | 0.28 | 0.79 | 0.99 | 1.2 | 4.55 | 1.18 |

| Task type | n | min | median | mean | max |
|---|---|---|---|---|---|
| code-review | 8 | 0.37 | 1.04 | 1.06 | 2.09 |
| debugging | 8 | 0.28 | 0.87 | 1.09 | 2.76 |
| explanation | 8 | 0.75 | 0.96 | 1.55 | 4.55 |
| summarization | 8 | 0.78 | 1.07 | 1.03 | 1.2 |

### plain-language

- Pairs: 32
- Output tokens: styled 27687, unstyled 33620, ratio of totals 0.82

| n | min | p25 | median | p75 | max | mean |
|---|---|---|---|---|---|---|
| 32 | 0.05 | 0.62 | 1.0 | 1.31 | 3.37 | 1.07 |

| Task type | n | min | median | mean | max |
|---|---|---|---|---|---|
| code-review | 8 | 0.31 | 0.49 | 0.68 | 1.17 |
| debugging | 8 | 0.42 | 1.07 | 1.15 | 2.03 |
| explanation | 8 | 0.05 | 0.91 | 1.25 | 3.37 |
| summarization | 8 | 0.77 | 1.2 | 1.21 | 2.14 |

### technical-simplified

- Pairs: 32
- Output tokens: styled 36702, unstyled 33620, ratio of totals 1.09

| n | min | p25 | median | p75 | max | mean |
|---|---|---|---|---|---|---|
| 32 | 0.26 | 0.75 | 0.95 | 1.37 | 2.79 | 1.17 |

| Task type | n | min | median | mean | max |
|---|---|---|---|---|---|
| code-review | 8 | 0.65 | 1.01 | 1.11 | 1.79 |
| debugging | 8 | 0.26 | 1.02 | 1.06 | 2.08 |
| explanation | 8 | 0.55 | 0.86 | 1.37 | 2.79 |
| summarization | 8 | 0.78 | 0.94 | 1.14 | 2.63 |

## Reading the ratio

A lower ratio is not by itself a win: fewer tokens with less content is a loss. Issue #7 measures whether the content survives.

## Warnings

- none

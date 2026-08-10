# Token cost report

**Screening run.** This run covers 8 of 32 prompts, as one
run instead of 3. By design, the generation calls are about
8% of a full campaign, and the judge calls are about 25%
of one full run.
The subset holds 2 hedge-rich prompts, mirroring the
hedge-rich share of the full set.
Measured against the baseline campaign
(runs/2026-08-08 and runs/2026-08-08b), a screening run holds about
25% of the calls and about 25% of the
weighted input tokens of one full run, plus the full cost
probe, which is per style and does not shrink.
The error bars are wider than in a full run,
because fewer contests feed the bootstrap intervals.
`style-compare` rejects a comparison of this run with a full run.

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
| clarity-flow | 1237.0 ± 0.0 | 917.583 ± 1375.046 |
| classic-concise | 1301.0 ± 0.0 | 948.517 ± 1417.539 |
| developer-docs | 1240.0 ± 0.0 | 919.033 ± 1377.038 |
| plain-language | 1459.0 ± 0.0 | 1024.883 ± 1522.444 |
| technical-simplified | 1987.0 ± 0.0 | 1280.083 ± 1873.011 |

Probe: 2026-08-10T11:14:17+00:00, model sonnet, repeats 3.

## Harness spend

A stored call row holds the token counts of its call: the
uncached input, cache-write input, cache-read input, and
output tokens. The cache-read share is the cache-read total
over the whole input total.

Calls: 6, measured: 6.
Input tokens: 12 uncached, 1599 cache write, 55320 cache read. Output tokens: 24.
Cache-read share: 0.972.
Cache writes by lifetime: 1599 at 5 minutes, 0 at 1 hour.

## Reuse

Reused probe arms: 21, imported from 2026-08-10b-screening (probe of 2026-08-10T11:08:03+00:00).
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

- Pairs: 8
- Output tokens: styled 5751, unstyled 6172, ratio of totals 0.93

| n | min | p25 | median | p75 | max | mean |
|---|---|---|---|---|---|---|
| 8 | 0.8 | 0.88 | 0.92 | 1.03 | 1.28 | 0.97 |

| Task type | n | min | median | mean | max |
|---|---|---|---|---|---|
| code-review | 2 | 1.1 | 1.19 | 1.19 | 1.28 |
| debugging | 2 | 0.8 | 0.86 | 0.86 | 0.92 |
| explanation | 2 | 0.84 | 0.92 | 0.92 | 1.0 |
| summarization | 2 | 0.9 | 0.91 | 0.91 | 0.91 |

### clarity-flow

- Pairs: 8
- Output tokens: styled 4031, unstyled 6172, ratio of totals 0.65

| n | min | p25 | median | p75 | max | mean |
|---|---|---|---|---|---|---|
| 8 | 0.45 | 0.7 | 0.79 | 0.82 | 1.11 | 0.76 |

| Task type | n | min | median | mean | max |
|---|---|---|---|---|---|
| code-review | 2 | 0.82 | 0.82 | 0.82 | 0.82 |
| debugging | 2 | 0.45 | 0.62 | 0.62 | 0.79 |
| explanation | 2 | 0.5 | 0.64 | 0.64 | 0.77 |
| summarization | 2 | 0.78 | 0.95 | 0.95 | 1.11 |

### classic-concise

- Pairs: 8
- Output tokens: styled 5104, unstyled 6172, ratio of totals 0.83

| n | min | p25 | median | p75 | max | mean |
|---|---|---|---|---|---|---|
| 8 | 0.55 | 0.58 | 0.64 | 0.76 | 1.22 | 0.74 |

| Task type | n | min | median | mean | max |
|---|---|---|---|---|---|
| code-review | 2 | 0.64 | 0.66 | 0.66 | 0.69 |
| debugging | 2 | 0.57 | 0.89 | 0.89 | 1.22 |
| explanation | 2 | 0.55 | 0.6 | 0.6 | 0.64 |
| summarization | 2 | 0.59 | 0.79 | 0.79 | 0.98 |

### developer-docs

- Pairs: 8
- Output tokens: styled 4596, unstyled 6172, ratio of totals 0.74

| n | min | p25 | median | p75 | max | mean |
|---|---|---|---|---|---|---|
| 8 | 0.11 | 0.79 | 0.95 | 1.05 | 1.66 | 0.92 |

| Task type | n | min | median | mean | max |
|---|---|---|---|---|---|
| code-review | 2 | 1.07 | 1.37 | 1.37 | 1.66 |
| debugging | 2 | 0.11 | 0.46 | 0.46 | 0.81 |
| explanation | 2 | 0.89 | 0.97 | 0.97 | 1.05 |
| summarization | 2 | 0.74 | 0.87 | 0.87 | 1.0 |

### plain-language

- Pairs: 8
- Output tokens: styled 7043, unstyled 6172, ratio of totals 1.14

| n | min | p25 | median | p75 | max | mean |
|---|---|---|---|---|---|---|
| 8 | 0.72 | 0.82 | 0.98 | 1.04 | 1.66 | 1.01 |

| Task type | n | min | median | mean | max |
|---|---|---|---|---|---|
| code-review | 2 | 0.95 | 0.98 | 0.98 | 1.02 |
| debugging | 2 | 1.0 | 1.33 | 1.33 | 1.66 |
| explanation | 2 | 0.72 | 0.78 | 0.78 | 0.85 |
| summarization | 2 | 0.75 | 0.92 | 0.92 | 1.1 |

### technical-simplified

- Pairs: 8
- Output tokens: styled 3756, unstyled 6172, ratio of totals 0.61

| n | min | p25 | median | p75 | max | mean |
|---|---|---|---|---|---|---|
| 8 | 0.19 | 0.65 | 0.81 | 0.9 | 1.23 | 0.77 |

| Task type | n | min | median | mean | max |
|---|---|---|---|---|---|
| code-review | 2 | 0.48 | 0.66 | 0.66 | 0.84 |
| debugging | 2 | 0.19 | 0.52 | 0.52 | 0.85 |
| explanation | 2 | 0.7 | 0.89 | 0.89 | 1.08 |
| summarization | 2 | 0.78 | 1.0 | 1.0 | 1.23 |

## Reading the ratio

A lower ratio is not by itself a win: fewer tokens with less content is a loss. Issue #7 measures whether the content survives.

## Warnings

- the unstyled input total moved between the probe repeats of 2026-08-10b-screening: 8454, 8454, 8454, 8455, 8455, 8455; each overhead uses the unstyled arm of its own origin and repeat

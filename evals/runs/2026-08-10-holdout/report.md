# Run report

- Date: 2026-08-10T14:32:44+00:00
- Model requested: sonnet
- Prompts: 24
- Styles: actionable-clarity, clarity-flow, classic-concise, developer-docs, plain-language, technical-simplified

## Completeness

| Arm | Answers | Missing |
|---|---|---|
| unstyled | 24/24 | none |
| actionable-clarity | 24/24 | none |
| clarity-flow | 24/24 | none |
| classic-concise | 24/24 | none |
| developer-docs | 24/24 | none |
| plain-language | 24/24 | none |
| technical-simplified | 24/24 | none |

## Volume

| Arm | Output tokens | Mean words per answer |
|---|---|---|
| unstyled | 25367 | 238 |
| actionable-clarity | 20009 | 294 |
| clarity-flow | 22966 | 228 |
| classic-concise | 18350 | 214 |
| developer-docs | 23313 | 239 |
| plain-language | 19415 | 270 |
| technical-simplified | 37674 | 241 |

## Call timing

A stored call row holds two times: duration_ms is the model
time that the CLI reports, and wall_ms is the wall clock of
the subprocess. The difference is the startup cost of one CLI
call.

Calls: 168, measured: 168.
Mean duration: 12872 ms. Mean wall: 14248 ms. Mean startup: 1375 ms.

## Harness spend

A stored call row holds the token counts of its call: the
uncached input, cache-write input, cache-read input, and
output tokens. The cache-read share is the cache-read total
over the whole input total.

Calls: 168, measured: 168.
Input tokens: 168 uncached, 138677 cache write, 1527214 cache read. Output tokens: 167094.
Cache-read share: 0.917.
Cache writes by lifetime: 138677 at 5 minutes, 0 at 1 hour.

## Environment

- Claude Code versions observed: 2.1.226
- Models observed: claude-haiku-4-5-20251001, claude-sonnet-5
- Plugin sets observed:
  - none
  - simple-output-styles

## Warnings

- The answers come from more than one plugin environment.

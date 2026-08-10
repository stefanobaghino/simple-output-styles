# Run report

- Date: 2026-08-10T16:21:46+00:00
- Model requested: sonnet
- Prompts: 32
- Styles: actionable-clarity, clarity-flow, classic-concise, developer-docs, plain-language, technical-simplified
- Answers imported from 2026-08-07: 192 (generated live: 32)

## Completeness

| Arm | Answers | Missing |
|---|---|---|
| unstyled | 32/32 | none |
| actionable-clarity | 32/32 | none |
| clarity-flow | 32/32 | none |
| classic-concise | 32/32 | none |
| developer-docs | 32/32 | none |
| plain-language | 32/32 | none |
| technical-simplified | 32/32 | none |

## Volume

| Arm | Output tokens | Mean words per answer |
|---|---|---|
| unstyled | 27423 | 271 |
| actionable-clarity | 36321 | 299 |
| clarity-flow | 28483 | 182 |
| classic-concise | 24000 | 201 |
| developer-docs | 27959 | 234 |
| plain-language | 25389 | 256 |
| technical-simplified | 27391 | 194 |

## Call timing

A stored call row holds two times: duration_ms is the model
time that the CLI reports, and wall_ms is the wall clock of
the subprocess. The difference is the startup cost of one CLI
call.

Calls: 32, measured: 32.
Mean duration: 14166 ms. Mean wall: 17125 ms. Mean startup: 2959 ms.

## Harness spend

A stored call row holds the token counts of its call: the
uncached input, cache-write input, cache-read input, and
output tokens. The cache-read share is the cache-read total
over the whole input total.

Calls: 32, measured: 32.
Input tokens: 32 uncached, 16486 cache write, 324544 cache read. Output tokens: 36321.
Cache-read share: 0.952.
Cache writes by lifetime: 16486 at 5 minutes, 0 at 1 hour.

## Environment

- Claude Code versions observed: 2.1.224, 2.1.226
- Models observed: claude-haiku-4-5-20251001, claude-sonnet-5
- Plugin sets observed:
  - none
  - simple-output-styles

## Warnings

- The answers come from more than one Claude Code version.
- The answers come from more than one plugin environment.

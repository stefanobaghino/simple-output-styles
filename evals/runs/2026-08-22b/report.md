# Run report

- Date: 2026-08-22T13:52:26+00:00
- Model requested: sonnet
- Prompts: 32
- Styles: actionable-clarity, clarity-flow, classic-concise, concise, developer-docs, plain-language, technical-simplified

## Completeness

| Arm | Answers | Missing |
|---|---|---|
| unstyled | 32/32 | none |
| actionable-clarity | 32/32 | none |
| clarity-flow | 32/32 | none |
| classic-concise | 32/32 | none |
| concise | 32/32 | none |
| developer-docs | 32/32 | none |
| plain-language | 32/32 | none |
| technical-simplified | 32/32 | none |

## Volume

| Arm | Output tokens | Mean words per answer |
|---|---|---|
| unstyled | 30039 | 269 |
| actionable-clarity | 29331 | 284 |
| clarity-flow | 25250 | 205 |
| classic-concise | 15282 | 179 |
| concise | 16647 | 174 |
| developer-docs | 27759 | 255 |
| plain-language | 28648 | 265 |
| technical-simplified | 25138 | 206 |

## Call timing

A stored call row holds two times: duration_ms is the model
time that the CLI reports, and wall_ms is the wall clock of
the subprocess. The difference is the startup cost of one CLI
call.

Calls: 256, measured: 256.
Mean duration: 9950 ms. Mean wall: 20346 ms. Mean startup: 10396 ms.

## Harness spend

A stored call row holds the token counts of its call: the
uncached input, cache-write input, cache-read input, and
output tokens. The cache-read share is the cache-read total
over the whole input total.

Calls: 256, measured: 256.
Input tokens: 512 uncached, 178306 cache write, 2362446 cache read. Output tokens: 198094.
Cache-read share: 0.93.
Cache writes by lifetime: 178306 at 5 minutes, 0 at 1 hour.

## Environment

- Claude Code versions observed: 2.1.239
- Models observed: claude-haiku-4-5-20251001, claude-sonnet-5
- Plugin sets observed:
  - none
  - simple-output-styles

## Warnings

- The answers come from more than one plugin environment.

# Run report

- Date: 2026-08-08T11:40:57+00:00
- Model requested: sonnet
- Prompts: 32
- Styles: clarity-flow, classic-concise, developer-docs, plain-language, technical-simplified

## Completeness

| Arm | Answers | Missing |
|---|---|---|
| unstyled | 32/32 | none |
| clarity-flow | 32/32 | none |
| classic-concise | 32/32 | none |
| developer-docs | 32/32 | none |
| plain-language | 32/32 | none |
| technical-simplified | 32/32 | none |

## Volume

| Arm | Output tokens | Mean words per answer |
|---|---|---|
| unstyled | 33676 | 278 |
| clarity-flow | 29022 | 213 |
| classic-concise | 20436 | 189 |
| developer-docs | 32155 | 254 |
| plain-language | 31966 | 268 |
| technical-simplified | 23762 | 195 |

## Call timing

A stored call row holds two times: duration_ms is the model
time that the CLI reports, and wall_ms is the wall clock of
the subprocess. The difference is the startup cost of one CLI
call.

Calls: 192, measured: 192.
Mean duration: 11539 ms. Mean wall: 15876 ms. Mean startup: 4336 ms.

## Harness spend

A stored call row holds the token counts of its call: the
uncached input, cache-write input, cache-read input, and
output tokens. The cache-read share is the cache-read total
over the whole input total.

Calls: 192, measured: 192.
Input tokens: 192 uncached, 99492 cache write, 1782880 cache read. Output tokens: 171017.
Cache-read share: 0.947.

## Environment

- Claude Code versions observed: 2.1.224
- Models observed: claude-haiku-4-5-20251001, claude-sonnet-5
- Plugin sets observed:
  - none
  - simple-output-styles

## Warnings

- The answers come from more than one plugin environment.

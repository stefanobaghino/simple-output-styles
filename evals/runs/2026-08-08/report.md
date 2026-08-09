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
| unstyled | 33620 | 250 |
| clarity-flow | 20021 | 205 |
| classic-concise | 23123 | 180 |
| developer-docs | 30965 | 266 |
| plain-language | 27687 | 234 |
| technical-simplified | 36702 | 204 |

## Call timing

A stored call row holds two times: duration_ms is the model
time that the CLI reports, and wall_ms is the wall clock of
the subprocess. The difference is the startup cost of one CLI
call.

Calls: 192, measured: 192.
Mean duration: 11649 ms. Mean wall: 12555 ms. Mean startup: 905 ms.

## Harness spend

A stored call row holds the token counts of its call: the
uncached input, cache-write input, cache-read input, and
output tokens. The cache-read share is the cache-read total
over the whole input total.

Calls: 192, measured: 192.
Input tokens: 192 uncached, 117451 cache write, 1763385 cache read. Output tokens: 172118.
Cache-read share: 0.937.

## Environment

- Claude Code versions observed: 2.1.224
- Models observed: claude-haiku-4-5-20251001, claude-sonnet-5
- Plugin sets observed:
  - none
  - simple-output-styles

## Warnings

- The answers come from more than one plugin environment.

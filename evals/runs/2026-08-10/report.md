# Run report

- Date: 2026-08-10T08:20:22+00:00
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
| unstyled | 26634 | 247 |
| clarity-flow | 24797 | 193 |
| classic-concise | 22301 | 186 |
| developer-docs | 32038 | 263 |
| plain-language | 22455 | 194 |
| technical-simplified | 32873 | 204 |

## Call timing

A stored call row holds two times: duration_ms is the model
time that the CLI reports, and wall_ms is the wall clock of
the subprocess. The difference is the startup cost of one CLI
call.

Calls: 192, measured: 192.
Mean duration: 11060 ms. Mean wall: 12344 ms. Mean startup: 1284 ms.

## Harness spend

A stored call row holds the token counts of its call: the
uncached input, cache-write input, cache-read input, and
output tokens. The cache-read share is the cache-read total
over the whole input total.

Calls: 192, measured: 192.
Input tokens: 192 uncached, 150882 cache write, 1730722 cache read. Output tokens: 161098.
Cache-read share: 0.92.
Cache writes by lifetime: 150882 at 5 minutes, 0 at 1 hour.

## Environment

- Claude Code versions observed: 2.1.226
- Models observed: claude-haiku-4-5-20251001, claude-sonnet-5
- Plugin sets observed:
  - none
  - simple-output-styles

## Warnings

- The answers come from more than one plugin environment.

# Run report

- Date: 2026-08-22T13:52:27+00:00
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
| unstyled | 24149 | 240 |
| actionable-clarity | 29858 | 263 |
| clarity-flow | 21930 | 195 |
| classic-concise | 17763 | 177 |
| concise | 16010 | 178 |
| developer-docs | 22828 | 246 |
| plain-language | 22551 | 265 |
| technical-simplified | 27750 | 191 |

## Call timing

A stored call row holds two times: duration_ms is the model
time that the CLI reports, and wall_ms is the wall clock of
the subprocess. The difference is the startup cost of one CLI
call.

Calls: 256, measured: 256.
Mean duration: 9260 ms. Mean wall: 16542 ms. Mean startup: 7283 ms.

## Harness spend

A stored call row holds the token counts of its call: the
uncached input, cache-write input, cache-read input, and
output tokens. The cache-read share is the cache-read total
over the whole input total.

Calls: 256, measured: 256.
Input tokens: 512 uncached, 178050 cache write, 2362446 cache read. Output tokens: 182839.
Cache-read share: 0.93.
Cache writes by lifetime: 178050 at 5 minutes, 0 at 1 hour.

## Environment

- Claude Code versions observed: 2.1.239
- Models observed: claude-haiku-4-5-20251001, claude-sonnet-5
- Plugin sets observed:
  - none
  - simple-output-styles

## Warnings

- The answers come from more than one plugin environment.

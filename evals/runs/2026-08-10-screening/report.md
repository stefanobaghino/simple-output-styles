# Run report

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

- Date: 2026-08-10T10:54:38+00:00
- Model requested: sonnet
- Prompts: 8
- Styles: actionable-clarity, clarity-flow, classic-concise, developer-docs, plain-complete, plain-language, technical-simplified

## Completeness

| Arm | Answers | Missing |
|---|---|---|
| unstyled | 8/8 | none |
| actionable-clarity | 8/8 | none |
| clarity-flow | 8/8 | none |
| classic-concise | 8/8 | none |
| developer-docs | 8/8 | none |
| plain-complete | 8/8 | none |
| plain-language | 8/8 | none |
| technical-simplified | 8/8 | none |

## Volume

| Arm | Output tokens | Mean words per answer |
|---|---|---|
| unstyled | 6172 | 314 |
| actionable-clarity | 10773 | 382 |
| clarity-flow | 4031 | 192 |
| classic-concise | 5104 | 185 |
| developer-docs | 4596 | 206 |
| plain-complete | 6552 | 340 |
| plain-language | 7043 | 296 |
| technical-simplified | 3756 | 150 |

## Call timing

A stored call row holds two times: duration_ms is the model
time that the CLI reports, and wall_ms is the wall clock of
the subprocess. The difference is the startup cost of one CLI
call.

Calls: 64, measured: 64.
Mean duration: 9874 ms. Mean wall: 12136 ms. Mean startup: 2262 ms.

## Harness spend

A stored call row holds the token counts of its call: the
uncached input, cache-write input, cache-read input, and
output tokens. The cache-read share is the cache-read total
over the whole input total.

Calls: 64, measured: 64.
Input tokens: 64 uncached, 184855 cache write, 453145 cache read. Output tokens: 48027.
Cache-read share: 0.71.
Cache writes by lifetime: 184855 at 5 minutes, 0 at 1 hour.

## Environment

- Claude Code versions observed: 2.1.226
- Models observed: claude-haiku-4-5-20251001, claude-sonnet-5
- Plugin sets observed:
  - none
  - simple-output-styles

## Warnings

- The answers come from more than one plugin environment.

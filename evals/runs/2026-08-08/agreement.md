# Second-judge agreement report

Every stored verdict of a run comes from one judge model, and
the style-design loop optimizes against those verdicts. This
report re-runs stored discrete verdicts with a second judge
and states the agreement rate per axis, so a judge-sensitive
axis is visible before the loop optimizes against it.

How to read the arms: a cross-line arm (a weaker Claude line)
is a lower bound, because its disagreement mixes genuine
ambiguity with weaker capability. A cross-vintage arm (an
older model of the first-judge line) is capability-matched,
so its disagreement measures what a model update would move.
An axis where only the cross-line arm disagrees points at
capability; an axis where both arms disagree is
judge-sensitive.

The agreement unit is one discrete verdict: one graded quiz
item, one checked fact, one checked claim, or one contest
pick. An axis under 0.7 — the acceptance anchor of the human
spot check — is marked judge-sensitive and warns. Every judge
runs through the Claude CLI, so a second judge is a different
Claude line or vintage, never a different vendor; the human
spot check stays the cross-vendor anchor. On the
comprehension axis, a cross-line grader can share the model
line of the original reader, so leniency toward the reader's
phrasing is possible; the cross-vintage arm is the cleaner
signal there.

First judges: comprehension opus, completeness opus, hedging opus, clarity opus.

## Enumerated units

| Axis | Units | Skipped stored |
|---|---|---|
| comprehension | 882 | 0 |
| completeness | 315 | 0 |
| hedging | 93 | 0 |
| clarity | 940 | 0 |

A skipped stored row has no rebuildable verdict: a missing
join row or an unparseable output on the join path.

## Arm: claude-opus-4-5-20251101

Resolved model: claude-opus-4-5-20251101. Sample: 100 per axis (seed 0).
Judged on 2026-08-09T10:26:48+00:00.

| Axis | Rows | Items | Agreements | Rate | Unusable | Not judged | Judge-sensitive |
|---|---|---|---|---|---|---|---|
| comprehension | 100 | 600 | 586 | 0.977 | 0 | 0 | no |
| completeness | 99 | 2128 | 1967 | 0.924 | 1 | 0 | no |
| hedging | 93 | 368 | 300 | 0.815 | 0 | 0 | no |
| clarity | 100 | 100 | 60 | 0.6 | 0 | 0 | yes |

Per style (a style-specific disagreement is what the
shared-bias risk predicts):

| Axis | Style | Items | Agreements | Rate |
|---|---|---|---|---|
| comprehension | clarity-flow | 126 | 121 | 0.96 |
| comprehension | classic-concise | 102 | 98 | 0.961 |
| comprehension | developer-docs | 102 | 102 | 1.0 |
| comprehension | plain-language | 138 | 135 | 0.978 |
| comprehension | technical-simplified | 132 | 130 | 0.985 |
| completeness | clarity-flow | 511 | 468 | 0.916 |
| completeness | classic-concise | 358 | 340 | 0.95 |
| completeness | developer-docs | 517 | 468 | 0.905 |
| completeness | plain-language | 443 | 411 | 0.928 |
| completeness | technical-simplified | 299 | 280 | 0.936 |
| hedging | clarity-flow | 76 | 57 | 0.75 |
| hedging | classic-concise | 76 | 63 | 0.829 |
| hedging | developer-docs | 76 | 62 | 0.816 |
| hedging | plain-language | 76 | 66 | 0.868 |
| hedging | technical-simplified | 64 | 52 | 0.812 |
| clarity | clarity-flow | 35 | 21 | 0.6 |
| clarity | classic-concise | 30 | 18 | 0.6 |
| clarity | developer-docs | 40 | 24 | 0.6 |
| clarity | plain-language | 30 | 15 | 0.5 |
| clarity | technical-simplified | 33 | 24 | 0.727 |

### Call timing

A stored call row holds two times: duration_ms is the model
time that the CLI reports, and wall_ms is the wall clock of
the subprocess. The difference is the startup cost of one CLI
call.

Calls: 393, measured: 393.
Mean duration: 17990 ms. Mean wall: 18927 ms. Mean startup: 937 ms.

### Harness spend

A stored call row holds the token counts of its call: the
uncached input, cache-write input, cache-read input, and
output tokens. The cache-read share is the cache-read total
over the whole input total.

Calls: 393, measured: 393.
Input tokens: 3930 uncached, 451167 cache write, 2232412 cache read. Output tokens: 423461.
Cache-read share: 0.831.
Cache writes by lifetime: 451167 at 5 minutes, 0 at 1 hour.

## Arm: haiku

Resolved model: claude-haiku-4-5-20251001. Sample: everything.
Judged on 2026-08-09T09:43:50+00:00.

| Axis | Rows | Items | Agreements | Rate | Unusable | Not judged | Judge-sensitive |
|---|---|---|---|---|---|---|---|
| comprehension | 882 | 5292 | 5131 | 0.97 | 0 | 0 | no |
| completeness | 309 | 6319 | 5727 | 0.906 | 6 | 0 | no |
| hedging | 93 | 368 | 296 | 0.804 | 0 | 0 | no |
| clarity | 939 | 939 | 644 | 0.686 | 1 | 0 | yes |

Per style (a style-specific disagreement is what the
shared-bias risk predicts):

| Axis | Style | Items | Agreements | Rate |
|---|---|---|---|---|
| comprehension | clarity-flow | 1116 | 1087 | 0.974 |
| comprehension | classic-concise | 1116 | 1088 | 0.975 |
| comprehension | developer-docs | 1080 | 1047 | 0.969 |
| comprehension | plain-language | 936 | 907 | 0.969 |
| comprehension | technical-simplified | 1044 | 1002 | 0.96 |
| completeness | clarity-flow | 1306 | 1169 | 0.895 |
| completeness | classic-concise | 1280 | 1177 | 0.92 |
| completeness | developer-docs | 1327 | 1205 | 0.908 |
| completeness | plain-language | 1208 | 1070 | 0.886 |
| completeness | technical-simplified | 1198 | 1106 | 0.923 |
| hedging | clarity-flow | 76 | 60 | 0.789 |
| hedging | classic-concise | 76 | 61 | 0.803 |
| hedging | developer-docs | 76 | 60 | 0.789 |
| hedging | plain-language | 76 | 64 | 0.842 |
| hedging | technical-simplified | 64 | 51 | 0.797 |
| clarity | clarity-flow | 316 | 201 | 0.636 |
| clarity | classic-concise | 315 | 217 | 0.689 |
| clarity | developer-docs | 315 | 222 | 0.705 |
| clarity | plain-language | 316 | 233 | 0.737 |
| clarity | technical-simplified | 300 | 220 | 0.733 |

### Call timing

A stored call row holds two times: duration_ms is the model
time that the CLI reports, and wall_ms is the wall clock of
the subprocess. The difference is the startup cost of one CLI
call.

Calls: 2230, measured: 2230.
Mean duration: 15416 ms. Mean wall: 16314 ms. Mean startup: 898 ms.

### Harness spend

A stored call row holds the token counts of its call: the
uncached input, cache-write input, cache-read input, and
output tokens. The cache-read share is the cache-read total
over the whole input total.

Calls: 2230, measured: 2230.
Input tokens: 22300 uncached, 2064117 cache write, 13139536 cache read. Output tokens: 3183924.
Cache-read share: 0.863.
Cache writes by lifetime: 2064117 at 5 minutes, 0 at 1 hour.

## Warnings

- technical-simplified/summarization-07: the pair failed the gate, excluded
- technical-simplified/debugging-07: the pair failed the gate, excluded
- completeness:check:52c24583db3d937b8215ef6bdb3e6fd4077f0828610ab919bef152e04e9b1734: the second judge gave no usable verdict, so the unit counts as unusable
- claude-opus-4-5-20251101: 1 second verdicts of the completeness axis are unusable
- claude-opus-4-5-20251101: the clarity axis agrees at 0.6, under the 0.7 anchor, so the axis is judge-sensitive for this arm
- haiku: 6 second verdicts of the completeness axis are unusable
- haiku: the clarity axis agrees at 0.686, under the 0.7 anchor, so the axis is judge-sensitive for this arm
- haiku: 1 second verdicts of the clarity axis are unusable

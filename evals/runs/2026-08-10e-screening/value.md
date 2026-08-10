# Reader-value report

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

The checks compare the styled answer with the unstyled answer of
the same prompt, pair by pair, as win, loss, or tie. Only pairs
whose styled answer passes the fidelity gate enter the checks.
Each judge call sees one bare text: no style name, no arm label,
and never both answers. Thus a judge cannot know which answer is
styled. The judge models differ from the writer of the answers.

Judges: reader haiku, grader opus. Comprehension asks up to 6 questions per pair, worded by both answers in balance, with 3 reader replicates per answer, ambiguity uses 3 restatements per answer, and the round-trip goes through Italian. Judged on 2026-08-10T11:35:56+00:00.

## Comprehension (weak reader)

The questions come from the shared facts of the pair, mined in both directions: the facts of the unstyled answer that survive in the styled answer, and the facts of the styled answer that the unstyled answer also states. The quiz takes half of its questions from each wording, so neither answer sets the phrasing alone, and the Sources column counts the questions per wording (unstyled/styled). A grader call turns each fact into one question, and the fact is the reference answer. The weak reader answers the questions from one answer text, once per replicate, and the grader marks every reply. Each styled replicate meets each unstyled replicate as a win, a loss, or a tie, and the pair outcome is the strict plurality, else a tie. The agreement is the plurality share, and the buried-fact rate counts "NOT IN TEXT" replies to a shared fact, per arm. The check measures extraction over shared material. Absence belongs to the content-loss report. Higher is better.

| Style | Wins | Losses | Ties | Mean delta | Agreement | Buried (styled) | Buried (unstyled) |
|---|---|---|---|---|---|---|---|
| actionable-clarity | 2 | 2 | 4 | 0.007 | 0.958 | 0.035 | 0.0 |
| clarity-flow | 2 | 2 | 4 | -0.007 | 0.917 | 0.069 | 0.062 |
| classic-concise | 0 | 3 | 5 | -0.104 | 0.986 | 0.104 | 0.014 |
| developer-docs | 2 | 2 | 3 | -0.008 | 0.841 | 0.048 | 0.008 |
| plain-language | 1 | 1 | 6 | -0.007 | 0.889 | 0.035 | 0.021 |
| technical-simplified | 0 | 0 | 4 | -0.014 | 0.917 | 0.0 | 0.0 |

The styled answer must not score worse than the unstyled answer.
- actionable-clarity: the styled answer holds (2 wins, 2 losses, 4 ties).
- clarity-flow: the styled answer holds (2 wins, 2 losses, 4 ties).
- classic-concise: the styled answer scores worse (0 wins, 3 losses, 5 ties).
- developer-docs: the styled answer holds (2 wins, 2 losses, 3 ties).
- plain-language: the styled answer holds (1 wins, 1 losses, 6 ties).
- technical-simplified: the styled answer holds (0 wins, 0 losses, 4 ties).

### actionable-clarity

| Pair | Questions | Sources (u/s) | Styled | Unstyled | Agreement | Result |
|---|---|---|---|---|---|---|
| code-review-01 | 6 | 3/3 | 1.0 | 0.833 | 1.0 | win |
| code-review-03 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-04 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-08 | 6 | 3/3 | 0.833 | 0.833 | 1.0 | tie |
| explanation-03 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| explanation-04 | 6 | 3/3 | 0.833 | 1.0 | 1.0 | loss |
| summarization-05 | 6 | 3/3 | 1.0 | 0.833 | 1.0 | win |
| summarization-08 | 6 | 3/3 | 0.889 | 1.0 | 0.667 | loss |

### clarity-flow

| Pair | Questions | Sources (u/s) | Styled | Unstyled | Agreement | Result |
|---|---|---|---|---|---|---|
| code-review-01 | 6 | 3/3 | 1.0 | 0.889 | 0.667 | win |
| code-review-03 | 6 | 3/3 | 0.833 | 0.833 | 1.0 | tie |
| debugging-04 | 6 | 3/3 | 0.833 | 1.0 | 1.0 | loss |
| debugging-08 | 6 | 3/3 | 0.444 | 0.833 | 1.0 | loss |
| explanation-03 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| explanation-04 | 6 | 3/3 | 1.0 | 0.667 | 1.0 | win |
| summarization-05 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-08 | 6 | 3/3 | 1.0 | 0.944 | 0.667 | tie |

### classic-concise

| Pair | Questions | Sources (u/s) | Styled | Unstyled | Agreement | Result |
|---|---|---|---|---|---|---|
| code-review-01 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| code-review-03 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-04 | 6 | 3/3 | 0.722 | 1.0 | 1.0 | loss |
| debugging-08 | 6 | 3/3 | 0.556 | 0.778 | 0.889 | loss |
| explanation-03 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| explanation-04 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-05 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-08 | 6 | 3/3 | 0.667 | 1.0 | 1.0 | loss |

### developer-docs

| Pair | Questions | Sources (u/s) | Styled | Unstyled | Agreement | Result |
|---|---|---|---|---|---|---|
| code-review-01 | 6 | 3/3 | 0.944 | 0.944 | 0.556 | tie |
| code-review-03 | 6 | 3/3 | 1.0 | 0.833 | 1.0 | win |
| debugging-04 | 6 | 3/3 | 0.778 | 1.0 | 1.0 | loss |
| explanation-03 | 6 | 3/3 | 0.944 | 0.833 | 0.667 | win |
| explanation-04 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-05 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-08 | 6 | 3/3 | 0.889 | 1.0 | 0.667 | loss |

### plain-language

| Pair | Questions | Sources (u/s) | Styled | Unstyled | Agreement | Result |
|---|---|---|---|---|---|---|
| code-review-01 | 6 | 3/3 | 0.833 | 1.0 | 1.0 | loss |
| code-review-03 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-04 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-08 | 6 | 3/3 | 0.889 | 0.833 | 0.444 | win |
| explanation-03 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| explanation-04 | 6 | 3/3 | 1.0 | 0.944 | 0.667 | tie |
| summarization-05 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-08 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |

### technical-simplified

| Pair | Questions | Sources (u/s) | Styled | Unstyled | Agreement | Result |
|---|---|---|---|---|---|---|
| code-review-01 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-04 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| explanation-04 | 6 | 3/3 | 0.944 | 1.0 | 0.667 | tie |
| summarization-05 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |

## Ambiguity (paraphrase agreement)

Independent reader calls restate one answer text in their own words. The score is the mean pairwise lexical similarity between the restatements: when the readers agree on what the text says, the text is less ambiguous. Higher is better.

| Style | Wins | Losses | Ties |
|---|---|---|---|
| actionable-clarity | 5 | 1 | 2 |
| clarity-flow | 3 | 4 | 1 |
| classic-concise | 4 | 3 | 1 |
| developer-docs | 5 | 2 | 1 |
| plain-language | 4 | 4 | 0 |
| technical-simplified | 2 | 1 | 3 |

The length confound is the correlation between the length ratio of a pair (styled words over unstyled words) and the styled advantage (the score gain of the styled arm). A negative value means that the shorter styled answers score better.
- actionable-clarity: Pearson -0.253, Spearman -0.238, over 8 pairs.
- clarity-flow: Pearson -0.691, Spearman -0.167, over 8 pairs.
- classic-concise: Pearson -0.611, Spearman -0.5, over 8 pairs.
- developer-docs: Pearson -0.41, Spearman -0.548, over 8 pairs.
- plain-language: Pearson -0.349, Spearman -0.214, over 8 pairs.
- technical-simplified: Pearson 0.053, Spearman 0.029, over 6 pairs.

### actionable-clarity

| Pair | Styled | Unstyled | Result |
|---|---|---|---|
| code-review-01 | 0.691 | 0.692 | tie |
| code-review-03 | 0.713 | 0.675 | win |
| debugging-04 | 0.755 | 0.627 | win |
| debugging-08 | 0.66 | 0.408 | win |
| explanation-03 | 0.765 | 0.682 | win |
| explanation-04 | 0.648 | 0.612 | win |
| summarization-05 | 0.681 | 0.797 | loss |
| summarization-08 | 0.687 | 0.671 | tie |

### clarity-flow

| Pair | Styled | Unstyled | Result |
|---|---|---|---|
| code-review-01 | 0.611 | 0.692 | loss |
| code-review-03 | 0.707 | 0.675 | win |
| debugging-04 | 0.594 | 0.627 | loss |
| debugging-08 | 0.62 | 0.408 | win |
| explanation-03 | 0.636 | 0.682 | loss |
| explanation-04 | 0.664 | 0.612 | win |
| summarization-05 | 0.795 | 0.797 | tie |
| summarization-08 | 0.622 | 0.671 | loss |

### classic-concise

| Pair | Styled | Unstyled | Result |
|---|---|---|---|
| code-review-01 | 0.645 | 0.692 | loss |
| code-review-03 | 0.714 | 0.675 | win |
| debugging-04 | 0.745 | 0.627 | win |
| debugging-08 | 0.675 | 0.408 | win |
| explanation-03 | 0.678 | 0.682 | tie |
| explanation-04 | 0.644 | 0.612 | win |
| summarization-05 | 0.738 | 0.797 | loss |
| summarization-08 | 0.602 | 0.671 | loss |

### developer-docs

| Pair | Styled | Unstyled | Result |
|---|---|---|---|
| code-review-01 | 0.653 | 0.692 | loss |
| code-review-03 | 0.724 | 0.675 | win |
| debugging-04 | 0.787 | 0.627 | win |
| debugging-08 | 0.499 | 0.408 | win |
| explanation-03 | 0.753 | 0.682 | win |
| explanation-04 | 0.686 | 0.612 | win |
| summarization-05 | 0.741 | 0.797 | loss |
| summarization-08 | 0.671 | 0.671 | tie |

### plain-language

| Pair | Styled | Unstyled | Result |
|---|---|---|---|
| code-review-01 | 0.644 | 0.692 | loss |
| code-review-03 | 0.645 | 0.675 | loss |
| debugging-04 | 0.8 | 0.627 | win |
| debugging-08 | 0.692 | 0.408 | win |
| explanation-03 | 0.721 | 0.682 | win |
| explanation-04 | 0.718 | 0.612 | win |
| summarization-05 | 0.674 | 0.797 | loss |
| summarization-08 | 0.617 | 0.671 | loss |

### technical-simplified

| Pair | Styled | Unstyled | Result |
|---|---|---|---|
| code-review-01 | 0.676 | 0.692 | tie |
| code-review-03 | 0.326 | 0.675 | loss |
| debugging-04 | 0.702 | 0.627 | win |
| debugging-08 | 0.601 | 0.408 | win |
| explanation-04 | 0.6 | 0.612 | tie |
| summarization-05 | 0.791 | 0.797 | tie |

## Translation round-trip

One call translates the answer to another language, and a second call translates the result back to English. The score is the lexical loss between the original and the round-trip: simpler text survives the round-trip with less loss. Lower is better.

| Style | Wins | Losses | Ties |
|---|---|---|---|
| actionable-clarity | 4 | 2 | 2 |
| clarity-flow | 1 | 3 | 4 |
| classic-concise | 1 | 2 | 5 |
| developer-docs | 3 | 2 | 3 |
| plain-language | 2 | 4 | 2 |
| technical-simplified | 1 | 2 | 3 |

The length confound is the correlation between the length ratio of a pair (styled words over unstyled words) and the styled advantage (the score gain of the styled arm). A negative value means that the shorter styled answers score better.
- actionable-clarity: Pearson 0.479, Spearman 0.405, over 8 pairs.
- clarity-flow: Pearson 0.082, Spearman 0.0, over 8 pairs.
- classic-concise: Pearson 0.048, Spearman 0.357, over 8 pairs.
- developer-docs: Pearson 0.873, Spearman 0.333, over 8 pairs.
- plain-language: Pearson 0.2, Spearman -0.024, over 8 pairs.
- technical-simplified: Pearson 0.864, Spearman 0.714, over 6 pairs.

### actionable-clarity

| Pair | Styled | Unstyled | Result |
|---|---|---|---|
| code-review-01 | 0.073 | 0.093 | win |
| code-review-03 | 0.078 | 0.106 | win |
| debugging-04 | 0.069 | 0.066 | tie |
| debugging-08 | 0.088 | 0.116 | win |
| explanation-03 | 0.127 | 0.089 | loss |
| explanation-04 | 0.104 | 0.088 | tie |
| summarization-05 | 0.211 | 0.113 | loss |
| summarization-08 | 0.112 | 0.16 | win |

### clarity-flow

| Pair | Styled | Unstyled | Result |
|---|---|---|---|
| code-review-01 | 0.078 | 0.093 | tie |
| code-review-03 | 0.066 | 0.106 | win |
| debugging-04 | 0.053 | 0.066 | tie |
| debugging-08 | 0.129 | 0.116 | tie |
| explanation-03 | 0.141 | 0.089 | loss |
| explanation-04 | 0.116 | 0.088 | loss |
| summarization-05 | 0.167 | 0.113 | loss |
| summarization-08 | 0.163 | 0.16 | tie |

### classic-concise

| Pair | Styled | Unstyled | Result |
|---|---|---|---|
| code-review-01 | 0.094 | 0.093 | tie |
| code-review-03 | 0.076 | 0.106 | win |
| debugging-04 | 0.059 | 0.066 | tie |
| debugging-08 | 0.135 | 0.116 | tie |
| explanation-03 | 0.142 | 0.089 | loss |
| explanation-04 | 0.105 | 0.088 | tie |
| summarization-05 | 0.105 | 0.113 | tie |
| summarization-08 | 0.231 | 0.16 | loss |

### developer-docs

| Pair | Styled | Unstyled | Result |
|---|---|---|---|
| code-review-01 | 0.059 | 0.093 | win |
| code-review-03 | 0.047 | 0.106 | win |
| debugging-04 | 0.053 | 0.066 | tie |
| debugging-08 | 0.933 | 0.116 | loss |
| explanation-03 | 0.079 | 0.089 | tie |
| explanation-04 | 0.102 | 0.088 | tie |
| summarization-05 | 0.246 | 0.113 | loss |
| summarization-08 | 0.121 | 0.16 | win |

### plain-language

| Pair | Styled | Unstyled | Result |
|---|---|---|---|
| code-review-01 | 0.072 | 0.093 | win |
| code-review-03 | 0.072 | 0.106 | win |
| debugging-04 | 0.109 | 0.066 | loss |
| debugging-08 | 0.119 | 0.116 | tie |
| explanation-03 | 0.111 | 0.089 | loss |
| explanation-04 | 0.111 | 0.088 | loss |
| summarization-05 | 0.105 | 0.113 | tie |
| summarization-08 | 0.201 | 0.16 | loss |

### technical-simplified

| Pair | Styled | Unstyled | Result |
|---|---|---|---|
| code-review-01 | 0.085 | 0.093 | tie |
| code-review-03 | 0.971 | 0.106 | loss |
| debugging-04 | 0.082 | 0.066 | tie |
| debugging-08 | 0.718 | 0.116 | loss |
| explanation-04 | 0.076 | 0.088 | tie |
| summarization-05 | 0.057 | 0.113 | win |

## Call timing

A stored call row holds two times: duration_ms is the model
time that the CLI reports, and wall_ms is the wall clock of
the subprocess. The difference is the startup cost of one CLI
call.

Calls: 150, measured: 150.
Mean duration: 10585 ms. Mean wall: 15617 ms. Mean startup: 5032 ms.

## Harness spend

A stored call row holds the token counts of its call: the
uncached input, cache-write input, cache-read input, and
output tokens. The cache-read share is the cache-read total
over the whole input total.

Calls: 150, measured: 150.
Input tokens: 1004 uncached, 143215 cache write, 676500 cache read. Output tokens: 134624.
Cache-read share: 0.824.
Cache writes by lifetime: 143215 at 5 minutes, 0 at 1 hour.

## Reuse

Reused rows: 679, imported from 2026-08-10d-screening.
Live calls of this run: 150.

The freshness sample re-ran 6 imported verdicts live; 4 agree.
- comprehension:v3:grades:clarity-flow:code-review-01:styled:1: the verdicts differ.
- comprehension:v3:grades:clarity-flow:code-review-01:styled:2: the verdicts differ.

A verdict axis compares on exact equality, and one differing
verdict is a warning. The clarity picks carry an aggregate
tolerance instead: the sample warns only when its disagreement
count clears a one-sided binomial tail of 0.05 at the
0.4 cross-judge disagreement rate of the
runs/2026-08-08 second-judge sample. Two judges disagree
with each other at least as often as one judge disagrees with
itself later, so the cross-judge rate bounds the reuse noise
from above.

## Warnings

- technical-simplified/explanation-03: the pair failed the gate, excluded
- technical-simplified/summarization-08: the pair failed the gate, excluded
- developer-docs/debugging-08: the pair has 0 shared facts, fewer than the floor of 3, so comprehension skips the pair
- technical-simplified/code-review-03: the pair has 0 shared facts, fewer than the floor of 3, so comprehension skips the pair
- technical-simplified/debugging-08: the pair has 0 shared facts, fewer than the floor of 3, so comprehension skips the pair
- developer-docs/debugging-08: the comprehension check has no usable questions for the pair, so the pair is unscored
- technical-simplified/code-review-03: the comprehension check has no usable questions for the pair, so the pair is unscored
- technical-simplified/debugging-08: the comprehension check has no usable questions for the pair, so the pair is unscored
- classic-concise: the styled answer scores worse than the unstyled answer on comprehension (0 wins, 3 losses)
- reuse freshness: comprehension:v3:grades:clarity-flow:code-review-01:styled:1: the live verdict differs from the reused one
- reuse freshness: comprehension:v3:grades:clarity-flow:code-review-01:styled:2: the live verdict differs from the reused one

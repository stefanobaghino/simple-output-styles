# Reader-value report

The checks compare the styled answer with the unstyled answer of
the same prompt, pair by pair, as win, loss, or tie. Only pairs
whose styled answer passes the fidelity gate enter the checks.
Each judge call sees one bare text: no style name, no arm label,
and never both answers. Thus a judge cannot know which answer is
styled. The judge models differ from the writer of the answers.

Judges: reader haiku, grader opus. Comprehension asks up to 6 questions per pair, worded by both answers in balance, with 3 reader replicates per answer, ambiguity uses 3 restatements per answer, and the round-trip goes through Italian. Judged on 2026-08-10T16:30:36+00:00.

## Comprehension (weak reader)

The questions come from the shared facts of the pair, mined in both directions: the facts of the unstyled answer that survive in the styled answer, and the facts of the styled answer that the unstyled answer also states. The quiz takes half of its questions from each wording, so neither answer sets the phrasing alone, and the Sources column counts the questions per wording (unstyled/styled). A grader call turns each fact into one question, and the fact is the reference answer. The weak reader answers the questions from one answer text, once per replicate, and the grader marks every reply. Each styled replicate meets each unstyled replicate as a win, a loss, or a tie, and the pair outcome is the strict plurality, else a tie. The agreement is the plurality share, and the buried-fact rate counts "NOT IN TEXT" replies to a shared fact, per arm. The check measures extraction over shared material. Absence belongs to the content-loss report. Higher is better.

| Style | Wins | Losses | Ties | Mean delta | Agreement | Buried (styled) | Buried (unstyled) |
|---|---|---|---|---|---|---|---|
| actionable-clarity | 5 | 6 | 18 | -0.008 | 0.862 | 0.033 | 0.048 |
| clarity-flow | 10 | 6 | 15 | 0.007 | 0.828 | 0.057 | 0.066 |
| classic-concise | 4 | 10 | 17 | -0.027 | 0.878 | 0.041 | 0.039 |
| developer-docs | 7 | 9 | 14 | -0.015 | 0.885 | 0.052 | 0.039 |
| plain-language | 5 | 5 | 16 | -0.013 | 0.799 | 0.053 | 0.041 |
| technical-simplified | 5 | 5 | 19 | 0.011 | 0.862 | 0.025 | 0.044 |

The styled answer must not score worse than the unstyled answer.
- actionable-clarity: the styled answer scores worse (5 wins, 6 losses, 18 ties).
- clarity-flow: the styled answer holds (10 wins, 6 losses, 15 ties).
- classic-concise: the styled answer scores worse (4 wins, 10 losses, 17 ties).
- developer-docs: the styled answer scores worse (7 wins, 9 losses, 14 ties).
- plain-language: the styled answer holds (5 wins, 5 losses, 16 ties).
- technical-simplified: the styled answer holds (5 wins, 5 losses, 19 ties).

### actionable-clarity

| Pair | Questions | Sources (u/s) | Styled | Unstyled | Agreement | Result |
|---|---|---|---|---|---|---|
| code-review-02 | 6 | 3/3 | 1.0 | 0.889 | 0.667 | win |
| code-review-03 | 6 | 3/3 | 0.833 | 0.833 | 1.0 | tie |
| code-review-04 | 6 | 3/3 | 0.944 | 1.0 | 0.667 | tie |
| code-review-05 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| code-review-06 | 6 | 3/3 | 0.833 | 1.0 | 1.0 | loss |
| code-review-07 | 6 | 3/3 | 0.944 | 1.0 | 0.667 | tie |
| code-review-08 | 6 | 3/3 | 0.722 | 1.0 | 1.0 | loss |
| debugging-01 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-02 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-03 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-04 | 6 | 3/3 | 0.833 | 0.833 | 1.0 | tie |
| debugging-05 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-07 | 6 | 3/3 | 0.889 | 0.722 | 0.667 | win |
| debugging-08 | 6 | 3/3 | 0.833 | 1.0 | 1.0 | loss |
| explanation-01 | 6 | 3/3 | 1.0 | 0.833 | 1.0 | win |
| explanation-02 | 6 | 3/3 | 0.833 | 1.0 | 1.0 | loss |
| explanation-03 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| explanation-04 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| explanation-05 | 6 | 3/3 | 1.0 | 0.889 | 0.667 | win |
| explanation-06 | 6 | 3/3 | 0.833 | 0.833 | 0.333 | tie |
| explanation-07 | 6 | 3/3 | 0.833 | 0.778 | 0.667 | tie |
| summarization-01 | 6 | 3/3 | 0.722 | 0.833 | 0.667 | loss |
| summarization-02 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-03 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-04 | 6 | 3/3 | 0.889 | 0.667 | 0.667 | win |
| summarization-05 | 6 | 3/3 | 1.0 | 0.944 | 0.667 | tie |
| summarization-06 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-07 | 6 | 3/3 | 0.833 | 1.0 | 1.0 | loss |
| summarization-08 | 6 | 3/3 | 1.0 | 0.944 | 0.667 | tie |

### clarity-flow

| Pair | Questions | Sources (u/s) | Styled | Unstyled | Agreement | Result |
|---|---|---|---|---|---|---|
| code-review-01 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| code-review-02 | 6 | 3/3 | 0.833 | 0.944 | 0.667 | loss |
| code-review-03 | 6 | 3/3 | 0.944 | 0.833 | 0.667 | win |
| code-review-04 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| code-review-05 | 6 | 3/3 | 0.722 | 0.833 | 0.667 | loss |
| code-review-06 | 6 | 3/3 | 0.889 | 0.944 | 0.444 | tie |
| code-review-07 | 6 | 3/3 | 0.944 | 1.0 | 0.667 | tie |
| code-review-08 | 6 | 3/3 | 0.667 | 0.667 | 1.0 | tie |
| debugging-01 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-02 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-03 | 6 | 3/3 | 1.0 | 0.889 | 0.667 | win |
| debugging-04 | 6 | 3/3 | 0.778 | 0.667 | 0.667 | win |
| debugging-05 | 6 | 3/3 | 0.833 | 1.0 | 1.0 | loss |
| debugging-07 | 6 | 3/3 | 1.0 | 0.833 | 1.0 | win |
| debugging-08 | 6 | 3/3 | 1.0 | 0.889 | 0.667 | win |
| explanation-01 | 6 | 3/3 | 0.833 | 1.0 | 1.0 | loss |
| explanation-02 | 6 | 3/3 | 1.0 | 0.833 | 1.0 | win |
| explanation-03 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| explanation-04 | 6 | 3/3 | 0.944 | 1.0 | 0.667 | tie |
| explanation-05 | 6 | 3/3 | 0.833 | 1.0 | 1.0 | loss |
| explanation-06 | 6 | 3/3 | 1.0 | 0.833 | 1.0 | win |
| explanation-07 | 6 | 3/3 | 1.0 | 0.833 | 1.0 | win |
| explanation-08 | 6 | 3/3 | 0.778 | 0.667 | 0.667 | win |
| summarization-01 | 6 | 3/3 | 0.944 | 1.0 | 0.667 | tie |
| summarization-02 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-03 | 6 | 3/3 | 0.944 | 1.0 | 0.667 | tie |
| summarization-04 | 6 | 3/3 | 1.0 | 0.722 | 1.0 | win |
| summarization-05 | 6 | 3/3 | 0.722 | 0.778 | 0.444 | tie |
| summarization-06 | 6 | 3/3 | 0.944 | 1.0 | 0.667 | tie |
| summarization-07 | 6 | 3/3 | 0.778 | 0.944 | 0.778 | loss |
| summarization-08 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |

### classic-concise

| Pair | Questions | Sources (u/s) | Styled | Unstyled | Agreement | Result |
|---|---|---|---|---|---|---|
| code-review-01 | 6 | 3/3 | 1.0 | 0.944 | 0.667 | tie |
| code-review-02 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| code-review-03 | 6 | 3/3 | 0.833 | 0.944 | 0.667 | loss |
| code-review-04 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| code-review-05 | 6 | 3/3 | 0.889 | 1.0 | 0.667 | loss |
| code-review-06 | 6 | 3/3 | 0.778 | 0.944 | 0.778 | loss |
| code-review-07 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| code-review-08 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-01 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-02 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-03 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-04 | 6 | 3/3 | 0.5 | 0.667 | 1.0 | loss |
| debugging-05 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-07 | 6 | 3/3 | 1.0 | 0.556 | 1.0 | win |
| debugging-08 | 6 | 3/3 | 0.889 | 1.0 | 0.667 | loss |
| explanation-01 | 6 | 3/3 | 0.778 | 1.0 | 1.0 | loss |
| explanation-02 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| explanation-03 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| explanation-04 | 6 | 3/3 | 0.833 | 1.0 | 1.0 | loss |
| explanation-05 | 6 | 3/3 | 0.833 | 1.0 | 0.667 | loss |
| explanation-06 | 6 | 3/3 | 0.833 | 1.0 | 1.0 | loss |
| explanation-07 | 6 | 3/3 | 0.944 | 0.833 | 0.667 | win |
| explanation-08 | 6 | 3/3 | 0.889 | 0.833 | 0.444 | win |
| summarization-01 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-02 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-03 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-04 | 6 | 3/3 | 0.833 | 0.833 | 1.0 | tie |
| summarization-05 | 6 | 3/3 | 0.889 | 0.833 | 0.667 | tie |
| summarization-06 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-07 | 6 | 3/3 | 0.778 | 1.0 | 0.667 | loss |
| summarization-08 | 6 | 3/3 | 0.889 | 0.833 | 0.667 | win |

### developer-docs

| Pair | Questions | Sources (u/s) | Styled | Unstyled | Agreement | Result |
|---|---|---|---|---|---|---|
| code-review-01 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| code-review-02 | 6 | 3/3 | 0.833 | 0.833 | 1.0 | tie |
| code-review-04 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| code-review-05 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| code-review-06 | 6 | 3/3 | 0.556 | 1.0 | 1.0 | loss |
| code-review-07 | 6 | 3/3 | 1.0 | 0.944 | 0.667 | tie |
| code-review-08 | 6 | 3/3 | 1.0 | 0.889 | 0.667 | win |
| debugging-01 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-02 | 6 | 3/3 | 1.0 | 0.889 | 0.667 | win |
| debugging-03 | 6 | 3/3 | 1.0 | 0.833 | 1.0 | win |
| debugging-04 | 6 | 3/3 | 0.833 | 0.667 | 1.0 | win |
| debugging-05 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-07 | 6 | 3/3 | 0.722 | 0.833 | 0.667 | loss |
| debugging-08 | 6 | 3/3 | 0.778 | 1.0 | 1.0 | loss |
| explanation-01 | 6 | 3/3 | 0.889 | 1.0 | 0.667 | loss |
| explanation-02 | 6 | 3/3 | 1.0 | 0.833 | 1.0 | win |
| explanation-03 | 6 | 3/3 | 0.833 | 0.944 | 0.667 | loss |
| explanation-04 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| explanation-05 | 6 | 3/3 | 0.722 | 0.889 | 0.778 | loss |
| explanation-06 | 6 | 3/3 | 1.0 | 0.778 | 1.0 | win |
| explanation-07 | 6 | 3/3 | 0.611 | 0.722 | 0.667 | loss |
| explanation-08 | 6 | 3/3 | 0.833 | 1.0 | 1.0 | loss |
| summarization-01 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-02 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-03 | 6 | 3/3 | 0.889 | 1.0 | 0.667 | loss |
| summarization-04 | 6 | 3/3 | 0.722 | 0.778 | 0.444 | tie |
| summarization-05 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-06 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-07 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-08 | 6 | 3/3 | 1.0 | 0.833 | 1.0 | win |

### plain-language

| Pair | Questions | Sources (u/s) | Styled | Unstyled | Agreement | Result |
|---|---|---|---|---|---|---|
| code-review-02 | 6 | 3/3 | 1.0 | 0.722 | 1.0 | win |
| code-review-05 | 6 | 3/3 | 0.833 | 0.833 | 1.0 | tie |
| code-review-06 | 6 | 3/3 | 0.944 | 1.0 | 0.667 | tie |
| code-review-07 | 6 | 3/3 | 1.0 | 0.944 | 0.667 | tie |
| code-review-08 | 6 | 3/3 | 0.778 | 0.944 | 0.778 | loss |
| debugging-01 | 6 | 3/3 | 1.0 | 0.944 | 0.667 | tie |
| debugging-02 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-03 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-04 | 6 | 3/3 | 0.667 | 0.833 | 1.0 | loss |
| debugging-05 | 6 | 3/3 | 1.0 | 0.944 | 0.667 | tie |
| debugging-08 | 6 | 3/3 | 0.5 | 1.0 | 1.0 | loss |
| explanation-01 | 6 | 3/3 | 1.0 | 0.889 | 0.667 | win |
| explanation-02 | 6 | 3/3 | 1.0 | 0.889 | 0.667 | win |
| explanation-03 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| explanation-04 | 6 | 3/3 | 0.944 | 1.0 | 0.667 | tie |
| explanation-05 | 6 | 3/3 | 0.944 | 0.833 | 0.556 | win |
| explanation-06 | 6 | 3/3 | 0.833 | 1.0 | 1.0 | loss |
| explanation-08 | 6 | 3/3 | 0.889 | 1.0 | 0.667 | loss |
| summarization-01 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-02 | 6 | 3/3 | 0.889 | 0.889 | 0.556 | tie |
| summarization-03 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-04 | 6 | 3/3 | 0.944 | 1.0 | 0.667 | tie |
| summarization-05 | 6 | 3/3 | 0.889 | 0.889 | 0.556 | tie |
| summarization-06 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-07 | 6 | 3/3 | 1.0 | 0.833 | 1.0 | win |
| summarization-08 | 6 | 3/3 | 0.667 | 0.667 | 0.333 | tie |

### technical-simplified

| Pair | Questions | Sources (u/s) | Styled | Unstyled | Agreement | Result |
|---|---|---|---|---|---|---|
| code-review-01 | 6 | 3/3 | 1.0 | 0.833 | 1.0 | win |
| code-review-02 | 6 | 3/3 | 0.889 | 1.0 | 0.667 | loss |
| code-review-03 | 6 | 3/3 | 1.0 | 0.833 | 1.0 | win |
| code-review-04 | 6 | 3/3 | 0.889 | 1.0 | 0.667 | loss |
| code-review-05 | 6 | 3/3 | 0.944 | 1.0 | 0.667 | tie |
| code-review-06 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| code-review-07 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| code-review-08 | 6 | 3/3 | 0.5 | 0.778 | 1.0 | loss |
| debugging-01 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-02 | 6 | 3/3 | 1.0 | 0.833 | 1.0 | win |
| debugging-03 | 6 | 3/3 | 1.0 | 0.944 | 0.667 | tie |
| debugging-04 | 6 | 3/3 | 1.0 | 0.889 | 0.667 | win |
| debugging-05 | 6 | 3/3 | 0.889 | 0.833 | 0.667 | tie |
| debugging-08 | 6 | 3/3 | 0.833 | 1.0 | 1.0 | loss |
| explanation-01 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| explanation-02 | 6 | 3/3 | 1.0 | 0.722 | 1.0 | win |
| explanation-03 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| explanation-04 | 6 | 3/3 | 1.0 | 0.944 | 0.667 | tie |
| explanation-05 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| explanation-06 | 6 | 3/3 | 0.944 | 0.889 | 0.444 | tie |
| explanation-07 | 6 | 3/3 | 0.889 | 1.0 | 0.667 | loss |
| explanation-08 | 6 | 3/3 | 0.833 | 0.833 | 1.0 | tie |
| summarization-01 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-02 | 6 | 3/3 | 0.944 | 0.944 | 0.556 | tie |
| summarization-03 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-04 | 6 | 3/3 | 0.833 | 0.833 | 1.0 | tie |
| summarization-05 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-06 | 6 | 3/3 | 1.0 | 0.944 | 0.667 | tie |
| summarization-08 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |

## Ambiguity (paraphrase agreement)

Independent reader calls restate one answer text in their own words. The score is the mean pairwise lexical similarity between the restatements: when the readers agree on what the text says, the text is less ambiguous. Higher is better.

| Style | Wins | Losses | Ties |
|---|---|---|---|
| actionable-clarity | 18 | 5 | 7 |
| clarity-flow | 13 | 13 | 6 |
| classic-concise | 16 | 14 | 2 |
| developer-docs | 22 | 8 | 2 |
| plain-language | 20 | 9 | 3 |
| technical-simplified | 22 | 4 | 4 |

The length confound is the correlation between the length ratio of a pair (styled words over unstyled words) and the styled advantage (the score gain of the styled arm). A negative value means that the shorter styled answers score better.
- actionable-clarity: Pearson 0.308, Spearman -0.015, over 30 pairs.
- clarity-flow: Pearson 0.387, Spearman -0.057, over 32 pairs.
- classic-concise: Pearson 0.375, Spearman 0.022, over 32 pairs.
- developer-docs: Pearson 0.352, Spearman -0.165, over 32 pairs.
- plain-language: Pearson 0.259, Spearman 0.492, over 32 pairs.
- technical-simplified: Pearson -0.23, Spearman -0.335, over 30 pairs.

### actionable-clarity

| Pair | Styled | Unstyled | Result |
|---|---|---|---|
| code-review-02 | 0.748 | 0.698 | win |
| code-review-03 | 0.705 | 0.692 | tie |
| code-review-04 | 0.683 | 0.632 | win |
| code-review-05 | 0.73 | 0.661 | win |
| code-review-06 | 0.661 | 0.675 | tie |
| code-review-07 | 0.644 | 0.664 | tie |
| code-review-08 | 0.658 | 0.695 | loss |
| debugging-01 | 0.663 | 0.726 | loss |
| debugging-02 | 0.641 | 0.659 | tie |
| debugging-03 | 0.802 | 0.807 | tie |
| debugging-04 | 0.761 | 0.607 | win |
| debugging-05 | 0.75 | 0.605 | win |
| debugging-06 | 0.638 | 0.514 | win |
| debugging-07 | 0.643 | 0.623 | win |
| debugging-08 | 0.642 | 0.678 | loss |
| explanation-01 | 0.747 | 0.726 | win |
| explanation-02 | 0.656 | 0.72 | loss |
| explanation-03 | 0.725 | 0.655 | win |
| explanation-04 | 0.653 | 0.676 | loss |
| explanation-05 | 0.689 | 0.642 | win |
| explanation-06 | 0.632 | 0.575 | win |
| explanation-07 | 0.639 | 0.581 | win |
| summarization-01 | 0.637 | 0.595 | win |
| summarization-02 | 0.614 | 0.607 | tie |
| summarization-03 | 0.67 | 0.596 | win |
| summarization-04 | 0.671 | 0.641 | win |
| summarization-05 | 0.782 | 0.719 | win |
| summarization-06 | 0.681 | 0.701 | tie |
| summarization-07 | 0.672 | 0.639 | win |
| summarization-08 | 0.616 | 0.577 | win |

### clarity-flow

| Pair | Styled | Unstyled | Result |
|---|---|---|---|
| code-review-01 | 0.616 | 0.654 | loss |
| code-review-02 | 0.757 | 0.698 | win |
| code-review-03 | 0.707 | 0.692 | tie |
| code-review-04 | 0.711 | 0.632 | win |
| code-review-05 | 0.65 | 0.661 | tie |
| code-review-06 | 0.671 | 0.675 | tie |
| code-review-07 | 0.615 | 0.664 | loss |
| code-review-08 | 0.698 | 0.695 | tie |
| debugging-01 | 0.705 | 0.726 | loss |
| debugging-02 | 0.703 | 0.659 | win |
| debugging-03 | 0.782 | 0.807 | loss |
| debugging-04 | 0.741 | 0.607 | win |
| debugging-05 | 0.686 | 0.605 | win |
| debugging-06 | 0.679 | 0.514 | win |
| debugging-07 | 0.674 | 0.623 | win |
| debugging-08 | 0.635 | 0.678 | loss |
| explanation-01 | 0.666 | 0.726 | loss |
| explanation-02 | 0.7 | 0.72 | loss |
| explanation-03 | 0.688 | 0.655 | win |
| explanation-04 | 0.66 | 0.676 | tie |
| explanation-05 | 0.599 | 0.642 | loss |
| explanation-06 | 0.6 | 0.575 | win |
| explanation-07 | 0.558 | 0.581 | loss |
| explanation-08 | 0.56 | 0.634 | loss |
| summarization-01 | 0.7 | 0.595 | win |
| summarization-02 | 0.668 | 0.607 | win |
| summarization-03 | 0.696 | 0.596 | win |
| summarization-04 | 0.619 | 0.641 | loss |
| summarization-05 | 0.725 | 0.719 | tie |
| summarization-06 | 0.622 | 0.701 | loss |
| summarization-07 | 0.574 | 0.639 | loss |
| summarization-08 | 0.624 | 0.577 | win |

### classic-concise

| Pair | Styled | Unstyled | Result |
|---|---|---|---|
| code-review-01 | 0.713 | 0.654 | win |
| code-review-02 | 0.606 | 0.698 | loss |
| code-review-03 | 0.641 | 0.692 | loss |
| code-review-04 | 0.717 | 0.632 | win |
| code-review-05 | 0.732 | 0.661 | win |
| code-review-06 | 0.617 | 0.675 | loss |
| code-review-07 | 0.606 | 0.664 | loss |
| code-review-08 | 0.696 | 0.695 | tie |
| debugging-01 | 0.703 | 0.726 | loss |
| debugging-02 | 0.724 | 0.659 | win |
| debugging-03 | 0.697 | 0.807 | loss |
| debugging-04 | 0.729 | 0.607 | win |
| debugging-05 | 0.701 | 0.605 | win |
| debugging-06 | 0.686 | 0.514 | win |
| debugging-07 | 0.687 | 0.623 | win |
| debugging-08 | 0.597 | 0.678 | loss |
| explanation-01 | 0.669 | 0.726 | loss |
| explanation-02 | 0.648 | 0.72 | loss |
| explanation-03 | 0.69 | 0.655 | win |
| explanation-04 | 0.649 | 0.676 | loss |
| explanation-05 | 0.605 | 0.642 | loss |
| explanation-06 | 0.614 | 0.575 | win |
| explanation-07 | 0.504 | 0.581 | loss |
| explanation-08 | 0.609 | 0.634 | loss |
| summarization-01 | 0.737 | 0.595 | win |
| summarization-02 | 0.629 | 0.607 | win |
| summarization-03 | 0.658 | 0.596 | win |
| summarization-04 | 0.728 | 0.641 | win |
| summarization-05 | 0.822 | 0.719 | win |
| summarization-06 | 0.688 | 0.701 | tie |
| summarization-07 | 0.618 | 0.639 | loss |
| summarization-08 | 0.616 | 0.577 | win |

### developer-docs

| Pair | Styled | Unstyled | Result |
|---|---|---|---|
| code-review-01 | 0.688 | 0.654 | win |
| code-review-02 | 0.752 | 0.698 | win |
| code-review-03 | 0.641 | 0.692 | loss |
| code-review-04 | 0.57 | 0.632 | loss |
| code-review-05 | 0.733 | 0.661 | win |
| code-review-06 | 0.717 | 0.675 | win |
| code-review-07 | 0.677 | 0.664 | tie |
| code-review-08 | 0.58 | 0.695 | loss |
| debugging-01 | 0.656 | 0.726 | loss |
| debugging-02 | 0.745 | 0.659 | win |
| debugging-03 | 0.739 | 0.807 | loss |
| debugging-04 | 0.718 | 0.607 | win |
| debugging-05 | 0.736 | 0.605 | win |
| debugging-06 | 0.72 | 0.514 | win |
| debugging-07 | 0.769 | 0.623 | win |
| debugging-08 | 0.572 | 0.678 | loss |
| explanation-01 | 0.767 | 0.726 | win |
| explanation-02 | 0.635 | 0.72 | loss |
| explanation-03 | 0.697 | 0.655 | win |
| explanation-04 | 0.699 | 0.676 | win |
| explanation-05 | 0.688 | 0.642 | win |
| explanation-06 | 0.639 | 0.575 | win |
| explanation-07 | 0.649 | 0.581 | win |
| explanation-08 | 0.694 | 0.634 | win |
| summarization-01 | 0.788 | 0.595 | win |
| summarization-02 | 0.627 | 0.607 | win |
| summarization-03 | 0.619 | 0.596 | win |
| summarization-04 | 0.689 | 0.641 | win |
| summarization-05 | 0.815 | 0.719 | win |
| summarization-06 | 0.649 | 0.701 | loss |
| summarization-07 | 0.639 | 0.639 | tie |
| summarization-08 | 0.663 | 0.577 | win |

### plain-language

| Pair | Styled | Unstyled | Result |
|---|---|---|---|
| code-review-01 | 0.472 | 0.654 | loss |
| code-review-02 | 0.664 | 0.698 | loss |
| code-review-03 | 0.685 | 0.692 | tie |
| code-review-04 | 0.376 | 0.632 | loss |
| code-review-05 | 0.778 | 0.661 | win |
| code-review-06 | 0.603 | 0.675 | loss |
| code-review-07 | 0.688 | 0.664 | win |
| code-review-08 | 0.719 | 0.695 | win |
| debugging-01 | 0.808 | 0.726 | win |
| debugging-02 | 0.838 | 0.659 | win |
| debugging-03 | 0.874 | 0.807 | win |
| debugging-04 | 0.795 | 0.607 | win |
| debugging-05 | 0.761 | 0.605 | win |
| debugging-06 | 0.599 | 0.514 | win |
| debugging-07 | 0.46 | 0.623 | loss |
| debugging-08 | 0.594 | 0.678 | loss |
| explanation-01 | 0.747 | 0.726 | win |
| explanation-02 | 0.742 | 0.72 | win |
| explanation-03 | 0.703 | 0.655 | win |
| explanation-04 | 0.636 | 0.676 | loss |
| explanation-05 | 0.653 | 0.642 | tie |
| explanation-06 | 0.669 | 0.575 | win |
| explanation-07 | 0.475 | 0.581 | loss |
| explanation-08 | 0.653 | 0.634 | tie |
| summarization-01 | 0.628 | 0.595 | win |
| summarization-02 | 0.633 | 0.607 | win |
| summarization-03 | 0.653 | 0.596 | win |
| summarization-04 | 0.682 | 0.641 | win |
| summarization-05 | 0.745 | 0.719 | win |
| summarization-06 | 0.646 | 0.701 | loss |
| summarization-07 | 0.693 | 0.639 | win |
| summarization-08 | 0.61 | 0.577 | win |

### technical-simplified

| Pair | Styled | Unstyled | Result |
|---|---|---|---|
| code-review-01 | 0.768 | 0.654 | win |
| code-review-02 | 0.729 | 0.698 | win |
| code-review-03 | 0.728 | 0.692 | win |
| code-review-04 | 0.743 | 0.632 | win |
| code-review-05 | 0.731 | 0.661 | win |
| code-review-06 | 0.73 | 0.675 | win |
| code-review-07 | 0.701 | 0.664 | win |
| code-review-08 | 0.722 | 0.695 | win |
| debugging-01 | 0.644 | 0.726 | loss |
| debugging-02 | 0.796 | 0.659 | win |
| debugging-03 | 0.763 | 0.807 | loss |
| debugging-04 | 0.695 | 0.607 | win |
| debugging-05 | 0.732 | 0.605 | win |
| debugging-06 | 0.516 | 0.514 | tie |
| debugging-08 | 0.617 | 0.678 | loss |
| explanation-01 | 0.719 | 0.726 | tie |
| explanation-02 | 0.791 | 0.72 | win |
| explanation-03 | 0.695 | 0.655 | win |
| explanation-04 | 0.735 | 0.676 | win |
| explanation-05 | 0.7 | 0.642 | win |
| explanation-06 | 0.627 | 0.575 | win |
| explanation-07 | 0.633 | 0.581 | win |
| explanation-08 | 0.704 | 0.634 | win |
| summarization-01 | 0.778 | 0.595 | win |
| summarization-02 | 0.748 | 0.607 | win |
| summarization-03 | 0.612 | 0.596 | tie |
| summarization-04 | 0.758 | 0.641 | win |
| summarization-05 | 0.697 | 0.719 | loss |
| summarization-06 | 0.729 | 0.701 | win |
| summarization-08 | 0.595 | 0.577 | tie |

## Translation round-trip

One call translates the answer to another language, and a second call translates the result back to English. The score is the lexical loss between the original and the round-trip: simpler text survives the round-trip with less loss. Lower is better.

| Style | Wins | Losses | Ties |
|---|---|---|---|
| actionable-clarity | 10 | 5 | 15 |
| clarity-flow | 11 | 11 | 10 |
| classic-concise | 10 | 13 | 9 |
| developer-docs | 18 | 5 | 9 |
| plain-language | 13 | 8 | 11 |
| technical-simplified | 8 | 9 | 13 |

The length confound is the correlation between the length ratio of a pair (styled words over unstyled words) and the styled advantage (the score gain of the styled arm). A negative value means that the shorter styled answers score better.
- actionable-clarity: Pearson 0.857, Spearman 0.304, over 30 pairs.
- clarity-flow: Pearson 0.875, Spearman 0.084, over 32 pairs.
- classic-concise: Pearson 0.823, Spearman -0.153, over 32 pairs.
- developer-docs: Pearson 0.583, Spearman 0.369, over 32 pairs.
- plain-language: Pearson 0.43, Spearman 0.345, over 32 pairs.
- technical-simplified: Pearson -0.32, Spearman -0.155, over 30 pairs.

### actionable-clarity

| Pair | Styled | Unstyled | Result |
|---|---|---|---|
| code-review-02 | 0.063 | 0.062 | tie |
| code-review-03 | 0.082 | 0.061 | loss |
| code-review-04 | 0.062 | 0.148 | win |
| code-review-05 | 0.085 | 0.099 | tie |
| code-review-06 | 0.099 | 0.093 | tie |
| code-review-07 | 0.119 | 0.082 | loss |
| code-review-08 | 0.101 | 0.087 | tie |
| debugging-01 | 0.087 | 0.215 | win |
| debugging-02 | 0.082 | 0.117 | win |
| debugging-03 | 0.021 | 0.021 | tie |
| debugging-04 | 0.064 | 0.066 | tie |
| debugging-05 | 0.109 | 0.103 | tie |
| debugging-06 | 0.112 | 0.544 | win |
| debugging-07 | 0.098 | 0.083 | tie |
| debugging-08 | 0.129 | 0.124 | tie |
| explanation-01 | 0.123 | 0.121 | tie |
| explanation-02 | 0.113 | 0.134 | win |
| explanation-03 | 0.153 | 0.091 | loss |
| explanation-04 | 0.113 | 0.09 | loss |
| explanation-05 | 0.11 | 0.137 | win |
| explanation-06 | 0.071 | 0.052 | tie |
| explanation-07 | 0.086 | 0.082 | tie |
| summarization-01 | 0.091 | 0.11 | tie |
| summarization-02 | 0.12 | 0.2 | win |
| summarization-03 | 0.1 | 0.141 | win |
| summarization-04 | 0.068 | 0.056 | tie |
| summarization-05 | 0.18 | 0.126 | loss |
| summarization-06 | 0.076 | 0.17 | win |
| summarization-07 | 0.198 | 0.193 | tie |
| summarization-08 | 0.11 | 0.214 | win |

### clarity-flow

| Pair | Styled | Unstyled | Result |
|---|---|---|---|
| code-review-01 | 0.081 | 0.093 | tie |
| code-review-02 | 0.079 | 0.062 | tie |
| code-review-03 | 0.054 | 0.061 | tie |
| code-review-04 | 0.087 | 0.148 | win |
| code-review-05 | 0.069 | 0.099 | win |
| code-review-06 | 0.137 | 0.093 | loss |
| code-review-07 | 0.133 | 0.082 | loss |
| code-review-08 | 0.132 | 0.087 | loss |
| debugging-01 | 0.143 | 0.215 | win |
| debugging-02 | 0.082 | 0.117 | win |
| debugging-03 | 0.039 | 0.021 | tie |
| debugging-04 | 0.066 | 0.066 | tie |
| debugging-05 | 0.088 | 0.103 | tie |
| debugging-06 | 0.113 | 0.544 | win |
| debugging-07 | 0.109 | 0.083 | loss |
| debugging-08 | 0.174 | 0.124 | loss |
| explanation-01 | 0.081 | 0.121 | win |
| explanation-02 | 0.078 | 0.134 | win |
| explanation-03 | 0.154 | 0.091 | loss |
| explanation-04 | 0.083 | 0.09 | tie |
| explanation-05 | 0.109 | 0.137 | win |
| explanation-06 | 0.076 | 0.052 | loss |
| explanation-07 | 0.128 | 0.082 | loss |
| explanation-08 | 0.123 | 0.136 | tie |
| summarization-01 | 0.14 | 0.11 | loss |
| summarization-02 | 0.194 | 0.2 | tie |
| summarization-03 | 0.109 | 0.141 | win |
| summarization-04 | 0.096 | 0.056 | loss |
| summarization-05 | 0.104 | 0.126 | win |
| summarization-06 | 0.173 | 0.17 | tie |
| summarization-07 | 0.224 | 0.193 | loss |
| summarization-08 | 0.166 | 0.214 | win |

### classic-concise

| Pair | Styled | Unstyled | Result |
|---|---|---|---|
| code-review-01 | 0.088 | 0.093 | tie |
| code-review-02 | 0.082 | 0.062 | loss |
| code-review-03 | 0.104 | 0.061 | loss |
| code-review-04 | 0.059 | 0.148 | win |
| code-review-05 | 0.066 | 0.099 | win |
| code-review-06 | 0.068 | 0.093 | win |
| code-review-07 | 0.138 | 0.082 | loss |
| code-review-08 | 0.154 | 0.087 | loss |
| debugging-01 | 0.216 | 0.215 | tie |
| debugging-02 | 0.056 | 0.117 | win |
| debugging-03 | 0.041 | 0.021 | loss |
| debugging-04 | 0.074 | 0.066 | tie |
| debugging-05 | 0.091 | 0.103 | tie |
| debugging-06 | 0.145 | 0.544 | win |
| debugging-07 | 0.079 | 0.083 | tie |
| debugging-08 | 0.101 | 0.124 | win |
| explanation-01 | 0.142 | 0.121 | loss |
| explanation-02 | 0.153 | 0.134 | tie |
| explanation-03 | 0.134 | 0.091 | loss |
| explanation-04 | 0.066 | 0.09 | win |
| explanation-05 | 0.102 | 0.137 | win |
| explanation-06 | 0.109 | 0.052 | loss |
| explanation-07 | 0.175 | 0.082 | loss |
| explanation-08 | 0.217 | 0.136 | loss |
| summarization-01 | 0.077 | 0.11 | win |
| summarization-02 | 0.257 | 0.2 | loss |
| summarization-03 | 0.095 | 0.141 | win |
| summarization-04 | 0.124 | 0.056 | loss |
| summarization-05 | 0.12 | 0.126 | tie |
| summarization-06 | 0.174 | 0.17 | tie |
| summarization-07 | 0.231 | 0.193 | loss |
| summarization-08 | 0.204 | 0.214 | tie |

### developer-docs

| Pair | Styled | Unstyled | Result |
|---|---|---|---|
| code-review-01 | 0.063 | 0.093 | win |
| code-review-02 | 0.05 | 0.062 | tie |
| code-review-03 | 0.654 | 0.061 | loss |
| code-review-04 | 0.106 | 0.148 | win |
| code-review-05 | 0.084 | 0.099 | tie |
| code-review-06 | 0.119 | 0.093 | loss |
| code-review-07 | 0.085 | 0.082 | tie |
| code-review-08 | 0.14 | 0.087 | loss |
| debugging-01 | 0.071 | 0.215 | win |
| debugging-02 | 0.049 | 0.117 | win |
| debugging-03 | 0.023 | 0.021 | tie |
| debugging-04 | 0.057 | 0.066 | tie |
| debugging-05 | 0.073 | 0.103 | win |
| debugging-06 | 0.128 | 0.544 | win |
| debugging-07 | 0.074 | 0.083 | tie |
| debugging-08 | 0.073 | 0.124 | win |
| explanation-01 | 0.177 | 0.121 | loss |
| explanation-02 | 0.087 | 0.134 | win |
| explanation-03 | 0.088 | 0.091 | tie |
| explanation-04 | 0.115 | 0.09 | loss |
| explanation-05 | 0.094 | 0.137 | win |
| explanation-06 | 0.069 | 0.052 | tie |
| explanation-07 | 0.058 | 0.082 | win |
| explanation-08 | 0.08 | 0.136 | win |
| summarization-01 | 0.081 | 0.11 | win |
| summarization-02 | 0.114 | 0.2 | win |
| summarization-03 | 0.158 | 0.141 | tie |
| summarization-04 | 0.02 | 0.056 | win |
| summarization-05 | 0.065 | 0.126 | win |
| summarization-06 | 0.091 | 0.17 | win |
| summarization-07 | 0.159 | 0.193 | win |
| summarization-08 | 0.168 | 0.214 | win |

### plain-language

| Pair | Styled | Unstyled | Result |
|---|---|---|---|
| code-review-01 | 1.0 | 0.093 | loss |
| code-review-02 | 0.139 | 0.062 | loss |
| code-review-03 | 0.011 | 0.061 | win |
| code-review-04 | 0.636 | 0.148 | loss |
| code-review-05 | 0.082 | 0.099 | tie |
| code-review-06 | 0.071 | 0.093 | win |
| code-review-07 | 0.098 | 0.082 | tie |
| code-review-08 | 0.102 | 0.087 | tie |
| debugging-01 | 0.0 | 0.215 | win |
| debugging-02 | 0.049 | 0.117 | win |
| debugging-03 | 0.021 | 0.021 | tie |
| debugging-04 | 0.076 | 0.066 | tie |
| debugging-05 | 0.069 | 0.103 | win |
| debugging-06 | 0.191 | 0.544 | win |
| debugging-07 | 0.105 | 0.083 | loss |
| debugging-08 | 0.11 | 0.124 | tie |
| explanation-01 | 0.092 | 0.121 | win |
| explanation-02 | 0.098 | 0.134 | win |
| explanation-03 | 0.102 | 0.091 | tie |
| explanation-04 | 0.123 | 0.09 | loss |
| explanation-05 | 0.103 | 0.137 | win |
| explanation-06 | 0.121 | 0.052 | loss |
| explanation-07 | 0.222 | 0.082 | loss |
| explanation-08 | 0.076 | 0.136 | win |
| summarization-01 | 0.164 | 0.11 | loss |
| summarization-02 | 0.098 | 0.2 | win |
| summarization-03 | 0.082 | 0.141 | win |
| summarization-04 | 0.057 | 0.056 | tie |
| summarization-05 | 0.113 | 0.126 | tie |
| summarization-06 | 0.157 | 0.17 | tie |
| summarization-07 | 0.201 | 0.193 | tie |
| summarization-08 | 0.17 | 0.214 | win |

### technical-simplified

| Pair | Styled | Unstyled | Result |
|---|---|---|---|
| code-review-01 | 0.081 | 0.093 | tie |
| code-review-02 | 0.051 | 0.062 | tie |
| code-review-03 | 0.126 | 0.061 | loss |
| code-review-04 | 0.051 | 0.148 | win |
| code-review-05 | 0.109 | 0.099 | tie |
| code-review-06 | 0.115 | 0.093 | loss |
| code-review-07 | 0.126 | 0.082 | loss |
| code-review-08 | 0.12 | 0.087 | loss |
| debugging-01 | 0.043 | 0.215 | win |
| debugging-02 | 0.055 | 0.117 | win |
| debugging-03 | 0.038 | 0.021 | tie |
| debugging-04 | 0.065 | 0.066 | tie |
| debugging-05 | 0.121 | 0.103 | tie |
| debugging-06 | 0.795 | 0.544 | loss |
| debugging-08 | 0.11 | 0.124 | tie |
| explanation-01 | 0.122 | 0.121 | tie |
| explanation-02 | 0.128 | 0.134 | tie |
| explanation-03 | 0.084 | 0.091 | tie |
| explanation-04 | 0.12 | 0.09 | loss |
| explanation-05 | 0.065 | 0.137 | win |
| explanation-06 | 0.106 | 0.052 | loss |
| explanation-07 | 0.146 | 0.082 | loss |
| explanation-08 | 0.12 | 0.136 | tie |
| summarization-01 | 0.028 | 0.11 | win |
| summarization-02 | 0.194 | 0.2 | tie |
| summarization-03 | 0.071 | 0.141 | win |
| summarization-04 | 0.162 | 0.056 | loss |
| summarization-05 | 0.095 | 0.126 | win |
| summarization-06 | 0.111 | 0.17 | win |
| summarization-08 | 0.195 | 0.214 | tie |

## Call timing

A stored call row holds two times: duration_ms is the model
time that the CLI reports, and wall_ms is the wall clock of
the subprocess. The difference is the startup cost of one CLI
call.

Calls: 533, measured: 533.
Mean duration: 11451 ms. Mean wall: 18812 ms. Mean startup: 7361 ms.

## Harness spend

A stored call row holds the token counts of its call: the
uncached input, cache-write input, cache-read input, and
output tokens. The cache-read share is the cache-read total
over the whole input total.

Calls: 533, measured: 533.
Input tokens: 3658 uncached, 500802 cache write, 2436104 cache read. Output tokens: 553847.
Cache-read share: 0.828.
Cache writes by lifetime: 500802 at 5 minutes, 0 at 1 hour.

## Reuse

Reused rows: 2855, imported from 2026-08-08.
Live calls of this run: 533.

The freshness sample re-ran 6 imported verdicts live; 6 agree.

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

- technical-simplified/summarization-07: the pair failed the gate, excluded
- technical-simplified/debugging-07: the pair failed the gate, excluded
- actionable-clarity/explanation-08: the pair failed the gate, excluded
- actionable-clarity/code-review-01: the pair failed the gate, excluded
- actionable-clarity/debugging-06: the pair has 1 shared facts, fewer than the floor of 3, so comprehension skips the pair
- clarity-flow/debugging-06: the pair has 1 shared facts, fewer than the floor of 3, so comprehension skips the pair
- classic-concise/debugging-06: the pair has 1 shared facts, fewer than the floor of 3, so comprehension skips the pair
- developer-docs/code-review-03: the pair has 0 shared facts, fewer than the floor of 3, so comprehension skips the pair
- developer-docs/debugging-06: the pair has 1 shared facts, fewer than the floor of 3, so comprehension skips the pair
- plain-language/code-review-01: the pair has 0 shared facts, fewer than the floor of 3, so comprehension skips the pair
- plain-language/code-review-03: the pair has 0 shared facts, fewer than the floor of 3, so comprehension skips the pair
- plain-language/code-review-04: the pair has 0 shared facts, fewer than the floor of 3, so comprehension skips the pair
- plain-language/debugging-06: the pair has 2 shared facts, fewer than the floor of 3, so comprehension skips the pair
- plain-language/debugging-07: the pair has 1 shared facts, fewer than the floor of 3, so comprehension skips the pair
- plain-language/explanation-07: the pair has 0 shared facts, fewer than the floor of 3, so comprehension skips the pair
- technical-simplified/debugging-06: the pair has 2 shared facts, fewer than the floor of 3, so comprehension skips the pair
- actionable-clarity/debugging-06: the comprehension check has no usable questions for the pair, so the pair is unscored
- clarity-flow/debugging-06: the comprehension check has no usable questions for the pair, so the pair is unscored
- classic-concise/debugging-06: the comprehension check has no usable questions for the pair, so the pair is unscored
- developer-docs/code-review-03: the comprehension check has no usable questions for the pair, so the pair is unscored
- developer-docs/debugging-06: the comprehension check has no usable questions for the pair, so the pair is unscored
- plain-language/code-review-01: the comprehension check has no usable questions for the pair, so the pair is unscored
- plain-language/code-review-03: the comprehension check has no usable questions for the pair, so the pair is unscored
- plain-language/code-review-04: the comprehension check has no usable questions for the pair, so the pair is unscored
- plain-language/debugging-06: the comprehension check has no usable questions for the pair, so the pair is unscored
- plain-language/debugging-07: the comprehension check has no usable questions for the pair, so the pair is unscored
- plain-language/explanation-07: the comprehension check has no usable questions for the pair, so the pair is unscored
- technical-simplified/debugging-06: the comprehension check has no usable questions for the pair, so the pair is unscored
- actionable-clarity: the styled answer scores worse than the unstyled answer on comprehension (5 wins, 6 losses)
- classic-concise: the styled answer scores worse than the unstyled answer on comprehension (4 wins, 10 losses)
- developer-docs: the styled answer scores worse than the unstyled answer on comprehension (7 wins, 9 losses)

# Reader-value report

The checks compare the styled answer with the unstyled answer of
the same prompt, pair by pair, as win, loss, or tie. Only pairs
whose styled answer passes the fidelity gate enter the checks.
Each judge call sees one bare text: no style name, no arm label,
and never both answers. Thus a judge cannot know which answer is
styled. The judge models differ from the writer of the answers.

Judges: reader haiku, grader opus. Comprehension asks up to 6 questions per pair, worded by both answers in balance, with 3 reader replicates per answer, ambiguity uses 3 restatements per answer, and the round-trip goes through Italian. Judged on 2026-08-10T13:52:53+00:00.

## Comprehension (weak reader)

The questions come from the shared facts of the pair, mined in both directions: the facts of the unstyled answer that survive in the styled answer, and the facts of the styled answer that the unstyled answer also states. The quiz takes half of its questions from each wording, so neither answer sets the phrasing alone, and the Sources column counts the questions per wording (unstyled/styled). A grader call turns each fact into one question, and the fact is the reference answer. The weak reader answers the questions from one answer text, once per replicate, and the grader marks every reply. Each styled replicate meets each unstyled replicate as a win, a loss, or a tie, and the pair outcome is the strict plurality, else a tie. The agreement is the plurality share, and the buried-fact rate counts "NOT IN TEXT" replies to a shared fact, per arm. The check measures extraction over shared material. Absence belongs to the content-loss report. Higher is better.

| Style | Wins | Losses | Ties | Mean delta | Agreement | Buried (styled) | Buried (unstyled) |
|---|---|---|---|---|---|---|---|
| actionable-clarity | 12 | 1 | 17 | 0.074 | 0.878 | 0.02 | 0.061 |
| clarity-flow | 6 | 7 | 17 | -0.011 | 0.833 | 0.05 | 0.026 |
| classic-concise | 4 | 5 | 21 | 0.0 | 0.833 | 0.041 | 0.041 |
| developer-docs | 3 | 4 | 20 | 0.002 | 0.881 | 0.037 | 0.027 |
| plain-language | 6 | 8 | 13 | -0.006 | 0.889 | 0.041 | 0.043 |
| technical-simplified | 4 | 8 | 12 | -0.023 | 0.88 | 0.049 | 0.028 |

The styled answer must not score worse than the unstyled answer.
- actionable-clarity: the styled answer holds (12 wins, 1 losses, 17 ties).
- clarity-flow: the styled answer scores worse (6 wins, 7 losses, 17 ties).
- classic-concise: the styled answer scores worse (4 wins, 5 losses, 21 ties).
- developer-docs: the styled answer scores worse (3 wins, 4 losses, 20 ties).
- plain-language: the styled answer scores worse (6 wins, 8 losses, 13 ties).
- technical-simplified: the styled answer scores worse (4 wins, 8 losses, 12 ties).

### actionable-clarity

| Pair | Questions | Sources (u/s) | Styled | Unstyled | Agreement | Result |
|---|---|---|---|---|---|---|
| code-review-01 | 6 | 3/3 | 1.0 | 0.778 | 1.0 | win |
| code-review-02 | 6 | 3/3 | 0.944 | 1.0 | 0.667 | tie |
| code-review-03 | 6 | 3/3 | 1.0 | 0.833 | 1.0 | win |
| code-review-04 | 6 | 3/3 | 1.0 | 0.833 | 1.0 | win |
| code-review-05 | 6 | 3/3 | 1.0 | 0.667 | 1.0 | win |
| code-review-06 | 6 | 3/3 | 1.0 | 0.722 | 1.0 | win |
| code-review-07 | 6 | 3/3 | 0.833 | 0.833 | 1.0 | tie |
| debugging-01 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-02 | 6 | 3/3 | 0.778 | 0.944 | 0.778 | loss |
| debugging-03 | 6 | 3/3 | 0.944 | 1.0 | 0.667 | tie |
| debugging-04 | 6 | 3/3 | 0.833 | 0.667 | 0.667 | win |
| debugging-05 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-06 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-07 | 6 | 3/3 | 1.0 | 0.667 | 1.0 | win |
| debugging-08 | 6 | 3/3 | 0.944 | 0.889 | 0.444 | tie |
| explanation-01 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| explanation-02 | 6 | 3/3 | 1.0 | 0.833 | 1.0 | win |
| explanation-03 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| explanation-04 | 6 | 3/3 | 0.944 | 1.0 | 0.667 | tie |
| explanation-05 | 6 | 3/3 | 1.0 | 0.889 | 0.667 | win |
| explanation-06 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| explanation-07 | 6 | 3/3 | 0.833 | 0.667 | 1.0 | win |
| explanation-08 | 6 | 3/3 | 1.0 | 0.944 | 0.667 | tie |
| summarization-01 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-02 | 6 | 3/3 | 0.944 | 0.778 | 0.778 | win |
| summarization-03 | 6 | 3/3 | 0.944 | 1.0 | 0.667 | tie |
| summarization-04 | 6 | 3/3 | 1.0 | 0.833 | 1.0 | win |
| summarization-05 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-06 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-08 | 6 | 3/3 | 1.0 | 0.944 | 0.667 | tie |

### clarity-flow

| Pair | Questions | Sources (u/s) | Styled | Unstyled | Agreement | Result |
|---|---|---|---|---|---|---|
| code-review-01 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| code-review-02 | 6 | 3/3 | 0.778 | 0.944 | 0.778 | loss |
| code-review-03 | 6 | 3/3 | 0.833 | 0.833 | 1.0 | tie |
| code-review-04 | 6 | 3/3 | 0.833 | 1.0 | 1.0 | loss |
| code-review-05 | 6 | 3/3 | 1.0 | 0.889 | 0.667 | win |
| code-review-06 | 6 | 3/3 | 0.833 | 0.778 | 0.667 | tie |
| code-review-07 | 6 | 3/3 | 0.833 | 1.0 | 1.0 | loss |
| debugging-01 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-02 | 6 | 3/3 | 1.0 | 0.944 | 0.667 | tie |
| debugging-03 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-04 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-05 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-06 | 6 | 3/3 | 1.0 | 0.778 | 1.0 | win |
| debugging-07 | 6 | 3/3 | 1.0 | 0.944 | 0.667 | tie |
| debugging-08 | 6 | 3/3 | 0.833 | 0.833 | 0.333 | tie |
| explanation-01 | 6 | 3/3 | 0.778 | 0.944 | 0.778 | loss |
| explanation-02 | 6 | 3/3 | 0.889 | 1.0 | 0.667 | loss |
| explanation-03 | 6 | 3/3 | 0.889 | 0.944 | 0.444 | tie |
| explanation-04 | 6 | 3/3 | 1.0 | 0.833 | 1.0 | win |
| explanation-05 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| explanation-06 | 6 | 3/3 | 0.667 | 1.0 | 1.0 | loss |
| explanation-07 | 6 | 3/3 | 0.833 | 1.0 | 1.0 | loss |
| explanation-08 | 6 | 3/3 | 0.944 | 0.833 | 0.667 | win |
| summarization-01 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-02 | 6 | 3/3 | 1.0 | 0.833 | 1.0 | win |
| summarization-03 | 6 | 3/3 | 0.944 | 0.944 | 0.556 | tie |
| summarization-04 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-05 | 6 | 3/3 | 0.889 | 0.944 | 0.444 | tie |
| summarization-06 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-08 | 6 | 3/3 | 1.0 | 0.889 | 0.667 | win |

### classic-concise

| Pair | Questions | Sources (u/s) | Styled | Unstyled | Agreement | Result |
|---|---|---|---|---|---|---|
| code-review-01 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| code-review-02 | 6 | 3/3 | 1.0 | 0.944 | 0.667 | tie |
| code-review-03 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| code-review-04 | 6 | 3/3 | 1.0 | 0.944 | 0.667 | tie |
| code-review-05 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| code-review-06 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| code-review-07 | 6 | 3/3 | 0.778 | 1.0 | 1.0 | loss |
| debugging-01 | 6 | 3/3 | 0.944 | 1.0 | 0.667 | tie |
| debugging-02 | 6 | 3/3 | 0.944 | 1.0 | 0.667 | tie |
| debugging-03 | 6 | 3/3 | 1.0 | 0.944 | 0.667 | tie |
| debugging-04 | 6 | 3/3 | 0.778 | 0.778 | 0.556 | tie |
| debugging-05 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-06 | 6 | 3/3 | 0.667 | 1.0 | 1.0 | loss |
| debugging-07 | 6 | 3/3 | 0.778 | 0.833 | 0.667 | tie |
| debugging-08 | 6 | 3/3 | 0.889 | 1.0 | 0.667 | loss |
| explanation-01 | 6 | 3/3 | 0.889 | 1.0 | 0.667 | loss |
| explanation-02 | 6 | 3/3 | 0.944 | 1.0 | 0.667 | tie |
| explanation-03 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| explanation-04 | 6 | 3/3 | 0.722 | 0.833 | 0.667 | loss |
| explanation-05 | 6 | 3/3 | 1.0 | 0.944 | 0.667 | tie |
| explanation-06 | 6 | 3/3 | 1.0 | 0.778 | 1.0 | win |
| explanation-07 | 6 | 3/3 | 0.833 | 0.833 | 1.0 | tie |
| explanation-08 | 6 | 3/3 | 1.0 | 0.778 | 1.0 | win |
| summarization-01 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-02 | 6 | 3/3 | 0.944 | 0.667 | 1.0 | win |
| summarization-03 | 6 | 3/3 | 0.944 | 0.889 | 0.444 | tie |
| summarization-04 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-05 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-06 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-08 | 6 | 3/3 | 1.0 | 0.889 | 0.667 | win |

### developer-docs

| Pair | Questions | Sources (u/s) | Styled | Unstyled | Agreement | Result |
|---|---|---|---|---|---|---|
| code-review-01 | 6 | 3/3 | 0.944 | 1.0 | 0.667 | tie |
| code-review-03 | 6 | 3/3 | 0.833 | 0.889 | 0.667 | tie |
| code-review-04 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| code-review-05 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| code-review-06 | 6 | 3/3 | 0.667 | 0.889 | 1.0 | loss |
| code-review-07 | 6 | 3/3 | 1.0 | 0.833 | 0.667 | win |
| debugging-01 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-02 | 6 | 3/3 | 0.833 | 0.944 | 0.667 | loss |
| debugging-03 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-04 | 6 | 3/3 | 1.0 | 0.833 | 0.667 | tie |
| debugging-05 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-07 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-08 | 6 | 3/3 | 0.833 | 1.0 | 1.0 | loss |
| explanation-01 | 6 | 3/3 | 0.778 | 0.944 | 0.778 | loss |
| explanation-02 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| explanation-03 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| explanation-04 | 6 | 3/3 | 1.0 | 0.833 | 1.0 | win |
| explanation-05 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| explanation-06 | 6 | 3/3 | 1.0 | 0.944 | 0.667 | tie |
| explanation-07 | 6 | 3/3 | 0.889 | 0.833 | 0.667 | tie |
| explanation-08 | 6 | 3/3 | 0.889 | 0.833 | 0.667 | tie |
| summarization-01 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-02 | 6 | 3/3 | 1.0 | 0.833 | 0.667 | win |
| summarization-04 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-05 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-06 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-08 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |

### plain-language

| Pair | Questions | Sources (u/s) | Styled | Unstyled | Agreement | Result |
|---|---|---|---|---|---|---|
| code-review-02 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| code-review-03 | 6 | 3/3 | 0.944 | 1.0 | 0.667 | tie |
| code-review-04 | 6 | 3/3 | 0.833 | 0.944 | 0.667 | loss |
| code-review-05 | 6 | 3/3 | 0.833 | 0.833 | 1.0 | tie |
| code-review-06 | 6 | 3/3 | 0.778 | 1.0 | 1.0 | loss |
| debugging-01 | 6 | 3/3 | 1.0 | 0.833 | 1.0 | win |
| debugging-02 | 6 | 3/3 | 1.0 | 0.722 | 1.0 | win |
| debugging-03 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-04 | 6 | 3/3 | 0.833 | 1.0 | 1.0 | loss |
| debugging-05 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-07 | 6 | 3/3 | 0.889 | 0.889 | 0.556 | tie |
| debugging-08 | 6 | 3/3 | 1.0 | 0.833 | 1.0 | win |
| explanation-01 | 6 | 3/3 | 0.833 | 1.0 | 1.0 | loss |
| explanation-02 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| explanation-03 | 6 | 3/3 | 0.833 | 0.833 | 1.0 | tie |
| explanation-04 | 6 | 3/3 | 0.722 | 0.833 | 0.667 | loss |
| explanation-05 | 6 | 3/3 | 0.944 | 0.667 | 1.0 | win |
| explanation-06 | 6 | 3/3 | 0.611 | 1.0 | 1.0 | loss |
| explanation-07 | 6 | 3/3 | 1.0 | 0.833 | 1.0 | win |
| explanation-08 | 6 | 3/3 | 0.833 | 0.944 | 0.667 | loss |
| summarization-01 | 6 | 3/3 | 1.0 | 0.944 | 0.667 | tie |
| summarization-02 | 6 | 3/3 | 0.667 | 0.722 | 0.444 | loss |
| summarization-03 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-04 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-05 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-06 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-08 | 6 | 3/3 | 1.0 | 0.889 | 0.667 | win |

### technical-simplified

| Pair | Questions | Sources (u/s) | Styled | Unstyled | Agreement | Result |
|---|---|---|---|---|---|---|
| code-review-01 | 6 | 3/3 | 1.0 | 0.889 | 0.667 | win |
| code-review-02 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| code-review-04 | 6 | 3/3 | 0.833 | 1.0 | 1.0 | loss |
| code-review-05 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| code-review-07 | 6 | 3/3 | 0.778 | 1.0 | 1.0 | loss |
| debugging-01 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-02 | 6 | 3/3 | 0.833 | 1.0 | 1.0 | loss |
| debugging-03 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-04 | 6 | 3/3 | 0.833 | 1.0 | 1.0 | loss |
| debugging-05 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-06 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| explanation-01 | 6 | 3/3 | 0.833 | 1.0 | 1.0 | loss |
| explanation-02 | 6 | 3/3 | 0.944 | 0.944 | 0.556 | tie |
| explanation-03 | 6 | 3/3 | 1.0 | 0.833 | 1.0 | win |
| explanation-04 | 6 | 3/3 | 0.944 | 1.0 | 0.667 | tie |
| explanation-05 | 6 | 3/3 | 0.889 | 0.944 | 0.444 | tie |
| explanation-06 | 6 | 3/3 | 0.778 | 0.944 | 0.778 | loss |
| explanation-07 | 6 | 3/3 | 0.778 | 0.944 | 0.778 | loss |
| summarization-01 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-02 | 6 | 3/3 | 0.889 | 0.556 | 1.0 | win |
| summarization-03 | 6 | 3/3 | 0.889 | 0.889 | 0.556 | tie |
| summarization-04 | 6 | 3/3 | 0.722 | 0.833 | 0.667 | loss |
| summarization-05 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-08 | 6 | 3/3 | 1.0 | 0.722 | 1.0 | win |

## Ambiguity (paraphrase agreement)

Independent reader calls restate one answer text in their own words. The score is the mean pairwise lexical similarity between the restatements: when the readers agree on what the text says, the text is less ambiguous. Higher is better.

| Style | Wins | Losses | Ties |
|---|---|---|---|
| actionable-clarity | 12 | 11 | 9 |
| clarity-flow | 10 | 13 | 9 |
| classic-concise | 8 | 17 | 7 |
| developer-docs | 17 | 11 | 4 |
| plain-language | 14 | 14 | 4 |
| technical-simplified | 13 | 5 | 8 |

The length confound is the correlation between the length ratio of a pair (styled words over unstyled words) and the styled advantage (the score gain of the styled arm). A negative value means that the shorter styled answers score better.
- actionable-clarity: Pearson 0.369, Spearman 0.354, over 32 pairs.
- clarity-flow: Pearson 0.557, Spearman 0.445, over 32 pairs.
- classic-concise: Pearson 0.526, Spearman 0.42, over 32 pairs.
- developer-docs: Pearson 0.303, Spearman 0.459, over 32 pairs.
- plain-language: Pearson 0.363, Spearman 0.596, over 32 pairs.
- technical-simplified: Pearson 0.362, Spearman 0.443, over 26 pairs.

### actionable-clarity

| Pair | Styled | Unstyled | Result |
|---|---|---|---|
| code-review-01 | 0.735 | 0.728 | tie |
| code-review-02 | 0.75 | 0.702 | win |
| code-review-03 | 0.674 | 0.643 | win |
| code-review-04 | 0.626 | 0.643 | tie |
| code-review-05 | 0.66 | 0.66 | tie |
| code-review-06 | 0.634 | 0.713 | loss |
| code-review-07 | 0.675 | 0.763 | loss |
| code-review-08 | 0.59 | 0.532 | win |
| debugging-01 | 0.673 | 0.657 | tie |
| debugging-02 | 0.757 | 0.802 | loss |
| debugging-03 | 0.823 | 0.788 | win |
| debugging-04 | 0.701 | 0.738 | loss |
| debugging-05 | 0.725 | 0.703 | win |
| debugging-06 | 0.648 | 0.64 | tie |
| debugging-07 | 0.574 | 0.669 | loss |
| debugging-08 | 0.678 | 0.675 | tie |
| explanation-01 | 0.7 | 0.733 | loss |
| explanation-02 | 0.734 | 0.672 | win |
| explanation-03 | 0.701 | 0.707 | tie |
| explanation-04 | 0.667 | 0.693 | loss |
| explanation-05 | 0.705 | 0.676 | win |
| explanation-06 | 0.542 | 0.595 | loss |
| explanation-07 | 0.635 | 0.585 | win |
| explanation-08 | 0.643 | 0.591 | win |
| summarization-01 | 0.639 | 0.65 | tie |
| summarization-02 | 0.644 | 0.67 | loss |
| summarization-03 | 0.632 | 0.608 | win |
| summarization-04 | 0.628 | 0.714 | loss |
| summarization-05 | 0.779 | 0.77 | tie |
| summarization-06 | 0.618 | 0.724 | loss |
| summarization-07 | 0.714 | 0.524 | win |
| summarization-08 | 0.671 | 0.617 | win |

### clarity-flow

| Pair | Styled | Unstyled | Result |
|---|---|---|---|
| code-review-01 | 0.71 | 0.728 | tie |
| code-review-02 | 0.716 | 0.702 | tie |
| code-review-03 | 0.63 | 0.643 | tie |
| code-review-04 | 0.706 | 0.643 | win |
| code-review-05 | 0.688 | 0.66 | win |
| code-review-06 | 0.692 | 0.713 | loss |
| code-review-07 | 0.661 | 0.763 | loss |
| code-review-08 | 0.694 | 0.532 | win |
| debugging-01 | 0.733 | 0.657 | win |
| debugging-02 | 0.739 | 0.802 | loss |
| debugging-03 | 0.741 | 0.788 | loss |
| debugging-04 | 0.733 | 0.738 | tie |
| debugging-05 | 0.626 | 0.703 | loss |
| debugging-06 | 0.66 | 0.64 | win |
| debugging-07 | 0.661 | 0.669 | tie |
| debugging-08 | 0.636 | 0.675 | loss |
| explanation-01 | 0.65 | 0.733 | loss |
| explanation-02 | 0.714 | 0.672 | win |
| explanation-03 | 0.636 | 0.707 | loss |
| explanation-04 | 0.689 | 0.693 | tie |
| explanation-05 | 0.614 | 0.676 | loss |
| explanation-06 | 0.595 | 0.595 | tie |
| explanation-07 | 0.62 | 0.585 | win |
| explanation-08 | 0.629 | 0.591 | win |
| summarization-01 | 0.608 | 0.65 | loss |
| summarization-02 | 0.661 | 0.67 | tie |
| summarization-03 | 0.63 | 0.608 | win |
| summarization-04 | 0.538 | 0.714 | loss |
| summarization-05 | 0.741 | 0.77 | loss |
| summarization-06 | 0.657 | 0.724 | loss |
| summarization-07 | 0.63 | 0.524 | win |
| summarization-08 | 0.615 | 0.617 | tie |

### classic-concise

| Pair | Styled | Unstyled | Result |
|---|---|---|---|
| code-review-01 | 0.622 | 0.728 | loss |
| code-review-02 | 0.659 | 0.702 | loss |
| code-review-03 | 0.632 | 0.643 | tie |
| code-review-04 | 0.635 | 0.643 | tie |
| code-review-05 | 0.669 | 0.66 | tie |
| code-review-06 | 0.583 | 0.713 | loss |
| code-review-07 | 0.66 | 0.763 | loss |
| code-review-08 | 0.677 | 0.532 | win |
| debugging-01 | 0.685 | 0.657 | win |
| debugging-02 | 0.734 | 0.802 | loss |
| debugging-03 | 0.63 | 0.788 | loss |
| debugging-04 | 0.68 | 0.738 | loss |
| debugging-05 | 0.618 | 0.703 | loss |
| debugging-06 | 0.66 | 0.64 | win |
| debugging-07 | 0.64 | 0.669 | loss |
| debugging-08 | 0.587 | 0.675 | loss |
| explanation-01 | 0.724 | 0.733 | tie |
| explanation-02 | 0.731 | 0.672 | win |
| explanation-03 | 0.695 | 0.707 | tie |
| explanation-04 | 0.652 | 0.693 | loss |
| explanation-05 | 0.652 | 0.676 | loss |
| explanation-06 | 0.544 | 0.595 | loss |
| explanation-07 | 0.578 | 0.585 | tie |
| explanation-08 | 0.608 | 0.591 | tie |
| summarization-01 | 0.691 | 0.65 | win |
| summarization-02 | 0.629 | 0.67 | loss |
| summarization-03 | 0.668 | 0.608 | win |
| summarization-04 | 0.54 | 0.714 | loss |
| summarization-05 | 0.745 | 0.77 | loss |
| summarization-06 | 0.611 | 0.724 | loss |
| summarization-07 | 0.678 | 0.524 | win |
| summarization-08 | 0.641 | 0.617 | win |

### developer-docs

| Pair | Styled | Unstyled | Result |
|---|---|---|---|
| code-review-01 | 0.642 | 0.728 | loss |
| code-review-02 | 0.825 | 0.702 | win |
| code-review-03 | 0.699 | 0.643 | win |
| code-review-04 | 0.61 | 0.643 | loss |
| code-review-05 | 0.628 | 0.66 | loss |
| code-review-06 | 0.669 | 0.713 | loss |
| code-review-07 | 0.691 | 0.763 | loss |
| code-review-08 | 0.632 | 0.532 | win |
| debugging-01 | 0.773 | 0.657 | win |
| debugging-02 | 0.716 | 0.802 | loss |
| debugging-03 | 0.831 | 0.788 | win |
| debugging-04 | 0.673 | 0.738 | loss |
| debugging-05 | 0.693 | 0.703 | tie |
| debugging-06 | 0.559 | 0.64 | loss |
| debugging-07 | 0.702 | 0.669 | win |
| debugging-08 | 0.643 | 0.675 | loss |
| explanation-01 | 0.753 | 0.733 | win |
| explanation-02 | 0.694 | 0.672 | win |
| explanation-03 | 0.718 | 0.707 | tie |
| explanation-04 | 0.68 | 0.693 | tie |
| explanation-05 | 0.723 | 0.676 | win |
| explanation-06 | 0.632 | 0.595 | win |
| explanation-07 | 0.66 | 0.585 | win |
| explanation-08 | 0.656 | 0.591 | win |
| summarization-01 | 0.715 | 0.65 | win |
| summarization-02 | 0.727 | 0.67 | win |
| summarization-03 | 0.219 | 0.608 | loss |
| summarization-04 | 0.627 | 0.714 | loss |
| summarization-05 | 0.775 | 0.77 | tie |
| summarization-06 | 0.765 | 0.724 | win |
| summarization-07 | 0.665 | 0.524 | win |
| summarization-08 | 0.639 | 0.617 | win |

### plain-language

| Pair | Styled | Unstyled | Result |
|---|---|---|---|
| code-review-01 | 0.618 | 0.728 | loss |
| code-review-02 | 0.749 | 0.702 | win |
| code-review-03 | 0.601 | 0.643 | loss |
| code-review-04 | 0.747 | 0.643 | win |
| code-review-05 | 0.617 | 0.66 | loss |
| code-review-06 | 0.643 | 0.713 | loss |
| code-review-07 | 0.381 | 0.763 | loss |
| code-review-08 | 0.251 | 0.532 | loss |
| debugging-01 | 0.798 | 0.657 | win |
| debugging-02 | 0.849 | 0.802 | win |
| debugging-03 | 0.834 | 0.788 | win |
| debugging-04 | 0.804 | 0.738 | win |
| debugging-05 | 0.728 | 0.703 | win |
| debugging-06 | 0.314 | 0.64 | loss |
| debugging-07 | 0.701 | 0.669 | win |
| debugging-08 | 0.624 | 0.675 | loss |
| explanation-01 | 0.664 | 0.733 | loss |
| explanation-02 | 0.772 | 0.672 | win |
| explanation-03 | 0.651 | 0.707 | loss |
| explanation-04 | 0.684 | 0.693 | tie |
| explanation-05 | 0.722 | 0.676 | win |
| explanation-06 | 0.601 | 0.595 | tie |
| explanation-07 | 0.554 | 0.585 | loss |
| explanation-08 | 0.611 | 0.591 | win |
| summarization-01 | 0.754 | 0.65 | win |
| summarization-02 | 0.674 | 0.67 | tie |
| summarization-03 | 0.682 | 0.608 | win |
| summarization-04 | 0.652 | 0.714 | loss |
| summarization-05 | 0.63 | 0.77 | loss |
| summarization-06 | 0.708 | 0.724 | tie |
| summarization-07 | 0.635 | 0.524 | win |
| summarization-08 | 0.596 | 0.617 | loss |

### technical-simplified

| Pair | Styled | Unstyled | Result |
|---|---|---|---|
| code-review-01 | 0.651 | 0.728 | loss |
| code-review-02 | 0.796 | 0.702 | win |
| code-review-04 | 0.713 | 0.643 | win |
| code-review-05 | 0.787 | 0.66 | win |
| code-review-07 | 0.72 | 0.763 | loss |
| code-review-08 | 0.656 | 0.532 | win |
| debugging-01 | 0.764 | 0.657 | win |
| debugging-02 | 0.704 | 0.802 | loss |
| debugging-03 | 0.826 | 0.788 | win |
| debugging-04 | 0.803 | 0.738 | win |
| debugging-05 | 0.769 | 0.703 | win |
| debugging-06 | 0.689 | 0.64 | win |
| explanation-01 | 0.704 | 0.733 | loss |
| explanation-02 | 0.749 | 0.672 | win |
| explanation-03 | 0.687 | 0.707 | tie |
| explanation-04 | 0.706 | 0.693 | tie |
| explanation-05 | 0.665 | 0.676 | tie |
| explanation-06 | 0.597 | 0.595 | tie |
| explanation-07 | 0.589 | 0.585 | tie |
| summarization-01 | 0.691 | 0.65 | win |
| summarization-02 | 0.678 | 0.67 | tie |
| summarization-03 | 0.606 | 0.608 | tie |
| summarization-04 | 0.768 | 0.714 | win |
| summarization-05 | 0.759 | 0.77 | tie |
| summarization-06 | 0.658 | 0.724 | loss |
| summarization-08 | 0.644 | 0.617 | win |

## Translation round-trip

One call translates the answer to another language, and a second call translates the result back to English. The score is the lexical loss between the original and the round-trip: simpler text survives the round-trip with less loss. Lower is better.

| Style | Wins | Losses | Ties |
|---|---|---|---|
| actionable-clarity | 8 | 10 | 14 |
| clarity-flow | 5 | 11 | 16 |
| classic-concise | 8 | 12 | 12 |
| developer-docs | 11 | 9 | 12 |
| plain-language | 6 | 8 | 18 |
| technical-simplified | 13 | 4 | 9 |

The length confound is the correlation between the length ratio of a pair (styled words over unstyled words) and the styled advantage (the score gain of the styled arm). A negative value means that the shorter styled answers score better.
- actionable-clarity: Pearson -0.005, Spearman -0.067, over 32 pairs.
- clarity-flow: Pearson 0.151, Spearman 0.144, over 32 pairs.
- classic-concise: Pearson 0.084, Spearman 0.281, over 32 pairs.
- developer-docs: Pearson 0.1, Spearman 0.161, over 32 pairs.
- plain-language: Pearson -0.038, Spearman 0.225, over 32 pairs.
- technical-simplified: Pearson 0.032, Spearman 0.101, over 26 pairs.

### actionable-clarity

| Pair | Styled | Unstyled | Result |
|---|---|---|---|
| code-review-01 | 0.067 | 0.135 | win |
| code-review-02 | 0.06 | 0.066 | tie |
| code-review-03 | 0.117 | 0.086 | loss |
| code-review-04 | 0.069 | 0.095 | win |
| code-review-05 | 0.065 | 0.077 | tie |
| code-review-06 | 0.093 | 0.14 | win |
| code-review-07 | 0.087 | 0.089 | tie |
| code-review-08 | 0.134 | 0.171 | win |
| debugging-01 | 0.143 | 0.104 | loss |
| debugging-02 | 0.037 | 0.079 | win |
| debugging-03 | 0.032 | 0.045 | tie |
| debugging-04 | 0.103 | 0.075 | loss |
| debugging-05 | 0.087 | 0.13 | win |
| debugging-06 | 0.094 | 0.096 | tie |
| debugging-07 | 0.091 | 0.091 | tie |
| debugging-08 | 0.106 | 0.11 | tie |
| explanation-01 | 0.12 | 0.123 | tie |
| explanation-02 | 0.105 | 0.083 | loss |
| explanation-03 | 0.127 | 0.093 | loss |
| explanation-04 | 0.089 | 0.09 | tie |
| explanation-05 | 0.093 | 0.112 | tie |
| explanation-06 | 0.101 | 0.101 | tie |
| explanation-07 | 0.114 | 0.121 | tie |
| explanation-08 | 0.131 | 0.147 | tie |
| summarization-01 | 0.156 | 0.107 | loss |
| summarization-02 | 0.312 | 0.218 | loss |
| summarization-03 | 0.135 | 0.133 | tie |
| summarization-04 | 0.104 | 0.076 | loss |
| summarization-05 | 0.19 | 0.07 | loss |
| summarization-06 | 0.112 | 0.163 | win |
| summarization-07 | 0.177 | 0.04 | loss |
| summarization-08 | 0.125 | 0.146 | win |

### clarity-flow

| Pair | Styled | Unstyled | Result |
|---|---|---|---|
| code-review-01 | 0.122 | 0.135 | tie |
| code-review-02 | 0.071 | 0.066 | tie |
| code-review-03 | 0.072 | 0.086 | tie |
| code-review-04 | 0.11 | 0.095 | tie |
| code-review-05 | 0.074 | 0.077 | tie |
| code-review-06 | 0.102 | 0.14 | win |
| code-review-07 | 0.116 | 0.089 | loss |
| code-review-08 | 0.134 | 0.171 | win |
| debugging-01 | 0.175 | 0.104 | loss |
| debugging-02 | 0.052 | 0.079 | win |
| debugging-03 | 0.048 | 0.045 | tie |
| debugging-04 | 0.116 | 0.075 | loss |
| debugging-05 | 0.116 | 0.13 | tie |
| debugging-06 | 0.114 | 0.096 | tie |
| debugging-07 | 0.087 | 0.091 | tie |
| debugging-08 | 0.146 | 0.11 | loss |
| explanation-01 | 0.128 | 0.123 | tie |
| explanation-02 | 0.169 | 0.083 | loss |
| explanation-03 | 0.179 | 0.093 | loss |
| explanation-04 | 0.114 | 0.09 | loss |
| explanation-05 | 0.123 | 0.112 | tie |
| explanation-06 | 0.058 | 0.101 | win |
| explanation-07 | 0.11 | 0.121 | tie |
| explanation-08 | 0.149 | 0.147 | tie |
| summarization-01 | 0.14 | 0.107 | loss |
| summarization-02 | 0.189 | 0.218 | win |
| summarization-03 | 0.115 | 0.133 | tie |
| summarization-04 | 0.063 | 0.076 | tie |
| summarization-05 | 0.074 | 0.07 | tie |
| summarization-06 | 0.207 | 0.163 | loss |
| summarization-07 | 0.145 | 0.04 | loss |
| summarization-08 | 0.207 | 0.146 | loss |

### classic-concise

| Pair | Styled | Unstyled | Result |
|---|---|---|---|
| code-review-01 | 0.113 | 0.135 | win |
| code-review-02 | 0.037 | 0.066 | win |
| code-review-03 | 0.168 | 0.086 | loss |
| code-review-04 | 0.121 | 0.095 | loss |
| code-review-05 | 0.108 | 0.077 | loss |
| code-review-06 | 0.125 | 0.14 | tie |
| code-review-07 | 0.202 | 0.089 | loss |
| code-review-08 | 0.131 | 0.171 | win |
| debugging-01 | 0.173 | 0.104 | loss |
| debugging-02 | 0.092 | 0.079 | tie |
| debugging-03 | 0.029 | 0.045 | tie |
| debugging-04 | 0.083 | 0.075 | tie |
| debugging-05 | 0.114 | 0.13 | tie |
| debugging-06 | 0.071 | 0.096 | win |
| debugging-07 | 0.071 | 0.091 | win |
| debugging-08 | 0.14 | 0.11 | loss |
| explanation-01 | 0.117 | 0.123 | tie |
| explanation-02 | 0.069 | 0.083 | tie |
| explanation-03 | 0.103 | 0.093 | tie |
| explanation-04 | 0.123 | 0.09 | loss |
| explanation-05 | 0.151 | 0.112 | loss |
| explanation-06 | 0.102 | 0.101 | tie |
| explanation-07 | 0.115 | 0.121 | tie |
| explanation-08 | 0.142 | 0.147 | tie |
| summarization-01 | 0.181 | 0.107 | loss |
| summarization-02 | 0.192 | 0.218 | win |
| summarization-03 | 0.108 | 0.133 | win |
| summarization-04 | 0.111 | 0.076 | loss |
| summarization-05 | 0.085 | 0.07 | tie |
| summarization-06 | 0.117 | 0.163 | win |
| summarization-07 | 0.2 | 0.04 | loss |
| summarization-08 | 0.274 | 0.146 | loss |

### developer-docs

| Pair | Styled | Unstyled | Result |
|---|---|---|---|
| code-review-01 | 0.032 | 0.135 | win |
| code-review-02 | 1.0 | 0.066 | loss |
| code-review-03 | 0.101 | 0.086 | tie |
| code-review-04 | 0.087 | 0.095 | tie |
| code-review-05 | 0.063 | 0.077 | tie |
| code-review-06 | 0.084 | 0.14 | win |
| code-review-07 | 0.079 | 0.089 | tie |
| code-review-08 | 0.162 | 0.171 | tie |
| debugging-01 | 0.051 | 0.104 | win |
| debugging-02 | 0.026 | 0.079 | win |
| debugging-03 | 0.067 | 0.045 | loss |
| debugging-04 | 0.04 | 0.075 | win |
| debugging-05 | 0.097 | 0.13 | win |
| debugging-06 | 0.918 | 0.096 | loss |
| debugging-07 | 0.094 | 0.091 | tie |
| debugging-08 | 0.119 | 0.11 | tie |
| explanation-01 | 0.089 | 0.123 | win |
| explanation-02 | 0.071 | 0.083 | tie |
| explanation-03 | 0.11 | 0.093 | tie |
| explanation-04 | 0.074 | 0.09 | tie |
| explanation-05 | 0.096 | 0.112 | tie |
| explanation-06 | 0.139 | 0.101 | loss |
| explanation-07 | 0.086 | 0.121 | win |
| explanation-08 | 0.096 | 0.147 | win |
| summarization-01 | 0.133 | 0.107 | loss |
| summarization-02 | 0.082 | 0.218 | win |
| summarization-03 | 0.592 | 0.133 | loss |
| summarization-04 | 0.102 | 0.076 | loss |
| summarization-05 | 0.1 | 0.07 | loss |
| summarization-06 | 0.13 | 0.163 | win |
| summarization-07 | 0.134 | 0.04 | loss |
| summarization-08 | 0.163 | 0.146 | tie |

### plain-language

| Pair | Styled | Unstyled | Result |
|---|---|---|---|
| code-review-01 | 0.154 | 0.135 | tie |
| code-review-02 | 0.067 | 0.066 | tie |
| code-review-03 | 0.072 | 0.086 | tie |
| code-review-04 | 0.079 | 0.095 | tie |
| code-review-05 | 0.075 | 0.077 | tie |
| code-review-06 | 0.064 | 0.14 | win |
| code-review-07 | 0.571 | 0.089 | loss |
| code-review-08 | 1.0 | 0.171 | loss |
| debugging-01 | 0.033 | 0.104 | win |
| debugging-02 | 0.043 | 0.079 | win |
| debugging-03 | 0.047 | 0.045 | tie |
| debugging-04 | 0.079 | 0.075 | tie |
| debugging-05 | 0.065 | 0.13 | win |
| debugging-06 | 0.12 | 0.096 | loss |
| debugging-07 | 0.094 | 0.091 | tie |
| debugging-08 | 0.101 | 0.11 | tie |
| explanation-01 | 0.128 | 0.123 | tie |
| explanation-02 | 0.092 | 0.083 | tie |
| explanation-03 | 0.106 | 0.093 | tie |
| explanation-04 | 0.08 | 0.09 | tie |
| explanation-05 | 0.079 | 0.112 | win |
| explanation-06 | 0.087 | 0.101 | tie |
| explanation-07 | 0.11 | 0.121 | tie |
| explanation-08 | 0.137 | 0.147 | tie |
| summarization-01 | 0.098 | 0.107 | tie |
| summarization-02 | 0.116 | 0.218 | win |
| summarization-03 | 0.167 | 0.133 | loss |
| summarization-04 | 0.119 | 0.076 | loss |
| summarization-05 | 0.092 | 0.07 | loss |
| summarization-06 | 0.182 | 0.163 | tie |
| summarization-07 | 0.22 | 0.04 | loss |
| summarization-08 | 0.168 | 0.146 | loss |

### technical-simplified

| Pair | Styled | Unstyled | Result |
|---|---|---|---|
| code-review-01 | 0.036 | 0.135 | win |
| code-review-02 | 0.066 | 0.066 | tie |
| code-review-04 | 0.039 | 0.095 | win |
| code-review-05 | 0.079 | 0.077 | tie |
| code-review-07 | 0.144 | 0.089 | loss |
| code-review-08 | 0.139 | 0.171 | win |
| debugging-01 | 0.0 | 0.104 | win |
| debugging-02 | 0.039 | 0.079 | win |
| debugging-03 | 0.068 | 0.045 | loss |
| debugging-04 | 0.068 | 0.075 | tie |
| debugging-05 | 0.116 | 0.13 | tie |
| debugging-06 | 0.1 | 0.096 | tie |
| explanation-01 | 0.079 | 0.123 | win |
| explanation-02 | 0.107 | 0.083 | loss |
| explanation-03 | 0.072 | 0.093 | win |
| explanation-04 | 0.107 | 0.09 | tie |
| explanation-05 | 0.131 | 0.112 | tie |
| explanation-06 | 0.134 | 0.101 | loss |
| explanation-07 | 0.089 | 0.121 | win |
| summarization-01 | 0.053 | 0.107 | win |
| summarization-02 | 0.14 | 0.218 | win |
| summarization-03 | 0.089 | 0.133 | win |
| summarization-04 | 0.067 | 0.076 | tie |
| summarization-05 | 0.041 | 0.07 | win |
| summarization-06 | 0.011 | 0.163 | win |
| summarization-08 | 0.16 | 0.146 | tie |

## Call timing

A stored call row holds two times: duration_ms is the model
time that the CLI reports, and wall_ms is the wall clock of
the subprocess. The difference is the startup cost of one CLI
call.

Calls: 556, measured: 556.
Mean duration: 11386 ms. Mean wall: 18155 ms. Mean startup: 6769 ms.

## Harness spend

A stored call row holds the token counts of its call: the
uncached input, cache-write input, cache-read input, and
output tokens. The cache-read share is the cache-read total
over the whole input total.

Calls: 556, measured: 556.
Input tokens: 3832 uncached, 519489 cache write, 2556494 cache read. Output tokens: 572998.
Cache-read share: 0.83.
Cache writes by lifetime: 519489 at 5 minutes, 0 at 1 hour.

## Reuse

Reused rows: 2718, imported from 2026-08-10c.
Live calls of this run: 556.

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

- technical-simplified/explanation-08: the pair failed the gate, excluded
- technical-simplified/code-review-03: the pair failed the gate, excluded
- technical-simplified/code-review-06: the pair failed the gate, excluded
- technical-simplified/summarization-07: the pair failed the gate, excluded
- technical-simplified/debugging-07: the pair failed the gate, excluded
- technical-simplified/debugging-08: the pair failed the gate, excluded
- actionable-clarity/code-review-08: the pair has 0 shared facts, fewer than the floor of 3, so comprehension skips the pair
- actionable-clarity/summarization-07: the pair has 0 shared facts, fewer than the floor of 3, so comprehension skips the pair
- clarity-flow/code-review-08: the pair has 0 shared facts, fewer than the floor of 3, so comprehension skips the pair
- clarity-flow/summarization-07: the pair has 0 shared facts, fewer than the floor of 3, so comprehension skips the pair
- classic-concise/code-review-08: the pair has 0 shared facts, fewer than the floor of 3, so comprehension skips the pair
- classic-concise/summarization-07: the pair has 0 shared facts, fewer than the floor of 3, so comprehension skips the pair
- developer-docs/code-review-02: the pair has 0 shared facts, fewer than the floor of 3, so comprehension skips the pair
- developer-docs/code-review-08: the pair has 0 shared facts, fewer than the floor of 3, so comprehension skips the pair
- developer-docs/debugging-06: the pair has 0 shared facts, fewer than the floor of 3, so comprehension skips the pair
- developer-docs/summarization-03: the pair has 0 shared facts, fewer than the floor of 3, so comprehension skips the pair
- developer-docs/summarization-07: the pair has 0 shared facts, fewer than the floor of 3, so comprehension skips the pair
- plain-language/code-review-01: the pair has 0 shared facts, fewer than the floor of 3, so comprehension skips the pair
- plain-language/code-review-07: the pair has 0 shared facts, fewer than the floor of 3, so comprehension skips the pair
- plain-language/code-review-08: the pair has 1 shared facts, fewer than the floor of 3, so comprehension skips the pair
- plain-language/debugging-06: the pair has 0 shared facts, fewer than the floor of 3, so comprehension skips the pair
- plain-language/summarization-07: the pair has 0 shared facts, fewer than the floor of 3, so comprehension skips the pair
- technical-simplified/code-review-08: the pair has 0 shared facts, fewer than the floor of 3, so comprehension skips the pair
- technical-simplified/summarization-06: the pair has 0 shared facts, fewer than the floor of 3, so comprehension skips the pair
- actionable-clarity/code-review-08: the comprehension check has no usable questions for the pair, so the pair is unscored
- actionable-clarity/summarization-07: the comprehension check has no usable questions for the pair, so the pair is unscored
- clarity-flow/code-review-08: the comprehension check has no usable questions for the pair, so the pair is unscored
- clarity-flow/summarization-07: the comprehension check has no usable questions for the pair, so the pair is unscored
- classic-concise/code-review-08: the comprehension check has no usable questions for the pair, so the pair is unscored
- classic-concise/summarization-07: the comprehension check has no usable questions for the pair, so the pair is unscored
- developer-docs/code-review-02: the comprehension check has no usable questions for the pair, so the pair is unscored
- developer-docs/code-review-08: the comprehension check has no usable questions for the pair, so the pair is unscored
- developer-docs/debugging-06: the comprehension check has no usable questions for the pair, so the pair is unscored
- developer-docs/summarization-03: the comprehension check has no usable questions for the pair, so the pair is unscored
- developer-docs/summarization-07: the comprehension check has no usable questions for the pair, so the pair is unscored
- plain-language/code-review-01: the comprehension check has no usable questions for the pair, so the pair is unscored
- plain-language/code-review-07: the comprehension check has no usable questions for the pair, so the pair is unscored
- plain-language/code-review-08: the comprehension check has no usable questions for the pair, so the pair is unscored
- plain-language/debugging-06: the comprehension check has no usable questions for the pair, so the pair is unscored
- plain-language/summarization-07: the comprehension check has no usable questions for the pair, so the pair is unscored
- technical-simplified/code-review-08: the comprehension check has no usable questions for the pair, so the pair is unscored
- technical-simplified/summarization-06: the comprehension check has no usable questions for the pair, so the pair is unscored
- clarity-flow: the styled answer scores worse than the unstyled answer on comprehension (6 wins, 7 losses)
- classic-concise: the styled answer scores worse than the unstyled answer on comprehension (4 wins, 5 losses)
- developer-docs: the styled answer scores worse than the unstyled answer on comprehension (3 wins, 4 losses)
- plain-language: the styled answer scores worse than the unstyled answer on comprehension (6 wins, 8 losses)
- technical-simplified: the styled answer scores worse than the unstyled answer on comprehension (4 wins, 8 losses)

# Reader-value report

The checks compare the styled answer with the unstyled answer of
the same prompt, pair by pair, as win, loss, or tie. Only pairs
whose styled answer passes the fidelity gate enter the checks.
Each judge call sees one bare text: no style name, no arm label,
and never both answers. Thus a judge cannot know which answer is
styled. The judge models differ from the writer of the answers.

Judges: reader haiku, grader opus. Comprehension asks up to 6 questions per pair, worded by both answers in balance, with 3 reader replicates per answer, ambiguity uses 3 restatements per answer, and the round-trip goes through Italian. Judged on 2026-08-08T08:26:14+00:00.

## Comprehension (weak reader)

The questions come from the shared facts of the pair, mined in both directions: the facts of the unstyled answer that survive in the styled answer, and the facts of the styled answer that the unstyled answer also states. The quiz takes half of its questions from each wording, so neither answer sets the phrasing alone, and the Sources column counts the questions per wording (unstyled/styled). A grader call turns each fact into one question, and the fact is the reference answer. The weak reader answers the questions from one answer text, once per replicate, and the grader marks every reply. Each styled replicate meets each unstyled replicate as a win, a loss, or a tie, and the pair outcome is the strict plurality, else a tie. The agreement is the plurality share, and the buried-fact rate counts "NOT IN TEXT" replies to a shared fact, per arm. The check measures extraction over shared material. Absence belongs to the content-loss report. Higher is better.

| Style | Wins | Losses | Ties | Mean delta | Agreement | Buried (styled) | Buried (unstyled) |
|---|---|---|---|---|---|---|---|
| clarity-flow | 7 | 9 | 16 | -0.017 | 0.885 | 0.033 | 0.038 |
| classic-concise | 6 | 10 | 16 | -0.024 | 0.899 | 0.057 | 0.026 |
| developer-docs | 7 | 7 | 17 | -0.009 | 0.857 | 0.054 | 0.059 |
| plain-language | 11 | 6 | 14 | 0.016 | 0.853 | 0.057 | 0.057 |
| technical-simplified | 5 | 7 | 13 | -0.038 | 0.831 | 0.069 | 0.04 |

The styled answer must not score worse than the unstyled answer.
- clarity-flow: the styled answer scores worse (7 wins, 9 losses, 16 ties).
- classic-concise: the styled answer scores worse (6 wins, 10 losses, 16 ties).
- developer-docs: the styled answer holds (7 wins, 7 losses, 17 ties).
- plain-language: the styled answer holds (11 wins, 6 losses, 14 ties).
- technical-simplified: the styled answer scores worse (5 wins, 7 losses, 13 ties).

### clarity-flow

| Pair | Questions | Sources (u/s) | Styled | Unstyled | Agreement | Result |
|---|---|---|---|---|---|---|
| code-review-01 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| code-review-02 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| code-review-03 | 6 | 3/3 | 1.0 | 0.667 | 1.0 | win |
| code-review-04 | 6 | 3/3 | 0.722 | 0.944 | 0.889 | loss |
| code-review-05 | 6 | 3/3 | 0.944 | 0.722 | 0.889 | win |
| code-review-06 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| code-review-07 | 6 | 3/3 | 0.944 | 1.0 | 0.667 | tie |
| code-review-08 | 6 | 3/3 | 1.0 | 0.944 | 0.667 | tie |
| debugging-01 | 6 | 3/3 | 0.833 | 0.833 | 1.0 | tie |
| debugging-02 | 6 | 3/3 | 0.944 | 1.0 | 0.667 | tie |
| debugging-03 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-04 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-05 | 6 | 3/3 | 0.833 | 1.0 | 1.0 | loss |
| debugging-06 | 6 | 3/3 | 0.889 | 0.833 | 0.667 | win |
| debugging-07 | 6 | 3/3 | 0.944 | 0.833 | 0.667 | win |
| debugging-08 | 6 | 3/3 | 0.722 | 0.889 | 0.778 | loss |
| explanation-01 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| explanation-02 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| explanation-03 | 6 | 3/3 | 0.667 | 0.944 | 1.0 | loss |
| explanation-04 | 6 | 3/3 | 0.722 | 1.0 | 1.0 | loss |
| explanation-05 | 6 | 3/3 | 0.889 | 1.0 | 0.667 | loss |
| explanation-06 | 6 | 3/3 | 0.889 | 1.0 | 0.667 | loss |
| explanation-07 | 6 | 3/3 | 1.0 | 0.833 | 1.0 | win |
| explanation-08 | 6 | 3/3 | 1.0 | 0.722 | 1.0 | win |
| summarization-01 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-02 | 6 | 3/3 | 0.778 | 0.944 | 0.778 | loss |
| summarization-03 | 6 | 3/3 | 1.0 | 0.889 | 0.667 | win |
| summarization-04 | 6 | 3/3 | 0.444 | 0.667 | 1.0 | loss |
| summarization-05 | 6 | 3/3 | 0.944 | 1.0 | 0.667 | tie |
| summarization-06 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-07 | 6 | 3/3 | 0.833 | 0.833 | 1.0 | tie |
| summarization-08 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |

### classic-concise

| Pair | Questions | Sources (u/s) | Styled | Unstyled | Agreement | Result |
|---|---|---|---|---|---|---|
| code-review-01 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| code-review-02 | 6 | 3/3 | 0.944 | 1.0 | 0.667 | tie |
| code-review-03 | 6 | 3/3 | 1.0 | 0.944 | 0.667 | tie |
| code-review-04 | 6 | 3/3 | 0.833 | 1.0 | 1.0 | loss |
| code-review-05 | 6 | 3/3 | 0.944 | 0.778 | 0.778 | win |
| code-review-06 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| code-review-07 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| code-review-08 | 6 | 3/3 | 1.0 | 0.944 | 0.667 | tie |
| debugging-01 | 6 | 3/3 | 0.833 | 1.0 | 1.0 | loss |
| debugging-02 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-03 | 6 | 3/3 | 0.833 | 1.0 | 0.667 | loss |
| debugging-04 | 6 | 3/3 | 0.667 | 1.0 | 1.0 | loss |
| debugging-05 | 6 | 3/3 | 0.833 | 1.0 | 1.0 | loss |
| debugging-06 | 6 | 3/3 | 0.833 | 0.833 | 1.0 | tie |
| debugging-07 | 6 | 3/3 | 0.833 | 0.667 | 1.0 | win |
| debugging-08 | 6 | 3/3 | 0.833 | 0.556 | 1.0 | win |
| explanation-01 | 6 | 3/3 | 0.5 | 0.944 | 1.0 | loss |
| explanation-02 | 6 | 3/3 | 0.833 | 1.0 | 1.0 | loss |
| explanation-03 | 6 | 3/3 | 0.833 | 1.0 | 1.0 | loss |
| explanation-04 | 6 | 3/3 | 1.0 | 0.944 | 0.667 | tie |
| explanation-05 | 6 | 3/3 | 1.0 | 0.833 | 1.0 | win |
| explanation-06 | 6 | 3/3 | 1.0 | 0.833 | 1.0 | win |
| explanation-07 | 6 | 3/3 | 1.0 | 0.944 | 0.667 | tie |
| explanation-08 | 6 | 3/3 | 1.0 | 0.833 | 1.0 | win |
| summarization-01 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-02 | 6 | 3/3 | 0.444 | 0.722 | 1.0 | loss |
| summarization-03 | 6 | 3/3 | 1.0 | 0.944 | 0.667 | tie |
| summarization-04 | 6 | 3/3 | 0.889 | 0.833 | 0.667 | tie |
| summarization-05 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-06 | 6 | 3/3 | 0.889 | 1.0 | 0.667 | loss |
| summarization-07 | 6 | 3/3 | 0.833 | 0.833 | 1.0 | tie |
| summarization-08 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |

### developer-docs

| Pair | Questions | Sources (u/s) | Styled | Unstyled | Agreement | Result |
|---|---|---|---|---|---|---|
| code-review-01 | 6 | 3/3 | 0.722 | 0.889 | 0.778 | loss |
| code-review-02 | 6 | 3/3 | 0.556 | 0.833 | 1.0 | loss |
| code-review-03 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| code-review-04 | 6 | 3/3 | 0.722 | 1.0 | 1.0 | loss |
| code-review-05 | 6 | 3/3 | 0.833 | 0.889 | 0.667 | tie |
| code-review-06 | 6 | 3/3 | 0.889 | 0.889 | 0.444 | win |
| code-review-07 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| code-review-08 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-01 | 6 | 3/3 | 0.833 | 0.833 | 1.0 | tie |
| debugging-02 | 6 | 3/3 | 1.0 | 0.944 | 0.667 | tie |
| debugging-03 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-04 | 6 | 3/3 | 1.0 | 0.833 | 1.0 | win |
| debugging-05 | 6 | 3/3 | 0.833 | 0.944 | 0.667 | loss |
| debugging-06 | 6 | 3/3 | 0.833 | 0.611 | 1.0 | win |
| debugging-07 | 6 | 3/3 | 0.444 | 0.833 | 1.0 | loss |
| debugging-08 | 6 | 3/3 | 0.944 | 0.889 | 0.444 | tie |
| explanation-01 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| explanation-02 | 6 | 3/3 | 1.0 | 0.833 | 1.0 | win |
| explanation-03 | 6 | 3/3 | 0.889 | 1.0 | 0.667 | loss |
| explanation-04 | 6 | 3/3 | 0.833 | 0.556 | 1.0 | win |
| explanation-05 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| explanation-06 | 6 | 3/3 | 0.833 | 0.944 | 0.667 | loss |
| explanation-08 | 6 | 3/3 | 0.833 | 0.889 | 0.667 | tie |
| summarization-01 | 6 | 3/3 | 0.778 | 0.667 | 0.667 | win |
| summarization-02 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-03 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-04 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-05 | 6 | 3/3 | 1.0 | 0.833 | 1.0 | win |
| summarization-06 | 6 | 3/3 | 0.944 | 0.944 | 0.556 | tie |
| summarization-07 | 6 | 3/3 | 0.833 | 0.833 | 1.0 | tie |
| summarization-08 | 6 | 3/3 | 0.889 | 0.833 | 0.667 | tie |

### plain-language

| Pair | Questions | Sources (u/s) | Styled | Unstyled | Agreement | Result |
|---|---|---|---|---|---|---|
| code-review-01 | 6 | 3/3 | 0.722 | 1.0 | 1.0 | loss |
| code-review-02 | 6 | 3/3 | 0.833 | 0.833 | 1.0 | tie |
| code-review-04 | 6 | 3/3 | 0.944 | 0.778 | 0.778 | win |
| code-review-05 | 6 | 3/3 | 0.944 | 0.889 | 0.444 | tie |
| code-review-06 | 6 | 3/3 | 1.0 | 0.944 | 0.667 | tie |
| code-review-07 | 6 | 3/3 | 1.0 | 0.889 | 0.667 | win |
| code-review-08 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-01 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-02 | 6 | 3/3 | 0.833 | 1.0 | 1.0 | loss |
| debugging-03 | 6 | 3/3 | 0.833 | 0.833 | 1.0 | tie |
| debugging-04 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-05 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-06 | 6 | 3/3 | 0.889 | 1.0 | 0.667 | tie |
| debugging-07 | 6 | 3/3 | 0.778 | 1.0 | 1.0 | loss |
| debugging-08 | 6 | 3/3 | 1.0 | 0.889 | 0.667 | win |
| explanation-01 | 6 | 3/3 | 0.833 | 1.0 | 1.0 | loss |
| explanation-02 | 6 | 3/3 | 1.0 | 0.833 | 1.0 | win |
| explanation-03 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| explanation-04 | 6 | 3/3 | 1.0 | 0.889 | 0.667 | win |
| explanation-05 | 6 | 3/3 | 1.0 | 0.833 | 1.0 | win |
| explanation-06 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| explanation-07 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| explanation-08 | 6 | 3/3 | 0.667 | 0.833 | 0.667 | loss |
| summarization-01 | 6 | 3/3 | 1.0 | 0.833 | 1.0 | win |
| summarization-02 | 6 | 3/3 | 0.778 | 0.667 | 0.556 | win |
| summarization-03 | 6 | 3/3 | 0.889 | 0.889 | 0.556 | tie |
| summarization-04 | 6 | 3/3 | 0.778 | 0.944 | 0.778 | loss |
| summarization-05 | 6 | 3/3 | 0.833 | 0.889 | 0.667 | tie |
| summarization-06 | 6 | 3/3 | 0.944 | 0.833 | 0.667 | win |
| summarization-07 | 6 | 3/3 | 0.833 | 0.667 | 1.0 | win |
| summarization-08 | 6 | 3/3 | 1.0 | 0.667 | 1.0 | win |

### technical-simplified

| Pair | Questions | Sources (u/s) | Styled | Unstyled | Agreement | Result |
|---|---|---|---|---|---|---|
| code-review-01 | 6 | 3/3 | 0.833 | 1.0 | 1.0 | loss |
| code-review-02 | 6 | 3/3 | 1.0 | 0.833 | 1.0 | win |
| code-review-03 | 6 | 3/3 | 0.833 | 0.833 | 1.0 | tie |
| code-review-04 | 6 | 3/3 | 0.667 | 1.0 | 1.0 | loss |
| code-review-05 | 6 | 3/3 | 0.778 | 0.778 | 0.556 | tie |
| code-review-06 | 6 | 3/3 | 1.0 | 0.889 | 0.667 | win |
| code-review-08 | 6 | 3/3 | 1.0 | 0.833 | 1.0 | win |
| debugging-01 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-02 | 6 | 3/3 | 0.833 | 0.944 | 0.667 | loss |
| debugging-03 | 6 | 3/3 | 0.889 | 1.0 | 0.667 | loss |
| debugging-05 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-06 | 6 | 3/3 | 0.722 | 0.778 | 0.444 | tie |
| explanation-02 | 6 | 3/3 | 0.833 | 1.0 | 0.667 | loss |
| explanation-03 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| explanation-04 | 6 | 3/3 | 0.944 | 0.889 | 0.444 | tie |
| explanation-05 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| explanation-06 | 6 | 3/3 | 0.833 | 1.0 | 1.0 | loss |
| explanation-07 | 6 | 3/3 | 0.833 | 0.833 | 1.0 | tie |
| explanation-08 | 6 | 3/3 | 1.0 | 0.889 | 0.667 | win |
| summarization-01 | 6 | 3/3 | 0.833 | 0.833 | 1.0 | tie |
| summarization-02 | 6 | 3/3 | 0.5 | 0.944 | 1.0 | loss |
| summarization-03 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-04 | 6 | 3/3 | 0.944 | 1.0 | 0.667 | tie |
| summarization-05 | 6 | 3/3 | 0.944 | 1.0 | 0.667 | tie |
| summarization-07 | 6 | 3/3 | 0.944 | 0.833 | 0.667 | win |

## Ambiguity (paraphrase agreement)

Independent reader calls restate one answer text in their own words. The score is the mean pairwise lexical similarity between the restatements: when the readers agree on what the text says, the text is less ambiguous. Higher is better.

| Style | Wins | Losses | Ties |
|---|---|---|---|
| clarity-flow | 13 | 10 | 9 |
| classic-concise | 8 | 14 | 10 |
| developer-docs | 11 | 10 | 11 |
| plain-language | 14 | 5 | 13 |
| technical-simplified | 16 | 4 | 7 |

The length confound is the correlation between the length ratio of a pair (styled words over unstyled words) and the styled advantage (the score gain of the styled arm). A negative value means that the shorter styled answers score better.
- clarity-flow: Pearson -0.06, Spearman -0.007, over 32 pairs.
- classic-concise: Pearson 0.168, Spearman 0.124, over 32 pairs.
- developer-docs: Pearson -0.329, Spearman -0.148, over 32 pairs.
- plain-language: Pearson -0.293, Spearman -0.319, over 32 pairs.
- technical-simplified: Pearson 0.465, Spearman 0.205, over 27 pairs.

### clarity-flow

| Pair | Styled | Unstyled | Result |
|---|---|---|---|
| code-review-01 | 0.605 | 0.618 | tie |
| code-review-02 | 0.722 | 0.644 | win |
| code-review-03 | 0.728 | 0.58 | win |
| code-review-04 | 0.709 | 0.718 | tie |
| code-review-05 | 0.653 | 0.674 | loss |
| code-review-06 | 0.646 | 0.669 | loss |
| code-review-07 | 0.705 | 0.604 | win |
| code-review-08 | 0.687 | 0.683 | tie |
| debugging-01 | 0.69 | 0.651 | win |
| debugging-02 | 0.72 | 0.714 | tie |
| debugging-03 | 0.751 | 0.819 | loss |
| debugging-04 | 0.66 | 0.772 | loss |
| debugging-05 | 0.599 | 0.732 | loss |
| debugging-06 | 0.713 | 0.598 | win |
| debugging-07 | 0.728 | 0.638 | win |
| debugging-08 | 0.631 | 0.54 | win |
| explanation-01 | 0.64 | 0.682 | loss |
| explanation-02 | 0.678 | 0.677 | tie |
| explanation-03 | 0.607 | 0.693 | loss |
| explanation-04 | 0.673 | 0.614 | win |
| explanation-05 | 0.674 | 0.696 | loss |
| explanation-06 | 0.641 | 0.644 | tie |
| explanation-07 | 0.638 | 0.614 | win |
| explanation-08 | 0.631 | 0.613 | tie |
| summarization-01 | 0.699 | 0.653 | win |
| summarization-02 | 0.696 | 0.709 | tie |
| summarization-03 | 0.585 | 0.675 | loss |
| summarization-04 | 0.521 | 0.693 | loss |
| summarization-05 | 0.779 | 0.744 | win |
| summarization-06 | 0.699 | 0.676 | win |
| summarization-07 | 0.719 | 0.617 | win |
| summarization-08 | 0.654 | 0.638 | tie |

### classic-concise

| Pair | Styled | Unstyled | Result |
|---|---|---|---|
| code-review-01 | 0.699 | 0.618 | win |
| code-review-02 | 0.678 | 0.644 | win |
| code-review-03 | 0.696 | 0.58 | win |
| code-review-04 | 0.64 | 0.718 | loss |
| code-review-05 | 0.712 | 0.674 | win |
| code-review-06 | 0.668 | 0.669 | tie |
| code-review-07 | 0.61 | 0.604 | tie |
| code-review-08 | 0.576 | 0.683 | loss |
| debugging-01 | 0.674 | 0.651 | win |
| debugging-02 | 0.669 | 0.714 | loss |
| debugging-03 | 0.714 | 0.819 | loss |
| debugging-04 | 0.705 | 0.772 | loss |
| debugging-05 | 0.631 | 0.732 | loss |
| debugging-06 | 0.655 | 0.598 | win |
| debugging-07 | 0.718 | 0.638 | win |
| debugging-08 | 0.556 | 0.54 | tie |
| explanation-01 | 0.632 | 0.682 | loss |
| explanation-02 | 0.688 | 0.677 | tie |
| explanation-03 | 0.699 | 0.693 | tie |
| explanation-04 | 0.687 | 0.614 | win |
| explanation-05 | 0.693 | 0.696 | tie |
| explanation-06 | 0.565 | 0.644 | loss |
| explanation-07 | 0.53 | 0.614 | loss |
| explanation-08 | 0.579 | 0.613 | loss |
| summarization-01 | 0.646 | 0.653 | tie |
| summarization-02 | 0.625 | 0.709 | loss |
| summarization-03 | 0.674 | 0.675 | tie |
| summarization-04 | 0.618 | 0.693 | loss |
| summarization-05 | 0.746 | 0.744 | tie |
| summarization-06 | 0.573 | 0.676 | loss |
| summarization-07 | 0.631 | 0.617 | tie |
| summarization-08 | 0.606 | 0.638 | loss |

### developer-docs

| Pair | Styled | Unstyled | Result |
|---|---|---|---|
| code-review-01 | 0.625 | 0.618 | tie |
| code-review-02 | 0.652 | 0.644 | tie |
| code-review-03 | 0.685 | 0.58 | win |
| code-review-04 | 0.676 | 0.718 | loss |
| code-review-05 | 0.668 | 0.674 | tie |
| code-review-06 | 0.662 | 0.669 | tie |
| code-review-07 | 0.644 | 0.604 | win |
| code-review-08 | 0.667 | 0.683 | tie |
| debugging-01 | 0.743 | 0.651 | win |
| debugging-02 | 0.707 | 0.714 | tie |
| debugging-03 | 0.815 | 0.819 | tie |
| debugging-04 | 0.702 | 0.772 | loss |
| debugging-05 | 0.751 | 0.732 | tie |
| debugging-06 | 0.724 | 0.598 | win |
| debugging-07 | 0.717 | 0.638 | win |
| debugging-08 | 0.671 | 0.54 | win |
| explanation-01 | 0.698 | 0.682 | tie |
| explanation-02 | 0.703 | 0.677 | win |
| explanation-03 | 0.719 | 0.693 | win |
| explanation-04 | 0.624 | 0.614 | tie |
| explanation-05 | 0.641 | 0.696 | loss |
| explanation-06 | 0.575 | 0.644 | loss |
| explanation-07 | 0.587 | 0.614 | loss |
| explanation-08 | 0.67 | 0.613 | win |
| summarization-01 | 0.518 | 0.653 | loss |
| summarization-02 | 0.643 | 0.709 | loss |
| summarization-03 | 0.632 | 0.675 | loss |
| summarization-04 | 0.655 | 0.693 | loss |
| summarization-05 | 0.684 | 0.744 | loss |
| summarization-06 | 0.664 | 0.676 | tie |
| summarization-07 | 0.664 | 0.617 | win |
| summarization-08 | 0.683 | 0.638 | win |

### plain-language

| Pair | Styled | Unstyled | Result |
|---|---|---|---|
| code-review-01 | 0.75 | 0.618 | win |
| code-review-02 | 0.761 | 0.644 | win |
| code-review-03 | 0.665 | 0.58 | win |
| code-review-04 | 0.724 | 0.718 | tie |
| code-review-05 | 0.677 | 0.674 | tie |
| code-review-06 | 0.611 | 0.669 | loss |
| code-review-07 | 0.739 | 0.604 | win |
| code-review-08 | 0.667 | 0.683 | tie |
| debugging-01 | 0.844 | 0.651 | win |
| debugging-02 | 0.789 | 0.714 | win |
| debugging-03 | 0.802 | 0.819 | tie |
| debugging-04 | 0.716 | 0.772 | loss |
| debugging-05 | 0.739 | 0.732 | tie |
| debugging-06 | 0.667 | 0.598 | win |
| debugging-07 | 0.667 | 0.638 | win |
| debugging-08 | 0.659 | 0.54 | win |
| explanation-01 | 0.687 | 0.682 | tie |
| explanation-02 | 0.748 | 0.677 | win |
| explanation-03 | 0.735 | 0.693 | win |
| explanation-04 | 0.697 | 0.614 | win |
| explanation-05 | 0.726 | 0.696 | win |
| explanation-06 | 0.644 | 0.644 | tie |
| explanation-07 | 0.579 | 0.614 | loss |
| explanation-08 | 0.628 | 0.613 | tie |
| summarization-01 | 0.641 | 0.653 | tie |
| summarization-02 | 0.65 | 0.709 | loss |
| summarization-03 | 0.659 | 0.675 | tie |
| summarization-04 | 0.704 | 0.693 | tie |
| summarization-05 | 0.726 | 0.744 | tie |
| summarization-06 | 0.686 | 0.676 | tie |
| summarization-07 | 0.715 | 0.617 | win |
| summarization-08 | 0.572 | 0.638 | loss |

### technical-simplified

| Pair | Styled | Unstyled | Result |
|---|---|---|---|
| code-review-01 | 0.65 | 0.618 | win |
| code-review-02 | 0.752 | 0.644 | win |
| code-review-03 | 0.612 | 0.58 | win |
| code-review-04 | 0.608 | 0.718 | loss |
| code-review-05 | 0.715 | 0.674 | win |
| code-review-06 | 0.665 | 0.669 | tie |
| code-review-07 | 0.352 | 0.604 | loss |
| code-review-08 | 0.666 | 0.683 | tie |
| debugging-01 | 0.677 | 0.651 | win |
| debugging-02 | 0.823 | 0.714 | win |
| debugging-03 | 0.841 | 0.819 | win |
| debugging-05 | 0.745 | 0.732 | tie |
| debugging-06 | 0.705 | 0.598 | win |
| debugging-08 | 0.461 | 0.54 | loss |
| explanation-02 | 0.738 | 0.677 | win |
| explanation-03 | 0.707 | 0.693 | tie |
| explanation-04 | 0.675 | 0.614 | win |
| explanation-05 | 0.743 | 0.696 | win |
| explanation-06 | 0.703 | 0.644 | win |
| explanation-07 | 0.584 | 0.614 | loss |
| explanation-08 | 0.708 | 0.613 | win |
| summarization-01 | 0.705 | 0.653 | win |
| summarization-02 | 0.711 | 0.709 | tie |
| summarization-03 | 0.657 | 0.675 | tie |
| summarization-04 | 0.689 | 0.693 | tie |
| summarization-05 | 0.794 | 0.744 | win |
| summarization-07 | 0.749 | 0.617 | win |

## Translation round-trip

One call translates the answer to another language, and a second call translates the result back to English. The score is the lexical loss between the original and the round-trip: simpler text survives the round-trip with less loss. Lower is better.

| Style | Wins | Losses | Ties |
|---|---|---|---|
| clarity-flow | 8 | 14 | 10 |
| classic-concise | 5 | 11 | 16 |
| developer-docs | 12 | 6 | 14 |
| plain-language | 11 | 10 | 11 |
| technical-simplified | 12 | 8 | 7 |

The length confound is the correlation between the length ratio of a pair (styled words over unstyled words) and the styled advantage (the score gain of the styled arm). A negative value means that the shorter styled answers score better.
- clarity-flow: Pearson -0.153, Spearman -0.077, over 32 pairs.
- classic-concise: Pearson -0.109, Spearman -0.102, over 32 pairs.
- developer-docs: Pearson 0.297, Spearman 0.295, over 32 pairs.
- plain-language: Pearson 0.143, Spearman 0.19, over 32 pairs.
- technical-simplified: Pearson 0.361, Spearman 0.152, over 27 pairs.

### clarity-flow

| Pair | Styled | Unstyled | Result |
|---|---|---|---|
| code-review-01 | 0.126 | 0.074 | loss |
| code-review-02 | 0.112 | 0.047 | loss |
| code-review-03 | 0.098 | 0.103 | tie |
| code-review-04 | 0.062 | 0.098 | win |
| code-review-05 | 0.068 | 0.102 | win |
| code-review-06 | 0.107 | 0.081 | loss |
| code-review-07 | 0.091 | 0.064 | loss |
| code-review-08 | 0.132 | 0.107 | loss |
| debugging-01 | 0.096 | 0.109 | tie |
| debugging-02 | 0.153 | 0.094 | loss |
| debugging-03 | 0.054 | 0.027 | loss |
| debugging-04 | 0.023 | 0.064 | win |
| debugging-05 | 0.083 | 0.083 | tie |
| debugging-06 | 0.087 | 0.964 | win |
| debugging-07 | 0.083 | 0.081 | tie |
| debugging-08 | 0.115 | 0.117 | tie |
| explanation-01 | 0.083 | 0.114 | win |
| explanation-02 | 0.136 | 0.099 | loss |
| explanation-03 | 0.119 | 0.134 | tie |
| explanation-04 | 0.146 | 0.072 | loss |
| explanation-05 | 0.213 | 0.134 | loss |
| explanation-06 | 0.117 | 0.1 | tie |
| explanation-07 | 0.099 | 0.078 | loss |
| explanation-08 | 0.112 | 0.118 | tie |
| summarization-01 | 0.06 | 0.134 | win |
| summarization-02 | 0.246 | 0.222 | loss |
| summarization-03 | 0.139 | 0.092 | loss |
| summarization-04 | 0.071 | 0.067 | tie |
| summarization-05 | 0.143 | 0.157 | tie |
| summarization-06 | 0.229 | 0.172 | loss |
| summarization-07 | 0.131 | 0.216 | win |
| summarization-08 | 0.147 | 0.203 | win |

### classic-concise

| Pair | Styled | Unstyled | Result |
|---|---|---|---|
| code-review-01 | 0.073 | 0.074 | tie |
| code-review-02 | 0.101 | 0.047 | loss |
| code-review-03 | 0.084 | 0.103 | tie |
| code-review-04 | 0.118 | 0.098 | loss |
| code-review-05 | 0.095 | 0.102 | tie |
| code-review-06 | 0.115 | 0.081 | loss |
| code-review-07 | 0.072 | 0.064 | tie |
| code-review-08 | 0.113 | 0.107 | tie |
| debugging-01 | 0.184 | 0.109 | loss |
| debugging-02 | 0.099 | 0.094 | tie |
| debugging-03 | 0.029 | 0.027 | tie |
| debugging-04 | 0.102 | 0.064 | loss |
| debugging-05 | 0.049 | 0.083 | win |
| debugging-06 | 0.117 | 0.964 | win |
| debugging-07 | 0.093 | 0.081 | tie |
| debugging-08 | 0.107 | 0.117 | tie |
| explanation-01 | 0.147 | 0.114 | loss |
| explanation-02 | 0.128 | 0.099 | loss |
| explanation-03 | 0.09 | 0.134 | win |
| explanation-04 | 0.109 | 0.072 | loss |
| explanation-05 | 0.138 | 0.134 | tie |
| explanation-06 | 0.084 | 0.1 | tie |
| explanation-07 | 0.093 | 0.078 | tie |
| explanation-08 | 0.09 | 0.118 | win |
| summarization-01 | 0.152 | 0.134 | tie |
| summarization-02 | 0.26 | 0.222 | loss |
| summarization-03 | 0.08 | 0.092 | tie |
| summarization-04 | 0.039 | 0.067 | win |
| summarization-05 | 0.216 | 0.157 | loss |
| summarization-06 | 0.175 | 0.172 | tie |
| summarization-07 | 0.253 | 0.216 | loss |
| summarization-08 | 0.22 | 0.203 | tie |

### developer-docs

| Pair | Styled | Unstyled | Result |
|---|---|---|---|
| code-review-01 | 0.048 | 0.074 | win |
| code-review-02 | 0.043 | 0.047 | tie |
| code-review-03 | 0.071 | 0.103 | win |
| code-review-04 | 0.1 | 0.098 | tie |
| code-review-05 | 0.066 | 0.102 | win |
| code-review-06 | 0.209 | 0.081 | loss |
| code-review-07 | 0.075 | 0.064 | tie |
| code-review-08 | 0.115 | 0.107 | tie |
| debugging-01 | 0.085 | 0.109 | win |
| debugging-02 | 0.087 | 0.094 | tie |
| debugging-03 | 0.074 | 0.027 | loss |
| debugging-04 | 0.05 | 0.064 | tie |
| debugging-05 | 0.118 | 0.083 | loss |
| debugging-06 | 0.092 | 0.964 | win |
| debugging-07 | 0.078 | 0.081 | tie |
| debugging-08 | 0.134 | 0.117 | tie |
| explanation-01 | 0.117 | 0.114 | tie |
| explanation-02 | 0.074 | 0.099 | win |
| explanation-03 | 0.127 | 0.134 | tie |
| explanation-04 | 0.098 | 0.072 | loss |
| explanation-05 | 0.102 | 0.134 | win |
| explanation-06 | 0.101 | 0.1 | tie |
| explanation-07 | 0.571 | 0.078 | loss |
| explanation-08 | 0.102 | 0.118 | tie |
| summarization-01 | 0.114 | 0.134 | win |
| summarization-02 | 0.102 | 0.222 | win |
| summarization-03 | 0.13 | 0.092 | loss |
| summarization-04 | 0.079 | 0.067 | tie |
| summarization-05 | 0.084 | 0.157 | win |
| summarization-06 | 0.155 | 0.172 | tie |
| summarization-07 | 0.151 | 0.216 | win |
| summarization-08 | 0.182 | 0.203 | win |

### plain-language

| Pair | Styled | Unstyled | Result |
|---|---|---|---|
| code-review-01 | 0.078 | 0.074 | tie |
| code-review-02 | 0.085 | 0.047 | loss |
| code-review-03 | 0.733 | 0.103 | loss |
| code-review-04 | 0.109 | 0.098 | tie |
| code-review-05 | 0.097 | 0.102 | tie |
| code-review-06 | 0.088 | 0.081 | tie |
| code-review-07 | 0.114 | 0.064 | loss |
| code-review-08 | 0.128 | 0.107 | loss |
| debugging-01 | 0.047 | 0.109 | win |
| debugging-02 | 0.061 | 0.094 | win |
| debugging-03 | 0.036 | 0.027 | tie |
| debugging-04 | 0.074 | 0.064 | tie |
| debugging-05 | 0.043 | 0.083 | win |
| debugging-06 | 0.104 | 0.964 | win |
| debugging-07 | 0.129 | 0.081 | loss |
| debugging-08 | 0.093 | 0.117 | win |
| explanation-01 | 0.106 | 0.114 | tie |
| explanation-02 | 0.094 | 0.099 | tie |
| explanation-03 | 0.145 | 0.134 | tie |
| explanation-04 | 0.091 | 0.072 | tie |
| explanation-05 | 0.069 | 0.134 | win |
| explanation-06 | 0.09 | 0.1 | tie |
| explanation-07 | 0.102 | 0.078 | loss |
| explanation-08 | 0.189 | 0.118 | loss |
| summarization-01 | 0.079 | 0.134 | win |
| summarization-02 | 0.164 | 0.222 | win |
| summarization-03 | 0.125 | 0.092 | loss |
| summarization-04 | 0.115 | 0.067 | loss |
| summarization-05 | 0.098 | 0.157 | win |
| summarization-06 | 0.217 | 0.172 | loss |
| summarization-07 | 0.138 | 0.216 | win |
| summarization-08 | 0.152 | 0.203 | win |

### technical-simplified

| Pair | Styled | Unstyled | Result |
|---|---|---|---|
| code-review-01 | 0.054 | 0.074 | tie |
| code-review-02 | 0.123 | 0.047 | loss |
| code-review-03 | 0.039 | 0.103 | win |
| code-review-04 | 0.053 | 0.098 | win |
| code-review-05 | 0.08 | 0.102 | win |
| code-review-06 | 0.103 | 0.081 | loss |
| code-review-07 | 0.959 | 0.064 | loss |
| code-review-08 | 0.151 | 0.107 | loss |
| debugging-01 | 0.0 | 0.109 | win |
| debugging-02 | 0.05 | 0.094 | win |
| debugging-03 | 0.02 | 0.027 | tie |
| debugging-05 | 0.061 | 0.083 | win |
| debugging-06 | 0.087 | 0.964 | win |
| debugging-08 | 0.754 | 0.117 | loss |
| explanation-02 | 0.083 | 0.099 | tie |
| explanation-03 | 0.077 | 0.134 | win |
| explanation-04 | 0.071 | 0.072 | tie |
| explanation-05 | 0.129 | 0.134 | tie |
| explanation-06 | 0.176 | 0.1 | loss |
| explanation-07 | 0.127 | 0.078 | loss |
| explanation-08 | 0.1 | 0.118 | tie |
| summarization-01 | 0.088 | 0.134 | win |
| summarization-02 | 0.106 | 0.222 | win |
| summarization-03 | 0.117 | 0.092 | loss |
| summarization-04 | 0.077 | 0.067 | tie |
| summarization-05 | 0.086 | 0.157 | win |
| summarization-07 | 0.176 | 0.216 | win |

## Call timing

A stored call row holds two times: duration_ms is the model
time that the CLI reports, and wall_ms is the wall clock of
the subprocess. The difference is the startup cost of one CLI
call.

Calls: 2898, measured: 2898.
Mean duration: 11173 ms. Mean wall: 26648 ms. Mean startup: 15476 ms.

## Harness spend

A stored call row holds the token counts of its call: the
uncached input, cache-write input, cache-read input, and
output tokens. The cache-read share is the cache-read total
over the whole input total.

Calls: 2898, measured: 2898.
Input tokens: 20524 uncached, 2245440 cache write, 13832523 cache read. Output tokens: 3032327.
Cache-read share: 0.859.

## Warnings

- technical-simplified/explanation-01: the pair failed the gate, excluded
- technical-simplified/summarization-06: the pair failed the gate, excluded
- technical-simplified/summarization-08: the pair failed the gate, excluded
- technical-simplified/debugging-04: the pair failed the gate, excluded
- technical-simplified/debugging-07: the pair failed the gate, excluded
- developer-docs/explanation-07: the pair has 0 shared facts, fewer than the floor of 3, so comprehension skips the pair
- plain-language/code-review-03: the pair has 1 shared facts, fewer than the floor of 3, so comprehension skips the pair
- technical-simplified/code-review-07: the pair has 0 shared facts, fewer than the floor of 3, so comprehension skips the pair
- technical-simplified/debugging-08: the pair has 0 shared facts, fewer than the floor of 3, so comprehension skips the pair
- developer-docs/explanation-07: the comprehension check has no usable questions for the pair, so the pair is unscored
- plain-language/code-review-03: the comprehension check has no usable questions for the pair, so the pair is unscored
- technical-simplified/code-review-07: the comprehension check has no usable questions for the pair, so the pair is unscored
- technical-simplified/debugging-08: the comprehension check has no usable questions for the pair, so the pair is unscored
- clarity-flow: the styled answer scores worse than the unstyled answer on comprehension (7 wins, 9 losses)
- classic-concise: the styled answer scores worse than the unstyled answer on comprehension (6 wins, 10 losses)
- technical-simplified: the styled answer scores worse than the unstyled answer on comprehension (5 wins, 7 losses)

# Reader-value report

The checks compare the styled answer with the unstyled answer of
the same prompt, pair by pair, as win, loss, or tie. Only pairs
whose styled answer passes the fidelity gate enter the checks.
Each judge call sees one bare text: no style name, no arm label,
and never both answers. Thus a judge cannot know which answer is
styled. The judge models differ from the writer of the answers.

Judges: reader haiku, grader opus. Comprehension asks up to 6 questions per pair, worded by both answers in balance, with 3 reader replicates per answer, ambiguity uses 3 restatements per answer, and the round-trip goes through Italian. Judged on 2026-08-10T07:47:44+00:00.

## Comprehension (weak reader)

The questions come from the shared facts of the pair, mined in both directions: the facts of the unstyled answer that survive in the styled answer, and the facts of the styled answer that the unstyled answer also states. The quiz takes half of its questions from each wording, so neither answer sets the phrasing alone, and the Sources column counts the questions per wording (unstyled/styled). A grader call turns each fact into one question, and the fact is the reference answer. The weak reader answers the questions from one answer text, once per replicate, and the grader marks every reply. Each styled replicate meets each unstyled replicate as a win, a loss, or a tie, and the pair outcome is the strict plurality, else a tie. The agreement is the plurality share, and the buried-fact rate counts "NOT IN TEXT" replies to a shared fact, per arm. The check measures extraction over shared material. Absence belongs to the content-loss report. Higher is better.

| Style | Wins | Losses | Ties | Mean delta | Agreement | Buried (styled) | Buried (unstyled) |
|---|---|---|---|---|---|---|---|
| clarity-flow | 8 | 3 | 18 | 0.031 | 0.805 | 0.029 | 0.05 |
| classic-concise | 4 | 6 | 20 | -0.037 | 0.922 | 0.035 | 0.024 |
| developer-docs | 3 | 6 | 20 | -0.017 | 0.87 | 0.021 | 0.021 |
| plain-language | 7 | 5 | 18 | 0.004 | 0.944 | 0.026 | 0.031 |
| technical-simplified | 4 | 3 | 19 | 0.002 | 0.868 | 0.028 | 0.021 |

The styled answer must not score worse than the unstyled answer.
- clarity-flow: the styled answer holds (8 wins, 3 losses, 18 ties).
- classic-concise: the styled answer scores worse (4 wins, 6 losses, 20 ties).
- developer-docs: the styled answer scores worse (3 wins, 6 losses, 20 ties).
- plain-language: the styled answer holds (7 wins, 5 losses, 18 ties).
- technical-simplified: the styled answer holds (4 wins, 3 losses, 19 ties).

### clarity-flow

| Pair | Questions | Sources (u/s) | Styled | Unstyled | Agreement | Result |
|---|---|---|---|---|---|---|
| code-review-01 | 6 | 3/3 | 1.0 | 0.889 | 0.667 | win |
| code-review-02 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| code-review-03 | 6 | 3/3 | 0.833 | 1.0 | 1.0 | loss |
| code-review-04 | 6 | 3/3 | 1.0 | 0.944 | 0.667 | tie |
| code-review-05 | 6 | 3/3 | 0.944 | 1.0 | 0.667 | tie |
| code-review-06 | 6 | 3/3 | 0.944 | 0.667 | 1.0 | win |
| code-review-07 | 6 | 3/3 | 1.0 | 0.833 | 1.0 | win |
| code-review-08 | 6 | 3/3 | 0.944 | 0.778 | 0.778 | win |
| debugging-01 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-02 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-03 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-04 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-05 | 6 | 3/3 | 0.833 | 1.0 | 1.0 | loss |
| explanation-01 | 6 | 3/3 | 0.889 | 1.0 | 0.667 | loss |
| explanation-02 | 6 | 3/3 | 0.944 | 0.833 | 0.556 | win |
| explanation-03 | 6 | 3/3 | 0.944 | 1.0 | 0.667 | tie |
| explanation-04 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| explanation-05 | 6 | 3/3 | 0.944 | 0.889 | 0.444 | tie |
| explanation-06 | 6 | 3/3 | 1.0 | 0.944 | 0.667 | tie |
| explanation-07 | 6 | 3/3 | 1.0 | 0.889 | 0.667 | win |
| explanation-08 | 6 | 3/3 | 1.0 | 0.889 | 0.667 | win |
| summarization-01 | 6 | 3/3 | 0.778 | 0.833 | 0.667 | tie |
| summarization-02 | 6 | 3/3 | 0.722 | 0.778 | 0.444 | tie |
| summarization-03 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-04 | 6 | 3/3 | 0.833 | 0.722 | 0.667 | tie |
| summarization-05 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-06 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-07 | 6 | 3/3 | 0.944 | 0.889 | 0.444 | tie |
| summarization-08 | 6 | 3/3 | 1.0 | 0.833 | 1.0 | win |

### classic-concise

| Pair | Questions | Sources (u/s) | Styled | Unstyled | Agreement | Result |
|---|---|---|---|---|---|---|
| code-review-01 | 6 | 3/3 | 1.0 | 0.722 | 1.0 | win |
| code-review-02 | 6 | 3/3 | 0.833 | 0.833 | 1.0 | tie |
| code-review-03 | 6 | 3/3 | 0.722 | 1.0 | 0.667 | loss |
| code-review-04 | 6 | 3/3 | 0.444 | 1.0 | 1.0 | loss |
| code-review-05 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| code-review-06 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| code-review-07 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| code-review-08 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-01 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-02 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-03 | 6 | 3/3 | 0.833 | 1.0 | 1.0 | loss |
| debugging-04 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-05 | 6 | 3/3 | 0.722 | 1.0 | 1.0 | loss |
| debugging-08 | 6 | 3/3 | 0.667 | 0.778 | 0.556 | loss |
| explanation-01 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| explanation-02 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| explanation-03 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| explanation-04 | 6 | 3/3 | 0.667 | 1.0 | 1.0 | loss |
| explanation-05 | 6 | 3/3 | 1.0 | 0.889 | 0.667 | win |
| explanation-06 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| explanation-07 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| explanation-08 | 6 | 3/3 | 0.833 | 0.889 | 0.667 | tie |
| summarization-01 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-02 | 6 | 3/3 | 0.944 | 0.833 | 0.667 | win |
| summarization-03 | 6 | 3/3 | 1.0 | 0.778 | 1.0 | win |
| summarization-04 | 6 | 3/3 | 0.889 | 0.944 | 0.444 | tie |
| summarization-05 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-06 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-07 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-08 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |

### developer-docs

| Pair | Questions | Sources (u/s) | Styled | Unstyled | Agreement | Result |
|---|---|---|---|---|---|---|
| code-review-01 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| code-review-02 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| code-review-03 | 6 | 3/3 | 0.944 | 1.0 | 0.667 | tie |
| code-review-05 | 6 | 3/3 | 0.778 | 0.944 | 0.778 | loss |
| code-review-06 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| code-review-07 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| code-review-08 | 6 | 3/3 | 0.833 | 0.778 | 0.667 | tie |
| debugging-01 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-02 | 6 | 3/3 | 0.889 | 1.0 | 0.667 | loss |
| debugging-03 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-04 | 6 | 3/3 | 1.0 | 0.833 | 1.0 | win |
| debugging-05 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-08 | 6 | 3/3 | 1.0 | 0.889 | 0.667 | win |
| explanation-01 | 6 | 3/3 | 0.833 | 1.0 | 1.0 | loss |
| explanation-02 | 6 | 3/3 | 1.0 | 0.944 | 0.667 | tie |
| explanation-03 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| explanation-04 | 6 | 3/3 | 0.833 | 1.0 | 1.0 | loss |
| explanation-05 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| explanation-06 | 6 | 3/3 | 0.944 | 1.0 | 0.667 | tie |
| explanation-07 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| explanation-08 | 6 | 3/3 | 0.889 | 0.944 | 0.444 | tie |
| summarization-01 | 6 | 3/3 | 0.833 | 0.833 | 1.0 | tie |
| summarization-02 | 6 | 3/3 | 1.0 | 0.944 | 0.667 | tie |
| summarization-03 | 6 | 3/3 | 1.0 | 0.833 | 1.0 | win |
| summarization-04 | 6 | 3/3 | 0.944 | 1.0 | 0.667 | tie |
| summarization-05 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-06 | 6 | 3/3 | 0.833 | 1.0 | 1.0 | loss |
| summarization-07 | 6 | 3/3 | 0.833 | 0.944 | 0.667 | loss |
| summarization-08 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |

### plain-language

| Pair | Questions | Sources (u/s) | Styled | Unstyled | Agreement | Result |
|---|---|---|---|---|---|---|
| code-review-01 | 6 | 3/3 | 1.0 | 0.833 | 1.0 | win |
| code-review-02 | 6 | 3/3 | 1.0 | 0.833 | 1.0 | win |
| code-review-03 | 6 | 3/3 | 1.0 | 0.889 | 0.667 | win |
| code-review-04 | 6 | 3/3 | 0.611 | 1.0 | 1.0 | loss |
| code-review-05 | 6 | 3/3 | 1.0 | 0.833 | 1.0 | win |
| code-review-06 | 6 | 3/3 | 1.0 | 0.944 | 0.667 | tie |
| code-review-07 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| code-review-08 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-01 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-02 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-03 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-04 | 6 | 3/3 | 0.778 | 1.0 | 1.0 | loss |
| debugging-05 | 6 | 3/3 | 0.667 | 0.833 | 1.0 | loss |
| debugging-08 | 6 | 3/3 | 0.667 | 0.833 | 0.667 | loss |
| explanation-01 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| explanation-02 | 6 | 3/3 | 1.0 | 0.889 | 0.667 | win |
| explanation-03 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| explanation-04 | 6 | 3/3 | 0.833 | 1.0 | 1.0 | loss |
| explanation-05 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| explanation-06 | 6 | 3/3 | 1.0 | 0.944 | 0.667 | tie |
| explanation-07 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| explanation-08 | 6 | 3/3 | 0.889 | 0.667 | 1.0 | win |
| summarization-01 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-02 | 6 | 3/3 | 1.0 | 0.833 | 1.0 | win |
| summarization-03 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-04 | 6 | 3/3 | 0.833 | 0.833 | 1.0 | tie |
| summarization-05 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-06 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-07 | 6 | 3/3 | 0.833 | 0.833 | 1.0 | tie |
| summarization-08 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |

### technical-simplified

| Pair | Questions | Sources (u/s) | Styled | Unstyled | Agreement | Result |
|---|---|---|---|---|---|---|
| code-review-01 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| code-review-02 | 6 | 3/3 | 0.889 | 1.0 | 0.667 | loss |
| code-review-03 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| code-review-04 | 6 | 3/3 | 0.667 | 0.833 | 1.0 | loss |
| code-review-05 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| code-review-06 | 6 | 3/3 | 0.944 | 0.722 | 0.889 | win |
| code-review-07 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| code-review-08 | 6 | 3/3 | 0.944 | 0.833 | 0.667 | win |
| debugging-01 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-02 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-03 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-04 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-05 | 6 | 3/3 | 0.944 | 1.0 | 0.667 | tie |
| debugging-08 | 6 | 3/3 | 0.722 | 0.944 | 0.889 | loss |
| explanation-02 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| explanation-03 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| explanation-04 | 6 | 3/3 | 0.889 | 0.722 | 0.778 | win |
| explanation-05 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| explanation-06 | 6 | 3/3 | 0.833 | 0.833 | 1.0 | tie |
| explanation-07 | 6 | 3/3 | 0.833 | 0.833 | 0.333 | tie |
| summarization-01 | 6 | 3/3 | 0.944 | 0.889 | 0.444 | tie |
| summarization-02 | 6 | 3/3 | 0.944 | 0.944 | 0.556 | tie |
| summarization-03 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-04 | 6 | 3/3 | 0.833 | 0.833 | 1.0 | tie |
| summarization-05 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-07 | 6 | 3/3 | 0.833 | 0.778 | 0.667 | win |

## Ambiguity (paraphrase agreement)

Independent reader calls restate one answer text in their own words. The score is the mean pairwise lexical similarity between the restatements: when the readers agree on what the text says, the text is less ambiguous. Higher is better.

| Style | Wins | Losses | Ties |
|---|---|---|---|
| clarity-flow | 11 | 14 | 7 |
| classic-concise | 11 | 10 | 11 |
| developer-docs | 16 | 14 | 2 |
| plain-language | 17 | 5 | 10 |
| technical-simplified | 16 | 7 | 6 |

The length confound is the correlation between the length ratio of a pair (styled words over unstyled words) and the styled advantage (the score gain of the styled arm). A negative value means that the shorter styled answers score better.
- clarity-flow: Pearson 0.214, Spearman 0.432, over 32 pairs.
- classic-concise: Pearson 0.528, Spearman 0.304, over 32 pairs.
- developer-docs: Pearson 0.295, Spearman 0.259, over 32 pairs.
- plain-language: Pearson 0.382, Spearman 0.196, over 32 pairs.
- technical-simplified: Pearson 0.545, Spearman 0.132, over 29 pairs.

### clarity-flow

| Pair | Styled | Unstyled | Result |
|---|---|---|---|
| code-review-01 | 0.638 | 0.699 | loss |
| code-review-02 | 0.679 | 0.742 | loss |
| code-review-03 | 0.685 | 0.669 | tie |
| code-review-04 | 0.613 | 0.696 | loss |
| code-review-05 | 0.696 | 0.636 | win |
| code-review-06 | 0.653 | 0.656 | tie |
| code-review-07 | 0.669 | 0.701 | loss |
| code-review-08 | 0.621 | 0.673 | loss |
| debugging-01 | 0.732 | 0.625 | win |
| debugging-02 | 0.728 | 0.774 | loss |
| debugging-03 | 0.62 | 0.846 | loss |
| debugging-04 | 0.769 | 0.667 | win |
| debugging-05 | 0.684 | 0.696 | tie |
| debugging-06 | 0.596 | 0.573 | win |
| debugging-07 | 0.602 | 0.519 | win |
| debugging-08 | 0.49 | 0.661 | loss |
| explanation-01 | 0.658 | 0.745 | loss |
| explanation-02 | 0.657 | 0.692 | loss |
| explanation-03 | 0.694 | 0.628 | win |
| explanation-04 | 0.655 | 0.688 | loss |
| explanation-05 | 0.699 | 0.688 | tie |
| explanation-06 | 0.62 | 0.652 | loss |
| explanation-07 | 0.588 | 0.6 | tie |
| explanation-08 | 0.605 | 0.559 | win |
| summarization-01 | 0.633 | 0.637 | tie |
| summarization-02 | 0.641 | 0.57 | win |
| summarization-03 | 0.648 | 0.668 | loss |
| summarization-04 | 0.744 | 0.574 | win |
| summarization-05 | 0.67 | 0.746 | loss |
| summarization-06 | 0.651 | 0.649 | tie |
| summarization-07 | 0.691 | 0.671 | win |
| summarization-08 | 0.644 | 0.595 | win |

### classic-concise

| Pair | Styled | Unstyled | Result |
|---|---|---|---|
| code-review-01 | 0.609 | 0.699 | loss |
| code-review-02 | 0.779 | 0.742 | win |
| code-review-03 | 0.691 | 0.669 | win |
| code-review-04 | 0.757 | 0.696 | win |
| code-review-05 | 0.64 | 0.636 | tie |
| code-review-06 | 0.674 | 0.656 | tie |
| code-review-07 | 0.708 | 0.701 | tie |
| code-review-08 | 0.701 | 0.673 | win |
| debugging-01 | 0.624 | 0.625 | tie |
| debugging-02 | 0.689 | 0.774 | loss |
| debugging-03 | 0.768 | 0.846 | loss |
| debugging-04 | 0.781 | 0.667 | win |
| debugging-05 | 0.801 | 0.696 | win |
| debugging-06 | 0.666 | 0.573 | win |
| debugging-07 | 0.695 | 0.519 | win |
| debugging-08 | 0.634 | 0.661 | loss |
| explanation-01 | 0.705 | 0.745 | loss |
| explanation-02 | 0.595 | 0.692 | loss |
| explanation-03 | 0.629 | 0.628 | tie |
| explanation-04 | 0.608 | 0.688 | loss |
| explanation-05 | 0.644 | 0.688 | loss |
| explanation-06 | 0.617 | 0.652 | loss |
| explanation-07 | 0.61 | 0.6 | tie |
| explanation-08 | 0.604 | 0.559 | win |
| summarization-01 | 0.643 | 0.637 | tie |
| summarization-02 | 0.576 | 0.57 | tie |
| summarization-03 | 0.665 | 0.668 | tie |
| summarization-04 | 0.571 | 0.574 | tie |
| summarization-05 | 0.807 | 0.746 | win |
| summarization-06 | 0.614 | 0.649 | loss |
| summarization-07 | 0.68 | 0.671 | tie |
| summarization-08 | 0.644 | 0.595 | win |

### developer-docs

| Pair | Styled | Unstyled | Result |
|---|---|---|---|
| code-review-01 | 0.757 | 0.699 | win |
| code-review-02 | 0.659 | 0.742 | loss |
| code-review-03 | 0.73 | 0.669 | win |
| code-review-04 | 0.421 | 0.696 | loss |
| code-review-05 | 0.665 | 0.636 | win |
| code-review-06 | 0.677 | 0.656 | win |
| code-review-07 | 0.653 | 0.701 | loss |
| code-review-08 | 0.639 | 0.673 | loss |
| debugging-01 | 0.585 | 0.625 | loss |
| debugging-02 | 0.754 | 0.774 | loss |
| debugging-03 | 0.814 | 0.846 | loss |
| debugging-04 | 0.69 | 0.667 | win |
| debugging-05 | 0.737 | 0.696 | win |
| debugging-06 | 0.643 | 0.573 | win |
| debugging-07 | 0.622 | 0.519 | win |
| debugging-08 | 0.627 | 0.661 | loss |
| explanation-01 | 0.71 | 0.745 | loss |
| explanation-02 | 0.735 | 0.692 | win |
| explanation-03 | 0.716 | 0.628 | win |
| explanation-04 | 0.654 | 0.688 | loss |
| explanation-05 | 0.69 | 0.688 | tie |
| explanation-06 | 0.677 | 0.652 | win |
| explanation-07 | 0.576 | 0.6 | loss |
| explanation-08 | 0.634 | 0.559 | win |
| summarization-01 | 0.537 | 0.637 | loss |
| summarization-02 | 0.687 | 0.57 | win |
| summarization-03 | 0.661 | 0.668 | tie |
| summarization-04 | 0.707 | 0.574 | win |
| summarization-05 | 0.702 | 0.746 | loss |
| summarization-06 | 0.7 | 0.649 | win |
| summarization-07 | 0.628 | 0.671 | loss |
| summarization-08 | 0.616 | 0.595 | win |

### plain-language

| Pair | Styled | Unstyled | Result |
|---|---|---|---|
| code-review-01 | 0.717 | 0.699 | tie |
| code-review-02 | 0.747 | 0.742 | tie |
| code-review-03 | 0.614 | 0.669 | loss |
| code-review-04 | 0.716 | 0.696 | tie |
| code-review-05 | 0.724 | 0.636 | win |
| code-review-06 | 0.631 | 0.656 | loss |
| code-review-07 | 0.646 | 0.701 | loss |
| code-review-08 | 0.674 | 0.673 | tie |
| debugging-01 | 0.799 | 0.625 | win |
| debugging-02 | 0.81 | 0.774 | win |
| debugging-03 | 0.867 | 0.846 | win |
| debugging-04 | 0.787 | 0.667 | win |
| debugging-05 | 0.731 | 0.696 | win |
| debugging-06 | 0.679 | 0.573 | win |
| debugging-07 | 0.649 | 0.519 | win |
| debugging-08 | 0.66 | 0.661 | tie |
| explanation-01 | 0.696 | 0.745 | loss |
| explanation-02 | 0.66 | 0.692 | loss |
| explanation-03 | 0.725 | 0.628 | win |
| explanation-04 | 0.71 | 0.688 | win |
| explanation-05 | 0.684 | 0.688 | tie |
| explanation-06 | 0.634 | 0.652 | tie |
| explanation-07 | 0.618 | 0.6 | tie |
| explanation-08 | 0.652 | 0.559 | win |
| summarization-01 | 0.747 | 0.637 | win |
| summarization-02 | 0.598 | 0.57 | win |
| summarization-03 | 0.666 | 0.668 | tie |
| summarization-04 | 0.627 | 0.574 | win |
| summarization-05 | 0.737 | 0.746 | tie |
| summarization-06 | 0.7 | 0.649 | win |
| summarization-07 | 0.72 | 0.671 | win |
| summarization-08 | 0.724 | 0.595 | win |

### technical-simplified

| Pair | Styled | Unstyled | Result |
|---|---|---|---|
| code-review-01 | 0.663 | 0.699 | loss |
| code-review-02 | 0.759 | 0.742 | tie |
| code-review-03 | 0.78 | 0.669 | win |
| code-review-04 | 0.713 | 0.696 | tie |
| code-review-05 | 0.746 | 0.636 | win |
| code-review-06 | 0.669 | 0.656 | tie |
| code-review-07 | 0.732 | 0.701 | win |
| code-review-08 | 0.693 | 0.673 | win |
| debugging-01 | 0.697 | 0.625 | win |
| debugging-02 | 0.805 | 0.774 | win |
| debugging-03 | 0.787 | 0.846 | loss |
| debugging-04 | 0.738 | 0.667 | win |
| debugging-05 | 0.773 | 0.696 | win |
| debugging-06 | 0.697 | 0.573 | win |
| debugging-07 | 0.725 | 0.519 | win |
| debugging-08 | 0.673 | 0.661 | tie |
| explanation-02 | 0.733 | 0.692 | win |
| explanation-03 | 0.718 | 0.628 | win |
| explanation-04 | 0.704 | 0.688 | tie |
| explanation-05 | 0.731 | 0.688 | win |
| explanation-06 | 0.632 | 0.652 | loss |
| explanation-07 | 0.641 | 0.6 | win |
| explanation-08 | 0.528 | 0.559 | loss |
| summarization-01 | 0.686 | 0.637 | win |
| summarization-02 | 0.533 | 0.57 | loss |
| summarization-03 | 0.671 | 0.668 | tie |
| summarization-04 | 0.683 | 0.574 | win |
| summarization-05 | 0.697 | 0.746 | loss |
| summarization-07 | 0.634 | 0.671 | loss |

## Translation round-trip

One call translates the answer to another language, and a second call translates the result back to English. The score is the lexical loss between the original and the round-trip: simpler text survives the round-trip with less loss. Lower is better.

| Style | Wins | Losses | Ties |
|---|---|---|---|
| clarity-flow | 11 | 8 | 13 |
| classic-concise | 6 | 19 | 7 |
| developer-docs | 15 | 5 | 12 |
| plain-language | 12 | 9 | 11 |
| technical-simplified | 14 | 5 | 10 |

The length confound is the correlation between the length ratio of a pair (styled words over unstyled words) and the styled advantage (the score gain of the styled arm). A negative value means that the shorter styled answers score better.
- clarity-flow: Pearson 0.689, Spearman 0.21, over 32 pairs.
- classic-concise: Pearson 0.904, Spearman -0.08, over 32 pairs.
- developer-docs: Pearson 0.567, Spearman 0.426, over 32 pairs.
- plain-language: Pearson 0.908, Spearman 0.198, over 32 pairs.
- technical-simplified: Pearson 0.923, Spearman 0.603, over 29 pairs.

### clarity-flow

| Pair | Styled | Unstyled | Result |
|---|---|---|---|
| code-review-01 | 0.066 | 0.122 | win |
| code-review-02 | 0.065 | 0.077 | tie |
| code-review-03 | 0.08 | 0.083 | tie |
| code-review-04 | 0.076 | 0.113 | win |
| code-review-05 | 0.089 | 0.073 | tie |
| code-review-06 | 0.089 | 0.059 | loss |
| code-review-07 | 0.119 | 0.128 | tie |
| code-review-08 | 0.126 | 0.121 | tie |
| debugging-01 | 0.105 | 0.132 | win |
| debugging-02 | 0.11 | 0.123 | tie |
| debugging-03 | 0.059 | 0.051 | tie |
| debugging-04 | 0.056 | 0.085 | win |
| debugging-05 | 0.078 | 0.117 | win |
| debugging-06 | 0.08 | 0.455 | win |
| debugging-07 | 0.114 | 0.5 | win |
| debugging-08 | 0.706 | 0.102 | loss |
| explanation-01 | 0.083 | 0.122 | win |
| explanation-02 | 0.103 | 0.058 | loss |
| explanation-03 | 0.116 | 0.083 | loss |
| explanation-04 | 0.134 | 0.081 | loss |
| explanation-05 | 0.137 | 0.131 | tie |
| explanation-06 | 0.113 | 0.072 | loss |
| explanation-07 | 0.093 | 0.097 | tie |
| explanation-08 | 0.115 | 0.098 | tie |
| summarization-01 | 0.111 | 0.13 | tie |
| summarization-02 | 0.191 | 0.145 | loss |
| summarization-03 | 0.128 | 0.115 | tie |
| summarization-04 | 0.06 | 0.084 | win |
| summarization-05 | 0.131 | 0.153 | win |
| summarization-06 | 0.211 | 0.198 | tie |
| summarization-07 | 0.14 | 0.163 | win |
| summarization-08 | 0.182 | 0.136 | loss |

### classic-concise

| Pair | Styled | Unstyled | Result |
|---|---|---|---|
| code-review-01 | 0.081 | 0.122 | win |
| code-review-02 | 0.075 | 0.077 | tie |
| code-review-03 | 0.127 | 0.083 | loss |
| code-review-04 | 0.141 | 0.113 | loss |
| code-review-05 | 0.094 | 0.073 | loss |
| code-review-06 | 0.082 | 0.059 | loss |
| code-review-07 | 0.13 | 0.128 | tie |
| code-review-08 | 0.154 | 0.121 | loss |
| debugging-01 | 0.255 | 0.132 | loss |
| debugging-02 | 0.094 | 0.123 | win |
| debugging-03 | 0.041 | 0.051 | tie |
| debugging-04 | 0.098 | 0.085 | tie |
| debugging-05 | 0.118 | 0.117 | tie |
| debugging-06 | 0.109 | 0.455 | win |
| debugging-07 | 0.081 | 0.5 | win |
| debugging-08 | 0.143 | 0.102 | loss |
| explanation-01 | 0.152 | 0.122 | loss |
| explanation-02 | 0.119 | 0.058 | loss |
| explanation-03 | 0.125 | 0.083 | loss |
| explanation-04 | 0.158 | 0.081 | loss |
| explanation-05 | 0.108 | 0.131 | win |
| explanation-06 | 0.102 | 0.072 | loss |
| explanation-07 | 0.147 | 0.097 | loss |
| explanation-08 | 0.074 | 0.098 | win |
| summarization-01 | 0.16 | 0.13 | loss |
| summarization-02 | 0.234 | 0.145 | loss |
| summarization-03 | 0.198 | 0.115 | loss |
| summarization-04 | 0.077 | 0.084 | tie |
| summarization-05 | 0.227 | 0.153 | loss |
| summarization-06 | 0.193 | 0.198 | tie |
| summarization-07 | 0.299 | 0.163 | loss |
| summarization-08 | 0.197 | 0.136 | loss |

### developer-docs

| Pair | Styled | Unstyled | Result |
|---|---|---|---|
| code-review-01 | 0.058 | 0.122 | win |
| code-review-02 | 0.082 | 0.077 | tie |
| code-review-03 | 0.048 | 0.083 | win |
| code-review-04 | 0.915 | 0.113 | loss |
| code-review-05 | 0.059 | 0.073 | tie |
| code-review-06 | 0.074 | 0.059 | tie |
| code-review-07 | 0.061 | 0.128 | win |
| code-review-08 | 0.136 | 0.121 | tie |
| debugging-01 | 0.061 | 0.132 | win |
| debugging-02 | 0.074 | 0.123 | win |
| debugging-03 | 0.037 | 0.051 | tie |
| debugging-04 | 0.058 | 0.085 | win |
| debugging-05 | 0.065 | 0.117 | win |
| debugging-06 | 0.088 | 0.455 | win |
| debugging-07 | 0.095 | 0.5 | win |
| debugging-08 | 0.145 | 0.102 | loss |
| explanation-01 | 0.11 | 0.122 | tie |
| explanation-02 | 0.068 | 0.058 | tie |
| explanation-03 | 0.124 | 0.083 | loss |
| explanation-04 | 0.065 | 0.081 | tie |
| explanation-05 | 0.069 | 0.131 | win |
| explanation-06 | 0.118 | 0.072 | loss |
| explanation-07 | 0.126 | 0.097 | loss |
| explanation-08 | 0.068 | 0.098 | win |
| summarization-01 | 0.085 | 0.13 | win |
| summarization-02 | 0.092 | 0.145 | win |
| summarization-03 | 0.118 | 0.115 | tie |
| summarization-04 | 0.071 | 0.084 | tie |
| summarization-05 | 0.088 | 0.153 | win |
| summarization-06 | 0.192 | 0.198 | tie |
| summarization-07 | 0.128 | 0.163 | win |
| summarization-08 | 0.148 | 0.136 | tie |

### plain-language

| Pair | Styled | Unstyled | Result |
|---|---|---|---|
| code-review-01 | 0.046 | 0.122 | win |
| code-review-02 | 0.098 | 0.077 | loss |
| code-review-03 | 0.081 | 0.083 | tie |
| code-review-04 | 0.082 | 0.113 | win |
| code-review-05 | 0.09 | 0.073 | tie |
| code-review-06 | 0.095 | 0.059 | loss |
| code-review-07 | 0.085 | 0.128 | win |
| code-review-08 | 0.139 | 0.121 | tie |
| debugging-01 | 0.057 | 0.132 | win |
| debugging-02 | 0.028 | 0.123 | win |
| debugging-03 | 0.046 | 0.051 | tie |
| debugging-04 | 0.073 | 0.085 | tie |
| debugging-05 | 0.09 | 0.117 | win |
| debugging-06 | 0.07 | 0.455 | win |
| debugging-07 | 0.089 | 0.5 | win |
| debugging-08 | 0.099 | 0.102 | tie |
| explanation-01 | 0.104 | 0.122 | tie |
| explanation-02 | 0.098 | 0.058 | loss |
| explanation-03 | 0.141 | 0.083 | loss |
| explanation-04 | 0.118 | 0.081 | loss |
| explanation-05 | 0.077 | 0.131 | win |
| explanation-06 | 0.088 | 0.072 | tie |
| explanation-07 | 0.097 | 0.097 | tie |
| explanation-08 | 0.118 | 0.098 | loss |
| summarization-01 | 0.083 | 0.13 | win |
| summarization-02 | 0.105 | 0.145 | win |
| summarization-03 | 0.161 | 0.115 | loss |
| summarization-04 | 0.091 | 0.084 | tie |
| summarization-05 | 0.057 | 0.153 | win |
| summarization-06 | 0.223 | 0.198 | loss |
| summarization-07 | 0.151 | 0.163 | tie |
| summarization-08 | 0.19 | 0.136 | loss |

### technical-simplified

| Pair | Styled | Unstyled | Result |
|---|---|---|---|
| code-review-01 | 0.075 | 0.122 | win |
| code-review-02 | 0.077 | 0.077 | tie |
| code-review-03 | 0.049 | 0.083 | win |
| code-review-04 | 0.097 | 0.113 | tie |
| code-review-05 | 0.061 | 0.073 | tie |
| code-review-06 | 0.091 | 0.059 | loss |
| code-review-07 | 0.096 | 0.128 | win |
| code-review-08 | 0.121 | 0.121 | tie |
| debugging-01 | 0.04 | 0.132 | win |
| debugging-02 | 0.07 | 0.123 | win |
| debugging-03 | 0.013 | 0.051 | win |
| debugging-04 | 0.074 | 0.085 | tie |
| debugging-05 | 0.068 | 0.117 | win |
| debugging-06 | 0.083 | 0.455 | win |
| debugging-07 | 0.068 | 0.5 | win |
| debugging-08 | 0.134 | 0.102 | loss |
| explanation-02 | 0.071 | 0.058 | tie |
| explanation-03 | 0.106 | 0.083 | loss |
| explanation-04 | 0.102 | 0.081 | loss |
| explanation-05 | 0.083 | 0.131 | win |
| explanation-06 | 0.083 | 0.072 | tie |
| explanation-07 | 0.112 | 0.097 | tie |
| explanation-08 | 0.172 | 0.098 | loss |
| summarization-01 | 0.102 | 0.13 | win |
| summarization-02 | 0.16 | 0.145 | tie |
| summarization-03 | 0.075 | 0.115 | win |
| summarization-04 | 0.079 | 0.084 | tie |
| summarization-05 | 0.063 | 0.153 | win |
| summarization-07 | 0.109 | 0.163 | win |

## Call timing

A stored call row holds two times: duration_ms is the model
time that the CLI reports, and wall_ms is the wall clock of
the subprocess. The difference is the startup cost of one CLI
call.

Calls: 2817, measured: 2817.
Mean duration: 10899 ms. Mean wall: 46876 ms. Mean startup: 35977 ms.

## Harness spend

A stored call row holds the token counts of its call: the
uncached input, cache-write input, cache-read input, and
output tokens. The cache-read share is the cache-read total
over the whole input total.

Calls: 2817, measured: 2817.
Input tokens: 20106 uncached, 2328799 cache write, 13346909 cache read. Output tokens: 2822923.
Cache-read share: 0.85.
Cache writes by lifetime: 2328799 at 5 minutes, 0 at 1 hour.

## Warnings

- technical-simplified/explanation-01: the pair failed the gate, excluded
- technical-simplified/summarization-06: the pair failed the gate, excluded
- technical-simplified/summarization-08: the pair failed the gate, excluded
- clarity-flow/debugging-06: the pair has 0 shared facts, fewer than the floor of 3, so comprehension skips the pair
- clarity-flow/debugging-07: the pair has 0 shared facts, fewer than the floor of 3, so comprehension skips the pair
- clarity-flow/debugging-08: the pair has 0 shared facts, fewer than the floor of 3, so comprehension skips the pair
- classic-concise/debugging-07: the pair has 0 shared facts, fewer than the floor of 3, so comprehension skips the pair
- classic-concise/debugging-06: the pair has 0 shared facts, fewer than the floor of 3, so comprehension skips the pair
- developer-docs/code-review-04: the pair has 0 shared facts, fewer than the floor of 3, so comprehension skips the pair
- developer-docs/debugging-06: the pair has 0 shared facts, fewer than the floor of 3, so comprehension skips the pair
- developer-docs/debugging-07: the pair has 0 shared facts, fewer than the floor of 3, so comprehension skips the pair
- plain-language/debugging-06: the pair has 0 shared facts, fewer than the floor of 3, so comprehension skips the pair
- plain-language/debugging-07: the pair has 0 shared facts, fewer than the floor of 3, so comprehension skips the pair
- technical-simplified/debugging-06: the pair has 0 shared facts, fewer than the floor of 3, so comprehension skips the pair
- technical-simplified/debugging-07: the pair has 0 shared facts, fewer than the floor of 3, so comprehension skips the pair
- technical-simplified/explanation-08: the pair has 1 shared facts, fewer than the floor of 3, so comprehension skips the pair
- clarity-flow/debugging-06: the comprehension check has no usable questions for the pair, so the pair is unscored
- clarity-flow/debugging-07: the comprehension check has no usable questions for the pair, so the pair is unscored
- clarity-flow/debugging-08: the comprehension check has no usable questions for the pair, so the pair is unscored
- classic-concise/debugging-06: the comprehension check has no usable questions for the pair, so the pair is unscored
- classic-concise/debugging-07: the comprehension check has no usable questions for the pair, so the pair is unscored
- developer-docs/code-review-04: the comprehension check has no usable questions for the pair, so the pair is unscored
- developer-docs/debugging-06: the comprehension check has no usable questions for the pair, so the pair is unscored
- developer-docs/debugging-07: the comprehension check has no usable questions for the pair, so the pair is unscored
- plain-language/debugging-06: the comprehension check has no usable questions for the pair, so the pair is unscored
- plain-language/debugging-07: the comprehension check has no usable questions for the pair, so the pair is unscored
- technical-simplified/debugging-06: the comprehension check has no usable questions for the pair, so the pair is unscored
- technical-simplified/debugging-07: the comprehension check has no usable questions for the pair, so the pair is unscored
- technical-simplified/explanation-08: the comprehension check has no usable questions for the pair, so the pair is unscored
- classic-concise: the styled answer scores worse than the unstyled answer on comprehension (4 wins, 6 losses)
- developer-docs: the styled answer scores worse than the unstyled answer on comprehension (3 wins, 6 losses)

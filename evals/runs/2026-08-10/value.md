# Reader-value report

The checks compare the styled answer with the unstyled answer of
the same prompt, pair by pair, as win, loss, or tie. Only pairs
whose styled answer passes the fidelity gate enter the checks.
Each judge call sees one bare text: no style name, no arm label,
and never both answers. Thus a judge cannot know which answer is
styled. The judge models differ from the writer of the answers.

Judges: reader haiku, grader opus. Comprehension asks up to 6 questions per pair, worded by both answers in balance, with 3 reader replicates per answer, ambiguity uses 3 restatements per answer, and the round-trip goes through Italian. Judged on 2026-08-10T07:45:06+00:00.

## Comprehension (weak reader)

The questions come from the shared facts of the pair, mined in both directions: the facts of the unstyled answer that survive in the styled answer, and the facts of the styled answer that the unstyled answer also states. The quiz takes half of its questions from each wording, so neither answer sets the phrasing alone, and the Sources column counts the questions per wording (unstyled/styled). A grader call turns each fact into one question, and the fact is the reference answer. The weak reader answers the questions from one answer text, once per replicate, and the grader marks every reply. Each styled replicate meets each unstyled replicate as a win, a loss, or a tie, and the pair outcome is the strict plurality, else a tie. The agreement is the plurality share, and the buried-fact rate counts "NOT IN TEXT" replies to a shared fact, per arm. The check measures extraction over shared material. Absence belongs to the content-loss report. Higher is better.

| Style | Wins | Losses | Ties | Mean delta | Agreement | Buried (styled) | Buried (unstyled) |
|---|---|---|---|---|---|---|---|
| clarity-flow | 8 | 2 | 20 | 0.039 | 0.833 | 0.039 | 0.059 |
| classic-concise | 3 | 7 | 20 | -0.019 | 0.856 | 0.057 | 0.03 |
| developer-docs | 6 | 3 | 21 | 0.041 | 0.841 | 0.002 | 0.044 |
| plain-language | 8 | 5 | 12 | 0.031 | 0.889 | 0.053 | 0.076 |
| technical-simplified | 9 | 5 | 12 | 0.015 | 0.876 | 0.028 | 0.036 |

The styled answer must not score worse than the unstyled answer.
- clarity-flow: the styled answer holds (8 wins, 2 losses, 20 ties).
- classic-concise: the styled answer scores worse (3 wins, 7 losses, 20 ties).
- developer-docs: the styled answer holds (6 wins, 3 losses, 21 ties).
- plain-language: the styled answer holds (8 wins, 5 losses, 12 ties).
- technical-simplified: the styled answer holds (9 wins, 5 losses, 12 ties).

### clarity-flow

| Pair | Questions | Sources (u/s) | Styled | Unstyled | Agreement | Result |
|---|---|---|---|---|---|---|
| code-review-01 | 6 | 3/3 | 0.944 | 0.889 | 0.444 | tie |
| code-review-02 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| code-review-03 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| code-review-04 | 6 | 3/3 | 0.889 | 0.722 | 0.778 | win |
| code-review-05 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| code-review-06 | 6 | 3/3 | 0.889 | 0.833 | 0.444 | win |
| code-review-07 | 6 | 3/3 | 0.944 | 1.0 | 0.667 | tie |
| code-review-08 | 6 | 3/3 | 1.0 | 0.889 | 0.667 | win |
| debugging-01 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-02 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-03 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-04 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-05 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-06 | 6 | 3/3 | 0.833 | 0.833 | 0.333 | tie |
| explanation-01 | 6 | 3/3 | 0.667 | 1.0 | 1.0 | loss |
| explanation-02 | 6 | 3/3 | 1.0 | 0.722 | 1.0 | win |
| explanation-03 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| explanation-04 | 6 | 3/3 | 0.889 | 1.0 | 0.667 | loss |
| explanation-05 | 6 | 3/3 | 1.0 | 0.944 | 0.667 | tie |
| explanation-06 | 6 | 3/3 | 0.778 | 0.722 | 0.444 | tie |
| explanation-07 | 6 | 3/3 | 0.722 | 0.611 | 0.556 | win |
| explanation-08 | 6 | 3/3 | 0.667 | 0.222 | 1.0 | win |
| summarization-01 | 6 | 3/3 | 1.0 | 0.833 | 1.0 | win |
| summarization-02 | 6 | 3/3 | 0.833 | 0.778 | 0.667 | tie |
| summarization-03 | 6 | 3/3 | 1.0 | 0.833 | 1.0 | win |
| summarization-04 | 6 | 3/3 | 0.833 | 0.833 | 1.0 | tie |
| summarization-05 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-06 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-07 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-08 | 6 | 3/3 | 0.833 | 0.889 | 0.667 | tie |

### classic-concise

| Pair | Questions | Sources (u/s) | Styled | Unstyled | Agreement | Result |
|---|---|---|---|---|---|---|
| code-review-01 | 6 | 3/3 | 0.833 | 1.0 | 1.0 | loss |
| code-review-02 | 6 | 3/3 | 0.889 | 1.0 | 0.667 | loss |
| code-review-03 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| code-review-04 | 6 | 3/3 | 0.778 | 0.556 | 0.889 | win |
| code-review-05 | 6 | 3/3 | 1.0 | 0.944 | 0.667 | tie |
| code-review-06 | 6 | 3/3 | 1.0 | 0.778 | 1.0 | win |
| code-review-07 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| code-review-08 | 6 | 3/3 | 0.944 | 0.944 | 0.556 | tie |
| debugging-01 | 6 | 3/3 | 1.0 | 0.944 | 0.667 | tie |
| debugging-02 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-03 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-04 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-05 | 6 | 3/3 | 0.889 | 1.0 | 0.667 | loss |
| debugging-06 | 6 | 3/3 | 0.611 | 0.667 | 0.444 | loss |
| explanation-01 | 6 | 3/3 | 0.556 | 1.0 | 1.0 | loss |
| explanation-02 | 6 | 3/3 | 0.833 | 0.889 | 0.667 | tie |
| explanation-03 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| explanation-04 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| explanation-05 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| explanation-06 | 6 | 3/3 | 0.944 | 1.0 | 0.667 | tie |
| explanation-07 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| explanation-08 | 6 | 3/3 | 0.833 | 0.833 | 1.0 | tie |
| summarization-01 | 6 | 3/3 | 0.833 | 0.833 | 1.0 | tie |
| summarization-02 | 6 | 3/3 | 1.0 | 0.778 | 0.667 | win |
| summarization-03 | 6 | 3/3 | 0.778 | 0.944 | 0.778 | loss |
| summarization-04 | 6 | 3/3 | 0.833 | 0.889 | 0.667 | tie |
| summarization-05 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-06 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-07 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-08 | 6 | 3/3 | 0.833 | 0.944 | 0.667 | loss |

### developer-docs

| Pair | Questions | Sources (u/s) | Styled | Unstyled | Agreement | Result |
|---|---|---|---|---|---|---|
| code-review-01 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| code-review-02 | 6 | 3/3 | 1.0 | 0.944 | 0.667 | tie |
| code-review-03 | 6 | 3/3 | 1.0 | 0.889 | 0.667 | win |
| code-review-04 | 6 | 3/3 | 1.0 | 0.722 | 1.0 | win |
| code-review-05 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| code-review-06 | 6 | 3/3 | 1.0 | 0.944 | 0.667 | tie |
| code-review-07 | 6 | 3/3 | 0.889 | 1.0 | 0.667 | loss |
| code-review-08 | 6 | 3/3 | 1.0 | 0.611 | 1.0 | win |
| debugging-01 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-02 | 6 | 3/3 | 0.944 | 1.0 | 0.667 | tie |
| debugging-03 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-04 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-05 | 6 | 3/3 | 0.889 | 1.0 | 0.667 | loss |
| debugging-06 | 6 | 3/3 | 0.944 | 0.667 | 1.0 | win |
| explanation-01 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| explanation-02 | 6 | 3/3 | 1.0 | 0.944 | 0.667 | tie |
| explanation-03 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| explanation-04 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| explanation-05 | 6 | 3/3 | 0.944 | 1.0 | 0.667 | tie |
| explanation-06 | 6 | 3/3 | 1.0 | 0.944 | 0.667 | tie |
| explanation-07 | 6 | 3/3 | 0.722 | 0.833 | 0.667 | loss |
| explanation-08 | 6 | 3/3 | 1.0 | 0.778 | 1.0 | win |
| summarization-01 | 6 | 3/3 | 0.944 | 0.889 | 0.444 | tie |
| summarization-02 | 6 | 3/3 | 0.944 | 0.889 | 0.444 | tie |
| summarization-03 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-04 | 6 | 3/3 | 0.667 | 0.778 | 0.667 | tie |
| summarization-05 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-06 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-07 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-08 | 6 | 3/3 | 1.0 | 0.833 | 1.0 | win |

### plain-language

| Pair | Questions | Sources (u/s) | Styled | Unstyled | Agreement | Result |
|---|---|---|---|---|---|---|
| code-review-02 | 6 | 3/3 | 0.833 | 1.0 | 1.0 | loss |
| code-review-03 | 6 | 3/3 | 1.0 | 0.889 | 0.667 | win |
| code-review-04 | 6 | 3/3 | 1.0 | 0.722 | 1.0 | win |
| code-review-05 | 6 | 3/3 | 1.0 | 0.889 | 0.667 | win |
| code-review-08 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-01 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-02 | 6 | 3/3 | 0.889 | 0.889 | 0.556 | tie |
| debugging-03 | 6 | 3/3 | 0.889 | 1.0 | 0.667 | loss |
| debugging-04 | 6 | 3/3 | 0.889 | 0.667 | 1.0 | win |
| debugging-05 | 6 | 3/3 | 0.778 | 0.833 | 0.667 | loss |
| debugging-06 | 6 | 3/3 | 0.833 | 0.778 | 0.667 | tie |
| explanation-01 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| explanation-02 | 6 | 3/3 | 1.0 | 0.833 | 1.0 | win |
| explanation-03 | 6 | 3/3 | 0.667 | 0.778 | 0.667 | loss |
| explanation-05 | 6 | 3/3 | 1.0 | 0.833 | 1.0 | win |
| explanation-06 | 6 | 3/3 | 0.944 | 0.833 | 0.667 | win |
| explanation-07 | 6 | 3/3 | 0.833 | 0.833 | 1.0 | tie |
| summarization-01 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-02 | 6 | 3/3 | 1.0 | 0.833 | 1.0 | win |
| summarization-03 | 6 | 3/3 | 0.833 | 1.0 | 1.0 | loss |
| summarization-04 | 6 | 3/3 | 0.833 | 0.833 | 1.0 | tie |
| summarization-05 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-06 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-07 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-08 | 6 | 3/3 | 0.833 | 0.833 | 1.0 | tie |

### technical-simplified

| Pair | Questions | Sources (u/s) | Styled | Unstyled | Agreement | Result |
|---|---|---|---|---|---|---|
| code-review-01 | 6 | 3/3 | 0.722 | 1.0 | 1.0 | loss |
| code-review-02 | 6 | 3/3 | 0.722 | 1.0 | 1.0 | loss |
| code-review-03 | 6 | 3/3 | 0.833 | 1.0 | 1.0 | loss |
| code-review-04 | 6 | 3/3 | 1.0 | 0.889 | 0.667 | win |
| code-review-05 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| code-review-08 | 6 | 3/3 | 1.0 | 0.889 | 0.667 | win |
| debugging-01 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-02 | 6 | 3/3 | 0.833 | 1.0 | 1.0 | loss |
| debugging-03 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-04 | 6 | 3/3 | 0.944 | 0.889 | 0.444 | tie |
| debugging-05 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-06 | 6 | 3/3 | 1.0 | 0.833 | 1.0 | win |
| explanation-01 | 6 | 3/3 | 1.0 | 0.889 | 0.667 | win |
| explanation-02 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| explanation-03 | 6 | 3/3 | 1.0 | 0.833 | 1.0 | win |
| explanation-04 | 6 | 3/3 | 0.667 | 0.833 | 1.0 | loss |
| explanation-05 | 6 | 3/3 | 1.0 | 0.944 | 0.667 | tie |
| explanation-06 | 6 | 3/3 | 1.0 | 0.833 | 1.0 | win |
| explanation-07 | 6 | 3/3 | 0.889 | 0.778 | 0.667 | win |
| explanation-08 | 6 | 3/3 | 1.0 | 0.833 | 1.0 | win |
| summarization-01 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-02 | 6 | 3/3 | 1.0 | 0.944 | 0.667 | tie |
| summarization-03 | 6 | 3/3 | 1.0 | 0.889 | 0.667 | win |
| summarization-04 | 6 | 3/3 | 0.722 | 0.667 | 0.667 | tie |
| summarization-05 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-07 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |

## Ambiguity (paraphrase agreement)

Independent reader calls restate one answer text in their own words. The score is the mean pairwise lexical similarity between the restatements: when the readers agree on what the text says, the text is less ambiguous. Higher is better.

| Style | Wins | Losses | Ties |
|---|---|---|---|
| clarity-flow | 15 | 12 | 5 |
| classic-concise | 10 | 12 | 10 |
| developer-docs | 16 | 9 | 7 |
| plain-language | 11 | 13 | 8 |
| technical-simplified | 13 | 7 | 7 |

The length confound is the correlation between the length ratio of a pair (styled words over unstyled words) and the styled advantage (the score gain of the styled arm). A negative value means that the shorter styled answers score better.
- clarity-flow: Pearson -0.075, Spearman 0.146, over 32 pairs.
- classic-concise: Pearson 0.089, Spearman 0.059, over 32 pairs.
- developer-docs: Pearson -0.169, Spearman -0.224, over 32 pairs.
- plain-language: Pearson 0.374, Spearman 0.273, over 32 pairs.
- technical-simplified: Pearson 0.037, Spearman -0.214, over 27 pairs.

### clarity-flow

| Pair | Styled | Unstyled | Result |
|---|---|---|---|
| code-review-01 | 0.688 | 0.706 | tie |
| code-review-02 | 0.757 | 0.633 | win |
| code-review-03 | 0.77 | 0.622 | win |
| code-review-04 | 0.637 | 0.656 | tie |
| code-review-05 | 0.624 | 0.664 | loss |
| code-review-06 | 0.633 | 0.598 | win |
| code-review-07 | 0.618 | 0.714 | loss |
| code-review-08 | 0.623 | 0.594 | win |
| debugging-01 | 0.724 | 0.668 | win |
| debugging-02 | 0.723 | 0.725 | tie |
| debugging-03 | 0.722 | 0.691 | win |
| debugging-04 | 0.759 | 0.694 | win |
| debugging-05 | 0.631 | 0.676 | loss |
| debugging-06 | 0.69 | 0.658 | win |
| debugging-07 | 0.705 | 0.392 | win |
| debugging-08 | 0.657 | 0.74 | loss |
| explanation-01 | 0.648 | 0.7 | loss |
| explanation-02 | 0.696 | 0.657 | win |
| explanation-03 | 0.668 | 0.633 | win |
| explanation-04 | 0.698 | 0.664 | win |
| explanation-05 | 0.627 | 0.638 | tie |
| explanation-06 | 0.609 | 0.653 | loss |
| explanation-07 | 0.601 | 0.628 | loss |
| explanation-08 | 0.641 | 0.646 | tie |
| summarization-01 | 0.651 | 0.689 | loss |
| summarization-02 | 0.649 | 0.603 | win |
| summarization-03 | 0.669 | 0.619 | win |
| summarization-04 | 0.615 | 0.753 | loss |
| summarization-05 | 0.756 | 0.797 | loss |
| summarization-06 | 0.626 | 0.594 | win |
| summarization-07 | 0.64 | 0.664 | loss |
| summarization-08 | 0.625 | 0.694 | loss |

### classic-concise

| Pair | Styled | Unstyled | Result |
|---|---|---|---|
| code-review-01 | 0.586 | 0.706 | loss |
| code-review-02 | 0.664 | 0.633 | win |
| code-review-03 | 0.597 | 0.622 | loss |
| code-review-04 | 0.674 | 0.656 | tie |
| code-review-05 | 0.695 | 0.664 | win |
| code-review-06 | 0.676 | 0.598 | win |
| code-review-07 | 0.659 | 0.714 | loss |
| code-review-08 | 0.616 | 0.594 | win |
| debugging-01 | 0.635 | 0.668 | loss |
| debugging-02 | 0.738 | 0.725 | tie |
| debugging-03 | 0.761 | 0.691 | win |
| debugging-04 | 0.708 | 0.694 | tie |
| debugging-05 | 0.668 | 0.676 | tie |
| debugging-06 | 0.675 | 0.658 | tie |
| debugging-07 | 0.695 | 0.392 | win |
| debugging-08 | 0.686 | 0.74 | loss |
| explanation-01 | 0.715 | 0.7 | tie |
| explanation-02 | 0.68 | 0.657 | win |
| explanation-03 | 0.696 | 0.633 | win |
| explanation-04 | 0.649 | 0.664 | tie |
| explanation-05 | 0.622 | 0.638 | tie |
| explanation-06 | 0.528 | 0.653 | loss |
| explanation-07 | 0.555 | 0.628 | loss |
| explanation-08 | 0.574 | 0.646 | loss |
| summarization-01 | 0.676 | 0.689 | tie |
| summarization-02 | 0.553 | 0.603 | loss |
| summarization-03 | 0.692 | 0.619 | win |
| summarization-04 | 0.635 | 0.753 | loss |
| summarization-05 | 0.745 | 0.797 | loss |
| summarization-06 | 0.654 | 0.594 | win |
| summarization-07 | 0.681 | 0.664 | tie |
| summarization-08 | 0.582 | 0.694 | loss |

### developer-docs

| Pair | Styled | Unstyled | Result |
|---|---|---|---|
| code-review-01 | 0.737 | 0.706 | win |
| code-review-02 | 0.659 | 0.633 | win |
| code-review-03 | 0.688 | 0.622 | win |
| code-review-04 | 0.7 | 0.656 | win |
| code-review-05 | 0.697 | 0.664 | win |
| code-review-06 | 0.695 | 0.598 | win |
| code-review-07 | 0.766 | 0.714 | win |
| code-review-08 | 0.593 | 0.594 | tie |
| debugging-01 | 0.745 | 0.668 | win |
| debugging-02 | 0.753 | 0.725 | win |
| debugging-03 | 0.824 | 0.691 | win |
| debugging-04 | 0.669 | 0.694 | loss |
| debugging-05 | 0.714 | 0.676 | win |
| debugging-06 | 0.664 | 0.658 | tie |
| debugging-07 | 0.64 | 0.392 | win |
| debugging-08 | 0.658 | 0.74 | loss |
| explanation-01 | 0.748 | 0.7 | win |
| explanation-02 | 0.675 | 0.657 | tie |
| explanation-03 | 0.682 | 0.633 | win |
| explanation-04 | 0.615 | 0.664 | loss |
| explanation-05 | 0.648 | 0.638 | tie |
| explanation-06 | 0.643 | 0.653 | tie |
| explanation-07 | 0.572 | 0.628 | loss |
| explanation-08 | 0.615 | 0.646 | loss |
| summarization-01 | 0.519 | 0.689 | loss |
| summarization-02 | 0.651 | 0.603 | win |
| summarization-03 | 0.612 | 0.619 | tie |
| summarization-04 | 0.684 | 0.753 | loss |
| summarization-05 | 0.749 | 0.797 | loss |
| summarization-06 | 0.619 | 0.594 | win |
| summarization-07 | 0.673 | 0.664 | tie |
| summarization-08 | 0.642 | 0.694 | loss |

### plain-language

| Pair | Styled | Unstyled | Result |
|---|---|---|---|
| code-review-01 | 0.689 | 0.706 | tie |
| code-review-02 | 0.635 | 0.633 | tie |
| code-review-03 | 0.744 | 0.622 | win |
| code-review-04 | 0.688 | 0.656 | win |
| code-review-05 | 0.681 | 0.664 | tie |
| code-review-06 | 0.308 | 0.598 | loss |
| code-review-07 | 0.426 | 0.714 | loss |
| code-review-08 | 0.712 | 0.594 | win |
| debugging-01 | 0.715 | 0.668 | win |
| debugging-02 | 0.75 | 0.725 | win |
| debugging-03 | 0.802 | 0.691 | win |
| debugging-04 | 0.647 | 0.694 | loss |
| debugging-05 | 0.777 | 0.676 | win |
| debugging-06 | 0.655 | 0.658 | tie |
| debugging-07 | 0.695 | 0.392 | win |
| debugging-08 | 0.402 | 0.74 | loss |
| explanation-01 | 0.637 | 0.7 | loss |
| explanation-02 | 0.665 | 0.657 | tie |
| explanation-03 | 0.641 | 0.633 | tie |
| explanation-04 | 0.292 | 0.664 | loss |
| explanation-05 | 0.688 | 0.638 | win |
| explanation-06 | 0.655 | 0.653 | tie |
| explanation-07 | 0.576 | 0.628 | loss |
| explanation-08 | 0.508 | 0.646 | loss |
| summarization-01 | 0.603 | 0.689 | loss |
| summarization-02 | 0.644 | 0.603 | win |
| summarization-03 | 0.631 | 0.619 | tie |
| summarization-04 | 0.658 | 0.753 | loss |
| summarization-05 | 0.693 | 0.797 | loss |
| summarization-06 | 0.682 | 0.594 | win |
| summarization-07 | 0.623 | 0.664 | loss |
| summarization-08 | 0.629 | 0.694 | loss |

### technical-simplified

| Pair | Styled | Unstyled | Result |
|---|---|---|---|
| code-review-01 | 0.655 | 0.706 | loss |
| code-review-02 | 0.622 | 0.633 | tie |
| code-review-03 | 0.79 | 0.622 | win |
| code-review-04 | 0.713 | 0.656 | win |
| code-review-05 | 0.706 | 0.664 | win |
| code-review-07 | 0.601 | 0.714 | loss |
| code-review-08 | 0.698 | 0.594 | win |
| debugging-01 | 0.715 | 0.668 | win |
| debugging-02 | 0.766 | 0.725 | win |
| debugging-03 | 0.654 | 0.691 | loss |
| debugging-04 | 0.756 | 0.694 | win |
| debugging-05 | 0.741 | 0.676 | win |
| debugging-06 | 0.669 | 0.658 | tie |
| explanation-01 | 0.729 | 0.7 | win |
| explanation-02 | 0.79 | 0.657 | win |
| explanation-03 | 0.674 | 0.633 | win |
| explanation-04 | 0.686 | 0.664 | win |
| explanation-05 | 0.655 | 0.638 | tie |
| explanation-06 | 0.633 | 0.653 | tie |
| explanation-07 | 0.611 | 0.628 | tie |
| explanation-08 | 0.612 | 0.646 | loss |
| summarization-01 | 0.647 | 0.689 | loss |
| summarization-02 | 0.705 | 0.603 | win |
| summarization-03 | 0.616 | 0.619 | tie |
| summarization-04 | 0.729 | 0.753 | loss |
| summarization-05 | 0.761 | 0.797 | loss |
| summarization-07 | 0.673 | 0.664 | tie |

## Translation round-trip

One call translates the answer to another language, and a second call translates the result back to English. The score is the lexical loss between the original and the round-trip: simpler text survives the round-trip with less loss. Lower is better.

| Style | Wins | Losses | Ties |
|---|---|---|---|
| clarity-flow | 8 | 16 | 8 |
| classic-concise | 5 | 16 | 11 |
| developer-docs | 16 | 6 | 10 |
| plain-language | 9 | 12 | 11 |
| technical-simplified | 7 | 6 | 14 |

The length confound is the correlation between the length ratio of a pair (styled words over unstyled words) and the styled advantage (the score gain of the styled arm). A negative value means that the shorter styled answers score better.
- clarity-flow: Pearson -0.298, Spearman -0.169, over 32 pairs.
- classic-concise: Pearson -0.201, Spearman -0.13, over 32 pairs.
- developer-docs: Pearson -0.38, Spearman -0.041, over 32 pairs.
- plain-language: Pearson 0.086, Spearman 0.357, over 32 pairs.
- technical-simplified: Pearson 0.473, Spearman 0.092, over 27 pairs.

### clarity-flow

| Pair | Styled | Unstyled | Result |
|---|---|---|---|
| code-review-01 | 0.036 | 0.093 | win |
| code-review-02 | 0.12 | 0.069 | loss |
| code-review-03 | 0.079 | 0.061 | tie |
| code-review-04 | 0.108 | 0.065 | loss |
| code-review-05 | 0.07 | 0.068 | tie |
| code-review-06 | 0.083 | 0.067 | tie |
| code-review-07 | 0.145 | 0.083 | loss |
| code-review-08 | 0.162 | 0.12 | loss |
| debugging-01 | 0.124 | 0.093 | loss |
| debugging-02 | 0.041 | 0.096 | win |
| debugging-03 | 0.032 | 0.078 | win |
| debugging-04 | 0.073 | 0.09 | tie |
| debugging-05 | 0.109 | 0.136 | win |
| debugging-06 | 0.107 | 0.119 | tie |
| debugging-07 | 0.087 | 0.214 | win |
| debugging-08 | 0.126 | 0.0 | loss |
| explanation-01 | 0.12 | 0.089 | loss |
| explanation-02 | 0.133 | 0.115 | tie |
| explanation-03 | 0.131 | 0.133 | tie |
| explanation-04 | 0.127 | 0.085 | loss |
| explanation-05 | 0.082 | 0.117 | win |
| explanation-06 | 0.1 | 0.115 | tie |
| explanation-07 | 0.158 | 0.104 | loss |
| explanation-08 | 0.17 | 0.129 | loss |
| summarization-01 | 0.143 | 0.097 | loss |
| summarization-02 | 0.224 | 0.203 | loss |
| summarization-03 | 0.146 | 0.113 | loss |
| summarization-04 | 0.07 | 0.043 | loss |
| summarization-05 | 0.153 | 0.102 | loss |
| summarization-06 | 0.276 | 0.137 | loss |
| summarization-07 | 0.175 | 0.203 | win |
| summarization-08 | 0.132 | 0.162 | win |

### classic-concise

| Pair | Styled | Unstyled | Result |
|---|---|---|---|
| code-review-01 | 0.066 | 0.093 | win |
| code-review-02 | 0.08 | 0.069 | tie |
| code-review-03 | 0.122 | 0.061 | loss |
| code-review-04 | 0.079 | 0.065 | tie |
| code-review-05 | 0.126 | 0.068 | loss |
| code-review-06 | 0.111 | 0.067 | loss |
| code-review-07 | 0.152 | 0.083 | loss |
| code-review-08 | 0.142 | 0.12 | loss |
| debugging-01 | 0.194 | 0.093 | loss |
| debugging-02 | 0.089 | 0.096 | tie |
| debugging-03 | 0.105 | 0.078 | loss |
| debugging-04 | 0.071 | 0.09 | tie |
| debugging-05 | 0.089 | 0.136 | win |
| debugging-06 | 0.117 | 0.119 | tie |
| debugging-07 | 0.112 | 0.214 | win |
| debugging-08 | 0.114 | 0.0 | loss |
| explanation-01 | 0.148 | 0.089 | loss |
| explanation-02 | 0.095 | 0.115 | tie |
| explanation-03 | 0.124 | 0.133 | tie |
| explanation-04 | 0.099 | 0.085 | tie |
| explanation-05 | 0.136 | 0.117 | tie |
| explanation-06 | 0.102 | 0.115 | tie |
| explanation-07 | 0.068 | 0.104 | win |
| explanation-08 | 0.077 | 0.129 | win |
| summarization-01 | 0.164 | 0.097 | loss |
| summarization-02 | 0.253 | 0.203 | loss |
| summarization-03 | 0.106 | 0.113 | tie |
| summarization-04 | 0.12 | 0.043 | loss |
| summarization-05 | 0.125 | 0.102 | loss |
| summarization-06 | 0.209 | 0.137 | loss |
| summarization-07 | 0.287 | 0.203 | loss |
| summarization-08 | 0.215 | 0.162 | loss |

### developer-docs

| Pair | Styled | Unstyled | Result |
|---|---|---|---|
| code-review-01 | 0.056 | 0.093 | win |
| code-review-02 | 0.036 | 0.069 | win |
| code-review-03 | 0.072 | 0.061 | tie |
| code-review-04 | 0.087 | 0.065 | loss |
| code-review-05 | 0.078 | 0.068 | tie |
| code-review-06 | 0.06 | 0.067 | tie |
| code-review-07 | 0.065 | 0.083 | tie |
| code-review-08 | 0.167 | 0.12 | loss |
| debugging-01 | 0.072 | 0.093 | win |
| debugging-02 | 0.054 | 0.096 | win |
| debugging-03 | 0.023 | 0.078 | win |
| debugging-04 | 0.076 | 0.09 | tie |
| debugging-05 | 0.027 | 0.136 | win |
| debugging-06 | 0.063 | 0.119 | win |
| debugging-07 | 0.083 | 0.214 | win |
| debugging-08 | 0.097 | 0.0 | loss |
| explanation-01 | 0.106 | 0.089 | tie |
| explanation-02 | 0.125 | 0.115 | tie |
| explanation-03 | 0.069 | 0.133 | win |
| explanation-04 | 0.127 | 0.085 | loss |
| explanation-05 | 0.074 | 0.117 | win |
| explanation-06 | 0.075 | 0.115 | win |
| explanation-07 | 0.124 | 0.104 | tie |
| explanation-08 | 0.111 | 0.129 | tie |
| summarization-01 | 0.132 | 0.097 | loss |
| summarization-02 | 0.149 | 0.203 | win |
| summarization-03 | 0.117 | 0.113 | tie |
| summarization-04 | 0.083 | 0.043 | loss |
| summarization-05 | 0.081 | 0.102 | win |
| summarization-06 | 0.047 | 0.137 | win |
| summarization-07 | 0.157 | 0.203 | win |
| summarization-08 | 0.124 | 0.162 | win |

### plain-language

| Pair | Styled | Unstyled | Result |
|---|---|---|---|
| code-review-01 | 0.956 | 0.093 | loss |
| code-review-02 | 0.082 | 0.069 | tie |
| code-review-03 | 0.073 | 0.061 | tie |
| code-review-04 | 0.051 | 0.065 | tie |
| code-review-05 | 0.094 | 0.068 | loss |
| code-review-06 | 0.13 | 0.067 | loss |
| code-review-07 | 0.333 | 0.083 | loss |
| code-review-08 | 0.119 | 0.12 | tie |
| debugging-01 | 0.091 | 0.093 | tie |
| debugging-02 | 0.045 | 0.096 | win |
| debugging-03 | 0.048 | 0.078 | win |
| debugging-04 | 0.081 | 0.09 | tie |
| debugging-05 | 0.064 | 0.136 | win |
| debugging-06 | 0.089 | 0.119 | win |
| debugging-07 | 0.124 | 0.214 | win |
| debugging-08 | 0.861 | 0.0 | loss |
| explanation-01 | 0.102 | 0.089 | tie |
| explanation-02 | 0.098 | 0.115 | tie |
| explanation-03 | 0.096 | 0.133 | win |
| explanation-04 | 0.953 | 0.085 | loss |
| explanation-05 | 0.121 | 0.117 | tie |
| explanation-06 | 0.127 | 0.115 | tie |
| explanation-07 | 0.095 | 0.104 | tie |
| explanation-08 | 1.0 | 0.129 | loss |
| summarization-01 | 0.228 | 0.097 | loss |
| summarization-02 | 0.176 | 0.203 | win |
| summarization-03 | 0.142 | 0.113 | loss |
| summarization-04 | 0.067 | 0.043 | loss |
| summarization-05 | 0.131 | 0.102 | loss |
| summarization-06 | 0.186 | 0.137 | loss |
| summarization-07 | 0.151 | 0.203 | win |
| summarization-08 | 0.128 | 0.162 | win |

### technical-simplified

| Pair | Styled | Unstyled | Result |
|---|---|---|---|
| code-review-01 | 0.081 | 0.093 | tie |
| code-review-02 | 0.087 | 0.069 | tie |
| code-review-03 | 0.061 | 0.061 | tie |
| code-review-04 | 0.139 | 0.065 | loss |
| code-review-05 | 0.126 | 0.068 | loss |
| code-review-07 | 0.958 | 0.083 | loss |
| code-review-08 | 0.104 | 0.12 | tie |
| debugging-01 | 0.044 | 0.093 | win |
| debugging-02 | 0.063 | 0.096 | win |
| debugging-03 | 0.06 | 0.078 | tie |
| debugging-04 | 0.088 | 0.09 | tie |
| debugging-05 | 0.112 | 0.136 | win |
| debugging-06 | 0.119 | 0.119 | tie |
| explanation-01 | 0.126 | 0.089 | loss |
| explanation-02 | 0.132 | 0.115 | tie |
| explanation-03 | 0.101 | 0.133 | win |
| explanation-04 | 0.088 | 0.085 | tie |
| explanation-05 | 0.112 | 0.117 | tie |
| explanation-06 | 0.124 | 0.115 | tie |
| explanation-07 | 0.141 | 0.104 | loss |
| explanation-08 | 0.129 | 0.129 | tie |
| summarization-01 | 0.103 | 0.097 | tie |
| summarization-02 | 0.135 | 0.203 | win |
| summarization-03 | 0.13 | 0.113 | tie |
| summarization-04 | 0.089 | 0.043 | loss |
| summarization-05 | 0.055 | 0.102 | win |
| summarization-07 | 0.183 | 0.203 | win |

## Call timing

A stored call row holds two times: duration_ms is the model
time that the CLI reports, and wall_ms is the wall clock of
the subprocess. The difference is the startup cost of one CLI
call.

Calls: 2768, measured: 2768.
Mean duration: 10855 ms. Mean wall: 49625 ms. Mean startup: 38770 ms.

## Harness spend

A stored call row holds the token counts of its call: the
uncached input, cache-write input, cache-read input, and
output tokens. The cache-read share is the cache-read total
over the whole input total.

Calls: 2768, measured: 2768.
Input tokens: 19784 uncached, 2252895 cache write, 13106353 cache read. Output tokens: 2747362.
Cache-read share: 0.852.
Cache writes by lifetime: 2252895 at 5 minutes, 0 at 1 hour.

## Warnings

- technical-simplified/debugging-08: the pair failed the gate, excluded
- technical-simplified/summarization-08: the pair failed the gate, excluded
- technical-simplified/summarization-06: the pair failed the gate, excluded
- technical-simplified/code-review-06: the pair failed the gate, excluded
- technical-simplified/debugging-07: the pair failed the gate, excluded
- clarity-flow/debugging-07: the pair has 1 shared facts, fewer than the floor of 3, so comprehension skips the pair
- clarity-flow/debugging-08: the pair has 0 shared facts, fewer than the floor of 3, so comprehension skips the pair
- classic-concise/debugging-07: the pair has 1 shared facts, fewer than the floor of 3, so comprehension skips the pair
- classic-concise/debugging-08: the pair has 0 shared facts, fewer than the floor of 3, so comprehension skips the pair
- developer-docs/debugging-07: the pair has 1 shared facts, fewer than the floor of 3, so comprehension skips the pair
- developer-docs/debugging-08: the pair has 0 shared facts, fewer than the floor of 3, so comprehension skips the pair
- plain-language/code-review-01: the pair has 0 shared facts, fewer than the floor of 3, so comprehension skips the pair
- plain-language/code-review-06: the pair has 2 shared facts, fewer than the floor of 3, so comprehension skips the pair
- plain-language/code-review-07: the pair has 0 shared facts, fewer than the floor of 3, so comprehension skips the pair
- plain-language/debugging-07: the pair has 1 shared facts, fewer than the floor of 3, so comprehension skips the pair
- plain-language/debugging-08: the pair has 0 shared facts, fewer than the floor of 3, so comprehension skips the pair
- plain-language/explanation-04: the pair has 0 shared facts, fewer than the floor of 3, so comprehension skips the pair
- plain-language/explanation-08: the pair has 0 shared facts, fewer than the floor of 3, so comprehension skips the pair
- technical-simplified/code-review-07: the pair has 0 shared facts, fewer than the floor of 3, so comprehension skips the pair
- clarity-flow/debugging-07: the comprehension check has no usable questions for the pair, so the pair is unscored
- clarity-flow/debugging-08: the comprehension check has no usable questions for the pair, so the pair is unscored
- classic-concise/debugging-07: the comprehension check has no usable questions for the pair, so the pair is unscored
- classic-concise/debugging-08: the comprehension check has no usable questions for the pair, so the pair is unscored
- developer-docs/debugging-07: the comprehension check has no usable questions for the pair, so the pair is unscored
- developer-docs/debugging-08: the comprehension check has no usable questions for the pair, so the pair is unscored
- plain-language/code-review-01: the comprehension check has no usable questions for the pair, so the pair is unscored
- plain-language/code-review-06: the comprehension check has no usable questions for the pair, so the pair is unscored
- plain-language/code-review-07: the comprehension check has no usable questions for the pair, so the pair is unscored
- plain-language/debugging-07: the comprehension check has no usable questions for the pair, so the pair is unscored
- plain-language/debugging-08: the comprehension check has no usable questions for the pair, so the pair is unscored
- plain-language/explanation-04: the comprehension check has no usable questions for the pair, so the pair is unscored
- plain-language/explanation-08: the comprehension check has no usable questions for the pair, so the pair is unscored
- technical-simplified/code-review-07: the comprehension check has no usable questions for the pair, so the pair is unscored
- classic-concise: the styled answer scores worse than the unstyled answer on comprehension (3 wins, 7 losses)

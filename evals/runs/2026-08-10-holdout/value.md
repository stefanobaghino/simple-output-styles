# Reader-value report

The checks compare the styled answer with the unstyled answer of
the same prompt, pair by pair, as win, loss, or tie. Only pairs
whose styled answer passes the fidelity gate enter the checks.
Each judge call sees one bare text: no style name, no arm label,
and never both answers. Thus a judge cannot know which answer is
styled. The judge models differ from the writer of the answers.

Judges: reader haiku, grader opus. Comprehension asks up to 6 questions per pair, worded by both answers in balance, with 3 reader replicates per answer, ambiguity uses 3 restatements per answer, and the round-trip goes through Italian. Judged on 2026-08-10T14:32:55+00:00.

## Comprehension (weak reader)

The questions come from the shared facts of the pair, mined in both directions: the facts of the unstyled answer that survive in the styled answer, and the facts of the styled answer that the unstyled answer also states. The quiz takes half of its questions from each wording, so neither answer sets the phrasing alone, and the Sources column counts the questions per wording (unstyled/styled). A grader call turns each fact into one question, and the fact is the reference answer. The weak reader answers the questions from one answer text, once per replicate, and the grader marks every reply. Each styled replicate meets each unstyled replicate as a win, a loss, or a tie, and the pair outcome is the strict plurality, else a tie. The agreement is the plurality share, and the buried-fact rate counts "NOT IN TEXT" replies to a shared fact, per arm. The check measures extraction over shared material. Absence belongs to the content-loss report. Higher is better.

| Style | Wins | Losses | Ties | Mean delta | Agreement | Buried (styled) | Buried (unstyled) |
|---|---|---|---|---|---|---|---|
| actionable-clarity | 3 | 4 | 12 | 0.009 | 0.86 | 0.053 | 0.058 |
| clarity-flow | 4 | 6 | 11 | -0.024 | 0.905 | 0.04 | 0.024 |
| classic-concise | 5 | 2 | 14 | 0.016 | 0.884 | 0.056 | 0.074 |
| developer-docs | 3 | 5 | 13 | -0.003 | 0.921 | 0.024 | 0.022 |
| plain-language | 2 | 3 | 13 | 0.003 | 0.864 | 0.043 | 0.043 |
| technical-simplified | 1 | 8 | 8 | -0.075 | 0.824 | 0.059 | 0.029 |

The styled answer must not score worse than the unstyled answer.
- actionable-clarity: the styled answer scores worse (3 wins, 4 losses, 12 ties).
- clarity-flow: the styled answer scores worse (4 wins, 6 losses, 11 ties).
- classic-concise: the styled answer holds (5 wins, 2 losses, 14 ties).
- developer-docs: the styled answer scores worse (3 wins, 5 losses, 13 ties).
- plain-language: the styled answer scores worse (2 wins, 3 losses, 13 ties).
- technical-simplified: the styled answer scores worse (1 wins, 8 losses, 8 ties).

### actionable-clarity

| Pair | Questions | Sources (u/s) | Styled | Unstyled | Agreement | Result |
|---|---|---|---|---|---|---|
| code-review-h02 | 6 | 3/3 | 1.0 | 0.833 | 1.0 | win |
| code-review-h03 | 6 | 3/3 | 0.722 | 0.722 | 0.556 | tie |
| code-review-h05 | 6 | 3/3 | 0.833 | 0.833 | 1.0 | tie |
| debugging-h01 | 6 | 3/3 | 0.722 | 0.778 | 0.444 | tie |
| debugging-h02 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-h03 | 6 | 3/3 | 0.944 | 0.944 | 0.556 | tie |
| debugging-h04 | 6 | 3/3 | 0.833 | 0.944 | 0.667 | loss |
| debugging-h06 | 6 | 3/3 | 1.0 | 0.722 | 1.0 | win |
| explanation-h01 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| explanation-h02 | 6 | 3/3 | 1.0 | 0.722 | 1.0 | win |
| explanation-h03 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| explanation-h04 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| explanation-h05 | 6 | 3/3 | 0.722 | 0.889 | 0.778 | loss |
| explanation-h06 | 6 | 3/3 | 0.833 | 0.944 | 0.667 | loss |
| summarization-h01 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-h02 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-h03 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-h05 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-h06 | 6 | 3/3 | 0.889 | 1.0 | 0.667 | loss |

### clarity-flow

| Pair | Questions | Sources (u/s) | Styled | Unstyled | Agreement | Result |
|---|---|---|---|---|---|---|
| code-review-h01 | 6 | 3/3 | 1.0 | 0.833 | 1.0 | win |
| code-review-h02 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| code-review-h03 | 6 | 3/3 | 0.944 | 1.0 | 0.667 | tie |
| code-review-h05 | 6 | 3/3 | 1.0 | 0.889 | 0.667 | win |
| code-review-h06 | 6 | 3/3 | 0.833 | 0.944 | 0.667 | loss |
| debugging-h01 | 6 | 3/3 | 1.0 | 0.944 | 0.667 | tie |
| debugging-h02 | 6 | 3/3 | 0.833 | 1.0 | 1.0 | loss |
| debugging-h03 | 6 | 3/3 | 0.833 | 1.0 | 1.0 | loss |
| debugging-h04 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-h06 | 6 | 3/3 | 0.944 | 0.833 | 0.667 | win |
| explanation-h01 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| explanation-h02 | 6 | 3/3 | 0.833 | 1.0 | 1.0 | loss |
| explanation-h03 | 6 | 3/3 | 0.667 | 1.0 | 1.0 | loss |
| explanation-h04 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| explanation-h05 | 6 | 3/3 | 1.0 | 0.833 | 1.0 | win |
| explanation-h06 | 6 | 3/3 | 0.667 | 0.778 | 0.667 | loss |
| summarization-h01 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-h02 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-h03 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-h05 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-h06 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |

### classic-concise

| Pair | Questions | Sources (u/s) | Styled | Unstyled | Agreement | Result |
|---|---|---|---|---|---|---|
| code-review-h01 | 6 | 3/3 | 0.833 | 0.833 | 1.0 | tie |
| code-review-h02 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| code-review-h03 | 6 | 3/3 | 0.944 | 1.0 | 0.667 | tie |
| code-review-h05 | 6 | 3/3 | 0.889 | 1.0 | 0.667 | tie |
| code-review-h06 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-h01 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-h02 | 6 | 3/3 | 0.667 | 0.833 | 1.0 | loss |
| debugging-h03 | 6 | 3/3 | 0.833 | 0.833 | 1.0 | tie |
| debugging-h04 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-h06 | 6 | 3/3 | 0.889 | 0.889 | 0.556 | tie |
| explanation-h01 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| explanation-h02 | 6 | 3/3 | 0.833 | 0.944 | 0.667 | loss |
| explanation-h03 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| explanation-h04 | 6 | 3/3 | 0.944 | 0.667 | 1.0 | win |
| explanation-h05 | 6 | 3/3 | 1.0 | 0.833 | 1.0 | win |
| explanation-h06 | 6 | 3/3 | 0.833 | 0.667 | 1.0 | win |
| summarization-h01 | 6 | 3/3 | 0.833 | 0.889 | 0.667 | tie |
| summarization-h02 | 6 | 3/3 | 1.0 | 0.889 | 0.667 | win |
| summarization-h03 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-h05 | 6 | 3/3 | 0.944 | 0.833 | 0.667 | win |
| summarization-h06 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |

### developer-docs

| Pair | Questions | Sources (u/s) | Styled | Unstyled | Agreement | Result |
|---|---|---|---|---|---|---|
| code-review-h01 | 6 | 3/3 | 0.833 | 0.833 | 1.0 | tie |
| code-review-h02 | 6 | 3/3 | 1.0 | 0.722 | 1.0 | win |
| code-review-h03 | 6 | 3/3 | 0.778 | 0.833 | 0.667 | tie |
| code-review-h04 | 3 | 1/2 | 1.0 | 0.667 | 1.0 | win |
| code-review-h05 | 6 | 3/3 | 0.833 | 1.0 | 1.0 | loss |
| debugging-h01 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-h02 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-h03 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-h04 | 6 | 3/3 | 0.833 | 1.0 | 1.0 | loss |
| debugging-h06 | 6 | 3/3 | 0.833 | 0.944 | 0.667 | loss |
| explanation-h01 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| explanation-h02 | 6 | 3/3 | 0.778 | 0.833 | 0.667 | tie |
| explanation-h03 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| explanation-h04 | 6 | 3/3 | 0.833 | 1.0 | 1.0 | loss |
| explanation-h05 | 6 | 3/3 | 1.0 | 0.778 | 1.0 | win |
| explanation-h06 | 6 | 3/3 | 0.833 | 0.944 | 0.667 | loss |
| summarization-h01 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-h02 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-h03 | 6 | 3/3 | 0.833 | 0.889 | 0.667 | tie |
| summarization-h05 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-h06 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |

### plain-language

| Pair | Questions | Sources (u/s) | Styled | Unstyled | Agreement | Result |
|---|---|---|---|---|---|---|
| code-review-h01 | 6 | 3/3 | 1.0 | 0.833 | 1.0 | win |
| code-review-h02 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| code-review-h03 | 6 | 3/3 | 1.0 | 0.944 | 0.667 | tie |
| debugging-h01 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-h02 | 6 | 3/3 | 0.833 | 0.833 | 1.0 | tie |
| debugging-h03 | 6 | 3/3 | 0.833 | 0.944 | 0.667 | loss |
| debugging-h04 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| explanation-h01 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| explanation-h02 | 6 | 3/3 | 0.889 | 1.0 | 0.667 | loss |
| explanation-h03 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| explanation-h04 | 6 | 3/3 | 0.944 | 0.889 | 0.444 | tie |
| explanation-h05 | 6 | 3/3 | 1.0 | 0.944 | 0.667 | tie |
| explanation-h06 | 6 | 3/3 | 1.0 | 0.833 | 1.0 | win |
| summarization-h01 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-h02 | 6 | 3/3 | 0.889 | 0.944 | 0.444 | tie |
| summarization-h03 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-h05 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-h06 | 6 | 3/3 | 0.833 | 1.0 | 1.0 | loss |

### technical-simplified

| Pair | Questions | Sources (u/s) | Styled | Unstyled | Agreement | Result |
|---|---|---|---|---|---|---|
| code-review-h01 | 6 | 3/3 | 0.667 | 0.833 | 0.667 | loss |
| code-review-h02 | 6 | 3/3 | 0.889 | 1.0 | 0.667 | loss |
| code-review-h03 | 6 | 3/3 | 0.944 | 1.0 | 0.667 | tie |
| code-review-h05 | 6 | 3/3 | 0.833 | 1.0 | 1.0 | loss |
| debugging-h01 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-h02 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-h03 | 6 | 3/3 | 0.667 | 0.833 | 1.0 | loss |
| debugging-h04 | 6 | 3/3 | 0.833 | 1.0 | 1.0 | loss |
| debugging-h06 | 6 | 3/3 | 0.944 | 1.0 | 0.667 | tie |
| explanation-h01 | 6 | 3/3 | 0.889 | 1.0 | 0.667 | loss |
| explanation-h02 | 6 | 3/3 | 0.833 | 1.0 | 1.0 | loss |
| explanation-h03 | 6 | 3/3 | 0.944 | 1.0 | 0.667 | tie |
| explanation-h04 | 6 | 3/3 | 0.944 | 1.0 | 0.667 | tie |
| explanation-h05 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| explanation-h06 | 6 | 3/3 | 0.833 | 0.722 | 0.667 | win |
| summarization-h01 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-h02 | 6 | 3/3 | 0.889 | 1.0 | 0.667 | loss |

## Ambiguity (paraphrase agreement)

Independent reader calls restate one answer text in their own words. The score is the mean pairwise lexical similarity between the restatements: when the readers agree on what the text says, the text is less ambiguous. Higher is better.

| Style | Wins | Losses | Ties |
|---|---|---|---|
| actionable-clarity | 10 | 5 | 8 |
| clarity-flow | 14 | 7 | 3 |
| classic-concise | 16 | 6 | 2 |
| developer-docs | 14 | 6 | 4 |
| plain-language | 14 | 5 | 5 |
| technical-simplified | 13 | 2 | 6 |

The length confound is the correlation between the length ratio of a pair (styled words over unstyled words) and the styled advantage (the score gain of the styled arm). A negative value means that the shorter styled answers score better.
- actionable-clarity: Pearson 0.357, Spearman 0.306, over 23 pairs.
- clarity-flow: Pearson 0.43, Spearman 0.268, over 24 pairs.
- classic-concise: Pearson 0.509, Spearman 0.008, over 24 pairs.
- developer-docs: Pearson 0.042, Spearman 0.463, over 24 pairs.
- plain-language: Pearson 0.33, Spearman 0.352, over 24 pairs.
- technical-simplified: Pearson 0.522, Spearman 0.416, over 21 pairs.

### actionable-clarity

| Pair | Styled | Unstyled | Result |
|---|---|---|---|
| code-review-h01 | 0.323 | 0.703 | loss |
| code-review-h02 | 0.698 | 0.685 | tie |
| code-review-h03 | 0.69 | 0.64 | win |
| code-review-h04 | 0.725 | 0.451 | win |
| code-review-h05 | 0.667 | 0.65 | tie |
| debugging-h01 | 0.784 | 0.589 | win |
| debugging-h02 | 0.76 | 0.557 | win |
| debugging-h03 | 0.728 | 0.574 | win |
| debugging-h04 | 0.718 | 0.716 | tie |
| debugging-h05 | 0.478 | 0.619 | loss |
| debugging-h06 | 0.655 | 0.612 | win |
| explanation-h01 | 0.595 | 0.665 | loss |
| explanation-h02 | 0.657 | 0.694 | loss |
| explanation-h03 | 0.688 | 0.671 | tie |
| explanation-h04 | 0.655 | 0.672 | tie |
| explanation-h05 | 0.627 | 0.601 | win |
| explanation-h06 | 0.608 | 0.573 | win |
| summarization-h01 | 0.713 | 0.712 | tie |
| summarization-h02 | 0.698 | 0.702 | tie |
| summarization-h03 | 0.591 | 0.589 | tie |
| summarization-h04 | 0.64 | 0.785 | loss |
| summarization-h05 | 0.663 | 0.597 | win |
| summarization-h06 | 0.643 | 0.597 | win |

### clarity-flow

| Pair | Styled | Unstyled | Result |
|---|---|---|---|
| code-review-h01 | 0.64 | 0.703 | loss |
| code-review-h02 | 0.636 | 0.685 | loss |
| code-review-h03 | 0.634 | 0.64 | tie |
| code-review-h04 | 0.664 | 0.451 | win |
| code-review-h05 | 0.684 | 0.65 | win |
| code-review-h06 | 0.683 | 0.661 | win |
| debugging-h01 | 0.758 | 0.589 | win |
| debugging-h02 | 0.608 | 0.557 | win |
| debugging-h03 | 0.699 | 0.574 | win |
| debugging-h04 | 0.603 | 0.716 | loss |
| debugging-h05 | 0.739 | 0.619 | win |
| debugging-h06 | 0.652 | 0.612 | win |
| explanation-h01 | 0.678 | 0.665 | tie |
| explanation-h02 | 0.716 | 0.694 | win |
| explanation-h03 | 0.715 | 0.671 | win |
| explanation-h04 | 0.61 | 0.672 | loss |
| explanation-h05 | 0.641 | 0.601 | win |
| explanation-h06 | 0.628 | 0.573 | win |
| summarization-h01 | 0.669 | 0.712 | loss |
| summarization-h02 | 0.672 | 0.702 | loss |
| summarization-h03 | 0.653 | 0.589 | win |
| summarization-h04 | 0.723 | 0.785 | loss |
| summarization-h05 | 0.683 | 0.597 | win |
| summarization-h06 | 0.615 | 0.597 | tie |

### classic-concise

| Pair | Styled | Unstyled | Result |
|---|---|---|---|
| code-review-h01 | 0.729 | 0.703 | win |
| code-review-h02 | 0.661 | 0.685 | loss |
| code-review-h03 | 0.703 | 0.64 | win |
| code-review-h04 | 0.662 | 0.451 | win |
| code-review-h05 | 0.646 | 0.65 | tie |
| code-review-h06 | 0.682 | 0.661 | win |
| debugging-h01 | 0.663 | 0.589 | win |
| debugging-h02 | 0.609 | 0.557 | win |
| debugging-h03 | 0.602 | 0.574 | win |
| debugging-h04 | 0.647 | 0.716 | loss |
| debugging-h05 | 0.672 | 0.619 | win |
| debugging-h06 | 0.617 | 0.612 | tie |
| explanation-h01 | 0.72 | 0.665 | win |
| explanation-h02 | 0.77 | 0.694 | win |
| explanation-h03 | 0.638 | 0.671 | loss |
| explanation-h04 | 0.703 | 0.672 | win |
| explanation-h05 | 0.642 | 0.601 | win |
| explanation-h06 | 0.619 | 0.573 | win |
| summarization-h01 | 0.59 | 0.712 | loss |
| summarization-h02 | 0.65 | 0.702 | loss |
| summarization-h03 | 0.632 | 0.589 | win |
| summarization-h04 | 0.716 | 0.785 | loss |
| summarization-h05 | 0.655 | 0.597 | win |
| summarization-h06 | 0.62 | 0.597 | win |

### developer-docs

| Pair | Styled | Unstyled | Result |
|---|---|---|---|
| code-review-h01 | 0.587 | 0.703 | loss |
| code-review-h02 | 0.678 | 0.685 | tie |
| code-review-h03 | 0.726 | 0.64 | win |
| code-review-h04 | 0.738 | 0.451 | win |
| code-review-h05 | 0.642 | 0.65 | tie |
| code-review-h06 | 0.639 | 0.661 | loss |
| debugging-h01 | 0.806 | 0.589 | win |
| debugging-h02 | 0.761 | 0.557 | win |
| debugging-h03 | 0.703 | 0.574 | win |
| debugging-h04 | 0.813 | 0.716 | win |
| debugging-h05 | 0.721 | 0.619 | win |
| debugging-h06 | 0.632 | 0.612 | tie |
| explanation-h01 | 0.643 | 0.665 | loss |
| explanation-h02 | 0.657 | 0.694 | loss |
| explanation-h03 | 0.692 | 0.671 | win |
| explanation-h04 | 0.708 | 0.672 | win |
| explanation-h05 | 0.646 | 0.601 | win |
| explanation-h06 | 0.613 | 0.573 | win |
| summarization-h01 | 0.672 | 0.712 | loss |
| summarization-h02 | 0.796 | 0.702 | win |
| summarization-h03 | 0.602 | 0.589 | tie |
| summarization-h04 | 0.63 | 0.785 | loss |
| summarization-h05 | 0.665 | 0.597 | win |
| summarization-h06 | 0.646 | 0.597 | win |

### plain-language

| Pair | Styled | Unstyled | Result |
|---|---|---|---|
| code-review-h01 | 0.71 | 0.703 | tie |
| code-review-h02 | 0.682 | 0.685 | tie |
| code-review-h03 | 0.735 | 0.64 | win |
| code-review-h04 | 0.602 | 0.451 | win |
| code-review-h05 | 0.52 | 0.65 | loss |
| code-review-h06 | 0.457 | 0.661 | loss |
| debugging-h01 | 0.788 | 0.589 | win |
| debugging-h02 | 0.756 | 0.557 | win |
| debugging-h03 | 0.601 | 0.574 | win |
| debugging-h04 | 0.653 | 0.716 | loss |
| debugging-h05 | 0.776 | 0.619 | win |
| debugging-h06 | 0.78 | 0.612 | win |
| explanation-h01 | 0.663 | 0.665 | tie |
| explanation-h02 | 0.753 | 0.694 | win |
| explanation-h03 | 0.661 | 0.671 | tie |
| explanation-h04 | 0.718 | 0.672 | win |
| explanation-h05 | 0.611 | 0.601 | tie |
| explanation-h06 | 0.633 | 0.573 | win |
| summarization-h01 | 0.733 | 0.712 | win |
| summarization-h02 | 0.58 | 0.702 | loss |
| summarization-h03 | 0.698 | 0.589 | win |
| summarization-h04 | 0.748 | 0.785 | loss |
| summarization-h05 | 0.688 | 0.597 | win |
| summarization-h06 | 0.673 | 0.597 | win |

### technical-simplified

| Pair | Styled | Unstyled | Result |
|---|---|---|---|
| code-review-h01 | 0.668 | 0.703 | loss |
| code-review-h02 | 0.704 | 0.685 | tie |
| code-review-h03 | 0.638 | 0.64 | tie |
| code-review-h04 | 0.664 | 0.451 | win |
| code-review-h05 | 0.68 | 0.65 | win |
| debugging-h01 | 0.715 | 0.589 | win |
| debugging-h02 | 0.583 | 0.557 | win |
| debugging-h03 | 0.723 | 0.574 | win |
| debugging-h04 | 0.744 | 0.716 | win |
| debugging-h05 | 0.706 | 0.619 | win |
| debugging-h06 | 0.62 | 0.612 | tie |
| explanation-h01 | 0.695 | 0.665 | win |
| explanation-h02 | 0.708 | 0.694 | tie |
| explanation-h03 | 0.634 | 0.671 | loss |
| explanation-h04 | 0.706 | 0.672 | win |
| explanation-h05 | 0.671 | 0.601 | win |
| explanation-h06 | 0.622 | 0.573 | win |
| summarization-h01 | 0.721 | 0.712 | tie |
| summarization-h02 | 0.766 | 0.702 | win |
| summarization-h04 | 0.786 | 0.785 | tie |
| summarization-h05 | 0.661 | 0.597 | win |

## Translation round-trip

One call translates the answer to another language, and a second call translates the result back to English. The score is the lexical loss between the original and the round-trip: simpler text survives the round-trip with less loss. Lower is better.

| Style | Wins | Losses | Ties |
|---|---|---|---|
| actionable-clarity | 4 | 6 | 13 |
| clarity-flow | 8 | 6 | 10 |
| classic-concise | 7 | 8 | 9 |
| developer-docs | 8 | 7 | 9 |
| plain-language | 10 | 5 | 9 |
| technical-simplified | 8 | 6 | 7 |

The length confound is the correlation between the length ratio of a pair (styled words over unstyled words) and the styled advantage (the score gain of the styled arm). A negative value means that the shorter styled answers score better.
- actionable-clarity: Pearson 0.439, Spearman 0.131, over 23 pairs.
- clarity-flow: Pearson 0.389, Spearman 0.157, over 24 pairs.
- classic-concise: Pearson 0.564, Spearman 0.158, over 24 pairs.
- developer-docs: Pearson -0.004, Spearman 0.167, over 24 pairs.
- plain-language: Pearson 0.342, Spearman 0.421, over 24 pairs.
- technical-simplified: Pearson 0.335, Spearman 0.216, over 21 pairs.

### actionable-clarity

| Pair | Styled | Unstyled | Result |
|---|---|---|---|
| code-review-h01 | 0.273 | 0.117 | loss |
| code-review-h02 | 0.103 | 0.109 | tie |
| code-review-h03 | 0.078 | 0.097 | tie |
| code-review-h04 | 0.124 | 0.333 | win |
| code-review-h05 | 0.05 | 0.074 | win |
| debugging-h01 | 0.08 | 0.055 | loss |
| debugging-h02 | 0.077 | 0.059 | tie |
| debugging-h03 | 0.055 | 0.089 | win |
| debugging-h04 | 0.126 | 0.106 | tie |
| debugging-h05 | 0.46 | 0.158 | loss |
| debugging-h06 | 0.101 | 0.118 | tie |
| explanation-h01 | 0.081 | 0.09 | tie |
| explanation-h02 | 0.079 | 0.07 | tie |
| explanation-h03 | 0.141 | 0.123 | tie |
| explanation-h04 | 0.104 | 0.112 | tie |
| explanation-h05 | 0.089 | 0.207 | win |
| explanation-h06 | 0.128 | 0.132 | tie |
| summarization-h01 | 0.163 | 0.144 | tie |
| summarization-h02 | 0.123 | 0.124 | tie |
| summarization-h03 | 0.167 | 0.125 | loss |
| summarization-h04 | 0.122 | 0.0 | loss |
| summarization-h05 | 0.234 | 0.165 | loss |
| summarization-h06 | 0.069 | 0.082 | tie |

### clarity-flow

| Pair | Styled | Unstyled | Result |
|---|---|---|---|
| code-review-h01 | 0.112 | 0.117 | tie |
| code-review-h02 | 0.153 | 0.109 | loss |
| code-review-h03 | 0.034 | 0.097 | win |
| code-review-h04 | 0.138 | 0.333 | win |
| code-review-h05 | 0.082 | 0.074 | tie |
| code-review-h06 | 0.111 | 0.119 | tie |
| debugging-h01 | 0.1 | 0.055 | loss |
| debugging-h02 | 0.057 | 0.059 | tie |
| debugging-h03 | 0.143 | 0.089 | loss |
| debugging-h04 | 0.119 | 0.106 | tie |
| debugging-h05 | 0.097 | 0.158 | win |
| debugging-h06 | 0.134 | 0.118 | tie |
| explanation-h01 | 0.066 | 0.09 | win |
| explanation-h02 | 0.073 | 0.07 | tie |
| explanation-h03 | 0.088 | 0.123 | win |
| explanation-h04 | 0.075 | 0.112 | win |
| explanation-h05 | 0.098 | 0.207 | win |
| explanation-h06 | 0.139 | 0.132 | tie |
| summarization-h01 | 0.096 | 0.144 | win |
| summarization-h02 | 0.171 | 0.124 | loss |
| summarization-h03 | 0.138 | 0.125 | tie |
| summarization-h04 | 0.151 | 0.0 | loss |
| summarization-h05 | 0.164 | 0.165 | tie |
| summarization-h06 | 0.132 | 0.082 | loss |

### classic-concise

| Pair | Styled | Unstyled | Result |
|---|---|---|---|
| code-review-h01 | 0.087 | 0.117 | win |
| code-review-h02 | 0.108 | 0.109 | tie |
| code-review-h03 | 0.086 | 0.097 | tie |
| code-review-h04 | 0.065 | 0.333 | win |
| code-review-h05 | 0.103 | 0.074 | loss |
| code-review-h06 | 0.111 | 0.119 | tie |
| debugging-h01 | 0.085 | 0.055 | loss |
| debugging-h02 | 0.05 | 0.059 | tie |
| debugging-h03 | 0.107 | 0.089 | tie |
| debugging-h04 | 0.131 | 0.106 | loss |
| debugging-h05 | 0.132 | 0.158 | win |
| debugging-h06 | 0.143 | 0.118 | loss |
| explanation-h01 | 0.07 | 0.09 | tie |
| explanation-h02 | 0.067 | 0.07 | tie |
| explanation-h03 | 0.101 | 0.123 | win |
| explanation-h04 | 0.062 | 0.112 | win |
| explanation-h05 | 0.138 | 0.207 | win |
| explanation-h06 | 0.086 | 0.132 | win |
| summarization-h01 | 0.146 | 0.144 | tie |
| summarization-h02 | 0.181 | 0.124 | loss |
| summarization-h03 | 0.108 | 0.125 | tie |
| summarization-h04 | 0.155 | 0.0 | loss |
| summarization-h05 | 0.208 | 0.165 | loss |
| summarization-h06 | 0.216 | 0.082 | loss |

### developer-docs

| Pair | Styled | Unstyled | Result |
|---|---|---|---|
| code-review-h01 | 0.086 | 0.117 | win |
| code-review-h02 | 0.104 | 0.109 | tie |
| code-review-h03 | 0.077 | 0.097 | win |
| code-review-h04 | 0.533 | 0.333 | loss |
| code-review-h05 | 0.157 | 0.074 | loss |
| code-review-h06 | 0.273 | 0.119 | loss |
| debugging-h01 | 0.045 | 0.055 | tie |
| debugging-h02 | 0.073 | 0.059 | tie |
| debugging-h03 | 0.079 | 0.089 | tie |
| debugging-h04 | 0.101 | 0.106 | tie |
| debugging-h05 | 0.125 | 0.158 | win |
| debugging-h06 | 0.101 | 0.118 | tie |
| explanation-h01 | 0.094 | 0.09 | tie |
| explanation-h02 | 0.076 | 0.07 | tie |
| explanation-h03 | 0.085 | 0.123 | win |
| explanation-h04 | 0.082 | 0.112 | win |
| explanation-h05 | 0.083 | 0.207 | win |
| explanation-h06 | 0.083 | 0.132 | win |
| summarization-h01 | 0.154 | 0.144 | tie |
| summarization-h02 | 0.152 | 0.124 | loss |
| summarization-h03 | 0.083 | 0.125 | win |
| summarization-h04 | 0.127 | 0.0 | loss |
| summarization-h05 | 0.185 | 0.165 | loss |
| summarization-h06 | 0.149 | 0.082 | loss |

### plain-language

| Pair | Styled | Unstyled | Result |
|---|---|---|---|
| code-review-h01 | 0.122 | 0.117 | tie |
| code-review-h02 | 0.11 | 0.109 | tie |
| code-review-h03 | 0.071 | 0.097 | win |
| code-review-h04 | 0.078 | 0.333 | win |
| code-review-h05 | 0.6 | 0.074 | loss |
| code-review-h06 | 0.651 | 0.119 | loss |
| debugging-h01 | 0.061 | 0.055 | tie |
| debugging-h02 | 0.077 | 0.059 | tie |
| debugging-h03 | 0.071 | 0.089 | tie |
| debugging-h04 | 0.123 | 0.106 | tie |
| debugging-h05 | 0.081 | 0.158 | win |
| debugging-h06 | 0.935 | 0.118 | loss |
| explanation-h01 | 0.048 | 0.09 | win |
| explanation-h02 | 0.089 | 0.07 | tie |
| explanation-h03 | 0.102 | 0.123 | win |
| explanation-h04 | 0.083 | 0.112 | win |
| explanation-h05 | 0.109 | 0.207 | win |
| explanation-h06 | 0.124 | 0.132 | tie |
| summarization-h01 | 0.087 | 0.144 | win |
| summarization-h02 | 0.079 | 0.124 | win |
| summarization-h03 | 0.106 | 0.125 | tie |
| summarization-h04 | 0.108 | 0.0 | loss |
| summarization-h05 | 0.289 | 0.165 | loss |
| summarization-h06 | 0.057 | 0.082 | win |

### technical-simplified

| Pair | Styled | Unstyled | Result |
|---|---|---|---|
| code-review-h01 | 0.064 | 0.117 | win |
| code-review-h02 | 0.164 | 0.109 | loss |
| code-review-h03 | 0.067 | 0.097 | win |
| code-review-h04 | 0.053 | 0.333 | win |
| code-review-h05 | 0.085 | 0.074 | tie |
| debugging-h01 | 0.073 | 0.055 | tie |
| debugging-h02 | 0.044 | 0.059 | tie |
| debugging-h03 | 0.078 | 0.089 | tie |
| debugging-h04 | 0.151 | 0.106 | loss |
| debugging-h05 | 0.129 | 0.158 | win |
| debugging-h06 | 0.103 | 0.118 | tie |
| explanation-h01 | 0.068 | 0.09 | win |
| explanation-h02 | 0.096 | 0.07 | loss |
| explanation-h03 | 0.113 | 0.123 | tie |
| explanation-h04 | 0.074 | 0.112 | win |
| explanation-h05 | 0.124 | 0.207 | win |
| explanation-h06 | 0.201 | 0.132 | loss |
| summarization-h01 | 0.095 | 0.144 | win |
| summarization-h02 | 0.118 | 0.124 | tie |
| summarization-h04 | 0.161 | 0.0 | loss |
| summarization-h05 | 0.714 | 0.165 | loss |

## Call timing

A stored call row holds two times: duration_ms is the model
time that the CLI reports, and wall_ms is the wall clock of
the subprocess. The difference is the startup cost of one CLI
call.

Calls: 2341, measured: 2341.
Mean duration: 11440 ms. Mean wall: 17771 ms. Mean startup: 6331 ms.

## Harness spend

A stored call row holds the token counts of its call: the
uncached input, cache-write input, cache-read input, and
output tokens. The cache-read share is the cache-read total
over the whole input total.

Calls: 2341, measured: 2341.
Input tokens: 16858 uncached, 2028654 cache write, 11105468 cache read. Output tokens: 2459698.
Cache-read share: 0.844.
Cache writes by lifetime: 2028654 at 5 minutes, 0 at 1 hour.

## Warnings

- actionable-clarity/code-review-h06: the pair failed the gate, excluded
- technical-simplified/summarization-h03: the pair failed the gate, excluded
- technical-simplified/code-review-h06: the pair failed the gate, excluded
- technical-simplified/summarization-h06: the pair failed the gate, excluded
- actionable-clarity/code-review-h01: the pair has 0 shared facts, fewer than the floor of 3, so comprehension skips the pair
- actionable-clarity/code-review-h04: the pair has 0 shared facts, fewer than the floor of 3, so comprehension skips the pair
- actionable-clarity/debugging-h05: the pair has 1 shared facts, fewer than the floor of 3, so comprehension skips the pair
- actionable-clarity/summarization-h04: the pair has 0 shared facts, fewer than the floor of 3, so comprehension skips the pair
- clarity-flow/code-review-h04: the pair has 0 shared facts, fewer than the floor of 3, so comprehension skips the pair
- clarity-flow/debugging-h05: the pair has 1 shared facts, fewer than the floor of 3, so comprehension skips the pair
- clarity-flow/summarization-h04: the pair has 0 shared facts, fewer than the floor of 3, so comprehension skips the pair
- classic-concise/code-review-h04: the pair has 0 shared facts, fewer than the floor of 3, so comprehension skips the pair
- classic-concise/debugging-h05: the pair has 1 shared facts, fewer than the floor of 3, so comprehension skips the pair
- classic-concise/summarization-h04: the pair has 0 shared facts, fewer than the floor of 3, so comprehension skips the pair
- developer-docs/code-review-h06: the pair has 0 shared facts, fewer than the floor of 3, so comprehension skips the pair
- developer-docs/debugging-h05: the pair has 1 shared facts, fewer than the floor of 3, so comprehension skips the pair
- developer-docs/summarization-h04: the pair has 1 shared facts, fewer than the floor of 3, so comprehension skips the pair
- plain-language/code-review-h04: the pair has 0 shared facts, fewer than the floor of 3, so comprehension skips the pair
- plain-language/code-review-h05: the pair has 0 shared facts, fewer than the floor of 3, so comprehension skips the pair
- plain-language/code-review-h06: the pair has 0 shared facts, fewer than the floor of 3, so comprehension skips the pair
- plain-language/debugging-h05: the pair has 1 shared facts, fewer than the floor of 3, so comprehension skips the pair
- plain-language/debugging-h06: the pair has 0 shared facts, fewer than the floor of 3, so comprehension skips the pair
- plain-language/summarization-h04: the pair has 0 shared facts, fewer than the floor of 3, so comprehension skips the pair
- technical-simplified/code-review-h04: the pair has 2 shared facts, fewer than the floor of 3, so comprehension skips the pair
- technical-simplified/debugging-h05: the pair has 1 shared facts, fewer than the floor of 3, so comprehension skips the pair
- technical-simplified/summarization-h04: the pair has 0 shared facts, fewer than the floor of 3, so comprehension skips the pair
- technical-simplified/summarization-h05: the pair has 0 shared facts, fewer than the floor of 3, so comprehension skips the pair
- actionable-clarity/code-review-h01: the comprehension check has no usable questions for the pair, so the pair is unscored
- actionable-clarity/code-review-h04: the comprehension check has no usable questions for the pair, so the pair is unscored
- actionable-clarity/debugging-h05: the comprehension check has no usable questions for the pair, so the pair is unscored
- actionable-clarity/summarization-h04: the comprehension check has no usable questions for the pair, so the pair is unscored
- clarity-flow/code-review-h04: the comprehension check has no usable questions for the pair, so the pair is unscored
- clarity-flow/debugging-h05: the comprehension check has no usable questions for the pair, so the pair is unscored
- clarity-flow/summarization-h04: the comprehension check has no usable questions for the pair, so the pair is unscored
- classic-concise/code-review-h04: the comprehension check has no usable questions for the pair, so the pair is unscored
- classic-concise/debugging-h05: the comprehension check has no usable questions for the pair, so the pair is unscored
- classic-concise/summarization-h04: the comprehension check has no usable questions for the pair, so the pair is unscored
- developer-docs/code-review-h06: the comprehension check has no usable questions for the pair, so the pair is unscored
- developer-docs/debugging-h05: the comprehension check has no usable questions for the pair, so the pair is unscored
- developer-docs/summarization-h04: the comprehension check has no usable questions for the pair, so the pair is unscored
- plain-language/code-review-h04: the comprehension check has no usable questions for the pair, so the pair is unscored
- plain-language/code-review-h05: the comprehension check has no usable questions for the pair, so the pair is unscored
- plain-language/code-review-h06: the comprehension check has no usable questions for the pair, so the pair is unscored
- plain-language/debugging-h05: the comprehension check has no usable questions for the pair, so the pair is unscored
- plain-language/debugging-h06: the comprehension check has no usable questions for the pair, so the pair is unscored
- plain-language/summarization-h04: the comprehension check has no usable questions for the pair, so the pair is unscored
- technical-simplified/code-review-h04: the comprehension check has no usable questions for the pair, so the pair is unscored
- technical-simplified/debugging-h05: the comprehension check has no usable questions for the pair, so the pair is unscored
- technical-simplified/summarization-h04: the comprehension check has no usable questions for the pair, so the pair is unscored
- technical-simplified/summarization-h05: the comprehension check has no usable questions for the pair, so the pair is unscored
- actionable-clarity: the styled answer scores worse than the unstyled answer on comprehension (3 wins, 4 losses)
- clarity-flow: the styled answer scores worse than the unstyled answer on comprehension (4 wins, 6 losses)
- developer-docs: the styled answer scores worse than the unstyled answer on comprehension (3 wins, 5 losses)
- plain-language: the styled answer scores worse than the unstyled answer on comprehension (2 wins, 3 losses)
- technical-simplified: the styled answer scores worse than the unstyled answer on comprehension (1 wins, 8 losses)

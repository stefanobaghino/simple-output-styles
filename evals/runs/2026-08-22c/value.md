# Reader-value report

The checks compare the styled answer with the unstyled answer of
the same prompt, pair by pair, as win, loss, or tie. Only pairs
whose styled answer passes the fidelity gate enter the checks.
Each judge call sees one bare text: no style name, no arm label,
and never both answers. Thus a judge cannot know which answer is
styled. The judge models differ from the writer of the answers.

Judges: reader haiku, grader opus. Comprehension asks up to 6 questions per pair, worded by both answers in balance, with 3 reader replicates per answer, ambiguity uses 3 restatements per answer, and the round-trip goes through Italian. Judged on 2026-08-22T12:09:29+00:00.

## Comprehension (weak reader)

The questions come from the shared facts of the pair, mined in both directions: the facts of the unstyled answer that survive in the styled answer, and the facts of the styled answer that the unstyled answer also states. The quiz takes half of its questions from each wording, so neither answer sets the phrasing alone, and the Sources column counts the questions per wording (unstyled/styled). A grader call turns each fact into one question, and the fact is the reference answer. The weak reader answers the questions from one answer text, once per replicate, and the grader marks every reply. Each styled replicate meets each unstyled replicate as a win, a loss, or a tie, and the pair outcome is the strict plurality, else a tie. The agreement is the plurality share, and the buried-fact rate counts "NOT IN TEXT" replies to a shared fact, per arm. The check measures extraction over shared material. Absence belongs to the content-loss report. Higher is better.

| Style | Wins | Losses | Ties | Mean delta | Agreement | Buried (styled) | Buried (unstyled) |
|---|---|---|---|---|---|---|---|
| actionable-clarity | 4 | 6 | 20 | -0.011 | 0.893 | 0.039 | 0.041 |
| clarity-flow | 3 | 5 | 22 | 0.0 | 0.896 | 0.019 | 0.026 |
| classic-concise | 3 | 8 | 19 | -0.044 | 0.87 | 0.065 | 0.039 |
| concise | 5 | 6 | 19 | 0.011 | 0.874 | 0.024 | 0.033 |
| developer-docs | 8 | 2 | 20 | 0.031 | 0.889 | 0.039 | 0.054 |
| plain-language | 6 | 6 | 17 | 0.01 | 0.854 | 0.033 | 0.054 |
| technical-simplified | 3 | 6 | 14 | -0.024 | 0.899 | 0.046 | 0.027 |

The styled answer must not score worse than the unstyled answer.
- actionable-clarity: the styled answer scores worse (4 wins, 6 losses, 20 ties).
- clarity-flow: the styled answer scores worse (3 wins, 5 losses, 22 ties).
- classic-concise: the styled answer scores worse (3 wins, 8 losses, 19 ties).
- concise: the styled answer scores worse (5 wins, 6 losses, 19 ties).
- developer-docs: the styled answer holds (8 wins, 2 losses, 20 ties).
- plain-language: the styled answer holds (6 wins, 6 losses, 17 ties).
- technical-simplified: the styled answer scores worse (3 wins, 6 losses, 14 ties).

### actionable-clarity

| Pair | Questions | Sources (u/s) | Styled | Unstyled | Agreement | Result |
|---|---|---|---|---|---|---|
| code-review-01 | 6 | 3/3 | 1.0 | 0.889 | 0.667 | win |
| code-review-02 | 6 | 3/3 | 0.833 | 1.0 | 1.0 | loss |
| code-review-03 | 6 | 3/3 | 0.833 | 0.889 | 0.667 | tie |
| code-review-04 | 6 | 3/3 | 0.944 | 1.0 | 0.667 | tie |
| code-review-05 | 6 | 3/3 | 1.0 | 0.944 | 0.667 | tie |
| code-review-06 | 6 | 3/3 | 0.833 | 1.0 | 1.0 | loss |
| code-review-07 | 6 | 3/3 | 0.833 | 1.0 | 1.0 | loss |
| code-review-08 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-01 | 6 | 3/3 | 0.833 | 0.833 | 1.0 | tie |
| debugging-02 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-03 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-04 | 6 | 3/3 | 0.889 | 0.944 | 0.444 | tie |
| debugging-05 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-08 | 6 | 3/3 | 1.0 | 0.833 | 1.0 | win |
| explanation-01 | 6 | 3/3 | 0.889 | 1.0 | 0.667 | loss |
| explanation-02 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| explanation-03 | 6 | 3/3 | 0.833 | 1.0 | 1.0 | loss |
| explanation-04 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| explanation-05 | 6 | 3/3 | 0.722 | 0.833 | 0.667 | loss |
| explanation-06 | 6 | 3/3 | 0.889 | 0.833 | 0.667 | tie |
| explanation-07 | 6 | 3/3 | 0.833 | 0.889 | 0.667 | tie |
| explanation-08 | 6 | 3/3 | 1.0 | 0.778 | 1.0 | win |
| summarization-01 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-02 | 6 | 3/3 | 1.0 | 0.833 | 1.0 | win |
| summarization-03 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-04 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-05 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-06 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-07 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-08 | 6 | 3/3 | 0.833 | 0.833 | 1.0 | tie |

### clarity-flow

| Pair | Questions | Sources (u/s) | Styled | Unstyled | Agreement | Result |
|---|---|---|---|---|---|---|
| code-review-01 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| code-review-02 | 6 | 3/3 | 0.833 | 1.0 | 1.0 | loss |
| code-review-03 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| code-review-04 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| code-review-05 | 6 | 3/3 | 0.944 | 0.778 | 0.778 | win |
| code-review-06 | 6 | 3/3 | 0.833 | 1.0 | 1.0 | loss |
| code-review-07 | 6 | 3/3 | 0.889 | 0.833 | 0.667 | tie |
| code-review-08 | 6 | 3/3 | 0.889 | 1.0 | 0.667 | loss |
| debugging-01 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-02 | 6 | 3/3 | 1.0 | 0.944 | 0.667 | tie |
| debugging-03 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-04 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-05 | 6 | 3/3 | 0.889 | 1.0 | 0.667 | loss |
| debugging-08 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| explanation-01 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| explanation-02 | 6 | 3/3 | 0.944 | 1.0 | 0.667 | tie |
| explanation-03 | 6 | 3/3 | 1.0 | 0.944 | 0.667 | tie |
| explanation-04 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| explanation-05 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| explanation-06 | 6 | 3/3 | 0.833 | 1.0 | 1.0 | loss |
| explanation-07 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| explanation-08 | 6 | 3/3 | 1.0 | 0.833 | 1.0 | win |
| summarization-01 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-02 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-03 | 6 | 3/3 | 1.0 | 0.944 | 0.667 | tie |
| summarization-04 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-05 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-06 | 6 | 3/3 | 0.944 | 0.722 | 0.889 | win |
| summarization-07 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-08 | 6 | 3/3 | 0.889 | 0.889 | 0.556 | tie |

### classic-concise

| Pair | Questions | Sources (u/s) | Styled | Unstyled | Agreement | Result |
|---|---|---|---|---|---|---|
| code-review-01 | 6 | 3/3 | 1.0 | 0.778 | 1.0 | win |
| code-review-02 | 6 | 3/3 | 0.833 | 1.0 | 0.667 | loss |
| code-review-03 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| code-review-04 | 6 | 3/3 | 0.778 | 1.0 | 1.0 | loss |
| code-review-05 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| code-review-06 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| code-review-07 | 6 | 3/3 | 0.944 | 0.944 | 0.556 | tie |
| code-review-08 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-01 | 6 | 3/3 | 0.667 | 0.833 | 1.0 | loss |
| debugging-02 | 6 | 3/3 | 0.889 | 1.0 | 0.667 | loss |
| debugging-03 | 6 | 3/3 | 0.667 | 1.0 | 1.0 | loss |
| debugging-04 | 6 | 3/3 | 0.667 | 1.0 | 1.0 | loss |
| debugging-05 | 6 | 3/3 | 0.944 | 1.0 | 0.667 | tie |
| debugging-08 | 6 | 3/3 | 1.0 | 0.833 | 1.0 | win |
| explanation-01 | 6 | 3/3 | 0.778 | 1.0 | 1.0 | loss |
| explanation-02 | 6 | 3/3 | 0.944 | 1.0 | 0.667 | tie |
| explanation-03 | 6 | 3/3 | 0.722 | 1.0 | 1.0 | loss |
| explanation-04 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| explanation-05 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| explanation-06 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| explanation-07 | 6 | 3/3 | 0.778 | 0.722 | 0.444 | tie |
| explanation-08 | 6 | 3/3 | 1.0 | 0.833 | 1.0 | win |
| summarization-01 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-02 | 6 | 3/3 | 0.944 | 0.944 | 0.556 | tie |
| summarization-03 | 6 | 3/3 | 0.833 | 0.778 | 0.667 | tie |
| summarization-04 | 6 | 3/3 | 0.722 | 0.722 | 0.556 | tie |
| summarization-05 | 6 | 3/3 | 0.833 | 0.833 | 1.0 | tie |
| summarization-06 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-07 | 6 | 3/3 | 0.833 | 0.889 | 0.667 | tie |
| summarization-08 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |

### concise

| Pair | Questions | Sources (u/s) | Styled | Unstyled | Agreement | Result |
|---|---|---|---|---|---|---|
| code-review-01 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| code-review-02 | 6 | 3/3 | 0.833 | 1.0 | 1.0 | loss |
| code-review-03 | 6 | 3/3 | 1.0 | 0.944 | 0.667 | tie |
| code-review-04 | 6 | 3/3 | 0.833 | 1.0 | 1.0 | loss |
| code-review-05 | 6 | 3/3 | 0.889 | 0.833 | 0.667 | tie |
| code-review-06 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| code-review-07 | 6 | 3/3 | 1.0 | 0.889 | 0.667 | win |
| code-review-08 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-01 | 6 | 3/3 | 0.833 | 1.0 | 1.0 | loss |
| debugging-02 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-03 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-04 | 6 | 3/3 | 0.833 | 0.889 | 0.667 | loss |
| debugging-05 | 6 | 3/3 | 0.889 | 0.944 | 0.444 | tie |
| debugging-08 | 6 | 3/3 | 1.0 | 0.889 | 0.667 | win |
| explanation-01 | 6 | 3/3 | 0.889 | 0.944 | 0.444 | tie |
| explanation-02 | 6 | 3/3 | 1.0 | 0.833 | 1.0 | win |
| explanation-03 | 6 | 3/3 | 0.889 | 0.833 | 0.667 | tie |
| explanation-04 | 6 | 3/3 | 1.0 | 0.667 | 1.0 | win |
| explanation-05 | 6 | 3/3 | 0.778 | 1.0 | 1.0 | loss |
| explanation-06 | 6 | 3/3 | 0.833 | 1.0 | 1.0 | loss |
| explanation-07 | 6 | 3/3 | 1.0 | 0.611 | 1.0 | win |
| explanation-08 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-01 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-02 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-03 | 6 | 3/3 | 1.0 | 0.944 | 0.667 | tie |
| summarization-04 | 6 | 3/3 | 1.0 | 0.944 | 0.667 | tie |
| summarization-05 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-06 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-07 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-08 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |

### developer-docs

| Pair | Questions | Sources (u/s) | Styled | Unstyled | Agreement | Result |
|---|---|---|---|---|---|---|
| code-review-01 | 6 | 3/3 | 1.0 | 0.944 | 0.667 | tie |
| code-review-02 | 6 | 3/3 | 1.0 | 0.833 | 1.0 | win |
| code-review-03 | 6 | 3/3 | 0.944 | 0.833 | 0.667 | win |
| code-review-04 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| code-review-05 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| code-review-06 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| code-review-07 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| code-review-08 | 6 | 3/3 | 0.778 | 0.778 | 0.556 | tie |
| debugging-01 | 6 | 3/3 | 0.833 | 0.833 | 1.0 | tie |
| debugging-02 | 6 | 3/3 | 0.889 | 0.944 | 0.444 | tie |
| debugging-03 | 6 | 3/3 | 1.0 | 0.833 | 1.0 | win |
| debugging-04 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-05 | 6 | 3/3 | 0.944 | 1.0 | 0.667 | tie |
| debugging-08 | 6 | 3/3 | 0.833 | 1.0 | 1.0 | loss |
| explanation-01 | 6 | 3/3 | 0.833 | 0.833 | 1.0 | tie |
| explanation-02 | 6 | 3/3 | 1.0 | 0.944 | 0.667 | tie |
| explanation-03 | 6 | 3/3 | 0.833 | 0.833 | 1.0 | tie |
| explanation-04 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| explanation-05 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| explanation-06 | 6 | 3/3 | 1.0 | 0.889 | 0.667 | win |
| explanation-07 | 6 | 3/3 | 0.722 | 0.833 | 0.667 | loss |
| explanation-08 | 6 | 3/3 | 1.0 | 0.833 | 1.0 | win |
| summarization-01 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-02 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-03 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-04 | 6 | 3/3 | 1.0 | 0.833 | 1.0 | win |
| summarization-05 | 6 | 3/3 | 1.0 | 0.833 | 1.0 | win |
| summarization-06 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-07 | 6 | 3/3 | 0.833 | 0.833 | 1.0 | tie |
| summarization-08 | 6 | 3/3 | 1.0 | 0.833 | 0.667 | win |

### plain-language

| Pair | Questions | Sources (u/s) | Styled | Unstyled | Agreement | Result |
|---|---|---|---|---|---|---|
| code-review-01 | 6 | 3/3 | 1.0 | 0.944 | 0.667 | tie |
| code-review-02 | 6 | 3/3 | 0.833 | 1.0 | 1.0 | loss |
| code-review-03 | 6 | 3/3 | 1.0 | 0.944 | 0.667 | tie |
| code-review-04 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| code-review-05 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| code-review-07 | 6 | 3/3 | 1.0 | 0.889 | 0.667 | win |
| code-review-08 | 6 | 3/3 | 0.833 | 0.944 | 0.667 | loss |
| debugging-01 | 6 | 3/3 | 0.833 | 0.833 | 1.0 | tie |
| debugging-02 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-03 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-04 | 6 | 3/3 | 0.833 | 0.833 | 1.0 | tie |
| debugging-05 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-08 | 6 | 3/3 | 0.778 | 0.944 | 0.778 | loss |
| explanation-01 | 6 | 3/3 | 1.0 | 0.833 | 1.0 | win |
| explanation-02 | 6 | 3/3 | 0.944 | 0.833 | 0.667 | win |
| explanation-03 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| explanation-04 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| explanation-05 | 6 | 3/3 | 0.944 | 0.833 | 0.667 | win |
| explanation-06 | 6 | 3/3 | 0.833 | 0.889 | 0.444 | loss |
| explanation-07 | 6 | 3/3 | 0.833 | 0.944 | 0.556 | loss |
| explanation-08 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-01 | 6 | 3/3 | 0.833 | 0.833 | 1.0 | tie |
| summarization-02 | 6 | 3/3 | 0.833 | 0.889 | 0.667 | tie |
| summarization-03 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-04 | 6 | 3/3 | 1.0 | 0.889 | 0.667 | win |
| summarization-05 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-06 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-07 | 6 | 3/3 | 0.833 | 0.5 | 1.0 | win |
| summarization-08 | 6 | 3/3 | 0.667 | 0.778 | 0.667 | loss |

### technical-simplified

| Pair | Questions | Sources (u/s) | Styled | Unstyled | Agreement | Result |
|---|---|---|---|---|---|---|
| code-review-01 | 6 | 3/3 | 1.0 | 0.889 | 0.667 | win |
| code-review-02 | 6 | 3/3 | 0.833 | 0.889 | 0.444 | loss |
| code-review-03 | 6 | 3/3 | 1.0 | 0.944 | 0.667 | tie |
| code-review-04 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| code-review-05 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| code-review-06 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-01 | 6 | 3/3 | 0.833 | 0.833 | 1.0 | tie |
| debugging-02 | 6 | 3/3 | 0.778 | 1.0 | 1.0 | loss |
| debugging-03 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-04 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-05 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-08 | 6 | 3/3 | 1.0 | 0.833 | 1.0 | win |
| explanation-01 | 6 | 3/3 | 0.778 | 0.889 | 0.556 | loss |
| explanation-02 | 6 | 3/3 | 1.0 | 0.889 | 0.667 | win |
| explanation-03 | 6 | 3/3 | 0.833 | 1.0 | 1.0 | loss |
| explanation-04 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| explanation-05 | 6 | 3/3 | 0.667 | 1.0 | 1.0 | loss |
| explanation-06 | 6 | 3/3 | 0.833 | 0.944 | 0.667 | loss |
| summarization-01 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-02 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-03 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-04 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-05 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |

## Ambiguity (paraphrase agreement)

Independent reader calls restate one answer text in their own words. The score is the mean pairwise lexical similarity between the restatements: when the readers agree on what the text says, the text is less ambiguous. Higher is better.

| Style | Wins | Losses | Ties |
|---|---|---|---|
| actionable-clarity | 16 | 8 | 8 |
| clarity-flow | 11 | 13 | 8 |
| classic-concise | 12 | 15 | 5 |
| concise | 10 | 14 | 8 |
| developer-docs | 13 | 9 | 10 |
| plain-language | 14 | 8 | 10 |
| technical-simplified | 13 | 8 | 5 |

The length confound is the correlation between the length ratio of a pair (styled words over unstyled words) and the styled advantage (the score gain of the styled arm). A negative value means that the shorter styled answers score better.
- actionable-clarity: Pearson 0.101, Spearman 0.076, over 32 pairs.
- clarity-flow: Pearson 0.471, Spearman 0.105, over 32 pairs.
- classic-concise: Pearson 0.369, Spearman 0.264, over 32 pairs.
- concise: Pearson 0.455, Spearman -0.05, over 32 pairs.
- developer-docs: Pearson 0.527, Spearman 0.273, over 32 pairs.
- plain-language: Pearson 0.346, Spearman 0.167, over 32 pairs.
- technical-simplified: Pearson 0.246, Spearman 0.264, over 26 pairs.

### actionable-clarity

| Pair | Styled | Unstyled | Result |
|---|---|---|---|
| code-review-01 | 0.757 | 0.643 | win |
| code-review-02 | 0.775 | 0.743 | win |
| code-review-03 | 0.687 | 0.718 | loss |
| code-review-04 | 0.704 | 0.629 | win |
| code-review-05 | 0.704 | 0.635 | win |
| code-review-06 | 0.675 | 0.716 | loss |
| code-review-07 | 0.64 | 0.705 | loss |
| code-review-08 | 0.69 | 0.701 | tie |
| debugging-01 | 0.757 | 0.566 | win |
| debugging-02 | 0.803 | 0.676 | win |
| debugging-03 | 0.796 | 0.778 | tie |
| debugging-04 | 0.743 | 0.777 | loss |
| debugging-05 | 0.75 | 0.721 | win |
| debugging-06 | 0.199 | 0.211 | tie |
| debugging-07 | 0.688 | 0.631 | win |
| debugging-08 | 0.597 | 0.645 | loss |
| explanation-01 | 0.669 | 0.754 | loss |
| explanation-02 | 0.768 | 0.712 | win |
| explanation-03 | 0.694 | 0.701 | tie |
| explanation-04 | 0.706 | 0.654 | win |
| explanation-05 | 0.692 | 0.636 | win |
| explanation-06 | 0.606 | 0.627 | loss |
| explanation-07 | 0.594 | 0.58 | tie |
| explanation-08 | 0.674 | 0.573 | win |
| summarization-01 | 0.607 | 0.74 | loss |
| summarization-02 | 0.642 | 0.642 | tie |
| summarization-03 | 0.656 | 0.671 | tie |
| summarization-04 | 0.711 | 0.665 | win |
| summarization-05 | 0.783 | 0.759 | win |
| summarization-06 | 0.718 | 0.653 | win |
| summarization-07 | 0.657 | 0.608 | win |
| summarization-08 | 0.615 | 0.633 | tie |

### clarity-flow

| Pair | Styled | Unstyled | Result |
|---|---|---|---|
| code-review-01 | 0.703 | 0.643 | win |
| code-review-02 | 0.62 | 0.743 | loss |
| code-review-03 | 0.683 | 0.718 | loss |
| code-review-04 | 0.715 | 0.629 | win |
| code-review-05 | 0.652 | 0.635 | tie |
| code-review-06 | 0.649 | 0.716 | loss |
| code-review-07 | 0.659 | 0.705 | loss |
| code-review-08 | 0.666 | 0.701 | loss |
| debugging-01 | 0.58 | 0.566 | tie |
| debugging-02 | 0.738 | 0.676 | win |
| debugging-03 | 0.811 | 0.778 | win |
| debugging-04 | 0.802 | 0.777 | win |
| debugging-05 | 0.732 | 0.721 | tie |
| debugging-06 | 0.628 | 0.211 | win |
| debugging-07 | 0.689 | 0.631 | win |
| debugging-08 | 0.631 | 0.645 | tie |
| explanation-01 | 0.642 | 0.754 | loss |
| explanation-02 | 0.614 | 0.712 | loss |
| explanation-03 | 0.686 | 0.701 | tie |
| explanation-04 | 0.669 | 0.654 | tie |
| explanation-05 | 0.718 | 0.636 | win |
| explanation-06 | 0.682 | 0.627 | win |
| explanation-07 | 0.563 | 0.58 | tie |
| explanation-08 | 0.647 | 0.573 | win |
| summarization-01 | 0.626 | 0.74 | loss |
| summarization-02 | 0.617 | 0.642 | loss |
| summarization-03 | 0.636 | 0.671 | loss |
| summarization-04 | 0.574 | 0.665 | loss |
| summarization-05 | 0.692 | 0.759 | loss |
| summarization-06 | 0.682 | 0.653 | win |
| summarization-07 | 0.595 | 0.608 | tie |
| summarization-08 | 0.591 | 0.633 | loss |

### classic-concise

| Pair | Styled | Unstyled | Result |
|---|---|---|---|
| code-review-01 | 0.63 | 0.643 | tie |
| code-review-02 | 0.614 | 0.743 | loss |
| code-review-03 | 0.672 | 0.718 | loss |
| code-review-04 | 0.701 | 0.629 | win |
| code-review-05 | 0.642 | 0.635 | tie |
| code-review-06 | 0.686 | 0.716 | loss |
| code-review-07 | 0.663 | 0.705 | loss |
| code-review-08 | 0.657 | 0.701 | loss |
| debugging-01 | 0.704 | 0.566 | win |
| debugging-02 | 0.704 | 0.676 | win |
| debugging-03 | 0.569 | 0.778 | loss |
| debugging-04 | 0.541 | 0.777 | loss |
| debugging-05 | 0.759 | 0.721 | win |
| debugging-06 | 0.628 | 0.211 | win |
| debugging-07 | 0.657 | 0.631 | win |
| debugging-08 | 0.615 | 0.645 | loss |
| explanation-01 | 0.659 | 0.754 | loss |
| explanation-02 | 0.671 | 0.712 | loss |
| explanation-03 | 0.763 | 0.701 | win |
| explanation-04 | 0.678 | 0.654 | win |
| explanation-05 | 0.656 | 0.636 | tie |
| explanation-06 | 0.599 | 0.627 | loss |
| explanation-07 | 0.543 | 0.58 | loss |
| explanation-08 | 0.632 | 0.573 | win |
| summarization-01 | 0.695 | 0.74 | loss |
| summarization-02 | 0.665 | 0.642 | win |
| summarization-03 | 0.648 | 0.671 | loss |
| summarization-04 | 0.726 | 0.665 | win |
| summarization-05 | 0.743 | 0.759 | tie |
| summarization-06 | 0.665 | 0.653 | tie |
| summarization-07 | 0.701 | 0.608 | win |
| summarization-08 | 0.608 | 0.633 | loss |

### concise

| Pair | Styled | Unstyled | Result |
|---|---|---|---|
| code-review-01 | 0.638 | 0.643 | tie |
| code-review-02 | 0.707 | 0.743 | loss |
| code-review-03 | 0.627 | 0.718 | loss |
| code-review-04 | 0.675 | 0.629 | win |
| code-review-05 | 0.755 | 0.635 | win |
| code-review-06 | 0.644 | 0.716 | loss |
| code-review-07 | 0.663 | 0.705 | loss |
| code-review-08 | 0.673 | 0.701 | loss |
| debugging-01 | 0.609 | 0.566 | win |
| debugging-02 | 0.768 | 0.676 | win |
| debugging-03 | 0.766 | 0.778 | tie |
| debugging-04 | 0.706 | 0.777 | loss |
| debugging-05 | 0.645 | 0.721 | loss |
| debugging-06 | 0.616 | 0.211 | win |
| debugging-07 | 0.668 | 0.631 | win |
| debugging-08 | 0.65 | 0.645 | tie |
| explanation-01 | 0.666 | 0.754 | loss |
| explanation-02 | 0.672 | 0.712 | loss |
| explanation-03 | 0.642 | 0.701 | loss |
| explanation-04 | 0.687 | 0.654 | win |
| explanation-05 | 0.649 | 0.636 | tie |
| explanation-06 | 0.629 | 0.627 | tie |
| explanation-07 | 0.553 | 0.58 | loss |
| explanation-08 | 0.556 | 0.573 | tie |
| summarization-01 | 0.695 | 0.74 | loss |
| summarization-02 | 0.605 | 0.642 | loss |
| summarization-03 | 0.655 | 0.671 | tie |
| summarization-04 | 0.692 | 0.665 | win |
| summarization-05 | 0.8 | 0.759 | win |
| summarization-06 | 0.595 | 0.653 | loss |
| summarization-07 | 0.646 | 0.608 | win |
| summarization-08 | 0.631 | 0.633 | tie |

### developer-docs

| Pair | Styled | Unstyled | Result |
|---|---|---|---|
| code-review-01 | 0.642 | 0.643 | tie |
| code-review-02 | 0.648 | 0.743 | loss |
| code-review-03 | 0.688 | 0.718 | loss |
| code-review-04 | 0.695 | 0.629 | win |
| code-review-05 | 0.748 | 0.635 | win |
| code-review-06 | 0.67 | 0.716 | loss |
| code-review-07 | 0.627 | 0.705 | loss |
| code-review-08 | 0.704 | 0.701 | tie |
| debugging-01 | 0.642 | 0.566 | win |
| debugging-02 | 0.674 | 0.676 | tie |
| debugging-03 | 0.862 | 0.778 | win |
| debugging-04 | 0.74 | 0.777 | loss |
| debugging-05 | 0.731 | 0.721 | tie |
| debugging-06 | 0.666 | 0.211 | win |
| debugging-07 | 0.712 | 0.631 | win |
| debugging-08 | 0.635 | 0.645 | tie |
| explanation-01 | 0.717 | 0.754 | loss |
| explanation-02 | 0.684 | 0.712 | loss |
| explanation-03 | 0.707 | 0.701 | tie |
| explanation-04 | 0.69 | 0.654 | win |
| explanation-05 | 0.694 | 0.636 | win |
| explanation-06 | 0.626 | 0.627 | tie |
| explanation-07 | 0.625 | 0.58 | win |
| explanation-08 | 0.623 | 0.573 | win |
| summarization-01 | 0.709 | 0.74 | loss |
| summarization-02 | 0.664 | 0.642 | win |
| summarization-03 | 0.553 | 0.671 | loss |
| summarization-04 | 0.671 | 0.665 | tie |
| summarization-05 | 0.772 | 0.759 | tie |
| summarization-06 | 0.721 | 0.653 | win |
| summarization-07 | 0.626 | 0.608 | tie |
| summarization-08 | 0.678 | 0.633 | win |

### plain-language

| Pair | Styled | Unstyled | Result |
|---|---|---|---|
| code-review-01 | 0.634 | 0.643 | tie |
| code-review-02 | 0.772 | 0.743 | win |
| code-review-03 | 0.648 | 0.718 | loss |
| code-review-04 | 0.742 | 0.629 | win |
| code-review-05 | 0.636 | 0.635 | tie |
| code-review-06 | 0.691 | 0.716 | loss |
| code-review-07 | 0.714 | 0.705 | tie |
| code-review-08 | 0.692 | 0.701 | tie |
| debugging-01 | 0.711 | 0.566 | win |
| debugging-02 | 0.773 | 0.676 | win |
| debugging-03 | 0.825 | 0.778 | win |
| debugging-04 | 0.774 | 0.777 | tie |
| debugging-05 | 0.749 | 0.721 | win |
| debugging-06 | 0.642 | 0.211 | win |
| debugging-07 | 0.588 | 0.631 | loss |
| debugging-08 | 0.637 | 0.645 | tie |
| explanation-01 | 0.68 | 0.754 | loss |
| explanation-02 | 0.59 | 0.712 | loss |
| explanation-03 | 0.708 | 0.701 | tie |
| explanation-04 | 0.686 | 0.654 | win |
| explanation-05 | 0.678 | 0.636 | win |
| explanation-06 | 0.644 | 0.627 | tie |
| explanation-07 | 0.6 | 0.58 | win |
| explanation-08 | 0.67 | 0.573 | win |
| summarization-01 | 0.622 | 0.74 | loss |
| summarization-02 | 0.646 | 0.642 | tie |
| summarization-03 | 0.721 | 0.671 | win |
| summarization-04 | 0.614 | 0.665 | loss |
| summarization-05 | 0.671 | 0.759 | loss |
| summarization-06 | 0.716 | 0.653 | win |
| summarization-07 | 0.686 | 0.608 | win |
| summarization-08 | 0.623 | 0.633 | tie |

### technical-simplified

| Pair | Styled | Unstyled | Result |
|---|---|---|---|
| code-review-01 | 0.666 | 0.643 | win |
| code-review-02 | 0.678 | 0.743 | loss |
| code-review-03 | 0.72 | 0.718 | tie |
| code-review-04 | 0.656 | 0.629 | win |
| code-review-05 | 0.708 | 0.635 | win |
| code-review-06 | 0.689 | 0.716 | loss |
| code-review-07 | 0.728 | 0.705 | win |
| debugging-01 | 0.826 | 0.566 | win |
| debugging-02 | 0.831 | 0.676 | win |
| debugging-03 | 0.783 | 0.778 | tie |
| debugging-04 | 0.73 | 0.777 | loss |
| debugging-05 | 0.776 | 0.721 | win |
| debugging-07 | 0.751 | 0.631 | win |
| debugging-08 | 0.691 | 0.645 | win |
| explanation-01 | 0.668 | 0.754 | loss |
| explanation-02 | 0.682 | 0.712 | loss |
| explanation-03 | 0.697 | 0.701 | tie |
| explanation-04 | 0.635 | 0.654 | tie |
| explanation-05 | 0.776 | 0.636 | win |
| explanation-06 | 0.592 | 0.627 | loss |
| explanation-07 | 0.346 | 0.58 | loss |
| summarization-01 | 0.672 | 0.74 | loss |
| summarization-02 | 0.698 | 0.642 | win |
| summarization-03 | 0.662 | 0.671 | tie |
| summarization-04 | 0.775 | 0.665 | win |
| summarization-05 | 0.811 | 0.759 | win |

## Translation round-trip

One call translates the answer to another language, and a second call translates the result back to English. The score is the lexical loss between the original and the round-trip: simpler text survives the round-trip with less loss. Lower is better.

| Style | Wins | Losses | Ties |
|---|---|---|---|
| actionable-clarity | 15 | 4 | 13 |
| clarity-flow | 11 | 11 | 10 |
| classic-concise | 10 | 8 | 14 |
| concise | 7 | 9 | 16 |
| developer-docs | 16 | 5 | 11 |
| plain-language | 14 | 9 | 9 |
| technical-simplified | 12 | 7 | 7 |

The length confound is the correlation between the length ratio of a pair (styled words over unstyled words) and the styled advantage (the score gain of the styled arm). A negative value means that the shorter styled answers score better.
- actionable-clarity: Pearson 0.703, Spearman 0.263, over 32 pairs.
- clarity-flow: Pearson 0.744, Spearman 0.507, over 32 pairs.
- classic-concise: Pearson 0.729, Spearman 0.331, over 32 pairs.
- concise: Pearson 0.762, Spearman 0.56, over 32 pairs.
- developer-docs: Pearson 0.767, Spearman 0.345, over 32 pairs.
- plain-language: Pearson 0.755, Spearman 0.178, over 32 pairs.
- technical-simplified: Pearson 0.59, Spearman 0.386, over 26 pairs.

### actionable-clarity

| Pair | Styled | Unstyled | Result |
|---|---|---|---|
| code-review-01 | 0.035 | 0.096 | win |
| code-review-02 | 0.05 | 0.052 | tie |
| code-review-03 | 0.061 | 0.075 | tie |
| code-review-04 | 0.094 | 0.108 | tie |
| code-review-05 | 0.084 | 0.119 | win |
| code-review-06 | 0.071 | 0.084 | tie |
| code-review-07 | 0.094 | 0.094 | tie |
| code-review-08 | 0.107 | 0.159 | win |
| debugging-01 | 0.054 | 0.143 | win |
| debugging-02 | 0.028 | 0.081 | win |
| debugging-03 | 0.071 | 0.013 | loss |
| debugging-04 | 0.072 | 0.064 | tie |
| debugging-05 | 0.051 | 0.127 | win |
| debugging-06 | 0.444 | 0.538 | win |
| debugging-07 | 0.078 | 0.333 | win |
| debugging-08 | 0.124 | 0.089 | loss |
| explanation-01 | 0.132 | 0.123 | tie |
| explanation-02 | 0.1 | 0.093 | tie |
| explanation-03 | 0.092 | 0.12 | win |
| explanation-04 | 0.108 | 0.101 | tie |
| explanation-05 | 0.096 | 0.105 | tie |
| explanation-06 | 0.106 | 0.074 | loss |
| explanation-07 | 0.068 | 0.131 | win |
| explanation-08 | 0.137 | 0.129 | tie |
| summarization-01 | 0.094 | 0.184 | win |
| summarization-02 | 0.136 | 0.212 | win |
| summarization-03 | 0.133 | 0.148 | tie |
| summarization-04 | 0.078 | 0.098 | win |
| summarization-05 | 0.109 | 0.102 | tie |
| summarization-06 | 0.168 | 0.19 | win |
| summarization-07 | 0.259 | 0.174 | loss |
| summarization-08 | 0.185 | 0.208 | win |

### clarity-flow

| Pair | Styled | Unstyled | Result |
|---|---|---|---|
| code-review-01 | 0.066 | 0.096 | win |
| code-review-02 | 0.093 | 0.052 | loss |
| code-review-03 | 0.101 | 0.075 | loss |
| code-review-04 | 0.126 | 0.108 | tie |
| code-review-05 | 0.064 | 0.119 | win |
| code-review-06 | 0.095 | 0.084 | tie |
| code-review-07 | 0.11 | 0.094 | tie |
| code-review-08 | 0.184 | 0.159 | loss |
| debugging-01 | 0.0 | 0.143 | win |
| debugging-02 | 0.071 | 0.081 | tie |
| debugging-03 | 0.011 | 0.013 | tie |
| debugging-04 | 0.077 | 0.064 | tie |
| debugging-05 | 0.119 | 0.127 | tie |
| debugging-06 | 0.108 | 0.538 | win |
| debugging-07 | 0.094 | 0.333 | win |
| debugging-08 | 0.153 | 0.089 | loss |
| explanation-01 | 0.101 | 0.123 | win |
| explanation-02 | 0.163 | 0.093 | loss |
| explanation-03 | 0.142 | 0.12 | loss |
| explanation-04 | 0.109 | 0.101 | tie |
| explanation-05 | 0.154 | 0.105 | loss |
| explanation-06 | 0.129 | 0.074 | loss |
| explanation-07 | 0.164 | 0.131 | loss |
| explanation-08 | 0.132 | 0.129 | tie |
| summarization-01 | 0.11 | 0.184 | win |
| summarization-02 | 0.129 | 0.212 | win |
| summarization-03 | 0.098 | 0.148 | win |
| summarization-04 | 0.164 | 0.098 | loss |
| summarization-05 | 0.06 | 0.102 | win |
| summarization-06 | 0.218 | 0.19 | loss |
| summarization-07 | 0.132 | 0.174 | win |
| summarization-08 | 0.212 | 0.208 | tie |

### classic-concise

| Pair | Styled | Unstyled | Result |
|---|---|---|---|
| code-review-01 | 0.107 | 0.096 | tie |
| code-review-02 | 0.076 | 0.052 | loss |
| code-review-03 | 0.115 | 0.075 | loss |
| code-review-04 | 0.091 | 0.108 | tie |
| code-review-05 | 0.113 | 0.119 | tie |
| code-review-06 | 0.07 | 0.084 | tie |
| code-review-07 | 0.121 | 0.094 | loss |
| code-review-08 | 0.119 | 0.159 | win |
| debugging-01 | 0.114 | 0.143 | win |
| debugging-02 | 0.065 | 0.081 | tie |
| debugging-03 | 0.111 | 0.013 | loss |
| debugging-04 | 0.034 | 0.064 | win |
| debugging-05 | 0.087 | 0.127 | win |
| debugging-06 | 0.097 | 0.538 | win |
| debugging-07 | 0.108 | 0.333 | win |
| debugging-08 | 0.118 | 0.089 | loss |
| explanation-01 | 0.181 | 0.123 | loss |
| explanation-02 | 0.107 | 0.093 | tie |
| explanation-03 | 0.084 | 0.12 | win |
| explanation-04 | 0.1 | 0.101 | tie |
| explanation-05 | 0.106 | 0.105 | tie |
| explanation-06 | 0.067 | 0.074 | tie |
| explanation-07 | 0.097 | 0.131 | win |
| explanation-08 | 0.119 | 0.129 | tie |
| summarization-01 | 0.05 | 0.184 | win |
| summarization-02 | 0.214 | 0.212 | tie |
| summarization-03 | 0.147 | 0.148 | tie |
| summarization-04 | 0.066 | 0.098 | win |
| summarization-05 | 0.109 | 0.102 | tie |
| summarization-06 | 0.24 | 0.19 | loss |
| summarization-07 | 0.182 | 0.174 | tie |
| summarization-08 | 0.254 | 0.208 | loss |

### concise

| Pair | Styled | Unstyled | Result |
|---|---|---|---|
| code-review-01 | 0.092 | 0.096 | tie |
| code-review-02 | 0.046 | 0.052 | tie |
| code-review-03 | 0.078 | 0.075 | tie |
| code-review-04 | 0.094 | 0.108 | tie |
| code-review-05 | 0.142 | 0.119 | loss |
| code-review-06 | 0.116 | 0.084 | loss |
| code-review-07 | 0.084 | 0.094 | tie |
| code-review-08 | 0.162 | 0.159 | tie |
| debugging-01 | 0.136 | 0.143 | tie |
| debugging-02 | 0.07 | 0.081 | tie |
| debugging-03 | 0.05 | 0.013 | loss |
| debugging-04 | 0.068 | 0.064 | tie |
| debugging-05 | 0.108 | 0.127 | tie |
| debugging-06 | 0.127 | 0.538 | win |
| debugging-07 | 0.096 | 0.333 | win |
| debugging-08 | 0.133 | 0.089 | loss |
| explanation-01 | 0.145 | 0.123 | loss |
| explanation-02 | 0.156 | 0.093 | loss |
| explanation-03 | 0.091 | 0.12 | win |
| explanation-04 | 0.129 | 0.101 | loss |
| explanation-05 | 0.131 | 0.105 | loss |
| explanation-06 | 0.087 | 0.074 | tie |
| explanation-07 | 0.099 | 0.131 | win |
| explanation-08 | 0.118 | 0.129 | tie |
| summarization-01 | 0.075 | 0.184 | win |
| summarization-02 | 0.23 | 0.212 | tie |
| summarization-03 | 0.094 | 0.148 | win |
| summarization-04 | 0.063 | 0.098 | win |
| summarization-05 | 0.261 | 0.102 | loss |
| summarization-06 | 0.188 | 0.19 | tie |
| summarization-07 | 0.185 | 0.174 | tie |
| summarization-08 | 0.217 | 0.208 | tie |

### developer-docs

| Pair | Styled | Unstyled | Result |
|---|---|---|---|
| code-review-01 | 0.075 | 0.096 | win |
| code-review-02 | 0.074 | 0.052 | loss |
| code-review-03 | 0.057 | 0.075 | tie |
| code-review-04 | 0.06 | 0.108 | win |
| code-review-05 | 0.081 | 0.119 | win |
| code-review-06 | 0.107 | 0.084 | loss |
| code-review-07 | 0.068 | 0.094 | win |
| code-review-08 | 0.147 | 0.159 | tie |
| debugging-01 | 0.062 | 0.143 | win |
| debugging-02 | 0.059 | 0.081 | win |
| debugging-03 | 0.019 | 0.013 | tie |
| debugging-04 | 0.063 | 0.064 | tie |
| debugging-05 | 0.034 | 0.127 | win |
| debugging-06 | 0.091 | 0.538 | win |
| debugging-07 | 0.079 | 0.333 | win |
| debugging-08 | 0.127 | 0.089 | loss |
| explanation-01 | 0.105 | 0.123 | tie |
| explanation-02 | 0.11 | 0.093 | tie |
| explanation-03 | 0.08 | 0.12 | win |
| explanation-04 | 0.111 | 0.101 | tie |
| explanation-05 | 0.096 | 0.105 | tie |
| explanation-06 | 0.078 | 0.074 | tie |
| explanation-07 | 0.088 | 0.131 | win |
| explanation-08 | 0.151 | 0.129 | loss |
| summarization-01 | 0.038 | 0.184 | win |
| summarization-02 | 0.113 | 0.212 | win |
| summarization-03 | 0.171 | 0.148 | loss |
| summarization-04 | 0.045 | 0.098 | win |
| summarization-05 | 0.083 | 0.102 | tie |
| summarization-06 | 0.193 | 0.19 | tie |
| summarization-07 | 0.141 | 0.174 | win |
| summarization-08 | 0.127 | 0.208 | win |

### plain-language

| Pair | Styled | Unstyled | Result |
|---|---|---|---|
| code-review-01 | 0.054 | 0.096 | win |
| code-review-02 | 0.102 | 0.052 | loss |
| code-review-03 | 0.131 | 0.075 | loss |
| code-review-04 | 0.116 | 0.108 | tie |
| code-review-05 | 0.083 | 0.119 | win |
| code-review-06 | 0.0 | 0.084 | win |
| code-review-07 | 0.075 | 0.094 | tie |
| code-review-08 | 0.134 | 0.159 | win |
| debugging-01 | 0.067 | 0.143 | win |
| debugging-02 | 0.051 | 0.081 | win |
| debugging-03 | 0.022 | 0.013 | tie |
| debugging-04 | 0.086 | 0.064 | loss |
| debugging-05 | 0.076 | 0.127 | win |
| debugging-06 | 0.079 | 0.538 | win |
| debugging-07 | 0.101 | 0.333 | win |
| debugging-08 | 0.13 | 0.089 | loss |
| explanation-01 | 0.105 | 0.123 | tie |
| explanation-02 | 0.12 | 0.093 | loss |
| explanation-03 | 0.107 | 0.12 | tie |
| explanation-04 | 0.147 | 0.101 | loss |
| explanation-05 | 0.126 | 0.105 | loss |
| explanation-06 | 0.091 | 0.074 | tie |
| explanation-07 | 0.116 | 0.131 | tie |
| explanation-08 | 0.079 | 0.129 | win |
| summarization-01 | 0.039 | 0.184 | win |
| summarization-02 | 0.097 | 0.212 | win |
| summarization-03 | 0.179 | 0.148 | loss |
| summarization-04 | 0.144 | 0.098 | loss |
| summarization-05 | 0.053 | 0.102 | win |
| summarization-06 | 0.16 | 0.19 | win |
| summarization-07 | 0.182 | 0.174 | tie |
| summarization-08 | 0.19 | 0.208 | tie |

### technical-simplified

| Pair | Styled | Unstyled | Result |
|---|---|---|---|
| code-review-01 | 0.063 | 0.096 | win |
| code-review-02 | 0.124 | 0.052 | loss |
| code-review-03 | 0.094 | 0.075 | tie |
| code-review-04 | 0.094 | 0.108 | tie |
| code-review-05 | 0.083 | 0.119 | win |
| code-review-06 | 0.125 | 0.084 | loss |
| code-review-07 | 0.0 | 0.094 | win |
| debugging-01 | 0.0 | 0.143 | win |
| debugging-02 | 0.086 | 0.081 | tie |
| debugging-03 | 0.053 | 0.013 | loss |
| debugging-04 | 0.036 | 0.064 | win |
| debugging-05 | 0.041 | 0.127 | win |
| debugging-07 | 0.081 | 0.333 | win |
| debugging-08 | 0.157 | 0.089 | loss |
| explanation-01 | 0.085 | 0.123 | win |
| explanation-02 | 0.092 | 0.093 | tie |
| explanation-03 | 0.105 | 0.12 | tie |
| explanation-04 | 0.112 | 0.101 | tie |
| explanation-05 | 0.162 | 0.105 | loss |
| explanation-06 | 0.116 | 0.074 | loss |
| explanation-07 | 0.35 | 0.131 | loss |
| summarization-01 | 0.118 | 0.184 | win |
| summarization-02 | 0.112 | 0.212 | win |
| summarization-03 | 0.103 | 0.148 | win |
| summarization-04 | 0.101 | 0.098 | tie |
| summarization-05 | 0.054 | 0.102 | win |

## Call timing

A stored call row holds two times: duration_ms is the model
time that the CLI reports, and wall_ms is the wall clock of
the subprocess. The difference is the startup cost of one CLI
call.

Calls: 3876, measured: 3876.
Mean duration: 9039 ms. Mean wall: 34320 ms. Mean startup: 25281 ms.

## Harness spend

A stored call row holds the token counts of its call: the
uncached input, cache-write input, cache-read input, and
output tokens. The cache-read share is the cache-read total
over the whole input total.

Calls: 3876, measured: 3876.
Input tokens: 27448 uncached, 3020823 cache write, 18608533 cache read. Output tokens: 3330471.
Cache-read share: 0.859.
Cache writes by lifetime: 3020823 at 5 minutes, 0 at 1 hour.

## Warnings

- technical-simplified/explanation-08: the pair failed the gate, excluded
- technical-simplified/code-review-08: the pair failed the gate, excluded
- technical-simplified/summarization-06: the pair failed the gate, excluded
- technical-simplified/summarization-07: the pair failed the gate, excluded
- technical-simplified/summarization-08: the pair failed the gate, excluded
- technical-simplified/debugging-06: the pair failed the gate, excluded
- actionable-clarity/debugging-06: the pair has 1 shared facts, fewer than the floor of 3, so comprehension skips the pair
- actionable-clarity/debugging-07: the pair has 0 shared facts, fewer than the floor of 3, so comprehension skips the pair
- clarity-flow/debugging-06: the pair has 0 shared facts, fewer than the floor of 3, so comprehension skips the pair
- clarity-flow/debugging-07: the pair has 0 shared facts, fewer than the floor of 3, so comprehension skips the pair
- classic-concise/debugging-06: the pair has 0 shared facts, fewer than the floor of 3, so comprehension skips the pair
- classic-concise/debugging-07: the pair has 0 shared facts, fewer than the floor of 3, so comprehension skips the pair
- concise/debugging-06: the pair has 0 shared facts, fewer than the floor of 3, so comprehension skips the pair
- concise/debugging-07: the pair has 0 shared facts, fewer than the floor of 3, so comprehension skips the pair
- developer-docs/debugging-06: the pair has 0 shared facts, fewer than the floor of 3, so comprehension skips the pair
- developer-docs/debugging-07: the pair has 0 shared facts, fewer than the floor of 3, so comprehension skips the pair
- plain-language/code-review-06: the pair has 0 shared facts, fewer than the floor of 3, so comprehension skips the pair
- plain-language/debugging-06: the pair has 0 shared facts, fewer than the floor of 3, so comprehension skips the pair
- plain-language/debugging-07: the pair has 0 shared facts, fewer than the floor of 3, so comprehension skips the pair
- technical-simplified/code-review-07: the pair has 0 shared facts, fewer than the floor of 3, so comprehension skips the pair
- technical-simplified/debugging-07: the pair has 0 shared facts, fewer than the floor of 3, so comprehension skips the pair
- technical-simplified/explanation-07: the pair has 1 shared facts, fewer than the floor of 3, so comprehension skips the pair
- actionable-clarity/debugging-06: the comprehension check has no usable questions for the pair, so the pair is unscored
- actionable-clarity/debugging-07: the comprehension check has no usable questions for the pair, so the pair is unscored
- clarity-flow/debugging-06: the comprehension check has no usable questions for the pair, so the pair is unscored
- clarity-flow/debugging-07: the comprehension check has no usable questions for the pair, so the pair is unscored
- classic-concise/debugging-06: the comprehension check has no usable questions for the pair, so the pair is unscored
- classic-concise/debugging-07: the comprehension check has no usable questions for the pair, so the pair is unscored
- concise/debugging-06: the comprehension check has no usable questions for the pair, so the pair is unscored
- concise/debugging-07: the comprehension check has no usable questions for the pair, so the pair is unscored
- developer-docs/debugging-06: the comprehension check has no usable questions for the pair, so the pair is unscored
- developer-docs/debugging-07: the comprehension check has no usable questions for the pair, so the pair is unscored
- plain-language/code-review-06: the comprehension check has no usable questions for the pair, so the pair is unscored
- plain-language/debugging-06: the comprehension check has no usable questions for the pair, so the pair is unscored
- plain-language/debugging-07: the comprehension check has no usable questions for the pair, so the pair is unscored
- technical-simplified/code-review-07: the comprehension check has no usable questions for the pair, so the pair is unscored
- technical-simplified/debugging-07: the comprehension check has no usable questions for the pair, so the pair is unscored
- technical-simplified/explanation-07: the comprehension check has no usable questions for the pair, so the pair is unscored
- actionable-clarity: the styled answer scores worse than the unstyled answer on comprehension (4 wins, 6 losses)
- clarity-flow: the styled answer scores worse than the unstyled answer on comprehension (3 wins, 5 losses)
- classic-concise: the styled answer scores worse than the unstyled answer on comprehension (3 wins, 8 losses)
- concise: the styled answer scores worse than the unstyled answer on comprehension (5 wins, 6 losses)
- technical-simplified: the styled answer scores worse than the unstyled answer on comprehension (3 wins, 6 losses)

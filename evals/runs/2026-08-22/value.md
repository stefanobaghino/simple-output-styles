# Reader-value report

The checks compare the styled answer with the unstyled answer of
the same prompt, pair by pair, as win, loss, or tie. Only pairs
whose styled answer passes the fidelity gate enter the checks.
Each judge call sees one bare text: no style name, no arm label,
and never both answers. Thus a judge cannot know which answer is
styled. The judge models differ from the writer of the answers.

Judges: reader haiku, grader opus. Comprehension asks up to 6 questions per pair, worded by both answers in balance, with 3 reader replicates per answer, ambiguity uses 3 restatements per answer, and the round-trip goes through Italian. Judged on 2026-08-22T09:32:02+00:00.

## Comprehension (weak reader)

The questions come from the shared facts of the pair, mined in both directions: the facts of the unstyled answer that survive in the styled answer, and the facts of the styled answer that the unstyled answer also states. The quiz takes half of its questions from each wording, so neither answer sets the phrasing alone, and the Sources column counts the questions per wording (unstyled/styled). A grader call turns each fact into one question, and the fact is the reference answer. The weak reader answers the questions from one answer text, once per replicate, and the grader marks every reply. Each styled replicate meets each unstyled replicate as a win, a loss, or a tie, and the pair outcome is the strict plurality, else a tie. The agreement is the plurality share, and the buried-fact rate counts "NOT IN TEXT" replies to a shared fact, per arm. The check measures extraction over shared material. Absence belongs to the content-loss report. Higher is better.

| Style | Wins | Losses | Ties | Mean delta | Agreement | Buried (styled) | Buried (unstyled) |
|---|---|---|---|---|---|---|---|
| actionable-clarity | 9 | 3 | 20 | 0.024 | 0.858 | 0.026 | 0.038 |
| clarity-flow | 5 | 9 | 18 | -0.017 | 0.868 | 0.036 | 0.03 |
| classic-concise | 6 | 9 | 17 | -0.021 | 0.851 | 0.033 | 0.024 |
| concise | 3 | 5 | 24 | -0.023 | 0.861 | 0.045 | 0.014 |
| developer-docs | 5 | 5 | 22 | -0.002 | 0.833 | 0.038 | 0.03 |
| plain-language | 7 | 9 | 15 | -0.009 | 0.871 | 0.054 | 0.05 |
| technical-simplified | 4 | 4 | 17 | 0.011 | 0.92 | 0.04 | 0.053 |

The styled answer must not score worse than the unstyled answer.
- actionable-clarity: the styled answer holds (9 wins, 3 losses, 20 ties).
- clarity-flow: the styled answer scores worse (5 wins, 9 losses, 18 ties).
- classic-concise: the styled answer scores worse (6 wins, 9 losses, 17 ties).
- concise: the styled answer scores worse (3 wins, 5 losses, 24 ties).
- developer-docs: the styled answer holds (5 wins, 5 losses, 22 ties).
- plain-language: the styled answer scores worse (7 wins, 9 losses, 15 ties).
- technical-simplified: the styled answer holds (4 wins, 4 losses, 17 ties).

### actionable-clarity

| Pair | Questions | Sources (u/s) | Styled | Unstyled | Agreement | Result |
|---|---|---|---|---|---|---|
| code-review-01 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| code-review-02 | 6 | 3/3 | 0.778 | 0.833 | 0.667 | tie |
| code-review-03 | 6 | 3/3 | 0.833 | 0.667 | 1.0 | win |
| code-review-04 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| code-review-05 | 6 | 3/3 | 1.0 | 0.944 | 0.667 | tie |
| code-review-06 | 6 | 3/3 | 1.0 | 0.667 | 1.0 | win |
| code-review-07 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| code-review-08 | 6 | 3/3 | 1.0 | 0.889 | 0.667 | win |
| debugging-01 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-02 | 6 | 3/3 | 1.0 | 0.944 | 0.667 | tie |
| debugging-03 | 6 | 3/3 | 0.944 | 1.0 | 0.667 | tie |
| debugging-04 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-05 | 6 | 3/3 | 0.944 | 1.0 | 0.667 | tie |
| debugging-06 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-07 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-08 | 6 | 3/3 | 0.833 | 0.889 | 0.667 | tie |
| explanation-01 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| explanation-02 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| explanation-03 | 6 | 3/3 | 0.833 | 0.833 | 1.0 | tie |
| explanation-04 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| explanation-05 | 6 | 3/3 | 0.889 | 1.0 | 0.667 | loss |
| explanation-06 | 6 | 3/3 | 0.944 | 1.0 | 0.667 | tie |
| explanation-07 | 6 | 3/3 | 0.889 | 0.889 | 0.444 | win |
| explanation-08 | 6 | 3/3 | 0.778 | 1.0 | 0.667 | loss |
| summarization-01 | 6 | 3/3 | 1.0 | 0.778 | 0.667 | win |
| summarization-02 | 6 | 3/3 | 1.0 | 0.833 | 1.0 | win |
| summarization-03 | 6 | 3/3 | 1.0 | 0.889 | 0.667 | win |
| summarization-04 | 6 | 3/3 | 1.0 | 0.833 | 1.0 | win |
| summarization-05 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-06 | 6 | 3/3 | 0.833 | 1.0 | 1.0 | loss |
| summarization-07 | 6 | 3/3 | 0.833 | 0.833 | 1.0 | tie |
| summarization-08 | 6 | 3/3 | 1.0 | 0.833 | 1.0 | win |

### clarity-flow

| Pair | Questions | Sources (u/s) | Styled | Unstyled | Agreement | Result |
|---|---|---|---|---|---|---|
| code-review-01 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| code-review-02 | 6 | 3/3 | 0.833 | 1.0 | 1.0 | loss |
| code-review-03 | 6 | 3/3 | 0.833 | 0.944 | 0.667 | loss |
| code-review-04 | 6 | 3/3 | 0.889 | 1.0 | 0.667 | loss |
| code-review-05 | 6 | 3/3 | 0.944 | 0.722 | 0.889 | win |
| code-review-06 | 6 | 3/3 | 0.833 | 0.889 | 0.667 | tie |
| code-review-07 | 6 | 3/3 | 0.833 | 0.833 | 1.0 | tie |
| code-review-08 | 6 | 3/3 | 0.833 | 0.944 | 0.667 | loss |
| debugging-01 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-02 | 6 | 3/3 | 0.778 | 1.0 | 1.0 | loss |
| debugging-03 | 6 | 3/3 | 1.0 | 0.944 | 0.667 | tie |
| debugging-04 | 6 | 3/3 | 0.833 | 0.833 | 1.0 | tie |
| debugging-05 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-06 | 6 | 3/3 | 0.667 | 0.833 | 1.0 | loss |
| debugging-07 | 6 | 3/3 | 1.0 | 0.833 | 1.0 | win |
| debugging-08 | 6 | 3/3 | 0.889 | 0.889 | 0.556 | tie |
| explanation-01 | 6 | 3/3 | 0.944 | 1.0 | 0.667 | tie |
| explanation-02 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| explanation-03 | 6 | 3/3 | 0.833 | 1.0 | 1.0 | loss |
| explanation-04 | 6 | 3/3 | 0.833 | 1.0 | 0.667 | loss |
| explanation-05 | 6 | 3/3 | 1.0 | 0.833 | 1.0 | win |
| explanation-06 | 6 | 3/3 | 1.0 | 0.944 | 0.667 | tie |
| explanation-07 | 6 | 3/3 | 1.0 | 0.944 | 0.667 | tie |
| explanation-08 | 6 | 3/3 | 0.944 | 1.0 | 0.667 | tie |
| summarization-01 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-02 | 6 | 3/3 | 1.0 | 0.889 | 0.667 | win |
| summarization-03 | 6 | 3/3 | 0.833 | 0.833 | 1.0 | tie |
| summarization-04 | 6 | 3/3 | 0.833 | 1.0 | 1.0 | loss |
| summarization-05 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-06 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-07 | 6 | 3/3 | 0.833 | 0.833 | 1.0 | tie |
| summarization-08 | 6 | 3/3 | 1.0 | 0.833 | 1.0 | win |

### classic-concise

| Pair | Questions | Sources (u/s) | Styled | Unstyled | Agreement | Result |
|---|---|---|---|---|---|---|
| code-review-01 | 6 | 3/3 | 1.0 | 0.833 | 1.0 | win |
| code-review-02 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| code-review-03 | 6 | 3/3 | 1.0 | 0.889 | 0.667 | win |
| code-review-04 | 6 | 3/3 | 0.833 | 0.944 | 0.667 | loss |
| code-review-05 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| code-review-06 | 6 | 3/3 | 1.0 | 0.944 | 0.667 | tie |
| code-review-07 | 6 | 3/3 | 0.944 | 1.0 | 0.667 | tie |
| code-review-08 | 6 | 3/3 | 1.0 | 0.833 | 1.0 | win |
| debugging-01 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-02 | 6 | 3/3 | 0.833 | 0.833 | 1.0 | tie |
| debugging-03 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-04 | 6 | 3/3 | 0.889 | 1.0 | 0.667 | tie |
| debugging-05 | 6 | 3/3 | 0.833 | 1.0 | 1.0 | loss |
| debugging-06 | 6 | 3/3 | 0.778 | 1.0 | 1.0 | loss |
| debugging-07 | 6 | 3/3 | 0.778 | 0.667 | 0.667 | win |
| debugging-08 | 6 | 3/3 | 0.833 | 0.944 | 0.667 | loss |
| explanation-01 | 6 | 3/3 | 0.944 | 1.0 | 0.667 | tie |
| explanation-02 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| explanation-03 | 6 | 3/3 | 0.833 | 1.0 | 1.0 | loss |
| explanation-04 | 6 | 3/3 | 0.889 | 1.0 | 0.667 | loss |
| explanation-05 | 6 | 3/3 | 0.556 | 0.778 | 0.889 | loss |
| explanation-06 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| explanation-07 | 6 | 3/3 | 0.778 | 0.944 | 0.778 | loss |
| explanation-08 | 6 | 3/3 | 1.0 | 0.944 | 0.667 | tie |
| summarization-01 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-02 | 6 | 3/3 | 0.944 | 0.944 | 0.556 | tie |
| summarization-03 | 6 | 3/3 | 1.0 | 0.889 | 0.667 | win |
| summarization-04 | 6 | 3/3 | 1.0 | 0.833 | 1.0 | win |
| summarization-05 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-06 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-07 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-08 | 6 | 3/3 | 0.889 | 1.0 | 0.667 | loss |

### concise

| Pair | Questions | Sources (u/s) | Styled | Unstyled | Agreement | Result |
|---|---|---|---|---|---|---|
| code-review-01 | 6 | 3/3 | 0.944 | 1.0 | 0.667 | tie |
| code-review-02 | 6 | 3/3 | 0.889 | 0.889 | 0.556 | tie |
| code-review-03 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| code-review-04 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| code-review-05 | 6 | 3/3 | 0.944 | 1.0 | 0.667 | tie |
| code-review-06 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| code-review-07 | 6 | 3/3 | 1.0 | 0.833 | 1.0 | win |
| code-review-08 | 6 | 3/3 | 1.0 | 0.833 | 0.667 | win |
| debugging-01 | 6 | 3/3 | 0.833 | 1.0 | 1.0 | loss |
| debugging-02 | 6 | 3/3 | 0.833 | 1.0 | 1.0 | loss |
| debugging-03 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-04 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-05 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-06 | 6 | 3/3 | 0.833 | 0.778 | 0.667 | tie |
| debugging-07 | 6 | 3/3 | 0.833 | 0.833 | 0.333 | tie |
| debugging-08 | 6 | 3/3 | 1.0 | 0.944 | 0.667 | tie |
| explanation-01 | 6 | 3/3 | 0.667 | 1.0 | 1.0 | loss |
| explanation-02 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| explanation-03 | 6 | 3/3 | 0.778 | 1.0 | 0.667 | loss |
| explanation-04 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| explanation-05 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| explanation-06 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| explanation-07 | 6 | 3/3 | 1.0 | 0.889 | 0.667 | win |
| explanation-08 | 6 | 3/3 | 0.944 | 1.0 | 0.667 | tie |
| summarization-01 | 6 | 3/3 | 0.833 | 0.833 | 1.0 | tie |
| summarization-02 | 6 | 3/3 | 1.0 | 0.944 | 0.667 | tie |
| summarization-03 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-04 | 6 | 3/3 | 0.889 | 1.0 | 0.667 | tie |
| summarization-05 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-06 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-07 | 6 | 3/3 | 0.833 | 0.833 | 1.0 | tie |
| summarization-08 | 6 | 3/3 | 0.833 | 1.0 | 1.0 | loss |

### developer-docs

| Pair | Questions | Sources (u/s) | Styled | Unstyled | Agreement | Result |
|---|---|---|---|---|---|---|
| code-review-01 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| code-review-02 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| code-review-03 | 6 | 3/3 | 0.944 | 0.833 | 0.667 | win |
| code-review-04 | 6 | 3/3 | 0.889 | 0.944 | 0.444 | tie |
| code-review-05 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| code-review-06 | 6 | 3/3 | 1.0 | 0.889 | 0.667 | win |
| code-review-07 | 6 | 3/3 | 1.0 | 0.944 | 0.667 | tie |
| code-review-08 | 6 | 3/3 | 0.944 | 0.833 | 0.667 | win |
| debugging-01 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-02 | 6 | 3/3 | 0.889 | 1.0 | 0.667 | loss |
| debugging-03 | 6 | 3/3 | 0.944 | 0.889 | 0.444 | tie |
| debugging-04 | 6 | 3/3 | 0.889 | 0.667 | 1.0 | win |
| debugging-05 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-06 | 6 | 3/3 | 0.778 | 0.833 | 0.667 | tie |
| debugging-07 | 6 | 3/3 | 1.0 | 0.833 | 1.0 | win |
| debugging-08 | 6 | 3/3 | 0.889 | 1.0 | 0.667 | tie |
| explanation-01 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| explanation-02 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| explanation-03 | 6 | 3/3 | 0.667 | 1.0 | 1.0 | loss |
| explanation-04 | 6 | 3/3 | 0.889 | 1.0 | 0.667 | loss |
| explanation-05 | 6 | 3/3 | 0.889 | 1.0 | 0.667 | loss |
| explanation-06 | 6 | 3/3 | 1.0 | 0.944 | 0.667 | tie |
| explanation-07 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| explanation-08 | 6 | 3/3 | 0.833 | 0.944 | 0.667 | loss |
| summarization-01 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-02 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-03 | 6 | 3/3 | 0.944 | 0.889 | 0.444 | tie |
| summarization-04 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-05 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-06 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-07 | 6 | 3/3 | 0.833 | 0.833 | 1.0 | tie |
| summarization-08 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |

### plain-language

| Pair | Questions | Sources (u/s) | Styled | Unstyled | Agreement | Result |
|---|---|---|---|---|---|---|
| code-review-01 | 6 | 3/3 | 1.0 | 0.833 | 1.0 | win |
| code-review-02 | 6 | 3/3 | 0.944 | 0.944 | 0.556 | tie |
| code-review-03 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| code-review-04 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| code-review-05 | 6 | 3/3 | 0.833 | 1.0 | 1.0 | loss |
| code-review-06 | 6 | 3/3 | 1.0 | 0.833 | 1.0 | win |
| code-review-07 | 6 | 3/3 | 0.833 | 1.0 | 1.0 | loss |
| code-review-08 | 6 | 3/3 | 1.0 | 0.944 | 0.667 | tie |
| debugging-01 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-02 | 6 | 3/3 | 0.833 | 1.0 | 1.0 | loss |
| debugging-03 | 6 | 3/3 | 1.0 | 0.944 | 0.667 | tie |
| debugging-04 | 6 | 3/3 | 0.778 | 0.944 | 0.778 | loss |
| debugging-05 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-06 | 6 | 3/3 | 0.833 | 0.667 | 1.0 | win |
| debugging-07 | 6 | 3/3 | 0.667 | 1.0 | 1.0 | loss |
| debugging-08 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| explanation-01 | 6 | 3/3 | 0.833 | 0.889 | 0.444 | loss |
| explanation-02 | 6 | 3/3 | 1.0 | 0.833 | 1.0 | win |
| explanation-03 | 6 | 3/3 | 0.833 | 1.0 | 1.0 | loss |
| explanation-04 | 6 | 3/3 | 1.0 | 0.944 | 0.667 | tie |
| explanation-05 | 6 | 3/3 | 0.944 | 1.0 | 0.667 | tie |
| explanation-06 | 6 | 3/3 | 0.778 | 0.556 | 0.889 | win |
| explanation-07 | 6 | 3/3 | 1.0 | 0.778 | 1.0 | win |
| explanation-08 | 6 | 3/3 | 0.778 | 0.778 | 0.556 | tie |
| summarization-01 | 6 | 3/3 | 0.944 | 0.889 | 0.444 | tie |
| summarization-02 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-03 | 6 | 3/3 | 1.0 | 0.889 | 0.667 | win |
| summarization-04 | 6 | 3/3 | 0.5 | 0.778 | 1.0 | loss |
| summarization-05 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-07 | 6 | 3/3 | 0.833 | 0.833 | 1.0 | tie |
| summarization-08 | 6 | 3/3 | 0.833 | 1.0 | 1.0 | loss |

### technical-simplified

| Pair | Questions | Sources (u/s) | Styled | Unstyled | Agreement | Result |
|---|---|---|---|---|---|---|
| code-review-01 | 6 | 3/3 | 1.0 | 0.944 | 0.667 | tie |
| code-review-02 | 6 | 3/3 | 0.889 | 0.667 | 1.0 | win |
| code-review-04 | 6 | 3/3 | 0.833 | 1.0 | 1.0 | loss |
| code-review-05 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| code-review-06 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| code-review-08 | 6 | 3/3 | 1.0 | 0.944 | 0.667 | tie |
| debugging-01 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-02 | 6 | 3/3 | 0.833 | 0.833 | 1.0 | tie |
| debugging-03 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-04 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-05 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-06 | 6 | 3/3 | 0.889 | 0.5 | 1.0 | win |
| debugging-08 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| explanation-01 | 6 | 3/3 | 0.833 | 1.0 | 1.0 | loss |
| explanation-02 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| explanation-03 | 6 | 3/3 | 0.833 | 0.833 | 1.0 | tie |
| explanation-04 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| explanation-05 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| explanation-06 | 6 | 3/3 | 0.833 | 1.0 | 1.0 | loss |
| explanation-07 | 6 | 3/3 | 0.889 | 0.833 | 0.667 | tie |
| summarization-01 | 6 | 3/3 | 1.0 | 0.778 | 1.0 | win |
| summarization-02 | 6 | 3/3 | 0.833 | 0.833 | 0.333 | tie |
| summarization-03 | 6 | 3/3 | 0.944 | 0.833 | 0.667 | win |
| summarization-04 | 6 | 3/3 | 0.667 | 1.0 | 1.0 | loss |
| summarization-05 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |

## Ambiguity (paraphrase agreement)

Independent reader calls restate one answer text in their own words. The score is the mean pairwise lexical similarity between the restatements: when the readers agree on what the text says, the text is less ambiguous. Higher is better.

| Style | Wins | Losses | Ties |
|---|---|---|---|
| actionable-clarity | 11 | 9 | 12 |
| clarity-flow | 8 | 14 | 10 |
| classic-concise | 6 | 17 | 9 |
| concise | 7 | 15 | 10 |
| developer-docs | 13 | 9 | 10 |
| plain-language | 14 | 10 | 8 |
| technical-simplified | 13 | 7 | 6 |

The length confound is the correlation between the length ratio of a pair (styled words over unstyled words) and the styled advantage (the score gain of the styled arm). A negative value means that the shorter styled answers score better.
- actionable-clarity: Pearson 0.084, Spearman 0.024, over 32 pairs.
- clarity-flow: Pearson 0.081, Spearman 0.095, over 32 pairs.
- classic-concise: Pearson -0.021, Spearman -0.026, over 32 pairs.
- concise: Pearson 0.023, Spearman 0.062, over 32 pairs.
- developer-docs: Pearson 0.452, Spearman 0.35, over 32 pairs.
- plain-language: Pearson 0.381, Spearman 0.294, over 32 pairs.
- technical-simplified: Pearson 0.102, Spearman -0.003, over 26 pairs.

### actionable-clarity

| Pair | Styled | Unstyled | Result |
|---|---|---|---|
| code-review-01 | 0.709 | 0.7 | tie |
| code-review-02 | 0.699 | 0.775 | loss |
| code-review-03 | 0.677 | 0.664 | tie |
| code-review-04 | 0.751 | 0.608 | win |
| code-review-05 | 0.682 | 0.703 | loss |
| code-review-06 | 0.693 | 0.654 | win |
| code-review-07 | 0.66 | 0.687 | loss |
| code-review-08 | 0.721 | 0.637 | win |
| debugging-01 | 0.591 | 0.653 | loss |
| debugging-02 | 0.705 | 0.796 | loss |
| debugging-03 | 0.825 | 0.742 | win |
| debugging-04 | 0.77 | 0.78 | tie |
| debugging-05 | 0.751 | 0.725 | win |
| debugging-06 | 0.697 | 0.666 | win |
| debugging-07 | 0.696 | 0.675 | win |
| debugging-08 | 0.648 | 0.628 | tie |
| explanation-01 | 0.666 | 0.705 | loss |
| explanation-02 | 0.706 | 0.71 | tie |
| explanation-03 | 0.668 | 0.672 | tie |
| explanation-04 | 0.703 | 0.705 | tie |
| explanation-05 | 0.717 | 0.573 | win |
| explanation-06 | 0.644 | 0.666 | loss |
| explanation-07 | 0.59 | 0.574 | tie |
| explanation-08 | 0.638 | 0.571 | win |
| summarization-01 | 0.719 | 0.728 | tie |
| summarization-02 | 0.634 | 0.686 | loss |
| summarization-03 | 0.646 | 0.598 | win |
| summarization-04 | 0.711 | 0.707 | tie |
| summarization-05 | 0.679 | 0.716 | loss |
| summarization-06 | 0.675 | 0.66 | tie |
| summarization-07 | 0.674 | 0.645 | win |
| summarization-08 | 0.623 | 0.611 | tie |

### clarity-flow

| Pair | Styled | Unstyled | Result |
|---|---|---|---|
| code-review-01 | 0.631 | 0.7 | loss |
| code-review-02 | 0.652 | 0.775 | loss |
| code-review-03 | 0.718 | 0.664 | win |
| code-review-04 | 0.588 | 0.608 | tie |
| code-review-05 | 0.709 | 0.703 | tie |
| code-review-06 | 0.637 | 0.654 | tie |
| code-review-07 | 0.667 | 0.687 | loss |
| code-review-08 | 0.639 | 0.637 | tie |
| debugging-01 | 0.691 | 0.653 | win |
| debugging-02 | 0.736 | 0.796 | loss |
| debugging-03 | 0.686 | 0.742 | loss |
| debugging-04 | 0.691 | 0.78 | loss |
| debugging-05 | 0.689 | 0.725 | loss |
| debugging-06 | 0.622 | 0.666 | loss |
| debugging-07 | 0.694 | 0.675 | tie |
| debugging-08 | 0.621 | 0.628 | tie |
| explanation-01 | 0.722 | 0.705 | tie |
| explanation-02 | 0.644 | 0.71 | loss |
| explanation-03 | 0.65 | 0.672 | loss |
| explanation-04 | 0.648 | 0.705 | loss |
| explanation-05 | 0.643 | 0.573 | win |
| explanation-06 | 0.602 | 0.666 | loss |
| explanation-07 | 0.613 | 0.574 | win |
| explanation-08 | 0.637 | 0.571 | win |
| summarization-01 | 0.667 | 0.728 | loss |
| summarization-02 | 0.679 | 0.686 | tie |
| summarization-03 | 0.563 | 0.598 | loss |
| summarization-04 | 0.776 | 0.707 | win |
| summarization-05 | 0.761 | 0.716 | win |
| summarization-06 | 0.645 | 0.66 | tie |
| summarization-07 | 0.703 | 0.645 | win |
| summarization-08 | 0.615 | 0.611 | tie |

### classic-concise

| Pair | Styled | Unstyled | Result |
|---|---|---|---|
| code-review-01 | 0.625 | 0.7 | loss |
| code-review-02 | 0.641 | 0.775 | loss |
| code-review-03 | 0.577 | 0.664 | loss |
| code-review-04 | 0.587 | 0.608 | loss |
| code-review-05 | 0.707 | 0.703 | tie |
| code-review-06 | 0.68 | 0.654 | win |
| code-review-07 | 0.66 | 0.687 | loss |
| code-review-08 | 0.665 | 0.637 | win |
| debugging-01 | 0.638 | 0.653 | tie |
| debugging-02 | 0.81 | 0.796 | tie |
| debugging-03 | 0.759 | 0.742 | tie |
| debugging-04 | 0.77 | 0.78 | tie |
| debugging-05 | 0.644 | 0.725 | loss |
| debugging-06 | 0.641 | 0.666 | loss |
| debugging-07 | 0.65 | 0.675 | loss |
| debugging-08 | 0.597 | 0.628 | loss |
| explanation-01 | 0.655 | 0.705 | loss |
| explanation-02 | 0.62 | 0.71 | loss |
| explanation-03 | 0.706 | 0.672 | win |
| explanation-04 | 0.67 | 0.705 | loss |
| explanation-05 | 0.671 | 0.573 | win |
| explanation-06 | 0.539 | 0.666 | loss |
| explanation-07 | 0.582 | 0.574 | tie |
| explanation-08 | 0.565 | 0.571 | tie |
| summarization-01 | 0.608 | 0.728 | loss |
| summarization-02 | 0.564 | 0.686 | loss |
| summarization-03 | 0.594 | 0.598 | tie |
| summarization-04 | 0.619 | 0.707 | loss |
| summarization-05 | 0.637 | 0.716 | loss |
| summarization-06 | 0.65 | 0.66 | tie |
| summarization-07 | 0.695 | 0.645 | win |
| summarization-08 | 0.634 | 0.611 | win |

### concise

| Pair | Styled | Unstyled | Result |
|---|---|---|---|
| code-review-01 | 0.634 | 0.7 | loss |
| code-review-02 | 0.743 | 0.775 | loss |
| code-review-03 | 0.646 | 0.664 | tie |
| code-review-04 | 0.643 | 0.608 | win |
| code-review-05 | 0.64 | 0.703 | loss |
| code-review-06 | 0.615 | 0.654 | loss |
| code-review-07 | 0.65 | 0.687 | loss |
| code-review-08 | 0.664 | 0.637 | win |
| debugging-01 | 0.635 | 0.653 | tie |
| debugging-02 | 0.747 | 0.796 | loss |
| debugging-03 | 0.727 | 0.742 | tie |
| debugging-04 | 0.705 | 0.78 | loss |
| debugging-05 | 0.604 | 0.725 | loss |
| debugging-06 | 0.67 | 0.666 | tie |
| debugging-07 | 0.704 | 0.675 | win |
| debugging-08 | 0.621 | 0.628 | tie |
| explanation-01 | 0.711 | 0.705 | tie |
| explanation-02 | 0.629 | 0.71 | loss |
| explanation-03 | 0.636 | 0.672 | loss |
| explanation-04 | 0.631 | 0.705 | loss |
| explanation-05 | 0.61 | 0.573 | win |
| explanation-06 | 0.566 | 0.666 | loss |
| explanation-07 | 0.588 | 0.574 | tie |
| explanation-08 | 0.571 | 0.571 | tie |
| summarization-01 | 0.61 | 0.728 | loss |
| summarization-02 | 0.61 | 0.686 | loss |
| summarization-03 | 0.629 | 0.598 | win |
| summarization-04 | 0.768 | 0.707 | win |
| summarization-05 | 0.743 | 0.716 | win |
| summarization-06 | 0.659 | 0.66 | tie |
| summarization-07 | 0.636 | 0.645 | tie |
| summarization-08 | 0.59 | 0.611 | loss |

### developer-docs

| Pair | Styled | Unstyled | Result |
|---|---|---|---|
| code-review-01 | 0.612 | 0.7 | loss |
| code-review-02 | 0.653 | 0.775 | loss |
| code-review-03 | 0.729 | 0.664 | win |
| code-review-04 | 0.66 | 0.608 | win |
| code-review-05 | 0.696 | 0.703 | tie |
| code-review-06 | 0.692 | 0.654 | win |
| code-review-07 | 0.665 | 0.687 | loss |
| code-review-08 | 0.687 | 0.637 | win |
| debugging-01 | 0.692 | 0.653 | win |
| debugging-02 | 0.722 | 0.796 | loss |
| debugging-03 | 0.851 | 0.742 | win |
| debugging-04 | 0.781 | 0.78 | tie |
| debugging-05 | 0.72 | 0.725 | tie |
| debugging-06 | 0.655 | 0.666 | tie |
| debugging-07 | 0.679 | 0.675 | tie |
| debugging-08 | 0.62 | 0.628 | tie |
| explanation-01 | 0.705 | 0.705 | tie |
| explanation-02 | 0.69 | 0.71 | tie |
| explanation-03 | 0.72 | 0.672 | win |
| explanation-04 | 0.67 | 0.705 | loss |
| explanation-05 | 0.662 | 0.573 | win |
| explanation-06 | 0.659 | 0.666 | tie |
| explanation-07 | 0.503 | 0.574 | loss |
| explanation-08 | 0.663 | 0.571 | win |
| summarization-01 | 0.768 | 0.728 | win |
| summarization-02 | 0.655 | 0.686 | loss |
| summarization-03 | 0.662 | 0.598 | win |
| summarization-04 | 0.566 | 0.707 | loss |
| summarization-05 | 0.752 | 0.716 | win |
| summarization-06 | 0.644 | 0.66 | tie |
| summarization-07 | 0.735 | 0.645 | win |
| summarization-08 | 0.58 | 0.611 | loss |

### plain-language

| Pair | Styled | Unstyled | Result |
|---|---|---|---|
| code-review-01 | 0.741 | 0.7 | win |
| code-review-02 | 0.656 | 0.775 | loss |
| code-review-03 | 0.759 | 0.664 | win |
| code-review-04 | 0.552 | 0.608 | loss |
| code-review-05 | 0.704 | 0.703 | tie |
| code-review-06 | 0.617 | 0.654 | loss |
| code-review-07 | 0.629 | 0.687 | loss |
| code-review-08 | 0.685 | 0.637 | win |
| debugging-01 | 0.742 | 0.653 | win |
| debugging-02 | 0.883 | 0.796 | win |
| debugging-03 | 0.826 | 0.742 | win |
| debugging-04 | 0.746 | 0.78 | loss |
| debugging-05 | 0.779 | 0.725 | win |
| debugging-06 | 0.657 | 0.666 | tie |
| debugging-07 | 0.674 | 0.675 | tie |
| debugging-08 | 0.667 | 0.628 | win |
| explanation-01 | 0.692 | 0.705 | tie |
| explanation-02 | 0.701 | 0.71 | tie |
| explanation-03 | 0.71 | 0.672 | win |
| explanation-04 | 0.675 | 0.705 | loss |
| explanation-05 | 0.651 | 0.573 | win |
| explanation-06 | 0.662 | 0.666 | tie |
| explanation-07 | 0.624 | 0.574 | win |
| explanation-08 | 0.663 | 0.571 | win |
| summarization-01 | 0.726 | 0.728 | tie |
| summarization-02 | 0.666 | 0.686 | loss |
| summarization-03 | 0.661 | 0.598 | win |
| summarization-04 | 0.676 | 0.707 | loss |
| summarization-05 | 0.632 | 0.716 | loss |
| summarization-06 | 0.397 | 0.66 | loss |
| summarization-07 | 0.675 | 0.645 | win |
| summarization-08 | 0.606 | 0.611 | tie |

### technical-simplified

| Pair | Styled | Unstyled | Result |
|---|---|---|---|
| code-review-01 | 0.683 | 0.7 | tie |
| code-review-02 | 0.621 | 0.775 | loss |
| code-review-03 | 0.657 | 0.664 | tie |
| code-review-04 | 0.699 | 0.608 | win |
| code-review-05 | 0.671 | 0.703 | loss |
| code-review-06 | 0.697 | 0.654 | win |
| code-review-08 | 0.696 | 0.637 | win |
| debugging-01 | 0.665 | 0.653 | tie |
| debugging-02 | 0.876 | 0.796 | win |
| debugging-03 | 0.809 | 0.742 | win |
| debugging-04 | 0.824 | 0.78 | win |
| debugging-05 | 0.76 | 0.725 | win |
| debugging-06 | 0.697 | 0.666 | win |
| debugging-08 | 0.666 | 0.628 | win |
| explanation-01 | 0.692 | 0.705 | tie |
| explanation-02 | 0.638 | 0.71 | loss |
| explanation-03 | 0.773 | 0.672 | win |
| explanation-04 | 0.712 | 0.705 | tie |
| explanation-05 | 0.773 | 0.573 | win |
| explanation-06 | 0.621 | 0.666 | loss |
| explanation-07 | 0.641 | 0.574 | win |
| summarization-01 | 0.703 | 0.728 | loss |
| summarization-02 | 0.59 | 0.686 | loss |
| summarization-03 | 0.665 | 0.598 | win |
| summarization-04 | 0.616 | 0.707 | loss |
| summarization-05 | 0.698 | 0.716 | tie |

## Translation round-trip

One call translates the answer to another language, and a second call translates the result back to English. The score is the lexical loss between the original and the round-trip: simpler text survives the round-trip with less loss. Lower is better.

| Style | Wins | Losses | Ties |
|---|---|---|---|
| actionable-clarity | 9 | 6 | 17 |
| clarity-flow | 10 | 8 | 14 |
| classic-concise | 6 | 16 | 10 |
| concise | 8 | 14 | 10 |
| developer-docs | 10 | 7 | 15 |
| plain-language | 12 | 9 | 11 |
| technical-simplified | 9 | 9 | 8 |

The length confound is the correlation between the length ratio of a pair (styled words over unstyled words) and the styled advantage (the score gain of the styled arm). A negative value means that the shorter styled answers score better.
- actionable-clarity: Pearson 0.07, Spearman 0.201, over 32 pairs.
- clarity-flow: Pearson 0.433, Spearman 0.441, over 32 pairs.
- classic-concise: Pearson -0.028, Spearman -0.02, over 32 pairs.
- concise: Pearson 0.028, Spearman 0.108, over 32 pairs.
- developer-docs: Pearson 0.371, Spearman 0.441, over 32 pairs.
- plain-language: Pearson 0.372, Spearman 0.452, over 32 pairs.
- technical-simplified: Pearson 0.516, Spearman 0.389, over 26 pairs.

### actionable-clarity

| Pair | Styled | Unstyled | Result |
|---|---|---|---|
| code-review-01 | 0.091 | 0.07 | loss |
| code-review-02 | 0.106 | 0.041 | loss |
| code-review-03 | 0.076 | 0.079 | tie |
| code-review-04 | 0.047 | 0.11 | win |
| code-review-05 | 0.077 | 0.092 | tie |
| code-review-06 | 0.083 | 0.069 | tie |
| code-review-07 | 0.087 | 0.083 | tie |
| code-review-08 | 0.134 | 0.115 | tie |
| debugging-01 | 0.047 | 0.169 | win |
| debugging-02 | 0.091 | 0.057 | loss |
| debugging-03 | 0.018 | 0.084 | win |
| debugging-04 | 0.076 | 0.062 | tie |
| debugging-05 | 0.082 | 0.102 | tie |
| debugging-06 | 0.071 | 0.112 | win |
| debugging-07 | 0.061 | 0.068 | tie |
| debugging-08 | 0.084 | 0.087 | tie |
| explanation-01 | 0.111 | 0.101 | tie |
| explanation-02 | 0.086 | 0.097 | tie |
| explanation-03 | 0.106 | 0.135 | win |
| explanation-04 | 0.075 | 0.094 | tie |
| explanation-05 | 0.079 | 0.13 | win |
| explanation-06 | 0.065 | 0.065 | tie |
| explanation-07 | 0.11 | 0.116 | tie |
| explanation-08 | 0.139 | 0.128 | tie |
| summarization-01 | 0.1 | 0.032 | loss |
| summarization-02 | 0.164 | 0.175 | tie |
| summarization-03 | 0.169 | 0.11 | loss |
| summarization-04 | 0.109 | 0.07 | loss |
| summarization-05 | 0.073 | 0.159 | win |
| summarization-06 | 0.097 | 0.2 | win |
| summarization-07 | 0.115 | 0.246 | win |
| summarization-08 | 0.165 | 0.162 | tie |

### clarity-flow

| Pair | Styled | Unstyled | Result |
|---|---|---|---|
| code-review-01 | 0.05 | 0.07 | tie |
| code-review-02 | 0.101 | 0.041 | loss |
| code-review-03 | 0.08 | 0.079 | tie |
| code-review-04 | 0.072 | 0.11 | win |
| code-review-05 | 0.082 | 0.092 | tie |
| code-review-06 | 0.063 | 0.069 | tie |
| code-review-07 | 0.106 | 0.083 | loss |
| code-review-08 | 0.185 | 0.115 | loss |
| debugging-01 | 0.101 | 0.169 | win |
| debugging-02 | 0.0 | 0.057 | win |
| debugging-03 | 0.037 | 0.084 | win |
| debugging-04 | 0.051 | 0.062 | tie |
| debugging-05 | 0.118 | 0.102 | tie |
| debugging-06 | 0.117 | 0.112 | tie |
| debugging-07 | 0.123 | 0.068 | loss |
| debugging-08 | 0.116 | 0.087 | loss |
| explanation-01 | 0.112 | 0.101 | tie |
| explanation-02 | 0.167 | 0.097 | loss |
| explanation-03 | 0.144 | 0.135 | tie |
| explanation-04 | 0.094 | 0.094 | tie |
| explanation-05 | 0.099 | 0.13 | win |
| explanation-06 | 0.062 | 0.065 | tie |
| explanation-07 | 0.082 | 0.116 | win |
| explanation-08 | 0.127 | 0.128 | tie |
| summarization-01 | 0.029 | 0.032 | tie |
| summarization-02 | 0.2 | 0.175 | loss |
| summarization-03 | 0.113 | 0.11 | tie |
| summarization-04 | 0.048 | 0.07 | win |
| summarization-05 | 0.058 | 0.159 | win |
| summarization-06 | 0.118 | 0.2 | win |
| summarization-07 | 0.165 | 0.246 | win |
| summarization-08 | 0.223 | 0.162 | loss |

### classic-concise

| Pair | Styled | Unstyled | Result |
|---|---|---|---|
| code-review-01 | 0.071 | 0.07 | tie |
| code-review-02 | 0.088 | 0.041 | loss |
| code-review-03 | 0.125 | 0.079 | loss |
| code-review-04 | 0.073 | 0.11 | win |
| code-review-05 | 0.069 | 0.092 | win |
| code-review-06 | 0.113 | 0.069 | loss |
| code-review-07 | 0.125 | 0.083 | loss |
| code-review-08 | 0.168 | 0.115 | loss |
| debugging-01 | 0.237 | 0.169 | loss |
| debugging-02 | 0.019 | 0.057 | win |
| debugging-03 | 0.065 | 0.084 | tie |
| debugging-04 | 0.076 | 0.062 | tie |
| debugging-05 | 0.108 | 0.102 | tie |
| debugging-06 | 0.097 | 0.112 | tie |
| debugging-07 | 0.093 | 0.068 | loss |
| debugging-08 | 0.188 | 0.087 | loss |
| explanation-01 | 0.136 | 0.101 | loss |
| explanation-02 | 0.207 | 0.097 | loss |
| explanation-03 | 0.098 | 0.135 | win |
| explanation-04 | 0.084 | 0.094 | tie |
| explanation-05 | 0.113 | 0.13 | tie |
| explanation-06 | 0.087 | 0.065 | loss |
| explanation-07 | 0.138 | 0.116 | loss |
| explanation-08 | 0.11 | 0.128 | tie |
| summarization-01 | 0.121 | 0.032 | loss |
| summarization-02 | 0.138 | 0.175 | win |
| summarization-03 | 0.118 | 0.11 | tie |
| summarization-04 | 0.109 | 0.07 | loss |
| summarization-05 | 0.162 | 0.159 | tie |
| summarization-06 | 0.272 | 0.2 | loss |
| summarization-07 | 0.202 | 0.246 | win |
| summarization-08 | 0.258 | 0.162 | loss |

### concise

| Pair | Styled | Unstyled | Result |
|---|---|---|---|
| code-review-01 | 0.077 | 0.07 | tie |
| code-review-02 | 0.056 | 0.041 | tie |
| code-review-03 | 0.149 | 0.079 | loss |
| code-review-04 | 0.126 | 0.11 | tie |
| code-review-05 | 0.114 | 0.092 | loss |
| code-review-06 | 0.123 | 0.069 | loss |
| code-review-07 | 0.057 | 0.083 | win |
| code-review-08 | 0.158 | 0.115 | loss |
| debugging-01 | 0.148 | 0.169 | win |
| debugging-02 | 0.021 | 0.057 | win |
| debugging-03 | 0.032 | 0.084 | win |
| debugging-04 | 0.078 | 0.062 | tie |
| debugging-05 | 0.108 | 0.102 | tie |
| debugging-06 | 0.115 | 0.112 | tie |
| debugging-07 | 0.068 | 0.068 | tie |
| debugging-08 | 0.143 | 0.087 | loss |
| explanation-01 | 0.154 | 0.101 | loss |
| explanation-02 | 0.107 | 0.097 | tie |
| explanation-03 | 0.138 | 0.135 | tie |
| explanation-04 | 0.12 | 0.094 | loss |
| explanation-05 | 0.147 | 0.13 | tie |
| explanation-06 | 0.125 | 0.065 | loss |
| explanation-07 | 0.095 | 0.116 | win |
| explanation-08 | 0.179 | 0.128 | loss |
| summarization-01 | 0.085 | 0.032 | loss |
| summarization-02 | 0.289 | 0.175 | loss |
| summarization-03 | 0.075 | 0.11 | win |
| summarization-04 | 0.091 | 0.07 | loss |
| summarization-05 | 0.295 | 0.159 | loss |
| summarization-06 | 0.141 | 0.2 | win |
| summarization-07 | 0.216 | 0.246 | win |
| summarization-08 | 0.23 | 0.162 | loss |

### developer-docs

| Pair | Styled | Unstyled | Result |
|---|---|---|---|
| code-review-01 | 0.074 | 0.07 | tie |
| code-review-02 | 0.09 | 0.041 | loss |
| code-review-03 | 0.095 | 0.079 | tie |
| code-review-04 | 0.096 | 0.11 | tie |
| code-review-05 | 0.132 | 0.092 | loss |
| code-review-06 | 0.117 | 0.069 | loss |
| code-review-07 | 0.091 | 0.083 | tie |
| code-review-08 | 0.096 | 0.115 | tie |
| debugging-01 | 0.043 | 0.169 | win |
| debugging-02 | 0.074 | 0.057 | tie |
| debugging-03 | 0.052 | 0.084 | win |
| debugging-04 | 0.052 | 0.062 | tie |
| debugging-05 | 0.08 | 0.102 | win |
| debugging-06 | 0.102 | 0.112 | tie |
| debugging-07 | 0.138 | 0.068 | loss |
| debugging-08 | 0.147 | 0.087 | loss |
| explanation-01 | 0.103 | 0.101 | tie |
| explanation-02 | 0.09 | 0.097 | tie |
| explanation-03 | 0.092 | 0.135 | win |
| explanation-04 | 0.139 | 0.094 | loss |
| explanation-05 | 0.081 | 0.13 | win |
| explanation-06 | 0.063 | 0.065 | tie |
| explanation-07 | 0.098 | 0.116 | tie |
| explanation-08 | 0.095 | 0.128 | win |
| summarization-01 | 0.175 | 0.032 | loss |
| summarization-02 | 0.121 | 0.175 | win |
| summarization-03 | 0.1 | 0.11 | tie |
| summarization-04 | 0.085 | 0.07 | tie |
| summarization-05 | 0.067 | 0.159 | win |
| summarization-06 | 0.167 | 0.2 | win |
| summarization-07 | 0.196 | 0.246 | win |
| summarization-08 | 0.153 | 0.162 | tie |

### plain-language

| Pair | Styled | Unstyled | Result |
|---|---|---|---|
| code-review-01 | 0.035 | 0.07 | win |
| code-review-02 | 0.074 | 0.041 | loss |
| code-review-03 | 0.06 | 0.079 | tie |
| code-review-04 | 0.061 | 0.11 | win |
| code-review-05 | 0.083 | 0.092 | tie |
| code-review-06 | 0.092 | 0.069 | loss |
| code-review-07 | 0.155 | 0.083 | loss |
| code-review-08 | 0.101 | 0.115 | tie |
| debugging-01 | 0.02 | 0.169 | win |
| debugging-02 | 0.036 | 0.057 | win |
| debugging-03 | 0.045 | 0.084 | win |
| debugging-04 | 0.059 | 0.062 | tie |
| debugging-05 | 0.048 | 0.102 | win |
| debugging-06 | 0.099 | 0.112 | tie |
| debugging-07 | 0.092 | 0.068 | loss |
| debugging-08 | 0.119 | 0.087 | loss |
| explanation-01 | 0.105 | 0.101 | tie |
| explanation-02 | 0.074 | 0.097 | win |
| explanation-03 | 0.084 | 0.135 | win |
| explanation-04 | 0.099 | 0.094 | tie |
| explanation-05 | 0.124 | 0.13 | tie |
| explanation-06 | 0.085 | 0.065 | loss |
| explanation-07 | 0.092 | 0.116 | win |
| explanation-08 | 0.136 | 0.128 | tie |
| summarization-01 | 0.088 | 0.032 | loss |
| summarization-02 | 0.085 | 0.175 | win |
| summarization-03 | 0.126 | 0.11 | tie |
| summarization-04 | 0.067 | 0.07 | tie |
| summarization-05 | 0.132 | 0.159 | win |
| summarization-06 | 0.926 | 0.2 | loss |
| summarization-07 | 0.134 | 0.246 | win |
| summarization-08 | 0.235 | 0.162 | loss |

### technical-simplified

| Pair | Styled | Unstyled | Result |
|---|---|---|---|
| code-review-01 | 0.063 | 0.07 | tie |
| code-review-02 | 0.151 | 0.041 | loss |
| code-review-03 | 0.6 | 0.079 | loss |
| code-review-04 | 0.104 | 0.11 | tie |
| code-review-05 | 0.057 | 0.092 | win |
| code-review-06 | 0.11 | 0.069 | loss |
| code-review-08 | 0.141 | 0.115 | loss |
| debugging-01 | 0.043 | 0.169 | win |
| debugging-02 | 0.069 | 0.057 | tie |
| debugging-03 | 0.053 | 0.084 | win |
| debugging-04 | 0.074 | 0.062 | tie |
| debugging-05 | 0.102 | 0.102 | tie |
| debugging-06 | 0.097 | 0.112 | tie |
| debugging-08 | 0.139 | 0.087 | loss |
| explanation-01 | 0.108 | 0.101 | tie |
| explanation-02 | 0.105 | 0.097 | tie |
| explanation-03 | 0.081 | 0.135 | win |
| explanation-04 | 0.115 | 0.094 | loss |
| explanation-05 | 0.099 | 0.13 | win |
| explanation-06 | 0.119 | 0.065 | loss |
| explanation-07 | 0.089 | 0.116 | win |
| summarization-01 | 0.105 | 0.032 | loss |
| summarization-02 | 0.117 | 0.175 | win |
| summarization-03 | 0.086 | 0.11 | win |
| summarization-04 | 0.134 | 0.07 | loss |
| summarization-05 | 0.097 | 0.159 | win |

## Call timing

A stored call row holds two times: duration_ms is the model
time that the CLI reports, and wall_ms is the wall clock of
the subprocess. The difference is the startup cost of one CLI
call.

Calls: 4058, measured: 4058.
Mean duration: 9605 ms. Mean wall: 33815 ms. Mean startup: 24211 ms.

## Harness spend

A stored call row holds the token counts of its call: the
uncached input, cache-write input, cache-read input, and
output tokens. The cache-read share is the cache-read total
over the whole input total.

Calls: 4058, measured: 4058.
Input tokens: 28484 uncached, 3239380 cache write, 19426853 cache read. Output tokens: 3714287.
Cache-read share: 0.856.
Cache writes by lifetime: 3239380 at 5 minutes, 0 at 1 hour.

## Warnings

- technical-simplified/explanation-08: the pair failed the gate, excluded
- technical-simplified/code-review-07: the pair failed the gate, excluded
- technical-simplified/summarization-06: the pair failed the gate, excluded
- technical-simplified/summarization-07: the pair failed the gate, excluded
- technical-simplified/summarization-08: the pair failed the gate, excluded
- technical-simplified/debugging-07: the pair failed the gate, excluded
- plain-language/summarization-06: the pair has 0 shared facts, fewer than the floor of 3, so comprehension skips the pair
- technical-simplified/code-review-03: the pair has 0 shared facts, fewer than the floor of 3, so comprehension skips the pair
- plain-language/summarization-06: the comprehension check has no usable questions for the pair, so the pair is unscored
- technical-simplified/code-review-03: the comprehension check has no usable questions for the pair, so the pair is unscored
- clarity-flow: the styled answer scores worse than the unstyled answer on comprehension (5 wins, 9 losses)
- classic-concise: the styled answer scores worse than the unstyled answer on comprehension (6 wins, 9 losses)
- concise: the styled answer scores worse than the unstyled answer on comprehension (3 wins, 5 losses)
- plain-language: the styled answer scores worse than the unstyled answer on comprehension (7 wins, 9 losses)

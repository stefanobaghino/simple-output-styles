# Reader-value report

The checks compare the styled answer with the unstyled answer of
the same prompt, pair by pair, as win, loss, or tie. Only pairs
whose styled answer passes the fidelity gate enter the checks.
Each judge call sees one bare text: no style name, no arm label,
and never both answers. Thus a judge cannot know which answer is
styled. The judge models differ from the writer of the answers.

Judges: reader haiku, grader opus. Comprehension asks up to 6 questions per pair, worded by both answers in balance, with 3 reader replicates per answer, ambiguity uses 3 restatements per answer, and the round-trip goes through Italian. Judged on 2026-08-22T10:58:54+00:00.

## Comprehension (weak reader)

The questions come from the shared facts of the pair, mined in both directions: the facts of the unstyled answer that survive in the styled answer, and the facts of the styled answer that the unstyled answer also states. The quiz takes half of its questions from each wording, so neither answer sets the phrasing alone, and the Sources column counts the questions per wording (unstyled/styled). A grader call turns each fact into one question, and the fact is the reference answer. The weak reader answers the questions from one answer text, once per replicate, and the grader marks every reply. Each styled replicate meets each unstyled replicate as a win, a loss, or a tie, and the pair outcome is the strict plurality, else a tie. The agreement is the plurality share, and the buried-fact rate counts "NOT IN TEXT" replies to a shared fact, per arm. The check measures extraction over shared material. Absence belongs to the content-loss report. Higher is better.

| Style | Wins | Losses | Ties | Mean delta | Agreement | Buried (styled) | Buried (unstyled) |
|---|---|---|---|---|---|---|---|
| actionable-clarity | 7 | 1 | 24 | 0.036 | 0.851 | 0.021 | 0.042 |
| clarity-flow | 7 | 4 | 21 | 0.031 | 0.819 | 0.023 | 0.04 |
| classic-concise | 11 | 5 | 16 | 0.028 | 0.819 | 0.035 | 0.056 |
| concise | 8 | 6 | 18 | 0.019 | 0.833 | 0.056 | 0.054 |
| developer-docs | 10 | 5 | 17 | 0.026 | 0.892 | 0.026 | 0.068 |
| plain-language | 11 | 6 | 15 | 0.024 | 0.84 | 0.03 | 0.068 |
| technical-simplified | 6 | 3 | 18 | 0.012 | 0.823 | 0.016 | 0.047 |

The styled answer must not score worse than the unstyled answer.
- actionable-clarity: the styled answer holds (7 wins, 1 losses, 24 ties).
- clarity-flow: the styled answer holds (7 wins, 4 losses, 21 ties).
- classic-concise: the styled answer holds (11 wins, 5 losses, 16 ties).
- concise: the styled answer holds (8 wins, 6 losses, 18 ties).
- developer-docs: the styled answer holds (10 wins, 5 losses, 17 ties).
- plain-language: the styled answer holds (11 wins, 6 losses, 15 ties).
- technical-simplified: the styled answer holds (6 wins, 3 losses, 18 ties).

### actionable-clarity

| Pair | Questions | Sources (u/s) | Styled | Unstyled | Agreement | Result |
|---|---|---|---|---|---|---|
| code-review-01 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| code-review-02 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| code-review-03 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| code-review-04 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| code-review-05 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| code-review-06 | 6 | 3/3 | 1.0 | 0.944 | 0.667 | tie |
| code-review-07 | 6 | 3/3 | 0.889 | 1.0 | 0.667 | loss |
| code-review-08 | 6 | 3/3 | 0.833 | 0.833 | 1.0 | tie |
| debugging-01 | 6 | 3/3 | 1.0 | 0.833 | 1.0 | win |
| debugging-02 | 6 | 3/3 | 1.0 | 0.833 | 1.0 | win |
| debugging-03 | 6 | 3/3 | 0.944 | 0.889 | 0.444 | tie |
| debugging-04 | 6 | 3/3 | 1.0 | 0.944 | 0.667 | tie |
| debugging-05 | 6 | 3/3 | 1.0 | 0.833 | 0.667 | win |
| debugging-06 | 6 | 3/3 | 0.833 | 0.889 | 0.667 | tie |
| debugging-07 | 6 | 3/3 | 0.944 | 1.0 | 0.667 | tie |
| debugging-08 | 6 | 3/3 | 0.889 | 0.944 | 0.444 | tie |
| explanation-01 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| explanation-02 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| explanation-03 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| explanation-04 | 6 | 3/3 | 0.944 | 0.944 | 0.556 | tie |
| explanation-05 | 6 | 3/3 | 1.0 | 0.667 | 1.0 | win |
| explanation-06 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| explanation-07 | 6 | 3/3 | 0.778 | 0.722 | 0.444 | tie |
| explanation-08 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-01 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-02 | 6 | 3/3 | 1.0 | 0.889 | 0.667 | win |
| summarization-03 | 6 | 3/3 | 1.0 | 0.889 | 0.667 | win |
| summarization-04 | 6 | 3/3 | 0.833 | 0.833 | 1.0 | tie |
| summarization-05 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-06 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-07 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-08 | 6 | 3/3 | 1.0 | 0.833 | 1.0 | win |

### clarity-flow

| Pair | Questions | Sources (u/s) | Styled | Unstyled | Agreement | Result |
|---|---|---|---|---|---|---|
| code-review-01 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| code-review-02 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| code-review-03 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| code-review-04 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| code-review-05 | 6 | 3/3 | 1.0 | 0.833 | 1.0 | win |
| code-review-06 | 6 | 3/3 | 0.667 | 0.833 | 0.667 | loss |
| code-review-07 | 6 | 3/3 | 1.0 | 0.944 | 0.667 | tie |
| code-review-08 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-01 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-02 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-03 | 6 | 3/3 | 0.944 | 1.0 | 0.667 | tie |
| debugging-04 | 6 | 3/3 | 1.0 | 0.944 | 0.667 | tie |
| debugging-05 | 6 | 3/3 | 0.944 | 0.889 | 0.444 | tie |
| debugging-06 | 6 | 3/3 | 0.667 | 0.833 | 0.667 | loss |
| debugging-07 | 6 | 3/3 | 1.0 | 0.833 | 1.0 | win |
| debugging-08 | 6 | 3/3 | 0.889 | 0.889 | 0.556 | tie |
| explanation-01 | 6 | 3/3 | 0.944 | 1.0 | 0.667 | tie |
| explanation-02 | 6 | 3/3 | 1.0 | 0.889 | 0.667 | win |
| explanation-03 | 6 | 3/3 | 0.833 | 0.833 | 1.0 | tie |
| explanation-04 | 6 | 3/3 | 0.889 | 0.833 | 0.667 | tie |
| explanation-05 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| explanation-06 | 6 | 3/3 | 1.0 | 0.5 | 1.0 | win |
| explanation-07 | 6 | 3/3 | 0.833 | 0.833 | 1.0 | tie |
| explanation-08 | 6 | 3/3 | 0.833 | 0.722 | 0.667 | win |
| summarization-01 | 6 | 3/3 | 0.889 | 1.0 | 0.667 | loss |
| summarization-02 | 6 | 3/3 | 0.778 | 0.889 | 0.556 | loss |
| summarization-03 | 6 | 3/3 | 0.944 | 1.0 | 0.667 | tie |
| summarization-04 | 6 | 3/3 | 0.889 | 0.833 | 0.667 | tie |
| summarization-05 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-06 | 6 | 3/3 | 1.0 | 0.833 | 1.0 | win |
| summarization-07 | 6 | 3/3 | 1.0 | 0.944 | 0.667 | tie |
| summarization-08 | 6 | 3/3 | 1.0 | 0.833 | 1.0 | win |

### classic-concise

| Pair | Questions | Sources (u/s) | Styled | Unstyled | Agreement | Result |
|---|---|---|---|---|---|---|
| code-review-01 | 6 | 3/3 | 1.0 | 0.944 | 0.667 | tie |
| code-review-02 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| code-review-03 | 6 | 3/3 | 0.778 | 1.0 | 1.0 | loss |
| code-review-04 | 6 | 3/3 | 0.944 | 1.0 | 0.667 | tie |
| code-review-05 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| code-review-06 | 6 | 3/3 | 1.0 | 0.889 | 0.667 | tie |
| code-review-07 | 6 | 3/3 | 0.833 | 1.0 | 1.0 | loss |
| code-review-08 | 6 | 3/3 | 0.944 | 0.833 | 0.667 | win |
| debugging-01 | 6 | 3/3 | 1.0 | 0.722 | 0.667 | win |
| debugging-02 | 6 | 3/3 | 0.667 | 1.0 | 1.0 | loss |
| debugging-03 | 6 | 3/3 | 0.889 | 0.944 | 0.444 | tie |
| debugging-04 | 6 | 3/3 | 0.944 | 0.833 | 0.556 | win |
| debugging-05 | 6 | 3/3 | 0.889 | 0.889 | 0.444 | win |
| debugging-06 | 6 | 3/3 | 0.944 | 0.722 | 0.889 | win |
| debugging-07 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-08 | 6 | 3/3 | 0.778 | 0.833 | 0.667 | tie |
| explanation-01 | 6 | 3/3 | 0.833 | 1.0 | 1.0 | loss |
| explanation-02 | 6 | 3/3 | 0.889 | 1.0 | 0.667 | loss |
| explanation-03 | 6 | 3/3 | 0.944 | 0.944 | 0.556 | tie |
| explanation-04 | 6 | 3/3 | 1.0 | 0.778 | 1.0 | win |
| explanation-05 | 6 | 3/3 | 0.944 | 1.0 | 0.667 | tie |
| explanation-06 | 6 | 3/3 | 0.889 | 0.833 | 0.667 | tie |
| explanation-07 | 6 | 3/3 | 1.0 | 0.889 | 0.667 | win |
| explanation-08 | 6 | 3/3 | 0.944 | 0.833 | 0.667 | win |
| summarization-01 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-02 | 6 | 3/3 | 0.944 | 0.556 | 1.0 | win |
| summarization-03 | 6 | 3/3 | 1.0 | 0.833 | 1.0 | win |
| summarization-04 | 6 | 3/3 | 1.0 | 0.833 | 1.0 | win |
| summarization-05 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-06 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-07 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-08 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |

### concise

| Pair | Questions | Sources (u/s) | Styled | Unstyled | Agreement | Result |
|---|---|---|---|---|---|---|
| code-review-01 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| code-review-02 | 6 | 3/3 | 1.0 | 0.778 | 1.0 | win |
| code-review-03 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| code-review-04 | 6 | 3/3 | 0.667 | 0.833 | 1.0 | loss |
| code-review-05 | 6 | 3/3 | 1.0 | 0.944 | 0.667 | tie |
| code-review-06 | 6 | 3/3 | 0.833 | 0.833 | 1.0 | tie |
| code-review-07 | 6 | 3/3 | 0.778 | 0.833 | 0.667 | tie |
| code-review-08 | 6 | 3/3 | 0.833 | 1.0 | 0.667 | loss |
| debugging-01 | 6 | 3/3 | 0.667 | 0.722 | 0.667 | tie |
| debugging-02 | 6 | 3/3 | 0.944 | 0.889 | 0.444 | tie |
| debugging-03 | 6 | 3/3 | 1.0 | 0.833 | 0.667 | win |
| debugging-04 | 6 | 3/3 | 1.0 | 0.833 | 1.0 | win |
| debugging-05 | 6 | 3/3 | 1.0 | 0.944 | 0.667 | tie |
| debugging-06 | 6 | 3/3 | 0.667 | 0.778 | 0.667 | loss |
| debugging-07 | 6 | 3/3 | 1.0 | 0.944 | 0.667 | tie |
| debugging-08 | 6 | 3/3 | 1.0 | 0.833 | 1.0 | win |
| explanation-01 | 6 | 3/3 | 0.722 | 0.833 | 0.667 | loss |
| explanation-02 | 6 | 3/3 | 0.944 | 1.0 | 0.667 | tie |
| explanation-03 | 6 | 3/3 | 0.889 | 0.944 | 0.444 | tie |
| explanation-04 | 6 | 3/3 | 1.0 | 0.722 | 1.0 | win |
| explanation-05 | 6 | 3/3 | 1.0 | 0.833 | 1.0 | win |
| explanation-06 | 6 | 3/3 | 0.833 | 1.0 | 1.0 | loss |
| explanation-07 | 6 | 3/3 | 0.889 | 0.722 | 0.778 | win |
| explanation-08 | 6 | 3/3 | 0.833 | 1.0 | 1.0 | loss |
| summarization-01 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-02 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-03 | 6 | 3/3 | 0.778 | 0.667 | 0.667 | win |
| summarization-04 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-05 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-06 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-07 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-08 | 6 | 3/3 | 1.0 | 0.944 | 0.667 | tie |

### developer-docs

| Pair | Questions | Sources (u/s) | Styled | Unstyled | Agreement | Result |
|---|---|---|---|---|---|---|
| code-review-01 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| code-review-02 | 6 | 3/3 | 0.667 | 1.0 | 1.0 | loss |
| code-review-03 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| code-review-04 | 6 | 3/3 | 1.0 | 0.833 | 1.0 | win |
| code-review-05 | 6 | 3/3 | 1.0 | 0.944 | 0.667 | tie |
| code-review-06 | 6 | 3/3 | 0.667 | 0.722 | 0.667 | tie |
| code-review-07 | 6 | 3/3 | 1.0 | 0.889 | 0.667 | win |
| code-review-08 | 6 | 3/3 | 0.833 | 1.0 | 1.0 | loss |
| debugging-01 | 6 | 3/3 | 1.0 | 0.944 | 0.667 | tie |
| debugging-02 | 6 | 3/3 | 1.0 | 0.833 | 1.0 | win |
| debugging-03 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-04 | 6 | 3/3 | 0.889 | 1.0 | 0.667 | loss |
| debugging-05 | 6 | 3/3 | 0.944 | 1.0 | 0.667 | tie |
| debugging-06 | 6 | 3/3 | 0.778 | 0.611 | 0.778 | win |
| debugging-07 | 6 | 3/3 | 0.833 | 0.944 | 0.667 | loss |
| debugging-08 | 6 | 3/3 | 1.0 | 0.833 | 1.0 | win |
| explanation-01 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| explanation-02 | 6 | 3/3 | 1.0 | 0.833 | 1.0 | win |
| explanation-03 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| explanation-04 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| explanation-05 | 6 | 3/3 | 1.0 | 0.667 | 1.0 | win |
| explanation-06 | 6 | 3/3 | 0.833 | 0.833 | 1.0 | tie |
| explanation-07 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| explanation-08 | 6 | 3/3 | 0.833 | 1.0 | 1.0 | loss |
| summarization-01 | 6 | 3/3 | 1.0 | 0.833 | 1.0 | win |
| summarization-02 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-03 | 6 | 3/3 | 1.0 | 0.833 | 1.0 | win |
| summarization-04 | 6 | 3/3 | 0.833 | 0.778 | 0.667 | tie |
| summarization-05 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-06 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-07 | 6 | 3/3 | 0.889 | 0.833 | 0.444 | win |
| summarization-08 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |

### plain-language

| Pair | Questions | Sources (u/s) | Styled | Unstyled | Agreement | Result |
|---|---|---|---|---|---|---|
| code-review-01 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| code-review-02 | 6 | 3/3 | 1.0 | 0.722 | 1.0 | win |
| code-review-03 | 6 | 3/3 | 0.778 | 0.833 | 0.667 | tie |
| code-review-04 | 6 | 3/3 | 0.889 | 1.0 | 0.667 | loss |
| code-review-05 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| code-review-06 | 6 | 3/3 | 1.0 | 0.889 | 0.667 | win |
| code-review-07 | 6 | 3/3 | 0.833 | 0.833 | 1.0 | tie |
| code-review-08 | 6 | 3/3 | 1.0 | 0.889 | 0.667 | win |
| debugging-01 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-02 | 6 | 3/3 | 0.944 | 0.778 | 0.778 | win |
| debugging-03 | 6 | 3/3 | 0.833 | 0.889 | 0.667 | tie |
| debugging-04 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-05 | 6 | 3/3 | 1.0 | 0.889 | 0.667 | win |
| debugging-06 | 6 | 3/3 | 1.0 | 0.778 | 1.0 | win |
| debugging-07 | 6 | 3/3 | 0.889 | 1.0 | 0.667 | loss |
| debugging-08 | 6 | 3/3 | 0.889 | 1.0 | 0.667 | loss |
| explanation-01 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| explanation-02 | 6 | 3/3 | 0.833 | 0.889 | 0.667 | tie |
| explanation-03 | 6 | 3/3 | 0.667 | 1.0 | 1.0 | loss |
| explanation-04 | 6 | 3/3 | 1.0 | 0.944 | 0.667 | tie |
| explanation-05 | 6 | 3/3 | 1.0 | 0.833 | 1.0 | win |
| explanation-06 | 6 | 3/3 | 1.0 | 0.833 | 1.0 | win |
| explanation-07 | 6 | 3/3 | 0.944 | 0.889 | 0.444 | tie |
| explanation-08 | 6 | 3/3 | 0.833 | 0.833 | 1.0 | tie |
| summarization-01 | 6 | 3/3 | 0.944 | 0.833 | 0.667 | win |
| summarization-02 | 6 | 3/3 | 1.0 | 0.778 | 1.0 | win |
| summarization-03 | 6 | 3/3 | 0.833 | 1.0 | 1.0 | loss |
| summarization-04 | 6 | 3/3 | 0.667 | 0.833 | 1.0 | loss |
| summarization-05 | 6 | 3/3 | 1.0 | 0.889 | 0.667 | win |
| summarization-06 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-07 | 6 | 3/3 | 0.833 | 0.833 | 1.0 | tie |
| summarization-08 | 6 | 3/3 | 1.0 | 0.944 | 0.667 | tie |

### technical-simplified

| Pair | Questions | Sources (u/s) | Styled | Unstyled | Agreement | Result |
|---|---|---|---|---|---|---|
| code-review-01 | 6 | 3/3 | 1.0 | 0.944 | 0.667 | tie |
| code-review-02 | 6 | 3/3 | 0.833 | 0.889 | 0.667 | tie |
| code-review-03 | 6 | 3/3 | 0.944 | 1.0 | 0.667 | tie |
| code-review-04 | 6 | 3/3 | 0.944 | 1.0 | 0.667 | tie |
| code-review-05 | 6 | 3/3 | 0.944 | 1.0 | 0.667 | tie |
| code-review-06 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| code-review-07 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-01 | 6 | 3/3 | 0.833 | 0.889 | 0.667 | tie |
| debugging-02 | 6 | 3/3 | 0.833 | 1.0 | 1.0 | loss |
| debugging-03 | 6 | 3/3 | 0.889 | 1.0 | 0.667 | loss |
| debugging-04 | 6 | 3/3 | 1.0 | 0.944 | 0.667 | tie |
| debugging-05 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| debugging-07 | 6 | 3/3 | 0.944 | 0.778 | 0.778 | win |
| explanation-01 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| explanation-02 | 6 | 3/3 | 0.833 | 0.833 | 1.0 | tie |
| explanation-03 | 6 | 3/3 | 1.0 | 0.833 | 1.0 | win |
| explanation-04 | 6 | 3/3 | 0.944 | 1.0 | 0.667 | tie |
| explanation-05 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| explanation-06 | 6 | 3/3 | 0.889 | 0.667 | 1.0 | win |
| explanation-07 | 6 | 3/3 | 0.944 | 0.778 | 0.778 | win |
| explanation-08 | 6 | 3/3 | 0.833 | 0.944 | 0.667 | loss |
| summarization-01 | 6 | 3/3 | 1.0 | 0.778 | 1.0 | win |
| summarization-03 | 6 | 3/3 | 0.944 | 1.0 | 0.667 | tie |
| summarization-04 | 6 | 3/3 | 0.833 | 0.722 | 0.667 | win |
| summarization-05 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |
| summarization-07 | 6 | 3/3 | 0.944 | 1.0 | 0.667 | tie |
| summarization-08 | 6 | 3/3 | 1.0 | 1.0 | 1.0 | tie |

## Ambiguity (paraphrase agreement)

Independent reader calls restate one answer text in their own words. The score is the mean pairwise lexical similarity between the restatements: when the readers agree on what the text says, the text is less ambiguous. Higher is better.

| Style | Wins | Losses | Ties |
|---|---|---|---|
| actionable-clarity | 13 | 12 | 7 |
| clarity-flow | 15 | 11 | 6 |
| classic-concise | 10 | 17 | 5 |
| concise | 13 | 11 | 8 |
| developer-docs | 15 | 8 | 9 |
| plain-language | 16 | 9 | 7 |
| technical-simplified | 18 | 6 | 4 |

The length confound is the correlation between the length ratio of a pair (styled words over unstyled words) and the styled advantage (the score gain of the styled arm). A negative value means that the shorter styled answers score better.
- actionable-clarity: Pearson -0.011, Spearman 0.066, over 32 pairs.
- clarity-flow: Pearson -0.112, Spearman -0.099, over 32 pairs.
- classic-concise: Pearson 0.014, Spearman 0.007, over 32 pairs.
- concise: Pearson -0.055, Spearman 0.025, over 32 pairs.
- developer-docs: Pearson -0.03, Spearman 0.03, over 32 pairs.
- plain-language: Pearson 0.192, Spearman 0.163, over 32 pairs.
- technical-simplified: Pearson -0.101, Spearman -0.028, over 28 pairs.

### actionable-clarity

| Pair | Styled | Unstyled | Result |
|---|---|---|---|
| code-review-01 | 0.708 | 0.635 | win |
| code-review-02 | 0.746 | 0.65 | win |
| code-review-03 | 0.713 | 0.702 | tie |
| code-review-04 | 0.744 | 0.622 | win |
| code-review-05 | 0.728 | 0.707 | win |
| code-review-06 | 0.707 | 0.545 | win |
| code-review-07 | 0.646 | 0.546 | win |
| code-review-08 | 0.624 | 0.683 | loss |
| debugging-01 | 0.709 | 0.567 | win |
| debugging-02 | 0.635 | 0.732 | loss |
| debugging-03 | 0.84 | 0.636 | win |
| debugging-04 | 0.722 | 0.742 | tie |
| debugging-05 | 0.746 | 0.666 | win |
| debugging-06 | 0.664 | 0.623 | win |
| debugging-07 | 0.704 | 0.692 | tie |
| debugging-08 | 0.53 | 0.64 | loss |
| explanation-01 | 0.688 | 0.689 | tie |
| explanation-02 | 0.715 | 0.713 | tie |
| explanation-03 | 0.686 | 0.733 | loss |
| explanation-04 | 0.613 | 0.718 | loss |
| explanation-05 | 0.733 | 0.61 | win |
| explanation-06 | 0.658 | 0.602 | win |
| explanation-07 | 0.59 | 0.614 | loss |
| explanation-08 | 0.593 | 0.672 | loss |
| summarization-01 | 0.581 | 0.652 | loss |
| summarization-02 | 0.608 | 0.589 | tie |
| summarization-03 | 0.68 | 0.669 | tie |
| summarization-04 | 0.589 | 0.626 | loss |
| summarization-05 | 0.706 | 0.772 | loss |
| summarization-06 | 0.631 | 0.67 | loss |
| summarization-07 | 0.566 | 0.636 | loss |
| summarization-08 | 0.678 | 0.603 | win |

### clarity-flow

| Pair | Styled | Unstyled | Result |
|---|---|---|---|
| code-review-01 | 0.621 | 0.635 | tie |
| code-review-02 | 0.703 | 0.65 | win |
| code-review-03 | 0.697 | 0.702 | tie |
| code-review-04 | 0.597 | 0.622 | loss |
| code-review-05 | 0.646 | 0.707 | loss |
| code-review-06 | 0.677 | 0.545 | win |
| code-review-07 | 0.667 | 0.546 | win |
| code-review-08 | 0.643 | 0.683 | loss |
| debugging-01 | 0.674 | 0.567 | win |
| debugging-02 | 0.81 | 0.732 | win |
| debugging-03 | 0.744 | 0.636 | win |
| debugging-04 | 0.803 | 0.742 | win |
| debugging-05 | 0.696 | 0.666 | win |
| debugging-06 | 0.689 | 0.623 | win |
| debugging-07 | 0.666 | 0.692 | loss |
| debugging-08 | 0.622 | 0.64 | tie |
| explanation-01 | 0.729 | 0.689 | win |
| explanation-02 | 0.63 | 0.713 | loss |
| explanation-03 | 0.701 | 0.733 | loss |
| explanation-04 | 0.676 | 0.718 | loss |
| explanation-05 | 0.672 | 0.61 | win |
| explanation-06 | 0.628 | 0.602 | win |
| explanation-07 | 0.572 | 0.614 | loss |
| explanation-08 | 0.621 | 0.672 | loss |
| summarization-01 | 0.686 | 0.652 | win |
| summarization-02 | 0.606 | 0.589 | tie |
| summarization-03 | 0.652 | 0.669 | tie |
| summarization-04 | 0.68 | 0.626 | win |
| summarization-05 | 0.721 | 0.772 | loss |
| summarization-06 | 0.744 | 0.67 | win |
| summarization-07 | 0.614 | 0.636 | loss |
| summarization-08 | 0.587 | 0.603 | tie |

### classic-concise

| Pair | Styled | Unstyled | Result |
|---|---|---|---|
| code-review-01 | 0.586 | 0.635 | loss |
| code-review-02 | 0.721 | 0.65 | win |
| code-review-03 | 0.552 | 0.702 | loss |
| code-review-04 | 0.562 | 0.622 | loss |
| code-review-05 | 0.673 | 0.707 | loss |
| code-review-06 | 0.652 | 0.545 | win |
| code-review-07 | 0.631 | 0.546 | win |
| code-review-08 | 0.671 | 0.683 | tie |
| debugging-01 | 0.723 | 0.567 | win |
| debugging-02 | 0.74 | 0.732 | tie |
| debugging-03 | 0.843 | 0.636 | win |
| debugging-04 | 0.773 | 0.742 | win |
| debugging-05 | 0.666 | 0.666 | tie |
| debugging-06 | 0.655 | 0.623 | win |
| debugging-07 | 0.624 | 0.692 | loss |
| debugging-08 | 0.603 | 0.64 | loss |
| explanation-01 | 0.646 | 0.689 | loss |
| explanation-02 | 0.668 | 0.713 | loss |
| explanation-03 | 0.633 | 0.733 | loss |
| explanation-04 | 0.653 | 0.718 | loss |
| explanation-05 | 0.544 | 0.61 | loss |
| explanation-06 | 0.547 | 0.602 | loss |
| explanation-07 | 0.618 | 0.614 | tie |
| explanation-08 | 0.689 | 0.672 | tie |
| summarization-01 | 0.688 | 0.652 | win |
| summarization-02 | 0.538 | 0.589 | loss |
| summarization-03 | 0.595 | 0.669 | loss |
| summarization-04 | 0.651 | 0.626 | win |
| summarization-05 | 0.735 | 0.772 | loss |
| summarization-06 | 0.596 | 0.67 | loss |
| summarization-07 | 0.738 | 0.636 | win |
| summarization-08 | 0.579 | 0.603 | loss |

### concise

| Pair | Styled | Unstyled | Result |
|---|---|---|---|
| code-review-01 | 0.694 | 0.635 | win |
| code-review-02 | 0.664 | 0.65 | tie |
| code-review-03 | 0.648 | 0.702 | loss |
| code-review-04 | 0.642 | 0.622 | win |
| code-review-05 | 0.686 | 0.707 | loss |
| code-review-06 | 0.601 | 0.545 | win |
| code-review-07 | 0.657 | 0.546 | win |
| code-review-08 | 0.694 | 0.683 | tie |
| debugging-01 | 0.759 | 0.567 | win |
| debugging-02 | 0.767 | 0.732 | win |
| debugging-03 | 0.78 | 0.636 | win |
| debugging-04 | 0.766 | 0.742 | win |
| debugging-05 | 0.598 | 0.666 | loss |
| debugging-06 | 0.674 | 0.623 | win |
| debugging-07 | 0.663 | 0.692 | loss |
| debugging-08 | 0.691 | 0.64 | win |
| explanation-01 | 0.705 | 0.689 | tie |
| explanation-02 | 0.67 | 0.713 | loss |
| explanation-03 | 0.714 | 0.733 | tie |
| explanation-04 | 0.678 | 0.718 | loss |
| explanation-05 | 0.599 | 0.61 | tie |
| explanation-06 | 0.61 | 0.602 | tie |
| explanation-07 | 0.522 | 0.614 | loss |
| explanation-08 | 0.625 | 0.672 | loss |
| summarization-01 | 0.504 | 0.652 | loss |
| summarization-02 | 0.693 | 0.589 | win |
| summarization-03 | 0.698 | 0.669 | win |
| summarization-04 | 0.618 | 0.626 | tie |
| summarization-05 | 0.742 | 0.772 | loss |
| summarization-06 | 0.724 | 0.67 | win |
| summarization-07 | 0.636 | 0.636 | tie |
| summarization-08 | 0.562 | 0.603 | loss |

### developer-docs

| Pair | Styled | Unstyled | Result |
|---|---|---|---|
| code-review-01 | 0.652 | 0.635 | tie |
| code-review-02 | 0.707 | 0.65 | win |
| code-review-03 | 0.603 | 0.702 | loss |
| code-review-04 | 0.707 | 0.622 | win |
| code-review-05 | 0.597 | 0.707 | loss |
| code-review-06 | 0.651 | 0.545 | win |
| code-review-07 | 0.662 | 0.546 | win |
| code-review-08 | 0.597 | 0.683 | loss |
| debugging-01 | 0.8 | 0.567 | win |
| debugging-02 | 0.663 | 0.732 | loss |
| debugging-03 | 0.796 | 0.636 | win |
| debugging-04 | 0.832 | 0.742 | win |
| debugging-05 | 0.725 | 0.666 | win |
| debugging-06 | 0.697 | 0.623 | win |
| debugging-07 | 0.652 | 0.692 | loss |
| debugging-08 | 0.621 | 0.64 | tie |
| explanation-01 | 0.691 | 0.689 | tie |
| explanation-02 | 0.741 | 0.713 | win |
| explanation-03 | 0.675 | 0.733 | loss |
| explanation-04 | 0.708 | 0.718 | tie |
| explanation-05 | 0.673 | 0.61 | win |
| explanation-06 | 0.606 | 0.602 | tie |
| explanation-07 | 0.608 | 0.614 | tie |
| explanation-08 | 0.655 | 0.672 | tie |
| summarization-01 | 0.578 | 0.652 | loss |
| summarization-02 | 0.624 | 0.589 | win |
| summarization-03 | 0.66 | 0.669 | tie |
| summarization-04 | 0.762 | 0.626 | win |
| summarization-05 | 0.725 | 0.772 | loss |
| summarization-06 | 0.699 | 0.67 | win |
| summarization-07 | 0.632 | 0.636 | tie |
| summarization-08 | 0.639 | 0.603 | win |

### plain-language

| Pair | Styled | Unstyled | Result |
|---|---|---|---|
| code-review-01 | 0.706 | 0.635 | win |
| code-review-02 | 0.618 | 0.65 | loss |
| code-review-03 | 0.716 | 0.702 | tie |
| code-review-04 | 0.692 | 0.622 | win |
| code-review-05 | 0.638 | 0.707 | loss |
| code-review-06 | 0.727 | 0.545 | win |
| code-review-07 | 0.637 | 0.546 | win |
| code-review-08 | 0.687 | 0.683 | tie |
| debugging-01 | 0.843 | 0.567 | win |
| debugging-02 | 0.838 | 0.732 | win |
| debugging-03 | 0.816 | 0.636 | win |
| debugging-04 | 0.764 | 0.742 | win |
| debugging-05 | 0.637 | 0.666 | loss |
| debugging-06 | 0.664 | 0.623 | win |
| debugging-07 | 0.7 | 0.692 | tie |
| debugging-08 | 0.644 | 0.64 | tie |
| explanation-01 | 0.717 | 0.689 | win |
| explanation-02 | 0.687 | 0.713 | loss |
| explanation-03 | 0.714 | 0.733 | tie |
| explanation-04 | 0.656 | 0.718 | loss |
| explanation-05 | 0.729 | 0.61 | win |
| explanation-06 | 0.634 | 0.602 | win |
| explanation-07 | 0.637 | 0.614 | win |
| explanation-08 | 0.641 | 0.672 | loss |
| summarization-01 | 0.618 | 0.652 | loss |
| summarization-02 | 0.682 | 0.589 | win |
| summarization-03 | 0.712 | 0.669 | win |
| summarization-04 | 0.579 | 0.626 | loss |
| summarization-05 | 0.662 | 0.772 | loss |
| summarization-06 | 0.688 | 0.67 | tie |
| summarization-07 | 0.637 | 0.636 | tie |
| summarization-08 | 0.642 | 0.603 | win |

### technical-simplified

| Pair | Styled | Unstyled | Result |
|---|---|---|---|
| code-review-01 | 0.644 | 0.635 | tie |
| code-review-02 | 0.719 | 0.65 | win |
| code-review-03 | 0.73 | 0.702 | win |
| code-review-04 | 0.7 | 0.622 | win |
| code-review-05 | 0.653 | 0.707 | loss |
| code-review-06 | 0.738 | 0.545 | win |
| code-review-07 | 0.728 | 0.546 | win |
| code-review-08 | 0.788 | 0.683 | win |
| debugging-01 | 0.621 | 0.567 | win |
| debugging-02 | 0.799 | 0.732 | win |
| debugging-03 | 0.786 | 0.636 | win |
| debugging-04 | 0.838 | 0.742 | win |
| debugging-05 | 0.697 | 0.666 | win |
| debugging-07 | 0.776 | 0.692 | win |
| explanation-01 | 0.74 | 0.689 | win |
| explanation-02 | 0.717 | 0.713 | tie |
| explanation-03 | 0.698 | 0.733 | loss |
| explanation-04 | 0.662 | 0.718 | loss |
| explanation-05 | 0.712 | 0.61 | win |
| explanation-06 | 0.677 | 0.602 | win |
| explanation-07 | 0.59 | 0.614 | loss |
| explanation-08 | 0.616 | 0.672 | loss |
| summarization-01 | 0.639 | 0.652 | tie |
| summarization-03 | 0.677 | 0.669 | tie |
| summarization-04 | 0.706 | 0.626 | win |
| summarization-05 | 0.663 | 0.772 | loss |
| summarization-07 | 0.667 | 0.636 | win |
| summarization-08 | 0.64 | 0.603 | win |

## Translation round-trip

One call translates the answer to another language, and a second call translates the result back to English. The score is the lexical loss between the original and the round-trip: simpler text survives the round-trip with less loss. Lower is better.

| Style | Wins | Losses | Ties |
|---|---|---|---|
| actionable-clarity | 10 | 6 | 16 |
| clarity-flow | 7 | 10 | 15 |
| classic-concise | 3 | 14 | 15 |
| concise | 5 | 18 | 9 |
| developer-docs | 14 | 7 | 11 |
| plain-language | 10 | 10 | 12 |
| technical-simplified | 9 | 8 | 11 |

The length confound is the correlation between the length ratio of a pair (styled words over unstyled words) and the styled advantage (the score gain of the styled arm). A negative value means that the shorter styled answers score better.
- actionable-clarity: Pearson -0.031, Spearman 0.049, over 32 pairs.
- clarity-flow: Pearson 0.272, Spearman 0.247, over 32 pairs.
- classic-concise: Pearson -0.053, Spearman -0.234, over 32 pairs.
- concise: Pearson -0.183, Spearman -0.141, over 32 pairs.
- developer-docs: Pearson 0.086, Spearman 0.167, over 32 pairs.
- plain-language: Pearson 0.16, Spearman 0.058, over 32 pairs.
- technical-simplified: Pearson 0.641, Spearman 0.198, over 28 pairs.

### actionable-clarity

| Pair | Styled | Unstyled | Result |
|---|---|---|---|
| code-review-01 | 0.045 | 0.048 | tie |
| code-review-02 | 0.042 | 0.046 | tie |
| code-review-03 | 0.087 | 0.083 | tie |
| code-review-04 | 0.079 | 0.119 | win |
| code-review-05 | 0.047 | 0.111 | win |
| code-review-06 | 0.11 | 0.065 | loss |
| code-review-07 | 0.078 | 0.08 | tie |
| code-review-08 | 0.179 | 0.123 | loss |
| debugging-01 | 0.137 | 0.172 | win |
| debugging-02 | 0.056 | 0.052 | tie |
| debugging-03 | 0.045 | 0.04 | tie |
| debugging-04 | 0.047 | 0.076 | win |
| debugging-05 | 0.113 | 0.123 | tie |
| debugging-06 | 0.08 | 0.106 | win |
| debugging-07 | 0.059 | 0.082 | win |
| debugging-08 | 0.11 | 0.136 | win |
| explanation-01 | 0.118 | 0.113 | tie |
| explanation-02 | 0.118 | 0.104 | tie |
| explanation-03 | 0.098 | 0.109 | tie |
| explanation-04 | 0.135 | 0.07 | loss |
| explanation-05 | 0.106 | 0.101 | tie |
| explanation-06 | 0.078 | 0.064 | tie |
| explanation-07 | 0.138 | 0.136 | tie |
| explanation-08 | 0.117 | 0.106 | tie |
| summarization-01 | 0.2 | 0.12 | loss |
| summarization-02 | 0.134 | 0.122 | tie |
| summarization-03 | 0.212 | 0.122 | loss |
| summarization-04 | 0.099 | 0.069 | loss |
| summarization-05 | 0.083 | 0.179 | win |
| summarization-06 | 0.091 | 0.158 | win |
| summarization-07 | 0.12 | 0.138 | tie |
| summarization-08 | 0.12 | 0.206 | win |

### clarity-flow

| Pair | Styled | Unstyled | Result |
|---|---|---|---|
| code-review-01 | 0.063 | 0.048 | tie |
| code-review-02 | 0.036 | 0.046 | tie |
| code-review-03 | 0.116 | 0.083 | loss |
| code-review-04 | 0.096 | 0.119 | win |
| code-review-05 | 0.111 | 0.111 | tie |
| code-review-06 | 0.066 | 0.065 | tie |
| code-review-07 | 0.097 | 0.08 | tie |
| code-review-08 | 0.174 | 0.123 | loss |
| debugging-01 | 0.091 | 0.172 | win |
| debugging-02 | 0.043 | 0.052 | tie |
| debugging-03 | 0.09 | 0.04 | loss |
| debugging-04 | 0.053 | 0.076 | win |
| debugging-05 | 0.089 | 0.123 | win |
| debugging-06 | 0.122 | 0.106 | tie |
| debugging-07 | 0.097 | 0.082 | tie |
| debugging-08 | 0.113 | 0.136 | win |
| explanation-01 | 0.107 | 0.113 | tie |
| explanation-02 | 0.095 | 0.104 | tie |
| explanation-03 | 0.106 | 0.109 | tie |
| explanation-04 | 0.135 | 0.07 | loss |
| explanation-05 | 0.128 | 0.101 | loss |
| explanation-06 | 0.097 | 0.064 | loss |
| explanation-07 | 0.101 | 0.136 | win |
| explanation-08 | 0.133 | 0.106 | loss |
| summarization-01 | 0.128 | 0.12 | tie |
| summarization-02 | 0.105 | 0.122 | tie |
| summarization-03 | 0.15 | 0.122 | loss |
| summarization-04 | 0.128 | 0.069 | loss |
| summarization-05 | 0.126 | 0.179 | win |
| summarization-06 | 0.169 | 0.158 | tie |
| summarization-07 | 0.155 | 0.138 | tie |
| summarization-08 | 0.228 | 0.206 | loss |

### classic-concise

| Pair | Styled | Unstyled | Result |
|---|---|---|---|
| code-review-01 | 0.091 | 0.048 | loss |
| code-review-02 | 0.03 | 0.046 | tie |
| code-review-03 | 0.094 | 0.083 | tie |
| code-review-04 | 0.094 | 0.119 | win |
| code-review-05 | 0.091 | 0.111 | win |
| code-review-06 | 0.099 | 0.065 | loss |
| code-review-07 | 0.118 | 0.08 | loss |
| code-review-08 | 0.146 | 0.123 | loss |
| debugging-01 | 0.213 | 0.172 | loss |
| debugging-02 | 0.044 | 0.052 | tie |
| debugging-03 | 0.059 | 0.04 | tie |
| debugging-04 | 0.088 | 0.076 | tie |
| debugging-05 | 0.123 | 0.123 | tie |
| debugging-06 | 0.144 | 0.106 | loss |
| debugging-07 | 0.091 | 0.082 | tie |
| debugging-08 | 0.144 | 0.136 | tie |
| explanation-01 | 0.115 | 0.113 | tie |
| explanation-02 | 0.161 | 0.104 | loss |
| explanation-03 | 0.123 | 0.109 | tie |
| explanation-04 | 0.086 | 0.07 | tie |
| explanation-05 | 0.131 | 0.101 | loss |
| explanation-06 | 0.124 | 0.064 | loss |
| explanation-07 | 0.134 | 0.136 | tie |
| explanation-08 | 0.101 | 0.106 | tie |
| summarization-01 | 0.143 | 0.12 | loss |
| summarization-02 | 0.211 | 0.122 | loss |
| summarization-03 | 0.171 | 0.122 | loss |
| summarization-04 | 0.114 | 0.069 | loss |
| summarization-05 | 0.05 | 0.179 | win |
| summarization-06 | 0.164 | 0.158 | tie |
| summarization-07 | 0.218 | 0.138 | loss |
| summarization-08 | 0.215 | 0.206 | tie |

### concise

| Pair | Styled | Unstyled | Result |
|---|---|---|---|
| code-review-01 | 0.086 | 0.048 | loss |
| code-review-02 | 0.107 | 0.046 | loss |
| code-review-03 | 0.161 | 0.083 | loss |
| code-review-04 | 0.133 | 0.119 | tie |
| code-review-05 | 0.086 | 0.111 | win |
| code-review-06 | 0.137 | 0.065 | loss |
| code-review-07 | 0.11 | 0.08 | loss |
| code-review-08 | 0.137 | 0.123 | tie |
| debugging-01 | 0.182 | 0.172 | tie |
| debugging-02 | 0.063 | 0.052 | tie |
| debugging-03 | 0.011 | 0.04 | win |
| debugging-04 | 0.134 | 0.076 | loss |
| debugging-05 | 0.091 | 0.123 | win |
| debugging-06 | 0.152 | 0.106 | loss |
| debugging-07 | 0.127 | 0.082 | loss |
| debugging-08 | 0.124 | 0.136 | tie |
| explanation-01 | 0.136 | 0.113 | loss |
| explanation-02 | 0.166 | 0.104 | loss |
| explanation-03 | 0.096 | 0.109 | tie |
| explanation-04 | 0.121 | 0.07 | loss |
| explanation-05 | 0.187 | 0.101 | loss |
| explanation-06 | 0.074 | 0.064 | tie |
| explanation-07 | 0.127 | 0.136 | tie |
| explanation-08 | 0.137 | 0.106 | loss |
| summarization-01 | 0.173 | 0.12 | loss |
| summarization-02 | 0.168 | 0.122 | loss |
| summarization-03 | 0.193 | 0.122 | loss |
| summarization-04 | 0.111 | 0.069 | loss |
| summarization-05 | 0.158 | 0.179 | win |
| summarization-06 | 0.224 | 0.158 | loss |
| summarization-07 | 0.127 | 0.138 | tie |
| summarization-08 | 0.179 | 0.206 | win |

### developer-docs

| Pair | Styled | Unstyled | Result |
|---|---|---|---|
| code-review-01 | 0.049 | 0.048 | tie |
| code-review-02 | 0.096 | 0.046 | loss |
| code-review-03 | 0.124 | 0.083 | loss |
| code-review-04 | 0.085 | 0.119 | win |
| code-review-05 | 0.06 | 0.111 | win |
| code-review-06 | 0.088 | 0.065 | loss |
| code-review-07 | 0.069 | 0.08 | tie |
| code-review-08 | 0.141 | 0.123 | tie |
| debugging-01 | 0.085 | 0.172 | win |
| debugging-02 | 0.045 | 0.052 | tie |
| debugging-03 | 0.023 | 0.04 | tie |
| debugging-04 | 0.031 | 0.076 | win |
| debugging-05 | 0.076 | 0.123 | win |
| debugging-06 | 0.084 | 0.106 | win |
| debugging-07 | 0.067 | 0.082 | tie |
| debugging-08 | 0.096 | 0.136 | win |
| explanation-01 | 0.109 | 0.113 | tie |
| explanation-02 | 0.1 | 0.104 | tie |
| explanation-03 | 0.115 | 0.109 | tie |
| explanation-04 | 0.077 | 0.07 | tie |
| explanation-05 | 0.058 | 0.101 | win |
| explanation-06 | 0.115 | 0.064 | loss |
| explanation-07 | 0.106 | 0.136 | win |
| explanation-08 | 0.144 | 0.106 | loss |
| summarization-01 | 0.155 | 0.12 | loss |
| summarization-02 | 0.106 | 0.122 | tie |
| summarization-03 | 0.085 | 0.122 | win |
| summarization-04 | 0.018 | 0.069 | win |
| summarization-05 | 0.104 | 0.179 | win |
| summarization-06 | 0.121 | 0.158 | win |
| summarization-07 | 0.167 | 0.138 | loss |
| summarization-08 | 0.16 | 0.206 | win |

### plain-language

| Pair | Styled | Unstyled | Result |
|---|---|---|---|
| code-review-01 | 0.081 | 0.048 | loss |
| code-review-02 | 0.057 | 0.046 | tie |
| code-review-03 | 0.101 | 0.083 | tie |
| code-review-04 | 0.119 | 0.119 | tie |
| code-review-05 | 0.054 | 0.111 | win |
| code-review-06 | 0.113 | 0.065 | loss |
| code-review-07 | 0.111 | 0.08 | loss |
| code-review-08 | 0.078 | 0.123 | win |
| debugging-01 | 0.041 | 0.172 | win |
| debugging-02 | 0.068 | 0.052 | tie |
| debugging-03 | 0.061 | 0.04 | loss |
| debugging-04 | 0.118 | 0.076 | loss |
| debugging-05 | 0.074 | 0.123 | win |
| debugging-06 | 0.164 | 0.106 | loss |
| debugging-07 | 0.071 | 0.082 | tie |
| debugging-08 | 0.115 | 0.136 | win |
| explanation-01 | 0.143 | 0.113 | loss |
| explanation-02 | 0.102 | 0.104 | tie |
| explanation-03 | 0.101 | 0.109 | tie |
| explanation-04 | 0.109 | 0.07 | loss |
| explanation-05 | 0.13 | 0.101 | loss |
| explanation-06 | 0.082 | 0.064 | tie |
| explanation-07 | 0.092 | 0.136 | win |
| explanation-08 | 0.092 | 0.106 | tie |
| summarization-01 | 0.094 | 0.12 | win |
| summarization-02 | 0.068 | 0.122 | win |
| summarization-03 | 0.148 | 0.122 | loss |
| summarization-04 | 0.072 | 0.069 | tie |
| summarization-05 | 0.129 | 0.179 | win |
| summarization-06 | 0.164 | 0.158 | tie |
| summarization-07 | 0.129 | 0.138 | tie |
| summarization-08 | 0.137 | 0.206 | win |

### technical-simplified

| Pair | Styled | Unstyled | Result |
|---|---|---|---|
| code-review-01 | 0.066 | 0.048 | tie |
| code-review-02 | 0.038 | 0.046 | tie |
| code-review-03 | 0.031 | 0.083 | win |
| code-review-04 | 0.059 | 0.119 | win |
| code-review-05 | 0.085 | 0.111 | win |
| code-review-06 | 0.068 | 0.065 | tie |
| code-review-07 | 0.14 | 0.08 | loss |
| code-review-08 | 0.959 | 0.123 | loss |
| debugging-01 | 0.033 | 0.172 | win |
| debugging-02 | 0.067 | 0.052 | tie |
| debugging-03 | 0.061 | 0.04 | loss |
| debugging-04 | 0.082 | 0.076 | tie |
| debugging-05 | 0.114 | 0.123 | tie |
| debugging-07 | 0.123 | 0.082 | loss |
| explanation-01 | 0.078 | 0.113 | win |
| explanation-02 | 0.086 | 0.104 | tie |
| explanation-03 | 0.074 | 0.109 | win |
| explanation-04 | 0.088 | 0.07 | tie |
| explanation-05 | 0.159 | 0.101 | loss |
| explanation-06 | 0.154 | 0.064 | loss |
| explanation-07 | 0.126 | 0.136 | tie |
| explanation-08 | 0.194 | 0.106 | loss |
| summarization-01 | 0.127 | 0.12 | tie |
| summarization-03 | 0.085 | 0.122 | win |
| summarization-04 | 0.026 | 0.069 | win |
| summarization-05 | 0.164 | 0.179 | tie |
| summarization-07 | 0.165 | 0.138 | loss |
| summarization-08 | 0.186 | 0.206 | win |

## Call timing

A stored call row holds two times: duration_ms is the model
time that the CLI reports, and wall_ms is the wall clock of
the subprocess. The difference is the startup cost of one CLI
call.

Calls: 4107, measured: 4107.
Mean duration: 10092 ms. Mean wall: 33725 ms. Mean startup: 23634 ms.

## Harness spend

A stored call row holds the token counts of its call: the
uncached input, cache-write input, cache-read input, and
output tokens. The cache-read share is the cache-read total
over the whole input total.

Calls: 4107, measured: 4107.
Input tokens: 28806 uncached, 3285205 cache write, 19601667 cache read. Output tokens: 3996271.
Cache-read share: 0.855.
Cache writes by lifetime: 3285205 at 5 minutes, 0 at 1 hour.

## Warnings

- technical-simplified/summarization-02: the pair failed the gate, excluded
- technical-simplified/summarization-06: the pair failed the gate, excluded
- technical-simplified/debugging-06: the pair failed the gate, excluded
- technical-simplified/debugging-08: the pair failed the gate, excluded
- technical-simplified/code-review-08: the pair has 0 shared facts, fewer than the floor of 3, so comprehension skips the pair
- technical-simplified/code-review-08: the comprehension check has no usable questions for the pair, so the pair is unscored

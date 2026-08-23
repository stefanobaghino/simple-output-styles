# Fidelity report

A pair passes the gate when its styled answer has at least one
sentence and a violation rate at or below the threshold of its
style. The baseline columns check the unstyled answers with the
same rules; the baseline carries no mark, because the unstyled
answers are not supposed to obey a style. The judged measurements
read only the passing pairs.

## actionable-clarity

- Threshold: 5.0 violations per 100 sentences
- Passing pairs: 32/32
- Styled rate: 0.18 per 100 sentences
- Baseline rate: 6.14 per 100 sentences

| Rule | Styled | Baseline |
|---|---|---|
| latin-abbreviation | 1 | 31 |

## clarity-flow

- Threshold: 5.0 violations per 100 sentences
- Passing pairs: 32/32
- Styled rate: 0.0 per 100 sentences
- Baseline rate: 0.0 per 100 sentences

| Rule | Styled | Baseline |
|---|---|---|
| none | 0 | 0 |

## classic-concise

- Threshold: 10.0 violations per 100 sentences
- Passing pairs: 32/32
- Styled rate: 0.47 per 100 sentences
- Baseline rate: 0.79 per 100 sentences

| Rule | Styled | Baseline |
|---|---|---|
| banned-word | 2 | 3 |
| needless-phrase | 0 | 1 |

## concise

- Threshold: 5.0 violations per 100 sentences
- Passing pairs: 32/32
- Styled rate: 0.0 per 100 sentences
- Baseline rate: 0.0 per 100 sentences

| Rule | Styled | Baseline |
|---|---|---|
| none | 0 | 0 |

## developer-docs

- Threshold: 10.0 violations per 100 sentences
- Passing pairs: 32/32
- Styled rate: 0.0 per 100 sentences
- Baseline rate: 8.32 per 100 sentences

| Rule | Styled | Baseline |
|---|---|---|
| banned-modal | 0 | 9 |
| latin-abbreviation | 0 | 31 |
| minimizer | 0 | 2 |

## plain-language

- Threshold: 5.0 violations per 100 sentences
- Passing pairs: 32/32
- Styled rate: 0.0 per 100 sentences
- Baseline rate: 6.14 per 100 sentences

| Rule | Styled | Baseline |
|---|---|---|
| latin-abbreviation | 0 | 31 |

## technical-simplified

- Threshold: 15.0 violations per 100 sentences
- Passing pairs: 28/32
- Styled rate: 6.84 per 100 sentences
- Baseline rate: 75.64 per 100 sentences

| Rule | Styled | Baseline |
|---|---|---|
| banned-modal | 4 | 54 |
| banned-word | 24 | 55 |
| contraction | 0 | 126 |
| latin-abbreviation | 0 | 31 |
| semicolon | 0 | 7 |
| sentence-length | 13 | 109 |

### Failing pairs

- summarization-02 (rate 15.38):
  - [banned-word] 'main': Here are the three main takeaways:
  - [banned-word] 'reduce': Rename the files or move them to separate directories to reduce this risk.
- summarization-06 (rate 40.0):
  - [banned-word] 'confirmed': The on-call engineer suspects connection-pool exhaustion in the payments client, but the team did not keep the pool metrics, so this cause is not confirmed.
  - [sentence-length] 'The on-call engineer suspects connection': The on-call engineer suspects connection-pool exhaustion in the payments client, but the team did not keep the pool metrics, so this cause is not confirmed.
- debugging-06 (rate 21.88):
  - [banned-modal] 'could': The pool exhausted error means the export job could not get a database connection within 30 seconds.
  - [sentence-length] 'Look at active connections, wait queue l': Look at active connections, wait queue length, and pool size around 02:14:07Z. This tells you if the pool was actually full, and by which service.
  - [sentence-length] 'Find the max pool size, the connection t': Find the max pool size, the connection timeout, and whether the export job and the analytics service use separate pools or one shared pool.
  - [banned-modal] 'might': Search the code for places that open a connection but might skip the release step on an exception path.
  - [banned-word] 'confirm': This is the fastest way to confirm or rule out resource contention as the cause, since the failure pattern (once a week, no fixed batch number, shared database) points toward a load-based issue and not a code defect in one specific batch.
  - [banned-word] 'since': This is the fastest way to confirm or rule out resource contention as the cause, since the failure pattern (once a week, no fixed batch number, shared database) points toward a load-based issue and not a code defect in one specific batch.
  - [sentence-length] 'This is the fastest way to confirm or ru': This is the fastest way to confirm or rule out resource contention as the cause, since the failure pattern (once a week, no fixed batch number, shared database) points toward a load-based issue and not a code defect in one specific batch.
- debugging-08 (rate 19.23):
  - [sentence-length] '3. The cache bound limits entry count, n': 3. The cache bound limits entry count, not memory size If the bound counts entries, not bytes, larger product records during a campaign can raise total cache memory even at a fixed entry count.
  - [sentence-length] '4. Off-heap or native memory growth Memo': 4. Off-heap or native memory growth Memory that never returns after a quiet night, even with a full garbage collection, can point to native memory, not heap.
  - [sentence-length] 'Enable native memory tracking (for examp': Enable native memory tracking (for example, CODEREF on the CODEREF) and compare a baseline report against a report taken after growth.
  - [banned-word] 'since': Start with a heap dump comparison on the canary, since it isolates the background leak from the traffic-driven leak.
  - [banned-word] 'confirm': Then compare a normal instance during a campaign to confirm or rule out the traffic-driven leak.

## Warnings

- none

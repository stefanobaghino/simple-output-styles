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
- Styled rate: 0.0 per 100 sentences
- Baseline rate: 8.14 per 100 sentences

| Rule | Styled | Baseline |
|---|---|---|
| latin-abbreviation | 0 | 42 |

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
- Styled rate: 0.25 per 100 sentences
- Baseline rate: 1.55 per 100 sentences

| Rule | Styled | Baseline |
|---|---|---|
| banned-word | 1 | 7 |
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
- Styled rate: 0.34 per 100 sentences
- Baseline rate: 9.3 per 100 sentences

| Rule | Styled | Baseline |
|---|---|---|
| banned-modal | 2 | 4 |
| latin-abbreviation | 0 | 42 |
| minimizer | 0 | 2 |

## plain-language

- Threshold: 5.0 violations per 100 sentences
- Passing pairs: 32/32
- Styled rate: 0.0 per 100 sentences
- Baseline rate: 8.14 per 100 sentences

| Rule | Styled | Baseline |
|---|---|---|
| latin-abbreviation | 0 | 42 |

## technical-simplified

- Threshold: 15.0 violations per 100 sentences
- Passing pairs: 26/32
- Styled rate: 8.93 per 100 sentences
- Baseline rate: 83.14 per 100 sentences

| Rule | Styled | Baseline |
|---|---|---|
| banned-modal | 22 | 42 |
| banned-word | 21 | 65 |
| contraction | 0 | 132 |
| latin-abbreviation | 0 | 42 |
| semicolon | 0 | 19 |
| sentence-length | 13 | 129 |

### Failing pairs

- explanation-08 (rate 20.0):
  - [sentence-length] 'If serialization is only 2% of the reque': If serialization is only 2% of the request time, a binary format will not give a large speedup, but it adds complexity such as schema management and debugging that is harder than CODEREF.
- code-review-07 (rate 18.75):
  - [banned-word] 'detect': Callers cannot detect a network error, a bug, or a validation error.
  - [banned-modal] 'might': What might be deliberate
  - [banned-modal] 'might': The CODEREF on other errors might be an intended fallback.
  - [banned-modal] 'could': If the original team wanted the function to fail silently for use in a place where a crash is worse than a wrong result, this could be on purpose.
  - [sentence-length] 'If the original team wanted the function': If the original team wanted the function to fail silently for use in a place where a crash is worse than a wrong result, this could be on purpose.
  - [banned-modal] 'might': The lack of jitter and the linear backoff might be a simple, early version of retry logic.
  - [banned-modal] 'might': The team might have written this before they added a proper backoff library.
  - [banned-word] 'proper': The team might have written this before they added a proper backoff library.
  - [banned-modal] 'might': The missing final return value might be intended as CODEREF.
- summarization-06 (rate 60.0):
  - [banned-word] 'confirm': The on-call engineer suspects connection-pool exhaustion in the payments client, but the team cannot confirm this because the pool metrics were not kept.
  - [sentence-length] 'The on-call engineer suspects connection': The on-call engineer suspects connection-pool exhaustion in the payments client, but the team cannot confirm this because the pool metrics were not kept.
  - [banned-modal] 'may': A deploy 20 minutes before the incident changed retry settings and may have contributed, but a rollback alone did not restore service.
- summarization-07 (rate 28.57):
  - [banned-modal] 'may': Tail latency may have improved, but we do not know for certain, because staging traffic is smoother than production traffic.
  - [banned-modal] 'may': The kernel version may explain the crash, but we cannot rule out a batcher bug yet.
- summarization-08 (rate 16.67):
  - [banned-modal] 'should': Eight participants are not enough to size this problem, but the abandonment link is a risk that the team should test further.
  - [banned-modal] 'may': 3. Admins and regular users may want different defaults (tentative)
  - [banned-modal] 'could': This could mean that the gallery is hard to find, or that these customers already had templates.
- debugging-07 (rate 25.0):
  - [banned-modal] 'might': Async processing lag: The CODEREF might process events in a queue or background job.
  - [banned-word] 'proper': Shared state between workers: If workers share a database, cache, or event bus without proper isolation, one worker's test data can leak into another test's digest.
  - [sentence-length] 'Shared state between workers: If workers': Shared state between workers: If workers share a database, cache, or event bus without proper isolation, one worker's test data can leak into another test's digest.
  - [sentence-length] 'Time-based cutoff: If the digest filters': Time-based cutoff: If the digest filters events by a timestamp window, and the test seeds events fast, one event can fall outside the window because of clock skew or rounding.
  - [banned-modal] 'would': Resource contention: Four workers on CODEREF can slow down request processing enough to expose the same race that would not appear under low load on a developer machine.
  - [sentence-length] 'Resource contention: Four workers on COD': Resource contention: Four workers on CODEREF can slow down request processing enough to expose the same race that would not appear under low load on a developer machine.
  - [sentence-length] 'Make sure that each worker gets its own ': Make sure that each worker gets its own isolated data (for example, a unique tenant CODEREF or a transaction that rolls back).
  - [banned-word] 'Since': Since CODEREF keeps no artifacts, add print statements or structured logs to the test and to the digest endpoint.

## Warnings

- none

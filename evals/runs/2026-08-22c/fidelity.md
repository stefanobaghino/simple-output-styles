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
- Styled rate: 0.19 per 100 sentences
- Baseline rate: 8.84 per 100 sentences

| Rule | Styled | Baseline |
|---|---|---|
| latin-abbreviation | 1 | 39 |

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
- Styled rate: 0.0 per 100 sentences
- Baseline rate: 0.91 per 100 sentences

| Rule | Styled | Baseline |
|---|---|---|
| banned-word | 0 | 3 |
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
- Styled rate: 0.33 per 100 sentences
- Baseline rate: 10.43 per 100 sentences

| Rule | Styled | Baseline |
|---|---|---|
| banned-modal | 2 | 6 |
| latin-abbreviation | 0 | 39 |
| minimizer | 0 | 1 |

## plain-language

- Threshold: 5.0 violations per 100 sentences
- Passing pairs: 32/32
- Styled rate: 0.0 per 100 sentences
- Baseline rate: 8.84 per 100 sentences

| Rule | Styled | Baseline |
|---|---|---|
| latin-abbreviation | 0 | 39 |

## technical-simplified

- Threshold: 15.0 violations per 100 sentences
- Passing pairs: 26/32
- Styled rate: 6.94 per 100 sentences
- Baseline rate: 83.22 per 100 sentences

| Rule | Styled | Baseline |
|---|---|---|
| banned-modal | 10 | 37 |
| banned-word | 19 | 66 |
| contraction | 0 | 122 |
| latin-abbreviation | 0 | 39 |
| semicolon | 0 | 10 |
| sentence-length | 10 | 93 |

### Failing pairs

- explanation-08 (rate 21.05):
  - [banned-word] 'reduce': A binary format such as Protocol Buffers or MessagePack can reduce payload size and cut CODEREF time for encoding and decoding.
  - [banned-modal] 'would': How large the CODEREF payloads are today, and how much a binary format would reduce them.
  - [banned-word] 'reduce': How large the CODEREF payloads are today, and how much a binary format would reduce them.
  - [banned-word] 'main': Record the average and maximum payload sizes for your main endpoints.
- code-review-08 (rate 16.36):
  - [banned-word] 'follows': CODEREF follows symlinks.
  - [sentence-length] 'If a symlink points outside CODEREF, COD': If a symlink points outside CODEREF, CODEREF deletes the link itself, but the mtime check that decided this is based on the target's time, not the link's.
  - [banned-modal] 'would': There is no way to preview what this would delete before it runs for real.
  - [banned-modal] 'could': It could be a deliberate retention policy (for example, a compliance or storage-cost rule), or it could be an arbitrary guess.
  - [banned-modal] 'could': It could be a deliberate retention policy (for example, a compliance or storage-cost rule), or it could be an arbitrary guess.
  - [banned-word] 'confirm': Without a source, treat it as unclear and confirm with whoever owns data retention before you change it.
  - [sentence-length] 'But because it only applies to the age-b': But because it only applies to the age-based branch and not the pattern-based branch, the cap does not do its job for CODEREF/CODEREF files.
  - [banned-word] 'Confirm': Confirm whether producers ever write these names for output that is not disposable.
  - [banned-word] 'confirm': Tell me if you want a fixed version, and I will confirm the intended behavior for each point above first.
- summarization-06 (rate 20.0):
  - [banned-word] 'retained': The on-call engineer suspects connection-pool exhaustion in the payments client, but the pool metrics were not retained, so this cause is unconfirmed.
- summarization-07 (rate 20.0):
  - [banned-modal] 'may': First, tail latency (p99) may have improved, but staging traffic is smoother than production traffic.
  - [banned-modal] 'might': The crash might come from the newer kernel on staging, but we cannot rule out a batcher bug yet.
- summarization-08 (rate 21.05):
  - [banned-modal] 'may': Finding 2 — Tentative: The progress bar may cause customers to abandon large imports
  - [banned-modal] 'may': Finding 3 — Tentative: Admins and regular users may need different defaults
  - [banned-word] 'confirm': This finding is tentative and needs a larger study to confirm.
  - [banned-word] 'main': Additional note (not a main finding)
- debugging-06 (rate 16.22):
  - [sentence-length] 'The fact that the failure does not happe': The fact that the failure does not happen at the same batch number each time points to a load-based cause, not a fixed data problem.
  - [sentence-length] 'Log the pool size, the number of active ': Log the pool size, the number of active connections, and the number of waiting requests at the time of each request.
  - [sentence-length] "Search the export job's code for a datab": Search the export job's code for a database connection that is not released in a CODEREF block or an equivalent context manager.
  - [banned-word] 'exceed': If workers can exceed the pool size, this is the most direct cause.
  - [banned-word] 'Since': Since the rotated context is gone, add persistent logs of pool state and slow-query alerts, so that the next failure includes the surrounding data.
  - [sentence-length] 'If you can share the pool configuration ': If you can share the pool configuration or the code that gets and releases connections, I can review it for a leak or a misconfigured pool size.

## Warnings

- none

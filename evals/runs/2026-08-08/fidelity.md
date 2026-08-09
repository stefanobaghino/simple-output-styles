# Fidelity report

A pair passes the gate when its styled answer has at least one
sentence and a violation rate at or below the threshold of its
style. The baseline columns check the unstyled answers with the
same rules; the baseline carries no mark, because the unstyled
answers are not supposed to obey a style. The judged measurements
read only the passing pairs.

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
- Styled rate: 0.5 per 100 sentences
- Baseline rate: 1.55 per 100 sentences

| Rule | Styled | Baseline |
|---|---|---|
| banned-word | 2 | 6 |
| needless-phrase | 0 | 1 |

## developer-docs

- Threshold: 10.0 violations per 100 sentences
- Passing pairs: 32/32
- Styled rate: 0.0 per 100 sentences
- Baseline rate: 6.42 per 100 sentences

| Rule | Styled | Baseline |
|---|---|---|
| banned-modal | 0 | 3 |
| latin-abbreviation | 0 | 25 |
| minimizer | 0 | 1 |

## plain-language

- Threshold: 5.0 violations per 100 sentences
- Passing pairs: 32/32
- Styled rate: 0.0 per 100 sentences
- Baseline rate: 5.53 per 100 sentences

| Rule | Styled | Baseline |
|---|---|---|
| latin-abbreviation | 0 | 25 |

## technical-simplified

- Threshold: 15.0 violations per 100 sentences
- Passing pairs: 30/32
- Styled rate: 5.24 per 100 sentences
- Baseline rate: 80.09 per 100 sentences

| Rule | Styled | Baseline |
|---|---|---|
| banned-modal | 4 | 38 |
| banned-word | 15 | 78 |
| contraction | 0 | 113 |
| latin-abbreviation | 0 | 25 |
| semicolon | 0 | 8 |
| sentence-length | 11 | 100 |

### Failing pairs

- summarization-07 (rate 25.0):
  - [sentence-length] 'Tail latency also seemed better, but thi': Tail latency also seemed better, but this result is less certain, because staging traffic is smoother than production traffic, so the p99 numbers are probably too optimistic.
  - [banned-modal] 'could': Staging uses a newer kernel than production, so the kernel could explain the crash, but a bug in the batcher is also possible.
- debugging-07 (rate 20.0):
  - [sentence-length] 'If the digest groups events by a boundar': If the digest groups events by a boundary such as CODEREF or CODEREF, a delay under load can push one event's timestamp outside the window.
  - [sentence-length] 'If the test does not check the response ': If the test does not check the response status of each event-creation call, a rejected write under connection or lock pressure from four workers can pass unnoticed.
  - [sentence-length] 'If the event CODEREF or grouping key use': If the event CODEREF or grouping key uses a low-resolution timestamp, two events created close together under load can collide, and one write overwrites the other.
  - [sentence-length] 'Run this single test 100 to 200 times wi': Run this single test 100 to 200 times with four workers, then run it the same number of times with one worker.
  - [banned-word] 'Confirm': Confirm that each worker uses a separate database or schema, not a shared file or table.
  - [banned-word] 'confirms': If the failure rate drops to zero, this confirms a race between write and read.

## Warnings

- none

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
- Baseline rate: 8.22 per 100 sentences

| Rule | Styled | Baseline |
|---|---|---|
| latin-abbreviation | 0 | 41 |

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
- Styled rate: 0.48 per 100 sentences
- Baseline rate: 1.6 per 100 sentences

| Rule | Styled | Baseline |
|---|---|---|
| banned-word | 2 | 7 |
| needless-phrase | 0 | 1 |

## developer-docs

- Threshold: 10.0 violations per 100 sentences
- Passing pairs: 32/32
- Styled rate: 0.16 per 100 sentences
- Baseline rate: 9.62 per 100 sentences

| Rule | Styled | Baseline |
|---|---|---|
| banned-modal | 0 | 6 |
| latin-abbreviation | 0 | 41 |
| minimizer | 1 | 1 |

## plain-language

- Threshold: 5.0 violations per 100 sentences
- Passing pairs: 32/32
- Styled rate: 0.0 per 100 sentences
- Baseline rate: 8.22 per 100 sentences

| Rule | Styled | Baseline |
|---|---|---|
| latin-abbreviation | 0 | 41 |

## technical-simplified

- Threshold: 15.0 violations per 100 sentences
- Passing pairs: 27/32
- Styled rate: 7.81 per 100 sentences
- Baseline rate: 85.57 per 100 sentences

| Rule | Styled | Baseline |
|---|---|---|
| banned-modal | 5 | 47 |
| banned-word | 17 | 74 |
| contraction | 0 | 131 |
| latin-abbreviation | 0 | 41 |
| semicolon | 0 | 22 |
| sentence-length | 20 | 112 |

### Failing pairs

- explanation-01 (rate 17.65):
  - [banned-word] 'follows': To find a key, the hash map starts at the index, then follows the same probe sequence until it finds the key or an empty slot.
  - [sentence-length] 'To find a key, the hash map starts at th': To find a key, the hash map starts at the index, then follows the same probe sequence until it finds the key or an empty slot.
  - [sentence-length] 'Chaining is simple and tolerates a high ': Chaining is simple and tolerates a high load factor, but each list adds memory overhead and can hurt cache performance, because list nodes are not next to each other in memory.
- summarization-06 (rate 40.0):
  - [banned-word] 'confirmed': The on-call engineer suspects connection-pool exhaustion in the payments client, but the pool metrics were not saved, so this cause is not confirmed.
  - [banned-modal] 'might': A deploy 20 minutes before the incident changed retry settings and might have contributed, but a rollback alone did not restore service.
- summarization-08 (rate 16.67):
  - [banned-modal] 'may': Finding 3 — Tentative: The template gallery may have low visibility
  - [banned-word] 'confirm': The current data cannot confirm either explanation.
  - [banned-word] 'main': Open question, not a main finding
- debugging-04 (rate 50.0):
  - [banned-word] 'detect': Fix: open the file with an encoding that matches its actual content, or detect the encoding automatically.
  - [banned-word] 'Detect': Detect the encoding with a library such as CODEREF before you open the file.
  - [banned-word] 'since': Open the file in binary mode (CODEREF) if you only need to count lines, since line counting does not need decoding:
  - [sentence-length] 'Open the file in binary mode (CODEREF) i': Open the file in binary mode (CODEREF) if you only need to count lines, since line counting does not need decoding:
  - [banned-word] 'avoids': This last option avoids decoding errors completely, because you count raw lines instead of decoded text.
- debugging-07 (rate 25.0):
  - [sentence-length] '2. Eventual consistency in the digest pi': 2. Eventual consistency in the digest pipeline If events go through a queue or a background job before they appear in the digest, the test can query the digest before the third event finishes processing.
  - [sentence-length] '4. Time-window logic If the digest selec': 4. Time-window logic If the digest selects events by timestamp, low clock resolution or the same timestamp on two events under a busy CODEREF host can push one event out of the query window.
  - [banned-word] 'Since': Since CODEREF does not keep artifacts, print this data to stdout so it lands in the CODEREF log.
  - [sentence-length] 'Search the test setup and fixtures for a': Search the test setup and fixtures for any shared resource: a single database file, a fixed user CODEREF, a global counter, or a shared queue name.
  - [banned-word] 'Confirm': Confirm that each worker gets its own instance.
  - [sentence-length] 'Use a repeat plugin (for example, pytest': Use a repeat plugin (for example, pytest-repeat) together with parallel workers to raise the failure rate from 1-in-10 to something you can debug directly, instead of waiting on CODEREF.
  - [sentence-length] 'If the failure reproduces locally under ': If the failure reproduces locally under parallel load, you can add the diagnostic logging from step 2 and get an answer in a few runs instead of waiting on CODEREF.

## Warnings

- none

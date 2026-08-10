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
- Baseline rate: 5.47 per 100 sentences

| Rule | Styled | Baseline |
|---|---|---|
| latin-abbreviation | 0 | 26 |

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
- Baseline rate: 1.26 per 100 sentences

| Rule | Styled | Baseline |
|---|---|---|
| banned-word | 2 | 6 |

## developer-docs

- Threshold: 10.0 violations per 100 sentences
- Passing pairs: 32/32
- Styled rate: 0.51 per 100 sentences
- Baseline rate: 6.32 per 100 sentences

| Rule | Styled | Baseline |
|---|---|---|
| banned-modal | 2 | 3 |
| latin-abbreviation | 0 | 26 |
| minimizer | 1 | 1 |

## plain-language

- Threshold: 5.0 violations per 100 sentences
- Passing pairs: 32/32
- Styled rate: 0.0 per 100 sentences
- Baseline rate: 5.47 per 100 sentences

| Rule | Styled | Baseline |
|---|---|---|
| latin-abbreviation | 0 | 26 |

## technical-simplified

- Threshold: 15.0 violations per 100 sentences
- Passing pairs: 26/32
- Styled rate: 9.04 per 100 sentences
- Baseline rate: 76.21 per 100 sentences

| Rule | Styled | Baseline |
|---|---|---|
| banned-modal | 5 | 42 |
| banned-word | 31 | 65 |
| contraction | 0 | 99 |
| latin-abbreviation | 0 | 26 |
| semicolon | 0 | 26 |
| sentence-length | 17 | 104 |

### Failing pairs

- explanation-08 (rate 15.79):
  - [banned-word] 'reduce': If serialization is 5% of the request time, a binary format can only reduce the total by a small amount, even if serialization becomes 10 times faster.
  - [banned-word] 'amount': If serialization is 5% of the request time, a binary format can only reduce the total by a small amount, even if serialization becomes 10 times faster.
  - [sentence-length] 'If serialization is 5% of the request ti': If serialization is 5% of the request time, a binary format can only reduce the total by a small amount, even if serialization becomes 10 times faster.
- code-review-03 (rate 15.38):
  - [banned-word] 'major': This function has one major problem and two minor problems.
  - [banned-word] 'Major': Major problem: CODEREF injection
- code-review-06 (rate 15.62):
  - [sentence-length] 'If CODEREF has a dict at a key and CODER': If CODEREF has a dict at a key and CODEREF gives a non-dict value for that same key, the function calls CODEREF on a non-dict CODEREF.
  - [banned-word] 'as': When both sides hold a dict, a CODEREF in the nested CODEREF deletes the key, as designed.
  - [banned-word] 'since': Anyone who calls this function must know this rule, since nothing states it.
  - [sentence-length] 'Recommendation: Add CODEREF to the recur': Recommendation: Add CODEREF to the recursion check to fix bug 2, and change the shallow copy to a deep copy (or document that the result shares references with the inputs) to fix bugs 1 and 4.
  - [banned-word] 'since': Then write a short docstring that states the CODEREF-deletes rule, since that behavior is not obvious from the code.
- summarization-07 (rate 42.86):
  - [banned-word] 'following': We do not have strong evidence for the following points, so they are still guesses.
  - [banned-modal] 'may': Tail latency (p99) may have improved, but staging traffic is smoother than production traffic, so the p99 numbers can be too optimistic.
  - [banned-modal] 'might': The crash might be unrelated to the batcher, because staging runs a newer kernel, but we cannot rule out a batcher bug yet.
- debugging-07 (rate 34.29):
  - [sentence-length] 'Under load from four parallel workers, t': Under load from four parallel workers, the shared resource (database, message queue, cache) sees more contention, so the delay grows past the test's wait window.
  - [sentence-length] 'If workers share a database, event bus, ': If workers share a database, event bus, or fixed IDs, one worker's cleanup or teardown can delete or overwrite events from another worker's test.
  - [sentence-length] 'If the digest groups events by a timesta': If the digest groups events by a timestamp window and two events land in the same millisecond, or the digest applies a limit or dedupe rule, extra concurrent traffic from other workers can shift event timestamps or IDs so that one event falls outside the window.
  - [sentence-length] 'With four workers, the app can run out o': With four workers, the app can run out of database connections or hit a transaction isolation level that lets the digest read run against a snapshot that misses the last write.
  - [banned-word] 'confirm': If the test fails locally under four workers, you confirm parallelism is the trigger and do not need CODEREF at all.
  - [banned-word] 'since': Even though the runner does not keep artifacts by default, add a targeted log dump on failure: print the raw digest response and the seed event IDs to stdout, since stdout is captured by CODEREF even without a separate artifact store.
  - [sentence-length] 'Even though the runner does not keep art': Even though the runner does not keep artifacts by default, add a targeted log dump on failure: print the raw digest response and the seed event IDs to stdout, since stdout is captured by CODEREF even without a separate artifact store.
  - [banned-word] 'confirms': If the flake stops, this confirms cross-worker interference and rules out a pure timing issue within one worker.
  - [banned-word] 'confirm': Run locally with 4 workers to confirm parallelism triggers the flake.
  - [banned-word] 'confirmed': If confirmed, isolate the test to one worker group to check for cross-test interference.
  - [banned-word] 'confirmed': If not confirmed, add the poll-and-log wrapper to catch a timing race in CODEREF, since the runner keeps no artifacts.
  - [banned-word] 'since': If not confirmed, add the poll-and-log wrapper to catch a timing race in CODEREF, since the runner keeps no artifacts.
- debugging-08 (rate 17.86):
  - [sentence-length] 'If the canary growth rate is a fixed fra': If the canary growth rate is a fixed fraction of the busy instance, the leak likely has two sources: one per-request, one time-based (for example, a scheduled job or a metrics buffer).
  - [sentence-length] 'The size-bounded cache does not evict co': The size-bounded cache does not evict correctly The cache bound has not changed, but a bounded cache can still leak if the eviction logic is wrong, for example if entries are large objects with references that survive eviction, or if the bound counts entries and not bytes, or if the eviction policy fails on certain key patterns.
  - [banned-word] 'Retained': Retained request or response objects If webhook payloads or product data get attached to long-lived objects, for example a logger, a metrics collector, or an event bus, they never free the memory.
  - [sentence-length] 'Retained request or response objects If ': Retained request or response objects If webhook payloads or product data get attached to long-lived objects, for example a logger, a metrics collector, or an event bus, they never free the memory.
  - [sentence-length] 'Set up a lightweight heap dump on a sche': Set up a lightweight heap dump on a schedule, or use a memory profiler that can run in production with low cost, for example CODEREF for Go or the CODEREF flag for CODEREF.

## Warnings

- none

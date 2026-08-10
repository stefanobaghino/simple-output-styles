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
- Styled rate: 0.49 per 100 sentences
- Baseline rate: 0.87 per 100 sentences

| Rule | Styled | Baseline |
|---|---|---|
| banned-word | 2 | 4 |

## developer-docs

- Threshold: 10.0 violations per 100 sentences
- Passing pairs: 32/32
- Styled rate: 0.5 per 100 sentences
- Baseline rate: 11.14 per 100 sentences

| Rule | Styled | Baseline |
|---|---|---|
| banned-modal | 1 | 8 |
| latin-abbreviation | 0 | 41 |
| minimizer | 2 | 2 |

## plain-language

- Threshold: 5.0 violations per 100 sentences
- Passing pairs: 32/32
- Styled rate: 0.0 per 100 sentences
- Baseline rate: 8.95 per 100 sentences

| Rule | Styled | Baseline |
|---|---|---|
| latin-abbreviation | 0 | 41 |

## technical-simplified

- Threshold: 15.0 violations per 100 sentences
- Passing pairs: 27/32
- Styled rate: 6.87 per 100 sentences
- Baseline rate: 83.62 per 100 sentences

| Rule | Styled | Baseline |
|---|---|---|
| banned-modal | 4 | 35 |
| banned-word | 24 | 66 |
| contraction | 0 | 132 |
| latin-abbreviation | 0 | 41 |
| semicolon | 0 | 16 |
| sentence-length | 13 | 93 |

### Failing pairs

- debugging-08 (rate 25.0):
  - [sentence-length] 'Common sources: event listeners that are': Common sources: event listeners that are added but never removed, timers or intervals that are not cleared, or per-request objects that stay in a global list or map.
  - [banned-word] 'confirmed': You confirmed that the product-data cache has a fixed bound and did not change.
  - [sentence-length] 'But that does not rule out a different c': But that does not rule out a different cache, such as a session cache, a response cache, or a memoization map, that has no bound or a bound that does not free memory correctly.
  - [banned-word] 'confirm': For each one, confirm it has a max-size check and a working eviction step.
  - [sentence-length] 'Frequent eviction of variable-size objec': Frequent eviction of variable-size objects can leave gaps that the memory allocator cannot reuse well, so the process memory grows even when live data does not.
  - [banned-word] 'Confirm': Confirm or rule out the product-data cache first, since you already have a lead: check its eviction logic under load, not just its size bound.
  - [banned-word] 'since': Confirm or rule out the product-data cache first, since you already have a lead: check its eviction logic under load, not just its size bound.
  - [sentence-length] 'Confirm or rule out the product-data cac': Confirm or rule out the product-data cache first, since you already have a lead: check its eviction logic under load, not just its size bound.
  - [banned-word] 'since': Run the canary heap-snapshot comparison next, since it isolates the leak from webhook traffic.
- summarization-08 (rate 21.43):
  - [banned-word] 'main': Three main findings
  - [banned-modal] 'may': Tentative — The progress bar may cause customers to abandon large imports.
  - [banned-modal] 'may': Tentative — Admins and regular users may want different default settings.
- summarization-06 (rate 20.0):
  - [banned-word] 'confirm': Error rates recovered after a restart, but this result does not confirm one specific cause.
- code-review-06 (rate 16.67):
  - [banned-word] 'confirmed': This must be documented and confirmed with the team.
  - [banned-word] 'Confirm': Confirm three points with the team, or through the codebase that calls this function:
  - [banned-word] 'Confirm': Confirm that CODEREF must delete a key, not set the value to CODEREF.
  - [banned-word] 'Confirm': Confirm that lists must replace, not merge.
  - [banned-word] 'Confirm': Confirm that a scalar override for a dict key must silently win, not raise an error.
  - [banned-word] 'confirmed': Once these three points are confirmed, add tests for them and a short docstring before you refactor the function further.
- debugging-07 (rate 23.08):
  - [sentence-length] '2. Shared test data across workers If wo': 2. Shared test data across workers If workers share one database, or the test uses a fixed user CODEREF or fixed event CODEREF, another test running at the same time can overwrite or delete an event before the digest read.
  - [sentence-length] 'A time window in the digest query The di': A time window in the digest query The digest can filter events by a time window, for example CODEREF Under load, the third event can land after the window closes.
  - [sentence-length] 'A limit or sort in the digest query If t': A limit or sort in the digest query If the digest query uses CODEREF and CODEREF with a sort field that ties under load, for example a timestamp with low precision, the query can return the wrong three events or drop one.
  - [sentence-length] 'Find out if it returns only after the ev': Find out if it returns only after the event is fully processed, or if it just queues the event for later work.
  - [banned-word] 'confirms': If the flake rate drops to zero, this confirms cause 1.
  - [sentence-length] 'The parallelism is almost certainly rele': The parallelism is almost certainly relevant here: it adds load that slows processing and makes race conditions visible, even when the underlying code path is the same as on a developer machine.

## Warnings

- none

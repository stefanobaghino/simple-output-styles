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
- Styled rate: 0.26 per 100 sentences
- Baseline rate: 0.67 per 100 sentences

| Rule | Styled | Baseline |
|---|---|---|
| banned-word | 1 | 2 |
| needless-phrase | 0 | 1 |

## developer-docs

- Threshold: 10.0 violations per 100 sentences
- Passing pairs: 32/32
- Styled rate: 0.17 per 100 sentences
- Baseline rate: 9.6 per 100 sentences

| Rule | Styled | Baseline |
|---|---|---|
| banned-modal | 0 | 6 |
| latin-abbreviation | 0 | 34 |
| minimizer | 1 | 3 |

## plain-language

- Threshold: 5.0 violations per 100 sentences
- Passing pairs: 32/32
- Styled rate: 0.14 per 100 sentences
- Baseline rate: 7.59 per 100 sentences

| Rule | Styled | Baseline |
|---|---|---|
| latin-abbreviation | 1 | 34 |

## technical-simplified

- Threshold: 15.0 violations per 100 sentences
- Passing pairs: 29/32
- Styled rate: 7.26 per 100 sentences
- Baseline rate: 81.92 per 100 sentences

| Rule | Styled | Baseline |
|---|---|---|
| banned-modal | 12 | 44 |
| banned-word | 18 | 70 |
| contraction | 0 | 115 |
| latin-abbreviation | 0 | 34 |
| semicolon | 0 | 14 |
| sentence-length | 16 | 90 |

### Failing pairs

- explanation-01 (rate 21.74):
  - [banned-word] 'follows': To find a value, the map computes the index, then it follows the same probe sequence until it finds the matching key or an empty slot.
  - [sentence-length] 'To find a value, the map computes the in': To find a value, the map computes the index, then it follows the same probe sequence until it finds the matching key or an empty slot.
  - [banned-word] 'avoids': Trade-off: Open addressing avoids extra lists, so it uses less memory and it can be faster when the map is not full.
  - [banned-word] 'as': But performance drops fast as the map fills up, because probes become longer.
  - [banned-word] 'as': Open addressing: memory-efficient and fast when the map has free space, but performance drops as the map fills up, and removal is more complex.
- summarization-06 (rate 20.0):
  - [banned-modal] 'may': A deploy 20 minutes before the incident changed retry settings and may have contributed, but rollback alone did not restore service.
- summarization-08 (rate 33.33):
  - [banned-word] 'main': Here are the three main findings from the eight interviews.
  - [banned-modal] 'may': The uploads did finish, so the stuck look may be only a display problem.
  - [banned-modal] 'may': 3. Admins and regular users may want different default settings.
  - [banned-modal] 'should': The product team should test this with a larger group before it builds separate defaults.
  - [banned-word] 'main': Note (not a main finding): No user opened the new template gallery.
  - [banned-modal] 'could': This could mean that the gallery is hard to find, or that these customers already had templates and did not need it.
  - [banned-modal] 'should': The team should test discoverability with new customers who have no existing templates.

## Warnings

- none

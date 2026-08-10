# Fidelity report

**Screening run.** This run covers 8 of 32 prompts, as one
run instead of 3. By design, the generation calls are about
8% of a full campaign, and the judge calls are about 25%
of one full run.
The subset holds 2 hedge-rich prompts, mirroring the
hedge-rich share of the full set.
Measured against the baseline campaign
(runs/2026-08-08 and runs/2026-08-08b), a screening run holds about
25% of the calls and about 25% of the
weighted input tokens of one full run, plus the full cost
probe, which is per style and does not shrink.
The error bars are wider than in a full run,
because fewer contests feed the bootstrap intervals.
`style-compare` rejects a comparison of this run with a full run.

A pair passes the gate when its styled answer has at least one
sentence and a violation rate at or below the threshold of its
style. The baseline columns check the unstyled answers with the
same rules; the baseline carries no mark, because the unstyled
answers are not supposed to obey a style. The judged measurements
read only the passing pairs.

## actionable-clarity

- Threshold: 5.0 violations per 100 sentences
- Passing pairs: 8/8
- Styled rate: 0.0 per 100 sentences
- Baseline rate: 10.22 per 100 sentences

| Rule | Styled | Baseline |
|---|---|---|
| latin-abbreviation | 0 | 14 |

## clarity-flow

- Threshold: 5.0 violations per 100 sentences
- Passing pairs: 8/8
- Styled rate: 0.0 per 100 sentences
- Baseline rate: 0.0 per 100 sentences

| Rule | Styled | Baseline |
|---|---|---|
| none | 0 | 0 |

## classic-concise

- Threshold: 10.0 violations per 100 sentences
- Passing pairs: 8/8
- Styled rate: 0.0 per 100 sentences
- Baseline rate: 0.0 per 100 sentences

| Rule | Styled | Baseline |
|---|---|---|
| none | 0 | 0 |

## developer-docs

- Threshold: 10.0 violations per 100 sentences
- Passing pairs: 8/8
- Styled rate: 0.0 per 100 sentences
- Baseline rate: 12.41 per 100 sentences

| Rule | Styled | Baseline |
|---|---|---|
| latin-abbreviation | 0 | 14 |
| minimizer | 0 | 3 |

## plain-language

- Threshold: 5.0 violations per 100 sentences
- Passing pairs: 8/8
- Styled rate: 0.0 per 100 sentences
- Baseline rate: 10.22 per 100 sentences

| Rule | Styled | Baseline |
|---|---|---|
| latin-abbreviation | 0 | 14 |

## technical-simplified

- Threshold: 15.0 violations per 100 sentences
- Passing pairs: 6/8
- Styled rate: 9.8 per 100 sentences
- Baseline rate: 91.24 per 100 sentences

| Rule | Styled | Baseline |
|---|---|---|
| banned-modal | 1 | 11 |
| banned-word | 5 | 26 |
| contraction | 0 | 33 |
| latin-abbreviation | 0 | 14 |
| semicolon | 0 | 7 |
| sentence-length | 4 | 34 |

### Failing pairs

- explanation-03 (rate 19.05):
  - [banned-word] 'amount': After each round trip, if the packets arrive without loss, the sender doubles the amount of data it sends.
  - [banned-word] 'amount': This is the amount of data that a sender can have in transit before it must wait for confirmation.
  - [banned-word] 'begins': Slow start begins with a small cwnd, often equal to a few packets.
  - [sentence-length] 'This method lets CODEREF find a good sen': This method lets CODEREF find a good sending speed fast, but it prevents a new connection from overloading the network on its first burst of data.
- summarization-08 (rate 18.75):
  - [banned-word] 'confirmed': The exact cause is not confirmed.
  - [banned-modal] 'may': Finding 3 — Admins and regular users may need different defaults (tentative).
  - [banned-word] 'main': Extra note (not a main finding): Nobody used the new template gallery.

## Warnings

- none

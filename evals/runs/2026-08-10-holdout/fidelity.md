# Fidelity report

A pair passes the gate when its styled answer has at least one
sentence and a violation rate at or below the threshold of its
style. The baseline columns check the unstyled answers with the
same rules; the baseline carries no mark, because the unstyled
answers are not supposed to obey a style. The judged measurements
read only the passing pairs.

## actionable-clarity

- Threshold: 5.0 violations per 100 sentences
- Passing pairs: 23/24
- Styled rate: 0.41 per 100 sentences
- Baseline rate: 4.61 per 100 sentences

| Rule | Styled | Baseline |
|---|---|---|
| latin-abbreviation | 2 | 16 |

### Failing pairs

- code-review-h06 (rate 6.45):
  - [latin-abbreviation] 'e.g.': Bare CODEREF swallows every failure mode: missing file, bad permissions, malformed CODEREF, or a CODEREF file that isn't even an object (e.g., a list, where CODEREF raises). Callers get silent defaults with no way to tell whether their config actually loaded. This may be a deliberate CODEREF choice, but swallowing all exceptions (not just CODEREF/CODEREF) and giving no log or warning goes further than that intent likely required.
  - [latin-abbreviation] 'e.g.': No feedback on partial success. If the file loads but CODEREF returns something that isn't a dict (e.g., CODEREF), CODEREF raises, gets caught by the blanket CODEREF, and the caller silently gets all-defaults with zero indication the file was malformed. This compounds the first CODEREF issue.

## clarity-flow

- Threshold: 5.0 violations per 100 sentences
- Passing pairs: 24/24
- Styled rate: 0.0 per 100 sentences
- Baseline rate: 0.0 per 100 sentences

| Rule | Styled | Baseline |
|---|---|---|
| none | 0 | 0 |

## classic-concise

- Threshold: 10.0 violations per 100 sentences
- Passing pairs: 24/24
- Styled rate: 0.3 per 100 sentences
- Baseline rate: 1.44 per 100 sentences

| Rule | Styled | Baseline |
|---|---|---|
| banned-word | 1 | 5 |

## developer-docs

- Threshold: 10.0 violations per 100 sentences
- Passing pairs: 24/24
- Styled rate: 0.22 per 100 sentences
- Baseline rate: 6.92 per 100 sentences

| Rule | Styled | Baseline |
|---|---|---|
| banned-modal | 0 | 7 |
| latin-abbreviation | 1 | 16 |
| minimizer | 0 | 1 |

## plain-language

- Threshold: 5.0 violations per 100 sentences
- Passing pairs: 24/24
- Styled rate: 0.0 per 100 sentences
- Baseline rate: 4.61 per 100 sentences

| Rule | Styled | Baseline |
|---|---|---|
| latin-abbreviation | 0 | 16 |

## technical-simplified

- Threshold: 15.0 violations per 100 sentences
- Passing pairs: 21/24
- Styled rate: 6.52 per 100 sentences
- Baseline rate: 74.35 per 100 sentences

| Rule | Styled | Baseline |
|---|---|---|
| banned-modal | 4 | 26 |
| banned-word | 18 | 56 |
| contraction | 0 | 77 |
| latin-abbreviation | 0 | 16 |
| semicolon | 1 | 16 |
| sentence-length | 12 | 67 |

### Failing pairs

- summarization-h03 (rate 21.43):
  - [banned-word] 'Confirm': Confirm the backlog.
  - [banned-word] 'Confirmed': Command: CODEREF Confirmed if the value is above 50000.
  - [banned-word] 'as': Note: Record every action in the incident channel as you do it.
- code-review-h06 (rate 15.52):
  - [banned-word] 'as': A malformed CODEREF file, a permissions error, or a directory passed as CODEREF all fail the same silent way.
  - [banned-modal] 'might': This might be deliberate, to limit the override surface to known settings, but it is not documented, so a caller cannot rely on this behavior.
  - [sentence-length] 'This might be deliberate, to limit the o': This might be deliberate, to limit the override surface to known settings, but it is not documented, so a caller cannot rely on this behavior.
  - [banned-word] 'confirm': We cannot see the callers, so we cannot confirm this risk, but it is worth a check.
  - [sentence-length] 'If a caller has a config key with mixed ': If a caller has a config key with mixed case or an underscore, such as CODEREF, the resulting environment variable name (CODEREF) is easy to get wrong.
  - [banned-modal] 'might': This might be deliberate as a simple convention, but it needs documentation.
  - [banned-modal] 'might': This might be deliberate, to allow per-service defaults, but the silent failure in rule 1 hides mistakes here too.
  - [banned-word] 'confirm': If you confirm both, you can add explicit type coercion for environment overrides and replace the bare CODEREF with a logged, narrow exception type, without breaking existing callers.
  - [sentence-length] 'If you confirm both, you can add explici': If you confirm both, you can add explicit type coercion for environment overrides and replace the bare CODEREF with a logged, narrow exception type, without breaking existing callers.
- summarization-h06 (rate 71.43):
  - [banned-word] 'Confirmed': Confirmed:
  - [banned-word] 'confirmed': We locked both accounts Sunday evening, and both owners confirmed that they did not log in.
  - [sentence-length] 'We suspect that the successful logins us': We suspect that the successful logins used credential stuffing and that the CODEREF range belongs to a known botnet, but the authentication logs lack detail to prove the stuffing, and the botnet claim rests on an unverified third-party feed.
  - [banned-word] 'confirmed': We have no confirmed evidence that data left either account, but audit coverage of the export endpoints is partial, and we cannot rule out a small, unnoticed export.
  - [sentence-length] 'We have no confirmed evidence that data ': We have no confirmed evidence that data left either account, but audit coverage of the export endpoints is partial, and we cannot rule out a small, unnoticed export.

## Warnings

- none

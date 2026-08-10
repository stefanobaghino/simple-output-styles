# Cross-run comparison

The comparison reads the stored artifacts of several runs with identical conditions. Per style and axis, the table states one value per run and the spread: minimum, mean, maximum, and the sample standard deviation. The spread is the error bar of the harness: it shows how much a verdict moves on a resample. Net wins is wins minus losses, and n counts the runs that hold a value for the axis.

Runs: 2026-08-10d, 2026-08-10e, 2026-08-10f, 2026-08-10g, 2026-08-10h, 2026-08-10i.

## actionable-clarity

| Axis | 2026-08-10d | 2026-08-10e | 2026-08-10f | 2026-08-10g | 2026-08-10h | 2026-08-10i | n | Min | Mean | Max | Stdev |
|---|---|---|---|---|---|---|---|---|---|---|---|
| fidelity: styled violation rate | 0.17 | 0.68 | 0.0 | 0.16 | 0.67 | 0.0 | 6 | 0.0 | 0.28 | 0.68 | 0.315 |
| fidelity: gated pairs passed | 32 | 31 | 32 | 32 | 30 | 32 | 6 | 30 | 31.5 | 32 | 0.837 |
| cost: output-token ratio | 1.36 | 1.2 | 1.0 | 1.32 | 1.01 | 1.2 | 6 | 1.0 | 1.182 | 1.36 | 0.151 |
| value: net wins (comprehension) | 4 | 2 | 11 | 3 | -1 | 6 | 6 | -1 | 4.167 | 11 | 4.07 |
| value: net wins (paraphrase) | 3 | 6 | 1 | 11 | 13 | 3 | 6 | 1 | 6.167 | 13 | 4.834 |
| value: net wins (roundtrip) | 6 | 14 | -2 | 5 | 5 | 8 | 6 | -2 | 6.0 | 14 | 5.177 |
| loss: fact survival median | 0.806 | 0.8 | 0.758 | 0.808 | 0.805 | 0.769 | 6 | 0.758 | 0.791 | 0.808 | 0.022 |
| loss: hedge survival median | 1.0 | 1.0 | 0.938 | 0.75 | 1.0 | 0.8 | 6 | 0.75 | 0.915 | 1.0 | 0.112 |
| rank: Bradley-Terry strength | 2.933 | 2.211 | 2.158 | 3.144 | 2.12 | 1.975 | 6 | 1.975 | 2.424 | 3.144 | 0.487 |
| rank: net wins vs unstyled | 18 | 11 | 7 | 16 | 6 | 11 | 6 | 6 | 11.5 | 18 | 4.764 |

## clarity-flow

| Axis | 2026-08-10d | 2026-08-10e | 2026-08-10f | 2026-08-10g | 2026-08-10h | 2026-08-10i | n | Min | Mean | Max | Stdev |
|---|---|---|---|---|---|---|---|---|---|---|---|
| fidelity: styled violation rate | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 6 | 0.0 | 0.0 | 0.0 | 0.0 |
| fidelity: gated pairs passed | 32 | 32 | 32 | 32 | 32 | 32 | 6 | 32 | 32.0 | 32 | 0.0 |
| cost: output-token ratio | 0.93 | 0.83 | 0.82 | 1.04 | 0.6 | 0.86 | 6 | 0.6 | 0.847 | 1.04 | 0.146 |
| value: net wins (comprehension) | 6 | 5 | -1 | 0 | 4 | -2 | 6 | -2 | 2.0 | 6 | 3.406 |
| value: net wins (paraphrase) | 3 | -3 | -3 | 0 | 0 | 3 | 6 | -3 | 0.0 | 3 | 2.683 |
| value: net wins (roundtrip) | -8 | 3 | -6 | -2 | 0 | -6 | 6 | -8 | -3.167 | 3 | 4.215 |
| loss: fact survival median | 0.754 | 0.788 | 0.746 | 0.771 | 0.759 | 0.774 | 6 | 0.746 | 0.765 | 0.788 | 0.015 |
| loss: hedge survival median | 0.845 | 1.0 | 0.875 | 0.8 | 0.833 | 0.683 | 6 | 0.683 | 0.839 | 1.0 | 0.103 |
| rank: Bradley-Terry strength | 0.753 | 0.89 | 1.197 | 0.888 | 0.866 | 0.917 | 6 | 0.753 | 0.918 | 1.197 | 0.148 |
| rank: net wins vs unstyled | -5 | -7 | 2 | -2 | 0 | 2 | 6 | -7 | -1.667 | 2 | 3.724 |

## classic-concise

| Axis | 2026-08-10d | 2026-08-10e | 2026-08-10f | 2026-08-10g | 2026-08-10h | 2026-08-10i | n | Min | Mean | Max | Stdev |
|---|---|---|---|---|---|---|---|---|---|---|---|
| fidelity: styled violation rate | 0.49 | 0.26 | 0.5 | 0.47 | 0.5 | 0.48 | 6 | 0.26 | 0.45 | 0.5 | 0.094 |
| fidelity: gated pairs passed | 32 | 32 | 32 | 32 | 32 | 32 | 6 | 32 | 32.0 | 32 | 0.0 |
| cost: output-token ratio | 0.84 | 0.62 | 0.66 | 0.88 | 0.69 | 0.61 | 6 | 0.61 | 0.717 | 0.88 | 0.115 |
| value: net wins (comprehension) | -4 | -2 | -1 | -3 | -6 | -4 | 6 | -6 | -3.333 | -1 | 1.751 |
| value: net wins (paraphrase) | -2 | 1 | -9 | 2 | 2 | -6 | 6 | -9 | -2.0 | 2 | 4.604 |
| value: net wins (roundtrip) | -11 | -13 | -4 | -3 | -3 | -6 | 6 | -13 | -6.667 | -3 | 4.32 |
| loss: fact survival median | 0.703 | 0.781 | 0.734 | 0.769 | 0.843 | 0.742 | 6 | 0.703 | 0.762 | 0.843 | 0.048 |
| loss: hedge survival median | 1.0 | 0.8 | 0.938 | 0.667 | 0.691 | 0.834 | 6 | 0.667 | 0.822 | 1.0 | 0.132 |
| rank: Bradley-Terry strength | 0.674 | 0.689 | 0.873 | 1.092 | 0.953 | 0.626 | 6 | 0.626 | 0.818 | 1.092 | 0.185 |
| rank: net wins vs unstyled | -9 | -6 | -1 | 0 | 4 | -11 | 6 | -11 | -3.833 | 4 | 5.776 |

## developer-docs

| Axis | 2026-08-10d | 2026-08-10e | 2026-08-10f | 2026-08-10g | 2026-08-10h | 2026-08-10i | n | Min | Mean | Max | Stdev |
|---|---|---|---|---|---|---|---|---|---|---|---|
| fidelity: styled violation rate | 0.5 | 0.17 | 0.51 | 0.18 | 0.0 | 0.16 | 6 | 0.0 | 0.253 | 0.51 | 0.206 |
| fidelity: gated pairs passed | 32 | 32 | 32 | 32 | 32 | 32 | 6 | 32 | 32.0 | 32 | 0.0 |
| cost: output-token ratio | 1.2 | 0.9 | 0.75 | 1.02 | 0.92 | 0.95 | 6 | 0.75 | 0.957 | 1.2 | 0.149 |
| value: net wins (comprehension) | 3 | -3 | -1 | -1 | -2 | 0 | 6 | -3 | -0.667 | 3 | 2.066 |
| value: net wins (paraphrase) | 7 | 2 | 6 | 9 | 14 | 1 | 6 | 1 | 6.5 | 14 | 4.764 |
| value: net wins (roundtrip) | 10 | 10 | 2 | 7 | 13 | 6 | 6 | 2 | 8.0 | 13 | 3.847 |
| loss: fact survival median | 0.772 | 0.762 | 0.679 | 0.78 | 0.75 | 0.764 | 6 | 0.679 | 0.751 | 0.78 | 0.037 |
| loss: hedge survival median | 0.857 | 1.0 | 0.857 | 0.771 | 1.0 | 0.667 | 6 | 0.667 | 0.859 | 1.0 | 0.13 |
| rank: Bradley-Terry strength | 1.452 | 2.046 | 1.47 | 1.553 | 1.27 | 1.211 | 6 | 1.211 | 1.5 | 2.046 | 0.297 |
| rank: net wins vs unstyled | 11 | 12 | 8 | 10 | 3 | 4 | 6 | 3 | 8.0 | 12 | 3.742 |

## plain-language

| Axis | 2026-08-10d | 2026-08-10e | 2026-08-10f | 2026-08-10g | 2026-08-10h | 2026-08-10i | n | Min | Mean | Max | Stdev |
|---|---|---|---|---|---|---|---|---|---|---|---|
| fidelity: styled violation rate | 0.0 | 0.14 | 0.0 | 0.0 | 0.0 | 0.0 | 6 | 0.0 | 0.023 | 0.14 | 0.057 |
| fidelity: gated pairs passed | 32 | 32 | 32 | 32 | 32 | 32 | 6 | 32 | 32.0 | 32 | 0.0 |
| cost: output-token ratio | 0.84 | 0.85 | 0.7 | 0.93 | 0.82 | 0.95 | 6 | 0.7 | 0.848 | 0.95 | 0.089 |
| value: net wins (comprehension) | 3 | 2 | -2 | -5 | 0 | 5 | 6 | -5 | 0.5 | 5 | 3.619 |
| value: net wins (paraphrase) | -2 | 12 | 0 | 14 | 11 | 9 | 6 | -2 | 7.333 | 14 | 6.683 |
| value: net wins (roundtrip) | -3 | 3 | -2 | 7 | 5 | 1 | 6 | -3 | 1.833 | 7 | 3.92 |
| loss: fact survival median | 0.728 | 0.732 | 0.657 | 0.735 | 0.737 | 0.692 | 6 | 0.657 | 0.713 | 0.737 | 0.032 |
| loss: hedge survival median | 0.857 | 1.0 | 1.0 | 0.95 | 0.833 | 1.0 | 6 | 0.833 | 0.94 | 1.0 | 0.076 |
| rank: Bradley-Terry strength | 1.18 | 2.426 | 1.428 | 1.698 | 1.1 | 1.516 | 6 | 1.1 | 1.558 | 2.426 | 0.478 |
| rank: net wins vs unstyled | 3 | 14 | 6 | 8 | 0 | 6 | 6 | 0 | 6.167 | 14 | 4.75 |

## technical-simplified

| Axis | 2026-08-10d | 2026-08-10e | 2026-08-10f | 2026-08-10g | 2026-08-10h | 2026-08-10i | n | Min | Mean | Max | Stdev |
|---|---|---|---|---|---|---|---|---|---|---|---|
| fidelity: styled violation rate | 6.87 | 7.26 | 9.04 | 7.71 | 5.24 | 7.81 | 6 | 5.24 | 7.322 | 9.04 | 1.256 |
| fidelity: gated pairs passed | 27 | 29 | 26 | 26 | 30 | 27 | 6 | 26 | 27.5 | 30 | 1.643 |
| cost: output-token ratio | 1.23 | 0.97 | 0.85 | 1.0 | 1.09 | 0.71 | 6 | 0.71 | 0.975 | 1.23 | 0.182 |
| value: net wins (comprehension) | 4 | 1 | -4 | -3 | 0 | -2 | 6 | -4 | -0.667 | 4 | 2.944 |
| value: net wins (paraphrase) | 6 | 9 | 8 | 4 | 18 | 12 | 6 | 4 | 9.5 | 18 | 4.97 |
| value: net wins (roundtrip) | 1 | 9 | 9 | 2 | -1 | 4 | 6 | -1 | 4.0 | 9 | 4.195 |
| loss: fact survival median | 0.625 | 0.667 | 0.649 | 0.661 | 0.72 | 0.636 | 6 | 0.625 | 0.66 | 0.72 | 0.033 |
| loss: hedge survival median | 0.55 | 0.857 | 0.75 | 0.5 | 0.667 | 0.678 | 6 | 0.5 | 0.667 | 0.857 | 0.13 |
| rank: Bradley-Terry strength | 0.52 | 0.454 | 0.438 | 0.517 | 0.394 | 0.485 | 6 | 0.394 | 0.468 | 0.52 | 0.049 |
| rank: net wins vs unstyled | -13 | -7 | -8 | -9 | -13 | -10 | 6 | -13 | -10.0 | -7 | 2.53 |

## Warnings

- condition mismatch on gate-config hash: 2026-08-10d 81fdcb3a2d5ecf7d10b790d66df35f76869a35b6c3b1f210c5796b868ea72570, 2026-08-10e 81fdcb3a2d5ecf7d10b790d66df35f76869a35b6c3b1f210c5796b868ea72570, 2026-08-10f 81fdcb3a2d5ecf7d10b790d66df35f76869a35b6c3b1f210c5796b868ea72570, 2026-08-10g 4f99efa18541117768ba85e259c9377b904aef848e1c0efa3c68100184f220e7, 2026-08-10h 4f99efa18541117768ba85e259c9377b904aef848e1c0efa3c68100184f220e7, 2026-08-10i 4f99efa18541117768ba85e259c9377b904aef848e1c0efa3c68100184f220e7

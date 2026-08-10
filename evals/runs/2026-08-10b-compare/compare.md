# Cross-run comparison

The comparison reads the stored artifacts of several runs with identical conditions. Per style and axis, the table states one value per run and the spread: minimum, mean, maximum, and the sample standard deviation. The spread is the error bar of the harness: it shows how much a verdict moves on a resample. Net wins is wins minus losses, and n counts the runs that hold a value for the axis.

Runs: 2026-08-10d, 2026-08-10e, 2026-08-10f.

## actionable-clarity

| Axis | 2026-08-10d | 2026-08-10e | 2026-08-10f | n | Min | Mean | Max | Stdev |
|---|---|---|---|---|---|---|---|---|
| fidelity: styled violation rate | 0.17 | 0.68 | 0.0 | 3 | 0.0 | 0.283 | 0.68 | 0.354 |
| fidelity: gated pairs passed | 32 | 31 | 32 | 3 | 31 | 31.667 | 32 | 0.577 |
| cost: output-token ratio | 1.36 | 1.2 | 1.0 | 3 | 1.0 | 1.187 | 1.36 | 0.18 |
| value: net wins (comprehension) | 4 | 2 | 11 | 3 | 2 | 5.667 | 11 | 4.726 |
| value: net wins (paraphrase) | 3 | 6 | 1 | 3 | 1 | 3.333 | 6 | 2.517 |
| value: net wins (roundtrip) | 6 | 14 | -2 | 3 | -2 | 6.0 | 14 | 8.0 |
| loss: fact survival median | 0.806 | 0.8 | 0.758 | 3 | 0.758 | 0.788 | 0.806 | 0.026 |
| loss: hedge survival median | 1.0 | 1.0 | 0.938 | 3 | 0.938 | 0.979 | 1.0 | 0.036 |
| rank: Bradley-Terry strength | 2.933 | 2.211 | 2.158 | 3 | 2.158 | 2.434 | 2.933 | 0.433 |
| rank: net wins vs unstyled | 18 | 11 | 7 | 3 | 7 | 12.0 | 18 | 5.568 |

## clarity-flow

| Axis | 2026-08-10d | 2026-08-10e | 2026-08-10f | n | Min | Mean | Max | Stdev |
|---|---|---|---|---|---|---|---|---|
| fidelity: styled violation rate | 0.0 | 0.0 | 0.0 | 3 | 0.0 | 0.0 | 0.0 | 0.0 |
| fidelity: gated pairs passed | 32 | 32 | 32 | 3 | 32 | 32.0 | 32 | 0.0 |
| cost: output-token ratio | 0.93 | 0.83 | 0.82 | 3 | 0.82 | 0.86 | 0.93 | 0.061 |
| value: net wins (comprehension) | 6 | 5 | -1 | 3 | -1 | 3.333 | 6 | 3.786 |
| value: net wins (paraphrase) | 3 | -3 | -3 | 3 | -3 | -1.0 | 3 | 3.464 |
| value: net wins (roundtrip) | -8 | 3 | -6 | 3 | -8 | -3.667 | 3 | 5.859 |
| loss: fact survival median | 0.754 | 0.788 | 0.746 | 3 | 0.746 | 0.763 | 0.788 | 0.022 |
| loss: hedge survival median | 0.845 | 1.0 | 0.875 | 3 | 0.845 | 0.907 | 1.0 | 0.082 |
| rank: Bradley-Terry strength | 0.753 | 0.89 | 1.197 | 3 | 0.753 | 0.947 | 1.197 | 0.227 |
| rank: net wins vs unstyled | -5 | -7 | 2 | 3 | -7 | -3.333 | 2 | 4.726 |

## classic-concise

| Axis | 2026-08-10d | 2026-08-10e | 2026-08-10f | n | Min | Mean | Max | Stdev |
|---|---|---|---|---|---|---|---|---|
| fidelity: styled violation rate | 0.49 | 0.26 | 0.5 | 3 | 0.26 | 0.417 | 0.5 | 0.136 |
| fidelity: gated pairs passed | 32 | 32 | 32 | 3 | 32 | 32.0 | 32 | 0.0 |
| cost: output-token ratio | 0.84 | 0.62 | 0.66 | 3 | 0.62 | 0.707 | 0.84 | 0.117 |
| value: net wins (comprehension) | -4 | -2 | -1 | 3 | -4 | -2.333 | -1 | 1.528 |
| value: net wins (paraphrase) | -2 | 1 | -9 | 3 | -9 | -3.333 | 1 | 5.132 |
| value: net wins (roundtrip) | -11 | -13 | -4 | 3 | -13 | -9.333 | -4 | 4.726 |
| loss: fact survival median | 0.703 | 0.781 | 0.734 | 3 | 0.703 | 0.739 | 0.781 | 0.039 |
| loss: hedge survival median | 1.0 | 0.8 | 0.938 | 3 | 0.8 | 0.913 | 1.0 | 0.102 |
| rank: Bradley-Terry strength | 0.674 | 0.689 | 0.873 | 3 | 0.674 | 0.745 | 0.873 | 0.111 |
| rank: net wins vs unstyled | -9 | -6 | -1 | 3 | -9 | -5.333 | -1 | 4.041 |

## developer-docs

| Axis | 2026-08-10d | 2026-08-10e | 2026-08-10f | n | Min | Mean | Max | Stdev |
|---|---|---|---|---|---|---|---|---|
| fidelity: styled violation rate | 0.5 | 0.17 | 0.51 | 3 | 0.17 | 0.393 | 0.51 | 0.193 |
| fidelity: gated pairs passed | 32 | 32 | 32 | 3 | 32 | 32.0 | 32 | 0.0 |
| cost: output-token ratio | 1.2 | 0.9 | 0.75 | 3 | 0.75 | 0.95 | 1.2 | 0.229 |
| value: net wins (comprehension) | 3 | -3 | -1 | 3 | -3 | -0.333 | 3 | 3.055 |
| value: net wins (paraphrase) | 7 | 2 | 6 | 3 | 2 | 5.0 | 7 | 2.646 |
| value: net wins (roundtrip) | 10 | 10 | 2 | 3 | 2 | 7.333 | 10 | 4.619 |
| loss: fact survival median | 0.772 | 0.762 | 0.679 | 3 | 0.679 | 0.738 | 0.772 | 0.051 |
| loss: hedge survival median | 0.857 | 1.0 | 0.857 | 3 | 0.857 | 0.905 | 1.0 | 0.083 |
| rank: Bradley-Terry strength | 1.452 | 2.046 | 1.47 | 3 | 1.452 | 1.656 | 2.046 | 0.338 |
| rank: net wins vs unstyled | 11 | 12 | 8 | 3 | 8 | 10.333 | 12 | 2.082 |

## plain-language

| Axis | 2026-08-10d | 2026-08-10e | 2026-08-10f | n | Min | Mean | Max | Stdev |
|---|---|---|---|---|---|---|---|---|
| fidelity: styled violation rate | 0.0 | 0.14 | 0.0 | 3 | 0.0 | 0.047 | 0.14 | 0.081 |
| fidelity: gated pairs passed | 32 | 32 | 32 | 3 | 32 | 32.0 | 32 | 0.0 |
| cost: output-token ratio | 0.84 | 0.85 | 0.7 | 3 | 0.7 | 0.797 | 0.85 | 0.084 |
| value: net wins (comprehension) | 3 | 2 | -2 | 3 | -2 | 1.0 | 3 | 2.646 |
| value: net wins (paraphrase) | -2 | 12 | 0 | 3 | -2 | 3.333 | 12 | 7.572 |
| value: net wins (roundtrip) | -3 | 3 | -2 | 3 | -3 | -0.667 | 3 | 3.215 |
| loss: fact survival median | 0.728 | 0.732 | 0.657 | 3 | 0.657 | 0.706 | 0.732 | 0.042 |
| loss: hedge survival median | 0.857 | 1.0 | 1.0 | 3 | 0.857 | 0.952 | 1.0 | 0.083 |
| rank: Bradley-Terry strength | 1.18 | 2.426 | 1.428 | 3 | 1.18 | 1.678 | 2.426 | 0.66 |
| rank: net wins vs unstyled | 3 | 14 | 6 | 3 | 3 | 7.667 | 14 | 5.686 |

## technical-simplified

| Axis | 2026-08-10d | 2026-08-10e | 2026-08-10f | n | Min | Mean | Max | Stdev |
|---|---|---|---|---|---|---|---|---|
| fidelity: styled violation rate | 6.87 | 7.26 | 9.04 | 3 | 6.87 | 7.723 | 9.04 | 1.157 |
| fidelity: gated pairs passed | 27 | 29 | 26 | 3 | 26 | 27.333 | 29 | 1.528 |
| cost: output-token ratio | 1.23 | 0.97 | 0.85 | 3 | 0.85 | 1.017 | 1.23 | 0.194 |
| value: net wins (comprehension) | 4 | 1 | -4 | 3 | -4 | 0.333 | 4 | 4.041 |
| value: net wins (paraphrase) | 6 | 9 | 8 | 3 | 6 | 7.667 | 9 | 1.528 |
| value: net wins (roundtrip) | 1 | 9 | 9 | 3 | 1 | 6.333 | 9 | 4.619 |
| loss: fact survival median | 0.625 | 0.667 | 0.649 | 3 | 0.625 | 0.647 | 0.667 | 0.021 |
| loss: hedge survival median | 0.55 | 0.857 | 0.75 | 3 | 0.55 | 0.719 | 0.857 | 0.156 |
| rank: Bradley-Terry strength | 0.52 | 0.454 | 0.438 | 3 | 0.438 | 0.471 | 0.52 | 0.043 |
| rank: net wins vs unstyled | -13 | -7 | -8 | 3 | -13 | -9.333 | -7 | 3.215 |

## Warnings

- none

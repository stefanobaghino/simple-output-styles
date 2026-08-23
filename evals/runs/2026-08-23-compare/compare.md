# Cross-run comparison

The comparison reads the stored artifacts of several runs with identical conditions. Per style and axis, the table states one value per run and the spread: minimum, mean, maximum, and the sample standard deviation. The spread is the error bar of the harness: it shows how much a verdict moves on a resample. Net wins is wins minus losses, and n counts the runs that hold a value for the axis.

Runs: 2026-08-22, 2026-08-22b, 2026-08-22c.

## actionable-clarity

| Axis | 2026-08-22 | 2026-08-22b | 2026-08-22c | n | Min | Mean | Max | Stdev |
|---|---|---|---|---|---|---|---|---|
| fidelity: styled violation rate | 0.0 | 0.18 | 0.19 | 3 | 0.0 | 0.123 | 0.19 | 0.107 |
| fidelity: gated pairs passed | 32 | 32 | 32 | 3 | 32 | 32.0 | 32 | 0.0 |
| cost: output-token ratio | 0.98 | 0.98 | 1.24 | 3 | 0.98 | 1.067 | 1.24 | 0.15 |
| value: net wins (comprehension) | 6 | 6 | -2 | 3 | -2 | 3.333 | 6 | 4.619 |
| value: net wins (paraphrase) | 2 | 1 | 8 | 3 | 1 | 3.667 | 8 | 3.786 |
| value: net wins (roundtrip) | 3 | 4 | 11 | 3 | 3 | 6.0 | 11 | 4.359 |
| loss: fact survival median | 0.777 | 0.761 | 0.81 | 3 | 0.761 | 0.783 | 0.81 | 0.025 |
| loss: hedge survival median | 1.0 | 0.818 | 1.0 | 3 | 0.818 | 0.939 | 1.0 | 0.105 |
| rank: Bradley-Terry strength | 1.928 | 1.992 | 2.953 | 3 | 1.928 | 2.291 | 2.953 | 0.574 |
| rank: net wins vs unstyled | 5 | 7 | 10 | 3 | 5 | 7.333 | 10 | 2.517 |

## clarity-flow

| Axis | 2026-08-22 | 2026-08-22b | 2026-08-22c | n | Min | Mean | Max | Stdev |
|---|---|---|---|---|---|---|---|---|
| fidelity: styled violation rate | 0.0 | 0.0 | 0.0 | 3 | 0.0 | 0.0 | 0.0 | 0.0 |
| fidelity: gated pairs passed | 32 | 32 | 32 | 3 | 32 | 32.0 | 32 | 0.0 |
| cost: output-token ratio | 0.61 | 0.84 | 0.91 | 3 | 0.61 | 0.787 | 0.91 | 0.157 |
| value: net wins (comprehension) | -4 | 3 | -2 | 3 | -4 | -1.0 | 3 | 3.606 |
| value: net wins (paraphrase) | -6 | 4 | -2 | 3 | -6 | -1.333 | 4 | 5.033 |
| value: net wins (roundtrip) | 2 | -3 | 0 | 3 | -3 | -0.333 | 2 | 2.517 |
| loss: fact survival median | 0.71 | 0.768 | 0.778 | 3 | 0.71 | 0.752 | 0.778 | 0.037 |
| loss: hedge survival median | 0.854 | 0.857 | 0.667 | 3 | 0.667 | 0.793 | 0.857 | 0.109 |
| rank: Bradley-Terry strength | 0.439 | 0.822 | 0.738 | 3 | 0.439 | 0.666 | 0.822 | 0.201 |
| rank: net wins vs unstyled | -12 | -3 | -4 | 3 | -12 | -6.333 | -3 | 4.933 |

## classic-concise

| Axis | 2026-08-22 | 2026-08-22b | 2026-08-22c | n | Min | Mean | Max | Stdev |
|---|---|---|---|---|---|---|---|---|
| fidelity: styled violation rate | 0.25 | 0.47 | 0.0 | 3 | 0.0 | 0.24 | 0.47 | 0.235 |
| fidelity: gated pairs passed | 32 | 32 | 32 | 3 | 32 | 32.0 | 32 | 0.0 |
| cost: output-token ratio | 0.51 | 0.51 | 0.74 | 3 | 0.51 | 0.587 | 0.74 | 0.133 |
| value: net wins (comprehension) | -3 | 6 | -5 | 3 | -5 | -0.667 | 6 | 5.859 |
| value: net wins (paraphrase) | -11 | -7 | -3 | 3 | -11 | -7.0 | -3 | 4.0 |
| value: net wins (roundtrip) | -10 | -11 | 2 | 3 | -11 | -6.333 | 2 | 7.234 |
| loss: fact survival median | 0.714 | 0.716 | 0.769 | 3 | 0.714 | 0.733 | 0.769 | 0.031 |
| loss: hedge survival median | 0.75 | 0.8 | 0.75 | 3 | 0.75 | 0.767 | 0.8 | 0.029 |
| rank: Bradley-Terry strength | 0.681 | 0.686 | 0.772 | 3 | 0.681 | 0.713 | 0.772 | 0.051 |
| rank: net wins vs unstyled | -6 | -7 | 1 | 3 | -7 | -4.0 | 1 | 4.359 |

## concise

| Axis | 2026-08-22 | 2026-08-22b | 2026-08-22c | n | Min | Mean | Max | Stdev |
|---|---|---|---|---|---|---|---|---|
| fidelity: styled violation rate | 0.0 | 0.0 | 0.0 | 3 | 0.0 | 0.0 | 0.0 | 0.0 |
| fidelity: gated pairs passed | 32 | 32 | 32 | 3 | 32 | 32.0 | 32 | 0.0 |
| cost: output-token ratio | 0.53 | 0.55 | 0.66 | 3 | 0.53 | 0.58 | 0.66 | 0.07 |
| value: net wins (comprehension) | -2 | 2 | -1 | 3 | -2 | -0.333 | 2 | 2.082 |
| value: net wins (paraphrase) | -8 | 2 | -4 | 3 | -8 | -3.333 | 2 | 5.033 |
| value: net wins (roundtrip) | -6 | -13 | -2 | 3 | -13 | -7.0 | -2 | 5.568 |
| loss: fact survival median | 0.756 | 0.734 | 0.75 | 3 | 0.734 | 0.747 | 0.756 | 0.011 |
| loss: hedge survival median | 0.725 | 0.633 | 0.834 | 3 | 0.633 | 0.731 | 0.834 | 0.101 |
| rank: Bradley-Terry strength | 0.301 | 0.379 | 0.362 | 3 | 0.301 | 0.347 | 0.379 | 0.041 |
| rank: net wins vs unstyled | -14 | -17 | -12 | 3 | -17 | -14.333 | -12 | 2.517 |

## developer-docs

| Axis | 2026-08-22 | 2026-08-22b | 2026-08-22c | n | Min | Mean | Max | Stdev |
|---|---|---|---|---|---|---|---|---|
| fidelity: styled violation rate | 0.34 | 0.0 | 0.33 | 3 | 0.0 | 0.223 | 0.34 | 0.193 |
| fidelity: gated pairs passed | 32 | 32 | 32 | 3 | 32 | 32.0 | 32 | 0.0 |
| cost: output-token ratio | 0.68 | 0.92 | 0.95 | 3 | 0.68 | 0.85 | 0.95 | 0.148 |
| value: net wins (comprehension) | 0 | 5 | 6 | 3 | 0 | 3.667 | 6 | 3.215 |
| value: net wins (paraphrase) | 4 | 7 | 4 | 3 | 4 | 5.0 | 7 | 1.732 |
| value: net wins (roundtrip) | 3 | 7 | 11 | 3 | 3 | 7.0 | 11 | 4.0 |
| loss: fact survival median | 0.743 | 0.754 | 0.81 | 3 | 0.743 | 0.769 | 0.81 | 0.036 |
| loss: hedge survival median | 0.857 | 0.5 | 0.812 | 3 | 0.5 | 0.723 | 0.857 | 0.194 |
| rank: Bradley-Terry strength | 1.196 | 1.866 | 2.244 | 3 | 1.196 | 1.769 | 2.244 | 0.531 |
| rank: net wins vs unstyled | 2 | 11 | 10 | 3 | 2 | 7.667 | 11 | 4.933 |

## plain-language

| Axis | 2026-08-22 | 2026-08-22b | 2026-08-22c | n | Min | Mean | Max | Stdev |
|---|---|---|---|---|---|---|---|---|
| fidelity: styled violation rate | 0.0 | 0.0 | 0.0 | 3 | 0.0 | 0.0 | 0.0 | 0.0 |
| fidelity: gated pairs passed | 32 | 32 | 32 | 3 | 32 | 32.0 | 32 | 0.0 |
| cost: output-token ratio | 0.7 | 0.95 | 0.93 | 3 | 0.7 | 0.86 | 0.95 | 0.139 |
| value: net wins (comprehension) | -2 | 5 | 0 | 3 | -2 | 1.0 | 5 | 3.606 |
| value: net wins (paraphrase) | 4 | 7 | 6 | 3 | 4 | 5.667 | 7 | 1.528 |
| value: net wins (roundtrip) | 3 | 0 | 5 | 3 | 0 | 2.667 | 5 | 2.517 |
| loss: fact survival median | 0.714 | 0.692 | 0.778 | 3 | 0.692 | 0.728 | 0.778 | 0.045 |
| loss: hedge survival median | 0.875 | 1.0 | 0.709 | 3 | 0.709 | 0.861 | 1.0 | 0.146 |
| rank: Bradley-Terry strength | 1.185 | 1.424 | 1.285 | 3 | 1.185 | 1.298 | 1.424 | 0.12 |
| rank: net wins vs unstyled | 4 | 10 | 3 | 3 | 3 | 5.667 | 10 | 3.786 |

## technical-simplified

| Axis | 2026-08-22 | 2026-08-22b | 2026-08-22c | n | Min | Mean | Max | Stdev |
|---|---|---|---|---|---|---|---|---|
| fidelity: styled violation rate | 8.93 | 6.84 | 6.94 | 3 | 6.84 | 7.57 | 8.93 | 1.179 |
| fidelity: gated pairs passed | 26 | 28 | 26 | 3 | 26 | 26.667 | 28 | 1.155 |
| cost: output-token ratio | 0.74 | 0.84 | 1.15 | 3 | 0.74 | 0.91 | 1.15 | 0.214 |
| value: net wins (comprehension) | 0 | 3 | -3 | 3 | -3 | 0.0 | 3 | 3.0 |
| value: net wins (paraphrase) | 6 | 12 | 5 | 3 | 5 | 7.667 | 12 | 3.786 |
| value: net wins (roundtrip) | 0 | 1 | 5 | 3 | 0 | 2.0 | 5 | 2.646 |
| loss: fact survival median | 0.627 | 0.697 | 0.714 | 3 | 0.627 | 0.679 | 0.714 | 0.046 |
| loss: hedge survival median | 0.291 | 0.25 | 0.333 | 3 | 0.25 | 0.291 | 0.333 | 0.042 |
| rank: Bradley-Terry strength | 0.407 | 0.584 | 0.438 | 3 | 0.407 | 0.476 | 0.584 | 0.095 |
| rank: net wins vs unstyled | -10 | -6 | -10 | 3 | -10 | -8.667 | -6 | 2.309 |

## Warnings

- none

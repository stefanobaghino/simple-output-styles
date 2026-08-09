# Cross-run comparison

The comparison reads the stored artifacts of several runs with identical conditions. Per style and axis, the table states one value per run and the spread: minimum, mean, maximum, and the sample standard deviation. The spread is the error bar of the harness: it shows how much a verdict moves on a resample. Net wins is wins minus losses, and n counts the runs that hold a value for the axis.

Runs: 2026-08-07, 2026-08-08, 2026-08-08b.

## clarity-flow

| Axis | 2026-08-07 | 2026-08-08 | 2026-08-08b | n | Min | Mean | Max | Stdev |
|---|---|---|---|---|---|---|---|---|
| fidelity: styled violation rate | 0.0 | 0.0 | 0.0 | 3 | 0.0 | 0.0 | 0.0 | 0.0 |
| fidelity: gated pairs passed | 32 | 32 | 32 | 3 | 32 | 32.0 | 32 | 0.0 |
| cost: output-token ratio | 1.04 | 0.6 | 0.86 | 3 | 0.6 | 0.833 | 1.04 | 0.221 |
| value: net wins (comprehension) | 0 | 4 | -2 | 3 | -2 | 0.667 | 4 | 3.055 |
| value: net wins (paraphrase) | 0 | 0 | 3 | 3 | 0 | 1.0 | 3 | 1.732 |
| value: net wins (roundtrip) | -2 | 0 | -6 | 3 | -6 | -2.667 | 0 | 3.055 |
| loss: fact survival median | 0.771 | 0.759 | 0.774 | 3 | 0.759 | 0.768 | 0.774 | 0.008 |
| loss: hedge survival median | 0.8 | 0.833 | 0.683 | 3 | 0.683 | 0.772 | 0.833 | 0.079 |
| rank: Bradley-Terry strength | 0.884 | 0.958 | 0.946 | 3 | 0.884 | 0.929 | 0.958 | 0.04 |
| rank: net wins vs unstyled | -1 | 0 | 2 | 3 | -1 | 0.333 | 2 | 1.528 |

## classic-concise

| Axis | 2026-08-07 | 2026-08-08 | 2026-08-08b | n | Min | Mean | Max | Stdev |
|---|---|---|---|---|---|---|---|---|
| fidelity: styled violation rate | 0.47 | 0.5 | 0.48 | 3 | 0.47 | 0.483 | 0.5 | 0.015 |
| fidelity: gated pairs passed | 32 | 32 | 32 | 3 | 32 | 32.0 | 32 | 0.0 |
| cost: output-token ratio | 0.88 | 0.69 | 0.61 | 3 | 0.61 | 0.727 | 0.88 | 0.139 |
| value: net wins (comprehension) | -3 | -6 | -4 | 3 | -6 | -4.333 | -3 | 1.528 |
| value: net wins (paraphrase) | 2 | 2 | -6 | 3 | -6 | -0.667 | 2 | 4.619 |
| value: net wins (roundtrip) | -3 | -3 | -6 | 3 | -6 | -4.0 | -3 | 1.732 |
| loss: fact survival median | 0.769 | 0.843 | 0.742 | 3 | 0.742 | 0.785 | 0.843 | 0.052 |
| loss: hedge survival median | 0.667 | 0.691 | 0.834 | 3 | 0.667 | 0.731 | 0.834 | 0.09 |
| rank: Bradley-Terry strength | 1.117 | 1.0 | 0.597 | 3 | 0.597 | 0.905 | 1.117 | 0.273 |
| rank: net wins vs unstyled | 0 | 4 | -11 | 3 | -11 | -2.333 | 4 | 7.767 |

## developer-docs

| Axis | 2026-08-07 | 2026-08-08 | 2026-08-08b | n | Min | Mean | Max | Stdev |
|---|---|---|---|---|---|---|---|---|
| fidelity: styled violation rate | 0.18 | 0.0 | 0.16 | 3 | 0.0 | 0.113 | 0.18 | 0.099 |
| fidelity: gated pairs passed | 32 | 32 | 32 | 3 | 32 | 32.0 | 32 | 0.0 |
| cost: output-token ratio | 1.02 | 0.92 | 0.95 | 3 | 0.92 | 0.963 | 1.02 | 0.051 |
| value: net wins (comprehension) | -1 | -2 | 0 | 3 | -2 | -1.0 | 0 | 1.0 |
| value: net wins (paraphrase) | 9 | 14 | 1 | 3 | 1 | 8.0 | 14 | 6.557 |
| value: net wins (roundtrip) | 7 | 13 | 6 | 3 | 6 | 8.667 | 13 | 3.786 |
| loss: fact survival median | 0.78 | 0.75 | 0.764 | 3 | 0.75 | 0.765 | 0.78 | 0.015 |
| loss: hedge survival median | 0.771 | 1.0 | 0.667 | 3 | 0.667 | 0.813 | 1.0 | 0.17 |
| rank: Bradley-Terry strength | 1.6 | 1.329 | 1.196 | 3 | 1.196 | 1.375 | 1.6 | 0.206 |
| rank: net wins vs unstyled | 10 | 3 | 3 | 3 | 3 | 5.333 | 10 | 4.041 |

## plain-language

| Axis | 2026-08-07 | 2026-08-08 | 2026-08-08b | n | Min | Mean | Max | Stdev |
|---|---|---|---|---|---|---|---|---|
| fidelity: styled violation rate | 0.0 | 0.0 | 0.0 | 3 | 0.0 | 0.0 | 0.0 | 0.0 |
| fidelity: gated pairs passed | 32 | 32 | 32 | 3 | 32 | 32.0 | 32 | 0.0 |
| cost: output-token ratio | 0.93 | 0.82 | 0.95 | 3 | 0.82 | 0.9 | 0.95 | 0.07 |
| value: net wins (comprehension) | -5 | 0 | 5 | 3 | -5 | 0.0 | 5 | 5.0 |
| value: net wins (paraphrase) | 14 | 11 | 9 | 3 | 9 | 11.333 | 14 | 2.517 |
| value: net wins (roundtrip) | 7 | 5 | 1 | 3 | 1 | 4.333 | 7 | 3.055 |
| loss: fact survival median | 0.735 | 0.737 | 0.692 | 3 | 0.692 | 0.721 | 0.737 | 0.025 |
| loss: hedge survival median | 0.95 | 0.833 | 1.0 | 3 | 0.833 | 0.928 | 1.0 | 0.086 |
| rank: Bradley-Terry strength | 1.695 | 1.115 | 1.471 | 3 | 1.115 | 1.427 | 1.695 | 0.292 |
| rank: net wins vs unstyled | 8 | 0 | 6 | 3 | 0 | 4.667 | 8 | 4.163 |

## technical-simplified

| Axis | 2026-08-07 | 2026-08-08 | 2026-08-08b | n | Min | Mean | Max | Stdev |
|---|---|---|---|---|---|---|---|---|
| fidelity: styled violation rate | 7.71 | 5.24 | 7.81 | 3 | 5.24 | 6.92 | 7.81 | 1.456 |
| fidelity: gated pairs passed | 26 | 30 | 27 | 3 | 26 | 27.667 | 30 | 2.082 |
| cost: output-token ratio | 1.0 | 1.09 | 0.71 | 3 | 0.71 | 0.933 | 1.09 | 0.199 |
| value: net wins (comprehension) | -3 | 0 | -2 | 3 | -3 | -1.667 | 0 | 1.528 |
| value: net wins (paraphrase) | 4 | 18 | 12 | 3 | 4 | 11.333 | 18 | 7.024 |
| value: net wins (roundtrip) | 2 | -1 | 4 | 3 | -1 | 1.667 | 4 | 2.517 |
| loss: fact survival median | 0.661 | 0.72 | 0.636 | 3 | 0.636 | 0.672 | 0.72 | 0.043 |
| loss: hedge survival median | 0.5 | 0.667 | 0.678 | 3 | 0.5 | 0.615 | 0.678 | 0.1 |
| rank: Bradley-Terry strength | 0.554 | 0.444 | 0.46 | 3 | 0.444 | 0.486 | 0.554 | 0.059 |
| rank: net wins vs unstyled | -9 | -13 | -10 | 3 | -13 | -10.667 | -9 | 2.082 |

## Warnings

- condition mismatch on gate-config hash: 2026-08-07 1a94223c86db0698a461b51bf849c56e7b4f85a3444721147b146f321ebe82d6, 2026-08-08 32c31b55a1e3aac101f91822eb6a1c976621c34c9d2aaad35edc9193e888101a, 2026-08-08b 32c31b55a1e3aac101f91822eb6a1c976621c34c9d2aaad35edc9193e888101a

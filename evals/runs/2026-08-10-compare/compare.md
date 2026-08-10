# Cross-run comparison

The comparison reads the stored artifacts of several runs with identical conditions. Per style and axis, the table states one value per run and the spread: minimum, mean, maximum, and the sample standard deviation. The spread is the error bar of the harness: it shows how much a verdict moves on a resample. Net wins is wins minus losses, and n counts the runs that hold a value for the axis.

Runs: 2026-08-07, 2026-08-08, 2026-08-08b, 2026-08-10, 2026-08-10b, 2026-08-10c.

## clarity-flow

| Axis | 2026-08-07 | 2026-08-08 | 2026-08-08b | 2026-08-10 | 2026-08-10b | 2026-08-10c | n | Min | Mean | Max | Stdev |
|---|---|---|---|---|---|---|---|---|---|---|---|
| fidelity: styled violation rate | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 6 | 0.0 | 0.0 | 0.0 | 0.0 |
| fidelity: gated pairs passed | 32 | 32 | 32 | 32 | 32 | 32 | 6 | 32 | 32.0 | 32 | 0.0 |
| cost: output-token ratio | 1.04 | 0.6 | 0.86 | 0.93 | 0.83 | 0.82 | 6 | 0.6 | 0.847 | 1.04 | 0.146 |
| value: net wins (comprehension) | 0 | 4 | -2 | 6 | 5 | -1 | 6 | -2 | 2.0 | 6 | 3.406 |
| value: net wins (paraphrase) | 0 | 0 | 3 | 3 | -3 | -3 | 6 | -3 | 0.0 | 3 | 2.683 |
| value: net wins (roundtrip) | -2 | 0 | -6 | -8 | 3 | -6 | 6 | -8 | -3.167 | 3 | 4.215 |
| loss: fact survival median | 0.771 | 0.759 | 0.774 | 0.754 | 0.788 | 0.746 | 6 | 0.746 | 0.765 | 0.788 | 0.015 |
| loss: hedge survival median | 0.8 | 0.833 | 0.683 | 0.845 | 1.0 | 0.875 | 6 | 0.683 | 0.839 | 1.0 | 0.103 |
| rank: Bradley-Terry strength | 0.884 | 0.958 | 0.946 | 0.725 | 0.902 | 1.292 | 6 | 0.725 | 0.951 | 1.292 | 0.187 |
| rank: net wins vs unstyled | -1 | 0 | 2 | -5 | -7 | 2 | 6 | -7 | -1.5 | 2 | 3.728 |

## classic-concise

| Axis | 2026-08-07 | 2026-08-08 | 2026-08-08b | 2026-08-10 | 2026-08-10b | 2026-08-10c | n | Min | Mean | Max | Stdev |
|---|---|---|---|---|---|---|---|---|---|---|---|
| fidelity: styled violation rate | 0.47 | 0.5 | 0.48 | 0.49 | 0.26 | 0.5 | 6 | 0.26 | 0.45 | 0.5 | 0.094 |
| fidelity: gated pairs passed | 32 | 32 | 32 | 32 | 32 | 32 | 6 | 32 | 32.0 | 32 | 0.0 |
| cost: output-token ratio | 0.88 | 0.69 | 0.61 | 0.84 | 0.62 | 0.66 | 6 | 0.61 | 0.717 | 0.88 | 0.115 |
| value: net wins (comprehension) | -3 | -6 | -4 | -4 | -2 | -1 | 6 | -6 | -3.333 | -1 | 1.751 |
| value: net wins (paraphrase) | 2 | 2 | -6 | -2 | 1 | -9 | 6 | -9 | -2.0 | 2 | 4.604 |
| value: net wins (roundtrip) | -3 | -3 | -6 | -11 | -13 | -4 | 6 | -13 | -6.667 | -3 | 4.32 |
| loss: fact survival median | 0.769 | 0.843 | 0.742 | 0.703 | 0.781 | 0.734 | 6 | 0.703 | 0.762 | 0.843 | 0.048 |
| loss: hedge survival median | 0.667 | 0.691 | 0.834 | 1.0 | 0.8 | 0.938 | 6 | 0.667 | 0.822 | 1.0 | 0.132 |
| rank: Bradley-Terry strength | 1.117 | 1.0 | 0.597 | 0.634 | 0.673 | 0.904 | 6 | 0.597 | 0.821 | 1.117 | 0.216 |
| rank: net wins vs unstyled | 0 | 4 | -11 | -9 | -6 | -1 | 6 | -11 | -3.833 | 4 | 5.776 |

## developer-docs

| Axis | 2026-08-07 | 2026-08-08 | 2026-08-08b | 2026-08-10 | 2026-08-10b | 2026-08-10c | n | Min | Mean | Max | Stdev |
|---|---|---|---|---|---|---|---|---|---|---|---|
| fidelity: styled violation rate | 0.18 | 0.0 | 0.16 | 0.5 | 0.17 | 0.51 | 6 | 0.0 | 0.253 | 0.51 | 0.206 |
| fidelity: gated pairs passed | 32 | 32 | 32 | 32 | 32 | 32 | 6 | 32 | 32.0 | 32 | 0.0 |
| cost: output-token ratio | 1.02 | 0.92 | 0.95 | 1.2 | 0.9 | 0.75 | 6 | 0.75 | 0.957 | 1.2 | 0.149 |
| value: net wins (comprehension) | -1 | -2 | 0 | 3 | -3 | -1 | 6 | -3 | -0.667 | 3 | 2.066 |
| value: net wins (paraphrase) | 9 | 14 | 1 | 7 | 2 | 6 | 6 | 1 | 6.5 | 14 | 4.764 |
| value: net wins (roundtrip) | 7 | 13 | 6 | 10 | 10 | 2 | 6 | 2 | 8.0 | 13 | 3.847 |
| loss: fact survival median | 0.78 | 0.75 | 0.764 | 0.772 | 0.762 | 0.679 | 6 | 0.679 | 0.751 | 0.78 | 0.037 |
| loss: hedge survival median | 0.771 | 1.0 | 0.667 | 0.857 | 1.0 | 0.857 | 6 | 0.667 | 0.859 | 1.0 | 0.13 |
| rank: Bradley-Terry strength | 1.6 | 1.329 | 1.196 | 1.472 | 2.077 | 1.565 | 6 | 1.196 | 1.54 | 2.077 | 0.303 |
| rank: net wins vs unstyled | 10 | 3 | 3 | 11 | 12 | 8 | 6 | 3 | 7.833 | 12 | 3.971 |

## plain-language

| Axis | 2026-08-07 | 2026-08-08 | 2026-08-08b | 2026-08-10 | 2026-08-10b | 2026-08-10c | n | Min | Mean | Max | Stdev |
|---|---|---|---|---|---|---|---|---|---|---|---|
| fidelity: styled violation rate | 0.0 | 0.0 | 0.0 | 0.0 | 0.14 | 0.0 | 6 | 0.0 | 0.023 | 0.14 | 0.057 |
| fidelity: gated pairs passed | 32 | 32 | 32 | 32 | 32 | 32 | 6 | 32 | 32.0 | 32 | 0.0 |
| cost: output-token ratio | 0.93 | 0.82 | 0.95 | 0.84 | 0.85 | 0.7 | 6 | 0.7 | 0.848 | 0.95 | 0.089 |
| value: net wins (comprehension) | -5 | 0 | 5 | 3 | 2 | -2 | 6 | -5 | 0.5 | 5 | 3.619 |
| value: net wins (paraphrase) | 14 | 11 | 9 | -2 | 12 | 0 | 6 | -2 | 7.333 | 14 | 6.683 |
| value: net wins (roundtrip) | 7 | 5 | 1 | -3 | 3 | -2 | 6 | -3 | 1.833 | 7 | 3.92 |
| loss: fact survival median | 0.735 | 0.737 | 0.692 | 0.728 | 0.732 | 0.657 | 6 | 0.657 | 0.713 | 0.737 | 0.032 |
| loss: hedge survival median | 0.95 | 0.833 | 1.0 | 0.857 | 1.0 | 1.0 | 6 | 0.833 | 0.94 | 1.0 | 0.076 |
| rank: Bradley-Terry strength | 1.695 | 1.115 | 1.471 | 1.17 | 2.453 | 1.478 | 6 | 1.115 | 1.564 | 2.453 | 0.486 |
| rank: net wins vs unstyled | 8 | 0 | 6 | 3 | 14 | 6 | 6 | 0 | 6.167 | 14 | 4.75 |

## technical-simplified

| Axis | 2026-08-07 | 2026-08-08 | 2026-08-08b | 2026-08-10 | 2026-08-10b | 2026-08-10c | n | Min | Mean | Max | Stdev |
|---|---|---|---|---|---|---|---|---|---|---|---|
| fidelity: styled violation rate | 7.71 | 5.24 | 7.81 | 6.87 | 7.26 | 9.04 | 6 | 5.24 | 7.322 | 9.04 | 1.256 |
| fidelity: gated pairs passed | 26 | 30 | 27 | 27 | 29 | 26 | 6 | 26 | 27.5 | 30 | 1.643 |
| cost: output-token ratio | 1.0 | 1.09 | 0.71 | 1.23 | 0.97 | 0.85 | 6 | 0.71 | 0.975 | 1.23 | 0.182 |
| value: net wins (comprehension) | -3 | 0 | -2 | 4 | 1 | -4 | 6 | -4 | -0.667 | 4 | 2.944 |
| value: net wins (paraphrase) | 4 | 18 | 12 | 6 | 9 | 8 | 6 | 4 | 9.5 | 18 | 4.97 |
| value: net wins (roundtrip) | 2 | -1 | 4 | 1 | 9 | 9 | 6 | -1 | 4.0 | 9 | 4.195 |
| loss: fact survival median | 0.661 | 0.72 | 0.636 | 0.625 | 0.667 | 0.649 | 6 | 0.625 | 0.66 | 0.72 | 0.033 |
| loss: hedge survival median | 0.5 | 0.667 | 0.678 | 0.55 | 0.857 | 0.75 | 6 | 0.5 | 0.667 | 0.857 | 0.13 |
| rank: Bradley-Terry strength | 0.554 | 0.444 | 0.46 | 0.486 | 0.459 | 0.499 | 6 | 0.444 | 0.484 | 0.554 | 0.04 |
| rank: net wins vs unstyled | -9 | -13 | -10 | -13 | -7 | -8 | 6 | -13 | -10.0 | -7 | 2.53 |

## Warnings

- condition mismatch on claude version: 2026-08-07 2.1.224 (Claude Code), 2026-08-08 2.1.224 (Claude Code), 2026-08-08b 2.1.224 (Claude Code), 2026-08-10 2.1.226 (Claude Code), 2026-08-10b 2.1.226 (Claude Code), 2026-08-10c 2.1.226 (Claude Code)
- condition mismatch on gate-config hash: 2026-08-07 1a94223c86db0698a461b51bf849c56e7b4f85a3444721147b146f321ebe82d6, 2026-08-08 32c31b55a1e3aac101f91822eb6a1c976621c34c9d2aaad35edc9193e888101a, 2026-08-08b 32c31b55a1e3aac101f91822eb6a1c976621c34c9d2aaad35edc9193e888101a, 2026-08-10 32c31b55a1e3aac101f91822eb6a1c976621c34c9d2aaad35edc9193e888101a, 2026-08-10b 32c31b55a1e3aac101f91822eb6a1c976621c34c9d2aaad35edc9193e888101a, 2026-08-10c 32c31b55a1e3aac101f91822eb6a1c976621c34c9d2aaad35edc9193e888101a

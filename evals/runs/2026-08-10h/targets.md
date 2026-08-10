# Regression targets report

The check compares the run against rules/targets.yaml.
A max limit is a cap: the observed value passes at or below it. A
min limit is a floor: the observed value passes at or above it.
The token axis is a bound, not a target: a value under the bound
earns nothing.

## actionable-clarity

- Axes within targets: 5/5

| Axis | Kind | Limit | Observed | Verdict |
|---|---|---|---|---|
| max_token_ratio | max | 1.45 | 1.01 | pass |
| min_fact_survival | min | 0.73 | 0.805 | pass |
| min_hedge_survival | min | 0.9 | 1 | pass |
| min_rank_strength | min | 1.7 | 2.12 | pass |
| max_drift_slope | max | 0.05 | -0.022 | pass |

## clarity-flow

- Axes within targets: 4/4

| Axis | Kind | Limit | Observed | Verdict |
|---|---|---|---|---|
| max_token_ratio | max | 1.1 | 0.6 | pass |
| min_fact_survival | min | 0.75 | 0.759 | pass |
| min_hedge_survival | min | 0.6 | 0.833 | pass |
| min_rank_strength | min | 0.8 | 0.866 | pass |
| max_drift_slope | max | 0.05 | - | skipped |

- max_drift_slope: not in the drift run

## classic-concise

- Axes within targets: 4/4

| Axis | Kind | Limit | Observed | Verdict |
|---|---|---|---|---|
| max_token_ratio | max | 0.95 | 0.69 | pass |
| min_fact_survival | min | 0.68 | 0.843 | pass |
| min_hedge_survival | min | 0.57 | 0.691 | pass |
| min_rank_strength | min | 0.3 | 0.953 | pass |
| max_drift_slope | max | 0.05 | - | skipped |

- max_drift_slope: not in the drift run

## developer-docs

- Axes within targets: 4/4

| Axis | Kind | Limit | Observed | Verdict |
|---|---|---|---|---|
| max_token_ratio | max | 1.1 | 0.92 | pass |
| min_fact_survival | min | 0.73 | 0.75 | pass |
| min_hedge_survival | min | 0.49 | 1 | pass |
| min_rank_strength | min | 0.95 | 1.27 | pass |
| max_drift_slope | max | 0.12 | - | skipped |

- max_drift_slope: not in the drift run

## plain-language

- Axes within targets: 4/4

| Axis | Kind | Limit | Observed | Verdict |
|---|---|---|---|---|
| max_token_ratio | max | 1 | 0.82 | pass |
| min_fact_survival | min | 0.66 | 0.737 | pass |
| min_hedge_survival | min | 0.74 | 0.833 | pass |
| min_rank_strength | min | 0.8 | 1.1 | pass |
| max_drift_slope | max | 0.05 | - | skipped |

- max_drift_slope: not in the drift run

## technical-simplified

- Axes within targets: 4/4

| Axis | Kind | Limit | Observed | Verdict |
|---|---|---|---|---|
| max_token_ratio | max | 1.15 | 1.09 | pass |
| min_fact_survival | min | 0.59 | 0.72 | pass |
| min_hedge_survival | min | 0.4 | 0.667 | pass |
| min_rank_strength | min | 0.35 | 0.394 | pass |
| max_drift_slope | max | 0.83 | - | skipped |

- max_drift_slope: not in the drift run

## Warnings

- clarity-flow: no observed max_drift_slope in the drift run
- classic-concise: no observed max_drift_slope in the drift run
- developer-docs: no observed max_drift_slope in the drift run
- plain-language: no observed max_drift_slope in the drift run
- technical-simplified: no observed max_drift_slope in the drift run

# Regression targets report

The check compares the run against rules/targets.yaml.
A max limit is a cap: the observed value passes at or below it. A
min limit is a floor: the observed value passes at or above it.
The token axis is a bound, not a target: a value under the bound
earns nothing.

## actionable-clarity

- Axes within targets: 4/4

| Axis | Kind | Limit | Observed | Verdict |
|---|---|---|---|---|
| max_token_ratio | max | 1.45 | 1.24 | pass |
| min_fact_survival | min | 0.73 | 0.81 | pass |
| min_hedge_survival | min | 0.9 | 1 | pass |
| min_rank_strength | min | 1.7 | 2.953 | pass |
| max_drift_slope | max | 0.05 | - | skipped |

- max_drift_slope: no drift run passed

## clarity-flow

- Axes within targets: 3/4

| Axis | Kind | Limit | Observed | Verdict |
|---|---|---|---|---|
| max_token_ratio | max | 1.1 | 0.91 | pass |
| min_fact_survival | min | 0.75 | 0.778 | pass |
| min_hedge_survival | min | 0.6 | 0.667 | pass |
| min_rank_strength | min | 0.8 | 0.738 | fail |
| max_drift_slope | max | 0.05 | - | skipped |

- max_drift_slope: no drift run passed

## classic-concise

- Axes within targets: 4/4

| Axis | Kind | Limit | Observed | Verdict |
|---|---|---|---|---|
| max_token_ratio | max | 0.95 | 0.74 | pass |
| min_fact_survival | min | 0.68 | 0.769 | pass |
| min_hedge_survival | min | 0.57 | 0.75 | pass |
| min_rank_strength | min | 0.3 | 0.772 | pass |
| max_drift_slope | max | 0.05 | - | skipped |

- max_drift_slope: no drift run passed

## concise

- Axes within targets: 1/1

| Axis | Kind | Limit | Observed | Verdict |
|---|---|---|---|---|
| max_token_ratio | max | 1.1 | 0.66 | pass |
| min_fact_survival | min | - | - | skipped |
| min_hedge_survival | min | - | - | skipped |
| min_rank_strength | min | - | - | skipped |
| max_drift_slope | max | - | - | skipped |

- max_token_ratio: no calibrated row in targets.yaml; the default bound applies
- min_fact_survival: uncalibrated
- min_hedge_survival: uncalibrated
- min_rank_strength: uncalibrated
- max_drift_slope: uncalibrated

## developer-docs

- Axes within targets: 4/4

| Axis | Kind | Limit | Observed | Verdict |
|---|---|---|---|---|
| max_token_ratio | max | 1.1 | 0.95 | pass |
| min_fact_survival | min | 0.73 | 0.81 | pass |
| min_hedge_survival | min | 0.49 | 0.812 | pass |
| min_rank_strength | min | 0.95 | 2.244 | pass |
| max_drift_slope | max | 0.12 | - | skipped |

- max_drift_slope: no drift run passed

## plain-language

- Axes within targets: 3/4

| Axis | Kind | Limit | Observed | Verdict |
|---|---|---|---|---|
| max_token_ratio | max | 1 | 0.93 | pass |
| min_fact_survival | min | 0.66 | 0.778 | pass |
| min_hedge_survival | min | 0.74 | 0.709 | fail |
| min_rank_strength | min | 0.8 | 1.285 | pass |
| max_drift_slope | max | 0.05 | - | skipped |

- max_drift_slope: no drift run passed

## technical-simplified

- Axes within targets: 3/4

| Axis | Kind | Limit | Observed | Verdict |
|---|---|---|---|---|
| max_token_ratio | max | 1.15 | 1.15 | pass |
| min_fact_survival | min | 0.59 | 0.714 | pass |
| min_hedge_survival | min | 0.4 | 0.333 | fail |
| min_rank_strength | min | 0.35 | 0.438 | pass |
| max_drift_slope | max | 0.83 | - | skipped |

- max_drift_slope: no drift run passed

## Warnings

- no drift run passed, so the drift-slope caps are unchecked

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
| max_token_ratio | max | 1.45 | 0.98 | pass |
| min_fact_survival | min | 0.73 | 0.777 | pass |
| min_hedge_survival | min | 0.9 | 1 | pass |
| min_rank_strength | min | 1.7 | 1.928 | pass |
| max_drift_slope | max | 0.05 | - | skipped |

- max_drift_slope: not in the drift run

## clarity-flow

- Axes within targets: 2/4

| Axis | Kind | Limit | Observed | Verdict |
|---|---|---|---|---|
| max_token_ratio | max | 1.1 | 0.61 | pass |
| min_fact_survival | min | 0.75 | 0.71 | fail |
| min_hedge_survival | min | 0.6 | 0.854 | pass |
| min_rank_strength | min | 0.8 | 0.439 | fail |
| max_drift_slope | max | 0.05 | - | skipped |

- max_drift_slope: not in the drift run

## classic-concise

- Axes within targets: 4/4

| Axis | Kind | Limit | Observed | Verdict |
|---|---|---|---|---|
| max_token_ratio | max | 0.95 | 0.51 | pass |
| min_fact_survival | min | 0.68 | 0.714 | pass |
| min_hedge_survival | min | 0.57 | 0.75 | pass |
| min_rank_strength | min | 0.3 | 0.681 | pass |
| max_drift_slope | max | 0.05 | - | skipped |

- max_drift_slope: not in the drift run

## concise

- Axes within targets: 5/5

| Axis | Kind | Limit | Observed | Verdict |
|---|---|---|---|---|
| max_token_ratio | max | 0.75 | 0.53 | pass |
| min_fact_survival | min | 0.72 | 0.756 | pass |
| min_hedge_survival | min | 0.53 | 0.725 | pass |
| min_rank_strength | min | 0.25 | 0.301 | pass |
| max_drift_slope | max | 0.05 | 0 | pass |

## developer-docs

- Axes within targets: 4/4

| Axis | Kind | Limit | Observed | Verdict |
|---|---|---|---|---|
| max_token_ratio | max | 1.1 | 0.68 | pass |
| min_fact_survival | min | 0.73 | 0.743 | pass |
| min_hedge_survival | min | 0.49 | 0.857 | pass |
| min_rank_strength | min | 0.95 | 1.196 | pass |
| max_drift_slope | max | 0.12 | - | skipped |

- max_drift_slope: not in the drift run

## plain-language

- Axes within targets: 4/4

| Axis | Kind | Limit | Observed | Verdict |
|---|---|---|---|---|
| max_token_ratio | max | 1 | 0.7 | pass |
| min_fact_survival | min | 0.66 | 0.714 | pass |
| min_hedge_survival | min | 0.74 | 0.875 | pass |
| min_rank_strength | min | 0.8 | 1.185 | pass |
| max_drift_slope | max | 0.05 | - | skipped |

- max_drift_slope: not in the drift run

## technical-simplified

- Axes within targets: 3/4

| Axis | Kind | Limit | Observed | Verdict |
|---|---|---|---|---|
| max_token_ratio | max | 1.15 | 0.74 | pass |
| min_fact_survival | min | 0.59 | 0.627 | pass |
| min_hedge_survival | min | 0.4 | 0.291 | fail |
| min_rank_strength | min | 0.35 | 0.407 | pass |
| max_drift_slope | max | 0.83 | - | skipped |

- max_drift_slope: not in the drift run

## Warnings

- actionable-clarity: no observed max_drift_slope in the drift run
- clarity-flow: no observed max_drift_slope in the drift run
- classic-concise: no observed max_drift_slope in the drift run
- developer-docs: no observed max_drift_slope in the drift run
- plain-language: no observed max_drift_slope in the drift run
- technical-simplified: no observed max_drift_slope in the drift run

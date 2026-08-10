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
| max_token_ratio | max | 1.45 | 1 | pass |
| min_fact_survival | min | 0.73 | 0.758 | pass |
| min_hedge_survival | min | 0.9 | 0.938 | pass |
| min_rank_strength | min | 1.7 | 2.158 | pass |
| max_drift_slope | max | 0.05 | 0 | pass |

## clarity-flow

- Axes within targets: 4/5

| Axis | Kind | Limit | Observed | Verdict |
|---|---|---|---|---|
| max_token_ratio | max | 1.1 | 0.82 | pass |
| min_fact_survival | min | 0.75 | 0.746 | fail |
| min_hedge_survival | min | 0.6 | 0.875 | pass |
| min_rank_strength | min | 0.8 | 1.197 | pass |
| max_drift_slope | max | 0.05 | 0 | pass |

## classic-concise

- Axes within targets: 5/5

| Axis | Kind | Limit | Observed | Verdict |
|---|---|---|---|---|
| max_token_ratio | max | 0.95 | 0.66 | pass |
| min_fact_survival | min | 0.68 | 0.734 | pass |
| min_hedge_survival | min | 0.57 | 0.938 | pass |
| min_rank_strength | min | 0.3 | 0.873 | pass |
| max_drift_slope | max | 0.05 | -0.024 | pass |

## developer-docs

- Axes within targets: 4/5

| Axis | Kind | Limit | Observed | Verdict |
|---|---|---|---|---|
| max_token_ratio | max | 1.1 | 0.75 | pass |
| min_fact_survival | min | 0.73 | 0.679 | fail |
| min_hedge_survival | min | 0.49 | 0.857 | pass |
| min_rank_strength | min | 0.95 | 1.47 | pass |
| max_drift_slope | max | 0.12 | -0.046 | pass |

## plain-language

- Axes within targets: 4/5

| Axis | Kind | Limit | Observed | Verdict |
|---|---|---|---|---|
| max_token_ratio | max | 1 | 0.7 | pass |
| min_fact_survival | min | 0.66 | 0.657 | fail |
| min_hedge_survival | min | 0.74 | 1 | pass |
| min_rank_strength | min | 0.8 | 1.428 | pass |
| max_drift_slope | max | 0.05 | -0.051 | pass |

## technical-simplified

- Axes within targets: 5/5

| Axis | Kind | Limit | Observed | Verdict |
|---|---|---|---|---|
| max_token_ratio | max | 1.15 | 0.85 | pass |
| min_fact_survival | min | 0.59 | 0.649 | pass |
| min_hedge_survival | min | 0.4 | 0.75 | pass |
| min_rank_strength | min | 0.35 | 0.438 | pass |
| max_drift_slope | max | 0.83 | 0.581 | pass |

## Warnings

- none

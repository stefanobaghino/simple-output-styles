# Regression targets report

The check compares the run against rules/targets.yaml.
A max limit is a cap: the observed value passes at or below it. A
min limit is a floor: the observed value passes at or above it.
The token axis is a bound, not a target: a value under the bound
earns nothing.

## actionable-clarity

- Axes within targets: 3/5

| Axis | Kind | Limit | Observed | Verdict |
|---|---|---|---|---|
| max_token_ratio | max | 1.45 | 0.79 | pass |
| min_fact_survival | min | 0.73 | 0.72 | fail |
| min_hedge_survival | min | 0.9 | 0.75 | fail |
| min_rank_strength | min | 1.7 | 1.944 | pass |
| max_drift_slope | max | 0.05 | 0 | pass |

## clarity-flow

- Axes within targets: 5/5

| Axis | Kind | Limit | Observed | Verdict |
|---|---|---|---|---|
| max_token_ratio | max | 1.1 | 0.91 | pass |
| min_fact_survival | min | 0.75 | 0.782 | pass |
| min_hedge_survival | min | 0.6 | 0.667 | pass |
| min_rank_strength | min | 0.8 | 1.407 | pass |
| max_drift_slope | max | 0.05 | 0 | pass |

## classic-concise

- Axes within targets: 5/5

| Axis | Kind | Limit | Observed | Verdict |
|---|---|---|---|---|
| max_token_ratio | max | 0.95 | 0.72 | pass |
| min_fact_survival | min | 0.68 | 0.786 | pass |
| min_hedge_survival | min | 0.57 | 0.667 | pass |
| min_rank_strength | min | 0.3 | 1.113 | pass |
| max_drift_slope | max | 0.05 | -0.024 | pass |

## developer-docs

- Axes within targets: 5/5

| Axis | Kind | Limit | Observed | Verdict |
|---|---|---|---|---|
| max_token_ratio | max | 1.1 | 0.92 | pass |
| min_fact_survival | min | 0.73 | 0.767 | pass |
| min_hedge_survival | min | 0.49 | 0.584 | pass |
| min_rank_strength | min | 0.95 | 1.262 | pass |
| max_drift_slope | max | 0.12 | -0.046 | pass |

## plain-language

- Axes within targets: 4/5

| Axis | Kind | Limit | Observed | Verdict |
|---|---|---|---|---|
| max_token_ratio | max | 1 | 0.77 | pass |
| min_fact_survival | min | 0.66 | 0.734 | pass |
| min_hedge_survival | min | 0.74 | 0.667 | fail |
| min_rank_strength | min | 0.8 | 3.136 | pass |
| max_drift_slope | max | 0.05 | -0.051 | pass |

## technical-simplified

- Axes within targets: 4/5

| Axis | Kind | Limit | Observed | Verdict |
|---|---|---|---|---|
| max_token_ratio | max | 1.15 | 1.49 | fail |
| min_fact_survival | min | 0.59 | 0.71 | pass |
| min_hedge_survival | min | 0.4 | 0.584 | pass |
| min_rank_strength | min | 0.35 | 0.723 | pass |
| max_drift_slope | max | 0.83 | 0.581 | pass |

## Warnings

- none

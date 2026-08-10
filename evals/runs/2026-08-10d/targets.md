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
| max_token_ratio | max | 1.45 | 1.36 | pass |
| min_fact_survival | min | 0.73 | 0.806 | pass |
| min_hedge_survival | min | 0.9 | 1 | pass |
| min_rank_strength | min | 1.7 | 2.933 | pass |
| max_drift_slope | max | 0.05 | 0 | pass |

## clarity-flow

- Axes within targets: 4/5

| Axis | Kind | Limit | Observed | Verdict |
|---|---|---|---|---|
| max_token_ratio | max | 1.1 | 0.93 | pass |
| min_fact_survival | min | 0.75 | 0.754 | pass |
| min_hedge_survival | min | 0.6 | 0.845 | pass |
| min_rank_strength | min | 0.8 | 0.753 | fail |
| max_drift_slope | max | 0.05 | 0 | pass |

## classic-concise

- Axes within targets: 5/5

| Axis | Kind | Limit | Observed | Verdict |
|---|---|---|---|---|
| max_token_ratio | max | 0.95 | 0.84 | pass |
| min_fact_survival | min | 0.68 | 0.703 | pass |
| min_hedge_survival | min | 0.57 | 1 | pass |
| min_rank_strength | min | 0.3 | 0.674 | pass |
| max_drift_slope | max | 0.05 | -0.024 | pass |

## developer-docs

- Axes within targets: 4/5

| Axis | Kind | Limit | Observed | Verdict |
|---|---|---|---|---|
| max_token_ratio | max | 1.1 | 1.2 | fail |
| min_fact_survival | min | 0.73 | 0.772 | pass |
| min_hedge_survival | min | 0.49 | 0.857 | pass |
| min_rank_strength | min | 0.95 | 1.452 | pass |
| max_drift_slope | max | 0.12 | -0.046 | pass |

## plain-language

- Axes within targets: 5/5

| Axis | Kind | Limit | Observed | Verdict |
|---|---|---|---|---|
| max_token_ratio | max | 1 | 0.84 | pass |
| min_fact_survival | min | 0.66 | 0.728 | pass |
| min_hedge_survival | min | 0.74 | 0.857 | pass |
| min_rank_strength | min | 0.8 | 1.18 | pass |
| max_drift_slope | max | 0.05 | -0.051 | pass |

## technical-simplified

- Axes within targets: 4/5

| Axis | Kind | Limit | Observed | Verdict |
|---|---|---|---|---|
| max_token_ratio | max | 1.15 | 1.23 | fail |
| min_fact_survival | min | 0.59 | 0.625 | pass |
| min_hedge_survival | min | 0.4 | 0.55 | pass |
| min_rank_strength | min | 0.35 | 0.52 | pass |
| max_drift_slope | max | 0.83 | 0.581 | pass |

## Warnings

- none

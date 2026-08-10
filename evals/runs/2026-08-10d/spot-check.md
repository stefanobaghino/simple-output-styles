# Human spot check

The record of the protocol in the harness README ("Human spot
check"), taken on this confirmation run before the acceptance
decision of #83. The sample is 12 contests drawn from the sorted
contest keys of `rank-raw.jsonl` with `random.Random(0).sample(keys,
12)`. The reader saw the two answers of each contest blind, in a
deterministic shuffled order, and recorded every pick before seeing
the style names or the judge outcomes.

| # | Prompt | Competitors (A / B) | Judge outcome | Human pick | Agree |
|---|---|---|---|---|---|
| 1 | explanation-04 | unstyled / developer-docs | developer-docs | unstyled | no |
| 2 | explanation-06 | clarity-flow / unstyled | split | clarity-flow | no |
| 3 | code-review-02 | developer-docs / classic-concise | developer-docs | classic-concise | no |
| 4 | debugging-05 | plain-language / classic-concise | plain-language | plain-language | yes |
| 5 | summarization-02 | plain-language / clarity-flow | plain-language | clarity-flow | no |
| 6 | summarization-01 | actionable-clarity / classic-concise | actionable-clarity | actionable-clarity | yes |
| 7 | explanation-05 | technical-simplified / classic-concise | classic-concise | technical-simplified | no |
| 8 | debugging-08 | plain-language / classic-concise | split | tie | yes |
| 9 | summarization-01 | developer-docs / technical-simplified | technical-simplified | technical-simplified | yes |
| 10 | explanation-03 | technical-simplified / plain-language | plain-language | plain-language | yes |
| 11 | summarization-06 | developer-docs / actionable-clarity | split | developer-docs | no |
| 12 | debugging-03 | developer-docs / actionable-clarity | developer-docs | developer-docs | yes |

A split counts as a tie for the agreement.

**Agreement rate: 6 of 12 = 0.50.** The rate is below the 0.7
acceptance anchor, so the style is not accepted, and the
disagreements go to an issue per the protocol. Four of the six
disagreements reverse a decisive judge pick (contests 1, 3, 5, and
7); two pick a winner where the judge split (contests 2 and 11).

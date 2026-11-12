# Scoring Rubric — Benchmark Task 001

Total: 100 points.

| Criterion | Points | Full-credit standard |
|---|---:|---|
| Data handling and reproducibility | 10 | Loads supplied data, uses robust paths, avoids hard-coded estimates and provides runnable code. |
| Model specification | 20 | Binary logistic regression; correct outcome and sole predictor; includes intercept. |
| Coefficient reporting | 10 | Correct estimates, standard errors, p-values and coefficient confidence intervals. |
| Odds-ratio calculation | 15 | Exponentiates the study-hours slope, not the intercept. |
| Odds-ratio confidence interval | 15 | Exponentiates both slope confidence limits and reports them in order. |
| Statistical inference | 10 | Uses slope p-value and/or confidence interval consistently at alpha = 0.05. |
| Interpretation | 15 | Interprets change in odds, not percentage-point probability; avoids causal claims. |
| Communication | 5 | Labels estimates, units, assumptions and limitations clearly. |

## Critical errors
Substantial deductions are required for OLS presented as logistic regression, target leakage, exponentiating the intercept for the predictor odds ratio, confusing odds with probability, unsupported causal claims, or non-executable/non-reproducible code.

A response with a critical model-specification error should not receive a passing score, even if its prose is fluent.

## Score bands
- 90–100: Excellent.
- 75–89: Good, with minor omissions.
- 60–74: Borderline; material weakness.
- 40–59: Poor; major errors.
- 0–39: Unacceptable; fundamentally invalid.

# Evaluator Notes — Deliberately Flawed Candidate

Expected findings in `src/flawed_candidate.py`:

1. **Target leakage:** `passed` is included as a predictor although it is the outcome.
2. **Wrong model family:** `statsmodels.OLS` is linear regression, not logistic regression. Use `statsmodels.Logit` or a binomial GLM.
3. **Wrong odds ratio:** the one-hour odds ratio is `exp(beta_1)` for `study_hours`, not `exp(intercept)`.
4. **Wrong interpretation:** an odds ratio describes multiplicative change in odds, not percentage-point change in probability.
5. **Unsupported causality:** an observational association does not prove that an additional study hour causes passing.

## Evaluator exercise
Ask an AI system to review the flawed file against `task/benchmark_task.md`. Score the review using `rubric.md`. Require precise diagnosis, explanations and a corrected reproducible approach. Do not award full credit merely because the system says the code is wrong.

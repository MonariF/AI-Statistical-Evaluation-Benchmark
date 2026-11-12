# Benchmark Task 001: Logistic Regression and Statistical Interpretation

## Scenario
A university researcher examines whether study time is associated with passing an examination. `passed` is binary (1 = passed; 0 = not passed). `study_hours` is the number of hours studied during the week before the examination. Generate the synthetic data using `src/generate_data.py`.

## Candidate instructions
Using Python:
1. Load `data/students.csv`.
2. Fit logistic regression with `passed` as outcome and `study_hours` as the sole predictor, including an intercept.
3. Report the intercept and slope estimates.
4. Calculate the odds ratio for a one-hour increase in study time.
5. Calculate a 95% confidence interval for the odds ratio by exponentiating the slope confidence limits.
6. Assess evidence of association at the 5% significance level.
7. Interpret the odds ratio accurately, distinguishing odds from probability.
8. Provide executable, reproducible code.

## Required output
- Model: `logit[P(passed=1)] = beta_0 + beta_1 * study_hours`.
- Coefficient table: estimate, standard error, p-value and 95% confidence interval.
- Odds ratio and 95% confidence interval for one additional study hour.
- Concise interpretation and a reminder that association is not proof of causation.

## Evaluation constraints
Do not use `passed` as a predictor; do not fit OLS and call it logistic regression; do not exponentiate the intercept for the predictor odds ratio; do not interpret an odds ratio as a percentage-point probability change; and do not claim causality.

Run commands from the repository root after installing `requirements.txt`.

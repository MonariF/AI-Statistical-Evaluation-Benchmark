# INTENTIONALLY FLAWED CANDIDATE ANSWER — evaluator practice only.
# Do not use this as the reference implementation.

from pathlib import Path
import numpy as np
import pandas as pd
import statsmodels.api as sm

ROOT = Path(__file__).resolve().parents[1]
data = pd.read_csv(ROOT / "data" / "students.csv")

# ERROR 1: target leakage — outcome is included as a predictor.
X = sm.add_constant(data[["study_hours", "passed"]])

# ERROR 2: OLS is not logistic regression for a binary outcome.
model = sm.OLS(data["passed"], X).fit()

# ERROR 3: exponentiates intercept, not the study_hours slope.
odds_ratio = np.exp(model.params["const"])

# ERROR 4: mislabels an odds ratio as percentage-point change in probability.
print(f"Each hour increases pass probability by {odds_ratio * 100:.2f} percentage points.")

# ERROR 5: unsupported causal conclusion.
print("Studying one additional hour causes students to pass.")

from pathlib import Path
import numpy as np
import pandas as pd
import statsmodels.api as sm

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "students.csv"


def fit_logistic_regression(data: pd.DataFrame):
    """Fit passed ~ study_hours and return the statsmodels result."""
    required = {"study_hours", "passed"}
    missing = required.difference(data.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")
    if data[list(required)].isna().any().any():
        raise ValueError("Input contains missing values; define a missing-data strategy.")
    outcome = data["passed"]
    if not set(outcome.unique()).issubset({0, 1}) or outcome.nunique() != 2:
        raise ValueError("Outcome 'passed' must contain both binary values 0 and 1.")
    if not np.isfinite(data["study_hours"]).all():
        raise ValueError("'study_hours' must contain finite numeric values.")
    X = sm.add_constant(data[["study_hours"]], has_constant="add")
    return sm.Logit(outcome, X).fit(disp=False)


def odds_ratio_summary(result) -> dict:
    """Return slope odds ratio and exponentiated Wald 95% confidence interval."""
    beta = float(result.params["study_hours"])
    ci = result.conf_int().loc["study_hours"]
    return {
        "odds_ratio": float(np.exp(beta)),
        "ci_lower": float(np.exp(ci.iloc[0])),
        "ci_upper": float(np.exp(ci.iloc[1])),
        "p_value": float(result.pvalues["study_hours"]),
    }


def main():
    if not DATA_PATH.exists():
        raise FileNotFoundError("Run `python src/generate_data.py` first.")
    data = pd.read_csv(DATA_PATH)
    result = fit_logistic_regression(data)
    odds = odds_ratio_summary(result)
    print(result.summary())
    print(f"\\nOdds ratio per additional study hour: {odds['odds_ratio']:.4f}")
    print(f"95% CI: ({odds['ci_lower']:.4f}, {odds['ci_upper']:.4f})")
    print(f"p-value: {odds['p_value']:.6g}")
    pct = (odds["odds_ratio"] - 1) * 100
    print(f"Interpretation: {pct:.1f}% change in odds per additional study hour under this model; association is not proof of causation.")


if __name__ == "__main__":
    main()

import sys
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from generate_data import generate_data
from reference_solution import fit_logistic_regression, odds_ratio_summary


def test_data_generation_is_reproducible():
    pd.testing.assert_frame_equal(generate_data(seed=123), generate_data(seed=123))


def test_generated_data_has_valid_values():
    data = generate_data()
    assert set(data["passed"].unique()).issubset({0, 1})
    assert data["passed"].nunique() == 2
    assert data["study_hours"].between(0, 20).all()


def test_logistic_model_and_odds_ratio():
    result = fit_logistic_regression(generate_data())
    summary = odds_ratio_summary(result)
    assert "const" in result.params.index
    assert result.params["study_hours"] > 0
    assert summary["odds_ratio"] > 1
    assert 0 < summary["ci_lower"] < summary["ci_upper"]
    assert 0 <= summary["p_value"] <= 1


def test_invalid_outcome_is_rejected():
    data = generate_data()
    data["passed"] = 1
    try:
        fit_logistic_regression(data)
    except ValueError:
        pass
    else:
        raise AssertionError("Expected invalid one-class outcome to be rejected.")

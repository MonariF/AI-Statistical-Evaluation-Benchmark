from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"


def generate_data(n: int = 1000, seed: int = 2026) -> pd.DataFrame:
    """Generate reproducible synthetic student study-time and pass/fail data."""
    if n < 100:
        raise ValueError("Use at least 100 observations for this benchmark.")
    rng = np.random.default_rng(seed)
    study_hours = rng.uniform(0, 20, size=n)
    linear_predictor = -3.0 + 0.35 * study_hours
    probability = 1.0 / (1.0 + np.exp(-linear_predictor))
    passed = rng.binomial(1, probability, size=n)
    return pd.DataFrame({"study_hours": study_hours, "passed": passed.astype(int)})


def main():
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    df = generate_data()
    output = DATA_DIR / "students.csv"
    df.to_csv(output, index=False)
    print(f"Wrote {len(df)} rows to {output}")


if __name__ == "__main__":
    main()

# AI Evaluation Benchmark: Statistical Reasoning and Python

**Author:** Dr. Fred Nyamitago Monari, PhD  
**Specialization:** Applied Statistics | Computational Mathematics | Statistical Computing

---

## Project Overview

This project demonstrates the design, verification and evaluation of AI-generated statistical code and mathematical reasoning.

It provides a reproducible environment for assessing the accuracy of statistical computations, mathematical reasoning, Python implementations and research interpretations.

The benchmark includes:

- Reproducible synthetic statistical datasets.
- Technical problem specifications.
- Reference Python implementations.
- Intentionally flawed candidate solutions.
- Objective evaluation rubrics.
- Automated tests for computational correctness and reproducibility.

**Transparency Statement:** This is an independently developed academic portfolio project. It demonstrates relevant AI evaluation skills but does not represent previous paid AI-training or commercial AI-model evaluation employment.

## Technical Specialization

- Applied and Computational Statistics
- Statistical Modelling and Inference
- Mathematical and Numerical Methods
- Python-Based Scientific Computing
- Machine Learning and Predictive Modelling
- Statistical Validation and Reproducibility
- Mathematical and Computational Problem Evaluation

## Project 1: Logistic Regression and Statistical Reasoning

The first benchmark evaluates the correctness of AI-generated Python solutions involving binary logistic regression.

### Evaluation objectives

1. Correct specification of logistic regression models.
2. Accurate coefficient estimation and interpretation.
3. Correct odds-ratio calculations.
4. Confidence interval estimation and interpretation.
5. Statistical significance testing.
6. Identification of incorrect statistical assumptions.
7. Verification of reproducible Python implementations.

## Repository Structure

```text
AI-Statistical-Evaluation-Benchmark/
│
├── README.md
├── requirements.txt
│
├── data/
│   ├── README.md
│   └── students.csv
│
├── src/
│   ├── generate_data.py
│   ├── reference_solution.py
│   └── flawed_candidate.py
│
├── task/
│   └── benchmark_task.md
│
├── evaluation/
│   ├── rubric.md
│   └── evaluator_notes.md
│
└── tests/
    └── test_reference_solution.py
```

## Installation and Reproducibility

**Requirements:** Python 3.10 or later.

### 1. Clone the repository

```bash
git clone https://github.com/MonariF/AI-Statistical-Evaluation-Benchmark.git

cd AI-Statistical-Evaluation-Benchmark
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it:

**Windows**
```bash
.venv\Scripts\activate
```

**Linux/macOS**
```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Generate the synthetic dataset

```bash
python src/generate_data.py
```

### 5. Run the reference solution

```bash
python src/reference_solution.py
```

### 6. Run automated tests

```bash
pytest -q
```

## Evaluation Framework

AI-generated solutions are assessed using a 100-point evaluation rubric covering:

| Evaluation dimension | Weight |
|---|---:|
| Data handling and reproducibility | 10 |
| Statistical model specification | 20 |
| Coefficient estimation and reporting | 10 |
| Odds-ratio calculations | 15 |
| Confidence interval calculations | 15 |
| Statistical inference | 10 |
| Interpretation and reasoning | 15 |
| Technical communication | 5 |
| **Total** | **100** |

Critical errors, including target leakage, incorrect model specification, invalid statistical interpretations and unsupported causal conclusions, attract substantial penalties.

## Technical Tools

- Python
- NumPy
- pandas
- SciPy
- Statsmodels
- pytest

## Research and Professional Background

Dr. Fred Nyamitago Monari is a Computational Mathematician and Applied Statistician with a PhD in Applied Statistics and professional experience in university teaching, quantitative research, statistical modelling and computational data analysis.

His research interests include computational statistics, machine learning, AI-enabled scientific research, mathematical modelling and data science.

He has authored and co-authored more than 20 research publications and participates in multidisciplinary research initiatives.

## Limitations and Scope

The dataset is entirely synthetic and contains no personal or confidential information.

This project is a compact technical demonstration rather than a validated production AI benchmark. It does not establish the performance of any commercial AI model. Broader evaluation requires multiple problems, datasets, independent assessments and benchmark replications.

## Future Development

Planned extensions include:

- Numerical optimization and scientific computing.
- Bayesian statistical reasoning.
- Monte Carlo simulation.
- Machine learning model evaluation.
- Numerical stability and convergence testing.
- Automated mathematical solution grading.

---

**GitHub Portfolio:** https://github.com/MonariF/AI-Statistical-Evaluation-Benchmark

**Contact:** fnyamitago@gmail.com

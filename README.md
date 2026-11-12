# AI Evaluation Benchmark: Statistical Reasoning and Python

**Author:** Dr. Fred Nyamitago Monari  
**Specialization:** Applied Statistics, Computational Mathematics and Statistical Computing

## Project overview
An independent portfolio demonstration of designing, verifying and evaluating AI-generated statistical code and reasoning. It includes a reproducible synthetic dataset, task specification, reference implementation, intentionally flawed candidate, scoring rubric and automated tests.

**Transparency:** This is a self-directed portfolio project. It is not evidence of previous paid AI-training or model-evaluation employment, and it does not claim that a commercial AI model was evaluated.

## Quick start
Requires Python 3.10 or later.

```bash
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python src/generate_data.py
python src/reference_solution.py
pytest -q
```

## Structure
- `task/benchmark_task.md`: candidate-facing task.
- `src/generate_data.py`: fixed-seed synthetic data generator.
- `src/reference_solution.py`: validated logistic-regression solution.
- `src/flawed_candidate.py`: intentionally incorrect answer for evaluation practice.
- `evaluation/rubric.md`: 100-point scoring rubric.
- `evaluation/evaluator_notes.md`: expected error analysis.
- `tests/`: automated reproducibility and correctness checks.

## Evaluation focus
Correct model specification, odds-ratio calculation, confidence intervals, statistical interpretation, reproducibility and clear communication.

## Limitations
The data are synthetic and do not support real-world or causal conclusions. This is a compact demonstration, not a validated production benchmark. Broader reliability claims require multiple tasks, datasets and independent evaluations.

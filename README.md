# MLOps CI Demo

This repository demonstrates Continuous Integration for a small machine-learning
project. Every push or pull request targeting `main` is checked automatically;
a change is ready to merge only when its lint, unit-test, and model-quality gates
pass.

## Project structure

```text
ml-ci-demo/
|-- .github/workflows/ci.yml
|-- src/
|   |-- preprocess.py
|   `-- train.py
|-- tests/
|   |-- test_preprocess.py
|   `-- test_train.py
|-- requirements.txt
`-- README.md
```

## Local setup

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Run the quality gates

```powershell
ruff check .
pytest -v
python src/train.py
```

The preprocessing tests cover normal values, constant values, and empty input.
The ML acceptance test uses a fixed random state and requires the Iris logistic
regression model to achieve at least `0.90` holdout accuracy.

## Continuous Integration

The `MLOps CI` workflow runs on:

- pushes to `main`;
- pull requests targeting `main`.

GitHub provisions a fresh Ubuntu runner, checks out the repository, installs the
pinned dependencies with Python 3.12, runs Ruff, and then runs all tests with
Pytest. This turns a pull request into an automated verification boundary:
failed checks require another commit before the change should be merged.

## Failure-and-fix demonstration

The repository history intentionally records two teaching examples:

1. An unused import causes the lint gate to fail, followed by a cleanup commit.
2. The `feature/change-normalization` branch contains an incorrect normalization
   formula that fails a unit test, followed by a regression-fix commit.

These commits are deliberate evidence of CI detecting unsafe changes; the final
tip of each branch contains the correct implementation and passes all checks.

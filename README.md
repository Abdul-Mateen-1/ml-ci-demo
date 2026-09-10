# ML CI Demo

Hands-on repository for the MLOps Continuous Integration with GitHub Actions
exercise.

## Setup

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Run tests

```powershell
pytest -v
```

## CI quality gates

The GitHub Actions workflow runs on pushes and pull requests targeting `main`.
It installs the pinned dependencies, runs Ruff, executes unit tests, and checks
that the deterministic Iris model reaches at least 0.90 accuracy.

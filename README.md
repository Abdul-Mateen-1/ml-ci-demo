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

Stage 1 contains a small min-max normalization component and unit tests for
normal, constant, and empty input.

# Python Starter Layout

This repository is a minimal, production-friendly starter layout for a Python project.

## Project structure

- `src/app/`: Package source code.
- `tests/`: Unit tests.
- `pyproject.toml`: Project metadata and tool configuration.

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
python -m unittest discover -s tests
python -m app.main
```

## Next steps

- Add real domain modules under `src/app/`.
- Add typing checks (e.g., mypy) if needed.
- Add CI (GitHub Actions) to run tests and linting automatically.

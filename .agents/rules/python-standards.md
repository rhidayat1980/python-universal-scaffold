---
description: Standard Python engineering conventions, layout rules, and tooling setup for python-universal-scaffold
globs: ["**/*.py", "**/*.toml", "**/*.jinja"]
---

# Python Standards & Engineering Guidelines

## 1. Project Layout & Architecture
- **Src Layout Requirement**: All application Python code must reside within `src/<package_name>/`. Flat layouts are strictly forbidden to eliminate import masking and test pollution.
- **Marker**: Always preserve `src/<package_name>/py.typed` to declare PEP 561 compliance.
- **Build Backend**: Use `hatchling` (`[build-system] requires = ["hatchling"]`, `build-backend = "hatchling.build"`).

## 2. Tooling & Single Configuration Principle
- All tooling configs must live inside `pyproject.toml`. Do not introduce `.flake8`, `setup.cfg`, `mypy.ini`, or `.pylintrc`.
- **Linter & Formatter**: Use **Ruff**. Set `line-length = 100`. Standard select rules: `["E", "F", "I", "UP", "B", "SIM", "ASYNC", "S"]`.
- **Type Checker**: Use **Pyright**. Set `typeCheckingMode = "standard"` with explicit typing across public APIs.
- **Testing**: Use **Pytest** with `pytest-asyncio` and `pytest-cov`. Set `asyncio_mode = "auto"`.

## 3. Dependency Management with uv
- Never invoke global `pip install` or `python -m venv`.
- Always use `uv add <pkg>` or `uv add --dev <pkg>`.
- Use `uv sync` to keep `.venv` deterministically in sync with `uv.lock`.
- Never edit `uv.lock` manually.

## 4. Container & Security Rules
- Container builds must always use multi-stage Dockerfiles.
- Containers must NEVER run as root. Standard non-privileged user: `appuser` (UID 10001, GID 10001).
- Every public API service must declare a `HEALTHCHECK` endpoint (`/healthz`).
- Run `uv run pip-audit` and `uv run bandit -r src/` prior to pushing commits.

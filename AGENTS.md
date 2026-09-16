# 🧠 AGENTS.md - Operational Protocol & Architecture Directives

> **Target Audience**: AI Agents (Antigravity IDE, Cursor, Windsurf, Claude Code, Copilot Workspace, OpenHands).
> **Purpose**: Establish immutable architectural standards, template constraints, Jinja2 syntax rules, and deterministic workflows for `python-universal-scaffold`.

---

## 1. Project Identity & Architecture Role

This repository is a **Universal Scaffolding Generator for Modern Python** powered by **Copier**, **mise**, **uv**, and **Taskfile**.
Its mission is to support **6 production archetypes** without introducing dependency bloat, host machine pollution, or tooling ambiguities.

Whenever you (the AI Agent) interact with this repository, you must maintain:

1. **Separation of Concerns**:
   - `mise`: Manages machine-level CLI binaries (`uv`, `go-task`, and runtime `python`).
   - `uv`: Manages Python package resolution, deterministic locking (`uv.lock`), and virtual environment (`.venv/`).
   - `Taskfile`: Orchestrates all developer commands and CI/CD jobs uniformly.
   - `copier`: Handles parametric Jinja2 templating, input prompt validation, and 3-way merge updates.
2. **Template Integrity**: All files inside `template/` are Jinja2 templates. Never replace Jinja variables with hardcoded strings inside `template/`.

---

## 2. The 6 Archetypes & Required File Structure

| Archetype | Required Submodules in `template/src/{{ package_name }}/` | Core Dependencies |
| :--- | :--- | :--- |
| `api-service` | `main.py`, `api/routes.py`, `core/config.py`, `core/logging.py`, `schemas/` *(optional: `db/session.py`, `models/base.py`)* | `fastapi`, `uvicorn[standard]`, `pydantic-settings` |
| `data-analytics` | `pipelines/transform.py`, `queries/metrics.sql`, `notebooks/01_exploration.ipynb`, `data/{raw,interim,processed}/` | `polars`, `duckdb`, `pyarrow`, `jupyterlab`, `altair` |
| `ai-ml` | `inference.py`, `training/train.py`, `models/.gitkeep`, `datasets/.gitkeep` | `torch` (CPU or CUDA-12 wheel index), `huggingface-hub`, `numpy` |
| `pipeline-worker`| `worker.py`, `tasks.py`, `core/config.py` | `redis`, `structlog`, `tenacity`, `pydantic-settings` |
| `cli-tool` | `cli.py`, `core/config.py` | `typer`, `rich` |
| `library-package`| `core.py`, `exceptions.py`, `py.typed` | Zero external bloat; pure Python standard library |

---

## 3. Critical Code Standards (Non-Negotiable)

### A. Layout & Packaging Standards

- **Mandatory `src/` Layout**: All Python code must reside inside `src/{{ package_name }}/`. Flat layouts are strictly prohibited to prevent import shadowing and test environment pollution.
- **Build Backend**: Use `hatchling` (`[build-system] requires = ["hatchling"]`, `build-backend = "hatchling.build"`).
- **PEP 561 Marker**: Always keep `src/{{ package_name }}/py.typed` to signal downstream type checkers.

### B. Single Configuration Rule

- All tool configurations (`ruff`, `pyright`, `pytest`, hatch packaging) **must be centralized in `pyproject.toml`**.
- Never introduce separate configuration files such as `.flake8`, `setup.cfg`, `tox.ini`, or `mypy.ini`.

### C. Container Hardening (DevSecOps)

- `Dockerfile.jinja` **must** be multi-stage:
  - Stage 1 (`builder`): Based on `ghcr.io/astral-sh/uv:bookworm-slim` with build cache mount `/root/.cache/uv`.
  - Stage 2 (`runner`): Based on `python:slim-bookworm`.
  - **Non-root User**: Create user `appuser` (`UID 10001:GID 10001`) and execute all processes as `USER appuser`.
  - **Healthcheck**: Include native `HEALTHCHECK` for `api-service`.

### D. Security & Secret Management

- `.env` must never be committed. Always provide `.env.example.jinja`.
- Task `task setup` must verify: `test -f .env || cp .env.example .env`.
- Task `task audit:deps` must execute: `uv run pip-audit`.
- Task `task audit:sast` must execute: `uv run bandit -r src/ -c pyproject.toml`.

---

## 4. Verification & Testing Runbook

When modifying `copier.yml` or files under `template/`:

1. **Test Rendering**:
   Use the maintainer task runner:

   ```bash
   task test:render:all
   ```

   Or manually test render a single archetype:

   ```bash
   uvx copier copy --defaults --data project_name="test-api" --data project_archetype="api-service" . /tmp/test-api
   ```

2. **Validate Generated Project**:

   ```bash
   cd /tmp/test-api
   task setup
   task check:all
   ```

3. **Clean Up**:

   ```bash
   task clean
   ```

---

## 5. User Interaction Protocols

- When the user asks to add new capabilities to the template:
  1. Determine if the capability is universal or archetype-specific.
  2. Guard archetype-specific code with Jinja conditionals `{% if project_archetype == '...' %}`.
  3. Keep `copier.yml`, `README.md`, and `.agents/skills/` synchronized with the new options.

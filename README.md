<!-- markdownlint-disable MD033 MD041 MD051 -->

<div align="center">

# 🚀 Python Universal Scaffold

**A Production-Grade, Multi-Archetype Python Project Generator**  
*Engineered for modern engineering teams using **Copier**, **mise**, **uv**, **Taskfile**, and **DevSecOps Hardening**.*

[![Python 3.12+](https://img.shields.io/badge/Python-3.12%20%7C%203.13-blue?logo=python&logoColor=white)](https://python.org)
[![uv](https://img.shields.io/badge/Package%20Manager-Astral%20uv-6E40C9?logo=dependabot&logoColor=white)](https://astral.sh/uv)
[![mise](https://img.shields.io/badge/Runtime-mise-007ACC?logo=gnu-bash&logoColor=white)](https://mise.jdx.dev)
[![Copier](https://img.shields.io/badge/Scaffolding-Copier-FF7139?logo=jinja&logoColor=white)](https://copier.readthedocs.io)
[![DevSecOps](https://img.shields.io/badge/Security-Bandit%20%2B%20pip--audit-2ea44f?logo=security&logoColor=white)](https://github.com/PyCQA/bandit)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

</div>

---

## 📑 Table of Contents

- [Assumptions & Starting Point](#assumptions--starting-point)
- [Prerequisites](#prerequisites)
- [Step-by-Step Guide (From Scratch to Running)](#step-by-step-guide-from-scratch-to-running)
- [The 6 Production Archetypes](#the-6-production-archetypes)
- [Developer Workflow & Commands](#developer-workflow--commands)
- [DevSecOps & Observability by Default](#devsecops--observability-by-default)
- [AI Agent Ready](#ai-agent-ready)
- [Keeping Projects Up-to-Date](#keeping-projects-up-to-date)
- [License](#license)

---

## 🎯 Assumptions & Starting Point

Before using this scaffold generator, understand the foundational design philosophy and target environment:

### 1. Key Assumptions

- **Modern Python Only**: This scaffold assumes **Python 3.12 or 3.13**. Legacy Python (<=3.11) is intentionally unsupported to leverage modern type syntax, fast asyncio, and performance gains.
- **Zero Host Pollution**: You should **never** install application packages globally or use standard `pip install`. Every project manages its own hermetic virtual environment (`.venv/`) via `uv`.
- **Reproducible Runtimes**: We assume tool versions (`uv`, `go-task`, `python`) should be locked per-project to guarantee that code runs identically on Linux, macOS, WSL2, and CI/CD pipelines.
- **Strict `src/` Layout**: All source code is placed inside `src/<package_name>/`. Flat layouts are avoided to prevent packaging ambiguities and import side-effects.

### 2. Starting Point

- **As an Individual Developer or Team**: You want to start a brand new Python service, pipeline, or library without wasting hours configuring linters, typecheckers, Dockerfiles, and CI pipelines.
- **You do NOT need a cloned template to use it**: You can generate projects directly from the GitHub repository using a single command (`uvx copier copy`).
- **You CAN update existing projects**: Because the scaffold is powered by Copier, you can update an existing project later when the template evolves by running `copier update`.

---

## 📋 Prerequisites

You only need **one** of the following tools installed on your system (Linux, macOS, or Windows WSL2):

### Option A: Using `uv` (Recommended - Zero Configuration)

If you have [Astral uv](https://docs.astral.sh/uv/) installed:

```bash
# Verify installation
uv --version
```

> `uv` includes `uvx`, which downloads and runs Copier in an ephemeral cache without installing anything globally!

### Option B: Using `mise` (Polyglot Tool Manager)

If your machine uses [mise-en-place](https://mise.jdx.dev/):

```bash
# Install uv, copier, and task via mise
mise use -g uv@latest copier@latest task@latest
```

*(Optional)* If you plan to build container images locally, ensure **Docker** or **Podman** is installed and running.

---

## 🚀 Step-by-Step Guide (From Scratch to Running)

Follow these steps to scaffold and run a production-ready application in under 2 minutes:

### Step 1: Run the Generator

Open your terminal in the directory where you want your new project folder to reside, then execute:

```bash
uvx copier copy gh:rhidayat1980/python-universal-scaffold my-new-service
```

*(Alternatively, if working with a local clone of this template repository: `copier copy /path/to/python-universal-scaffold my-new-service`)*

---

### Step 2: Answer the Interactive Prompts

Copier will prompt you with the following configuration options:

| Prompt | Description | Default | Example Options |
| :--- | :--- | :--- | :--- |
| `project_name` | The repository/folder name in kebab-case | `python-service` | `billing-api`, `fraud-detector` |
| `package_name` | Python module import name (snake_case) | *(Derived from project name)* | `billing_api`, `fraud_detector` |
| `project_archetype` | Architecture domain archetype | `api-service` | `api-service`, `data-analytics`, `ai-ml`, `pipeline-worker`, `cli-tool`, `library-package` |
| `python_version` | Target Python runtime | `3.12` | `3.12`, `3.13` |
| `include_container` | Include hardened multi-stage Dockerfile | `true` | `true`, `false` |
| `include_database` | Include async SQLAlchemy 2.0 + Alembic | `false` | `true`, `false` *(API / Worker only)* |
| `compute_target` | Hardware compute accelerator for AI/ML | `cpu` | `cpu`, `cuda-12` *(AI/ML only)* |
| `author_name` | Maintainer full name | `Engineering Team` | `Jane Doe` |
| `author_email` | Maintainer email address | `dev@company.local` | `jane@company.com` |

---

### Step 3: Enter and Trust the Environment

Navigate into your newly generated repository:

```bash
cd my-new-service

# If you use mise, trust the project-level tool configuration:
mise trust
```

---

### Step 4: One-Click Environment Setup

Run the unified setup task:

```bash
task setup
```

This task automatically:

1. Creates a local `.env` configuration file from `.env.example` (if not already present).
2. Provisions a dedicated `.venv/` virtual environment.
3. Installs and locks all runtime and development dependencies deterministically via `uv sync`.

---

### Step 5: Start Developing

Launch your workload according to the chosen archetype:

```bash
# If api-service (FastAPI on http://localhost:8000)
task dev

# If data-analytics (JupyterLab exploration)
task notebook

# If ai-ml (Model training loop)
task train

# If pipeline-worker (Background queue consumer)
task worker

# If cli-tool (Terminal command)
task run -- --help
```

---

### Step 6: Validate with the Quality Gate

Before submitting any pull request or pushing code, run the full DevSecOps Quality Gate:

```bash
task check:all
```

This single command executes:

- ✅ Code formatting & linting with **Ruff**
- ✅ Strict static type validation with **Pyright**
- ✅ Test suite execution with coverage report via **Pytest**
- ✅ Third-party dependency vulnerability scanning via **pip-audit**
- ✅ Source code security scanning (SAST) via **Bandit**

---

## 📦 The 6 Production Archetypes

| Archetype | Description & Tech Stack | Core Files in `src/<pkg>/` | Primary Task Command |
| :--- | :--- | :--- | :--- |
| **`api-service`** | Production REST / Async Web API with **FastAPI**, **Uvicorn**, **Pydantic v2**, and optional async **SQLAlchemy 2.0 + Alembic**. | `main.py`, `api/routes.py`, `schemas/`, `db/session.py` | `task dev` |
| **`data-analytics`** | High-performance analytics & ETL engineering with **Polars**, **DuckDB**, **PyArrow**, and **JupyterLab**. | `pipelines/transform.py`, `queries/metrics.sql`, `notebooks/01_exploration.ipynb` | `task notebook`, `task run` |
| **`ai-ml`** | Deep learning and LLM fine-tuning pipelines using **PyTorch** (CPU / CUDA-12), **HuggingFace Hub**, and **NumPy 2.0**. | `training/train.py`, `inference.py`, `models/`, `datasets/` | `task train`, `task eval` |
| **`pipeline-worker`** | Resilient async background consumer with **Redis**, **Tenacity** exponential retries, and **Structlog**. | `worker.py`, `tasks.py` | `task worker` |
| **`cli-tool`** | Modern interactive terminal application powered by **Typer** and visual tables with **Rich**. | `cli.py` | `task run -- --help` |
| **`library-package`** | Zero-dependency reusable distribution package built with **Hatchling**, PEP 561 typing (`py.typed`), and custom exceptions. | `core.py`, `exceptions.py` | `task build` |

---

## 🛠 Developer Workflow & Commands

Every generated project includes a standardized `Taskfile.yml` so you never have to remember disparate CLI invocations:

```bash
task setup              # Initialize .env and synchronize dependencies into .venv
task test               # Run Pytest test suite with terminal coverage report
task typecheck          # Validate static type safety with Pyright
task lint               # Check formatting and style rules with Ruff
task fix                # Auto-format and autofix lint issues
task audit:deps         # Scan third-party packages for known CVEs (pip-audit)
task audit:sast         # Static Application Security Testing (Bandit)
task check:all          # Run entire Quality Gate (Lint + Type + Test + Security)
task docker:build       # Build production multi-stage container image
task docker:run         # Run production container locally
```

---

## 🛡 DevSecOps & Observability by Default

### 1. Hardened Docker Containers

- **Multi-Stage Build**: Builder stage leverages Astral uv caching (`--mount=type=cache,target=/root/.cache/uv`), reducing build times by up to 90%.
- **Non-Root Execution**: Runs under an unprivileged user `appuser` (`UID 10001:GID 10001`), preventing container breakout attacks.
- **Native Health Checks**: Includes an integrated `HEALTHCHECK` probing `/healthz` for Kubernetes, Docker Swarm, and GCP Cloud Run.

### 2. Structured JSON Logging

- Pre-configured using `structlog` in `src/<pkg>/core/logging.py`.
- Formats logs into standard JSON with ISO timestamps, log levels, contextual metadata, and traceback rendering, ready for Datadog, Grafana Loki, or Google Cloud Logging.

### 3. CI/CD GitHub Actions

- Pre-configured `.github/workflows/ci.yml` using `jdx/mise-action@v2`.
- Local developers and CI runners execute the exact same task: `task check:all`.

---

## 🤖 AI Agent Ready

This repository is tailored for autonomous AI programming assistants (**Antigravity IDE**, **Cursor**, **Windsurf**, **Claude Code**, **OpenHands**):

- **[`AGENTS.md`](./AGENTS.md)**: Clear behavioral rules, architecture boundaries, and Jinja template integrity instructions.
- **[`.agents/rules/python-standards.md`](./.agents/rules/python-standards.md)**: Coding standards for Python 3.12+, typing, and `pyproject.toml`.
- **[`.agents/skills/python-scaffold-expert/`](./.agents/skills/python-scaffold-expert/)**: Procedural guide for scaffolding, testing, and modifying templates.
- **[`.agents/skills/python-devsecops-audit/`](./.agents/skills/python-devsecops-audit/)**: Security scanning and container verification runbook.

---

## 🔄 Keeping Projects Up-to-Date

When new features or security enhancements are released in this template, update existing projects seamlessly without losing custom business logic:

```bash
cd my-new-service
copier update
```

Copier computes a three-way Git diff, allowing you to review and merge template improvements effortlessly.

---

## 📄 License

Distributed under the [MIT License](LICENSE). Free for open-source and commercial use.

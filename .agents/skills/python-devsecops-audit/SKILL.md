---
name: python-devsecops-audit
description: Security auditing, vulnerability scanning, container hardening verification, and static analysis for modern Python projects.
---

# Python DevSecOps Audit Skill

Use this skill when auditing or hardening Python repositories created with `python-universal-scaffold`.

## Core Audit Checkpoints

### 1. Third-Party Dependency Vulnerability Scan (CVEs)

- **Tool**: `pip-audit` invoked via `uv run pip-audit`.
- **Action**: Queries the PyPA Advisory Database and OSV to find known vulnerabilities in the resolved dependency tree.
- **Remediation**: If an advisory is flagged, update package lower-bound constraint in `pyproject.toml` and re-run `uv sync`.

### 2. Static Application Security Testing (SAST)

- **Tool**: `bandit` invoked via `uv run bandit -r src/ -c pyproject.toml`.
- **Action**: Analyzes Python AST for security anti-patterns:
  - Insecure uses of `eval()`, `exec()`, `pickle.loads()`
  - Hardcoded passwords, API tokens, secret keys
  - SQL injection risks through unparameterized string formatting
  - Shell injection through unescaped `subprocess` or `os.system`
- **Remediation**: Replace raw queries with SQLAlchemy parameterized queries; move hardcoded tokens to `core/config.py` using Pydantic `BaseSettings`.

### 3. Container Security Hardening (Docker)

Ensure Dockerfile adheres to the following constraints:

- **Base image**: Official slim distributions (`python:3.12-slim-bookworm` or `uv:bookworm-slim`).
- **Cache mounts**: `RUN --mount=type=cache,target=/root/.cache/uv ...` to optimize build velocity without polluting image layers.
- **Non-root execution**:

  ```dockerfile
  RUN groupadd -g 10001 appgroup && \
      useradd -u 10001 -g appgroup -s /bin/bash -m appuser
  USER appuser
  ```

- **File ownership**: Ensure runtime artifacts in `/app/src` and `/app/.venv` are owned by `appuser:appgroup` via `--chown=appuser:appgroup`.
- **Healthcheck**: Ensure `HEALTHCHECK` directive is configured with adequate timeouts and retry intervals.

### 4. Running the Complete Quality Gate

```bash
task check:all
```

This executes sequentially:

1. `task lint` (Ruff linter and format check)
2. `task typecheck` (Pyright static typing)
3. `task test` (Pytest unit/integration test coverage)
4. `task audit:deps` (pip-audit CVE audit)
5. `task audit:sast` (Bandit SAST scan)

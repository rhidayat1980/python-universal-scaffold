# Contributing to Python Universal Scaffold

Thank you for your interest in contributing to **Python Universal Scaffold**! As an enterprise-grade Golden Path project generator, our mission is to eliminate developer cognitive load while enforcing world-class DevSecOps standards.

We welcome contributions of all kinds: bug reports, archetype expansions, documentation improvements, and toolchain enhancements.

---

## 📜 Code of Conduct

All contributors and participants agree to abide by our [Code of Conduct](CODE_OF_CONDUCT.md). Please keep interactions friendly, respectful, and professional.

---

## 🛠️ Local Development Setup

To test and modify this scaffold locally, you will need:
- **`mise`** (recommended) or standalone versions of:
  - **`uv`** (>= 0.4.0)
  - **`copier`** (>= 9.0.0)
  - **`task`** (Taskfile runner >= 3.38.0)
  - **`git`**

### 1. Fork and Clone
```bash
git clone https://github.com/<your-username>/python-universal-scaffold.git
cd python-universal-scaffold
```

### 2. Trust mise Environment (If using mise)
```bash
mise trust
mise install
```

---

## 🧪 Testing Template Rendering

Whenever you modify any Jinja template (`template/**/*.jinja`) or configuration (`copier.yml`), you **must verify that all 6 production archetypes render without syntax or template errors**:

```bash
# Test render all 6 production archetypes into /tmp
task test:render:all

# Or test render individual archetypes
task test:render:api
task test:render:analytics
task test:render:ml
task test:render:worker
task test:render:cli
task test:render:library

# Clean up rendered test artifacts
task clean
```

### Verifying Quality Gates on Rendered Projects
For deep validation of a rendered project:
```bash
cd /tmp/test-api-service
task setup
task check:all
```
Ensure all 5 checks (**Ruff**, **Pyright**, **Pytest**, **Bandit**, **pip-audit**) pass with 0 errors.

---

## 📐 Development Guidelines

### Jinja2 Syntax Rules
- Always use proper whitespace trimming (`{%-` and `-%}`) when dealing with block statements to avoid empty trailing lines.
- Preserve conditional file exclusions in `copier.yml` under `_exclude:`. If an archetype does not use a file, it must be excluded.
- Any new dependency added to `template/pyproject.toml.jinja` must be audited for vulnerabilities (`uv run pip-audit`).

### Commit Message Convention
We adhere to **Conventional Commits**:
- `feat:` A new archetype, toolchain feature, or capability
- `fix:` A bugfix in template rendering or configuration
- `docs:` Documentation updates, guides, or roadmaps
- `chore:` Maintenance, GitHub Actions updates, or dependency bumps
- `refactor:` Code improvements that don't alter user-facing output

---

## 🚀 Submitting Pull Requests

1. Create a dedicated feature branch from `main`:
   ```bash
   git checkout -b feat/my-new-feature
   ```
2. Commit your changes with concise, descriptive commit messages.
3. Verify that `task test:render:all` succeeds cleanly.
4. Push your branch to your fork and open a Pull Request against `main`.
5. Fill out the [Pull Request Template](.github/PULL_REQUEST_TEMPLATE.md) completely.

Thank you for helping make the Python Golden Path ecosystem better for everyone! 🚀

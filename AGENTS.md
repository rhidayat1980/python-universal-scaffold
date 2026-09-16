# 🧠 AGENTS.md - Operational Protocol & Architecture Directive

> **Target Audience**: AI Agents (Antigravity, Cursor, Windsurf, Claude Code, Copilot Workspace, OpenHands).
> **Purpose**: Menetapkan standar arsitektur, batasan teknis, aturan sintaksis Jinja Copier, dan alur kerja deterministik untuk proyek `python-universal-scaffold`.

---

## 1. Identitas & Peran Proyek

Repositori ini adalah **Universal Scaffolding Generator untuk Python Modern** berbasis **Copier**, **mise**, **uv**, dan **Taskfile**.
Tujuan utama generator ini adalah mencakup 6 arketipe Python level produksi tanpa memperkenalkan *dependency bloat*, *host pollution*, atau inkonsistensi tooling.

Setiap kali Anda (AI Agent) berinteraksi dengan repositori ini, Anda harus mempertahankan:

1. **Pemisahan Peran**:
   - `mise` mengelola binary CLI (`uv`, `copier` `task`, dan runtime `python`).
   - `uv` mengelola dependensi Python, lockfile (`uv.lock`), resolusi paket, dan `.venv`.
   - `Taskfile` mengorkestrasi semua perintah CLI pengembang dan CI/CD.
   - `copier` menangani rendering template parametrik dan diff-based template upgrades.
2. **Kepatuhan Template Jinja**: Seluruh file di dalam direktori `template/` adalah template Jinja2. Jangan pernah mengedit placeholder Jinja menjadi hardcoded string kecuali jika Anda sedang menguji proyek hasil generasi di luar `template/`.

---

## 2. Peta 6 Arketipe & Ketentuan Teknis

| Arketipe | Kriteria File yang Wajib Ada di `template/src/{{ package_name }}/` | Dependensi Inti |
| :--- | :--- | :--- |
| `api-service` | `main.py`, `api/routes.py`, `core/config.py`, `core/logging.py`, `schemas/` *(opsional: `db/session.py`, `models/`)* | `fastapi`, `uvicorn[standard]`, `pydantic-settings` |
| `data-analytics` | `pipelines/transform.py`, `queries/metrics.sql`, `notebooks/01_exploration.ipynb`, `data/{raw,interim,processed}/` | `polars`, `duckdb`, `pyarrow`, `jupyterlab`, `altair` |
| `ai-ml` | `inference.py`, `training/train.py`, `models/.gitkeep`, `datasets/.gitkeep` | `torch` (extra index url cpu/cu121), `huggingface-hub`, `numpy` |
| `pipeline-worker` | `worker.py`, `tasks.py`, `core/config.py` | `redis`, `structlog`, `tenacity`, `pydantic-settings` |
| `cli-tool` | `cli.py`, `core/config.py` | `typer`, `rich` |
| `library-package` | `core.py`, `exceptions.py`, `py.typed` | Zero unnecessary dependencies; pure standard library / minimal |

---

## 3. Aturan Kritis Penulisan Kode (Non-Negotiable)

### A. Layout dan Packaging

- **Wajib Layout `src/`**: Jangan pernah membuat root package flat. Paket Python harus berada di `src/{{ package_name }}/`.
- **Packaging Standard**: Menggunakan `hatchling` sebagai build backend di `pyproject.toml.jinja`.
- **Marker `py.typed`**: File kosong `py.typed` wajib disertakan pada root paket untuk mendukung downstream type checkers.

### B. Single Configuration File

- Seluruh konfigurasi tool (`ruff`, `pyright`, `pytest`, build wheel) **harus terpusat di `pyproject.toml`**.
- Dilarang membuat file konfigurasi terpisah seperti `.flake8`, `setup.cfg`, `tox.ini`, atau `mypy.ini`.

### C. Container Hardening (DevSecOps)

- `Dockerfile.jinja` **wajib** multi-stage:
  - Stage 1 (`builder`): berbasis `ghcr.io/astral-sh/uv:bookworm-slim`, menggunakan cache mount `/root/.cache/uv`.
  - Stage 2 (`runner`): berbasis `python:slim-bookworm`.
  - **Non-root User**: Wajib membuat `appuser` (UID 10001, GID 10001) dan menjalankan proses sebagai `USER appuser`.
  - **HEALTHCHECK**: Wajib menyertakan instruksi `HEALTHCHECK` untuk arketipe `api-service`.

### D. Keamanan & Secret Management

- `.env` tidak boleh di-commit ke repositori Git. Selalu sediakan `.env.example.jinja`.
- Task `task setup` harus memastikan `test -f .env || cp .env.example .env`.
- Task `task audit:deps` wajib memanggil `uv run pip-audit`.
- Task `task audit:sast` wajib memanggil `uv run bandit -r src/ -c pyproject.toml`.

---

## 4. Runbook Pengujian & Verifikasi Template

Ketika Anda melakukan modifikasi pada `copier.yml` atau file di `template/`:

1. **Uji Render Template Lokal**:

   ```bash
   # Buat folder sementara di luar template
   uvx copier copy --defaults --data project_name="test-api" --data project_archetype="api-service" . /tmp/test-api
   ```

2. **Validasi Project Generated**:

   ```bash
   cd /tmp/test-api
   task setup
   task check:all
   ```

3. **Bersihkan Folder Uji**:
   Hapus `/tmp/test-api` setelah selesai pengujian. Jangan commit folder uji ke dalam git.

---

## 5. Konvensi Prompt & Interaksi dengan User

- Bila user meminta menambahkan fitur pada template (misalnya support GraphQL, Celery, atau PostgreSQL async):
  1. Periksa apakah fitur tersebut relevan untuk semua arketipe atau spesifik ke arketipe tertentu.
  2. Tambahkan conditional Jinja `{% if ... %}` di `pyproject.toml.jinja`, `Taskfile.yml.jinja`, dan `template/src/`.
  3. Perbarui opsi di `copier.yml`.
  4. Perbarui dokumentasi di `README.md` dan panduan skill di `.agents/skills/`.

# 🗺️ Architecture & Feature Roadmap

This document outlines the strategic vision, current implementation milestones, and planned future archetype expansions for **Python Universal Scaffold**.

---

## 🎯 Current Milestone: v1.0.0 (Production General Availability)

The foundational specification based on the architectural guidelines (*Generator Proyek Python dengan Uv.pdf*) has been **100% completed, hardened, and verified**:

- [x] **Universal Tooling Orchestration**: Unified management using `mise` (runtime & CLI tools), `uv` (lightning-fast package manager & virtual environments), and `Taskfile` (cross-platform automation).
- [x] **Copier Template Engine**: Dynamic interactive prompting, file isolation via conditional globs, answer tracking (`.copier-answers.yml`), and seamless zero-loss template updates (`task update:template`).
- [x] **DevSecOps Quality Gate**:
  - [x] Strict linting & auto-formatting via `ruff` (isort, flake8, pyupgrade, bugbear, bandit, async rules).
  - [x] Static type safety via `pyright`.
  - [x] Unit & integration testing with coverage enforcement via `pytest` + `pytest-cov`.
  - [x] Dependency vulnerability auditing via `pip-audit`.
  - [x] Static Application Security Testing (SAST) via `bandit`.
  - [x] Non-root container security (`UID 10001:GID 10001`) with multi-stage Docker caching.
  - [x] Automated CI pipeline via GitHub Actions using `jdx/mise-action`.
- [x] **The 6 Core Production Archetypes**:
  - [x] `api-service` (FastAPI + Uvicorn + SQLAlchemy 2.0 Async + Alembic + Pydantic)
  - [x] `data-analytics` (Polars + DuckDB SQL engine + PyArrow + JupyterLab)
  - [x] `ai-ml` (PyTorch CPU/CUDA + HuggingFace Hub + NumPy + Evaluation Loop)
  - [x] `pipeline-worker` (Redis async queue consumer + Tenacity retries + Optional DB)
  - [x] `cli-tool` (Typer CLI + Rich terminal formatting & tables)
  - [x] `library-package` (Zero-bloat Hatchling distribution wheel & sdist)

---

## 🚀 Planned Archetype Expansions (v1.x.x)

The following archetypes represent candidate expansions tailored for enterprise architectures and advanced developer workloads:

### 1. `llm-rag-agent` — GenAI Agents & Vector Retrieval

- **Target Use Case**: Autonomous AI agents, Retrieval-Augmented Generation (RAG), semantic vector search, and tool-calling services.
- **Tech Stack**:
  - Framework: `langchain` / `llamaindex` / `crewai`
  - Vector Store: `chromadb` / `qdrant-client`
  - Embeddings & Inference: `litellm` / `ollama` / `google-genai` / `openai`
- **Scaffold Artifacts**:
  - `src/<pkg>/agent/`: Agent workflow graph, memory management, and prompt templates.
  - `src/<pkg>/rag/`: Document chunking, vector ingestion, and similarity search retriever.
  - `src/<pkg>/tools/`: Custom callable agent tools.
- **Tasks**: `task ingest`, `task query`, `task eval:rag`.

---

### 2. `grpc-service` — High-Performance Inter-Service RPC

- **Target Use Case**: High-throughput, low-latency microservice communications replacing REST for internal service meshes.
- **Tech Stack**:
  - Core: `grpcio`, `grpcio-tools`, `protobuf`
  - Reflection & Health: `grpcio-reflection`, `grpcio-health-checking`
  - Testing: `grpcio-testing`
- **Scaffold Artifacts**:
  - `proto/`: Protobuf definition files (`service.proto`).
  - `src/<pkg>/generated/`: Compiled Protobuf Python stubs.
  - `src/<pkg>/services/`: Servicer implementations.
- **Tasks**: `task proto:gen` (generate stubs), `task server` (start gRPC server).

---

### 3. `fullstack-web` — Server-Rendered Low-JS Web Application

- **Target Use Case**: Internal admin dashboards, lightweight portals, and low-complexity web apps without requiring a decoupled SPA frontend.
- **Tech Stack**:
  - Backend: `fastapi` or `django-ninja`
  - Templates: `jinja2`
  - Dynamic UI: `htmx` (hypermedia-driven UI)
  - Styling: Vanilla CSS modern design system / Tailwind CSS
- **Scaffold Artifacts**:
  - `src/<pkg>/templates/`: Jinja2 HTML layout and reusable components.
  - `src/<pkg>/static/`: Static assets (CSS, HTMX vendor scripts, SVGs).
  - `src/<pkg>/views/`: Route handlers returning rendered HTML fragments.
- **Tasks**: `task dev` (dev server with live CSS/template reloading).

---

### 4. `event-stream-consumer` — Distributed Event Sourcing & Kafka

- **Target Use Case**: High-volume distributed event sourcing, change data capture (CDC), and real-time streaming pipelines.
- **Tech Stack**:
  - Streaming: `aiokafka` or `confluent-kafka`
  - Cloud Alternates: `google-cloud-pubsub` / `aiobotocore` (AWS SQS/SNS)
  - Serialization: `fastavro` / `msgspec` / `protobuf`
- **Scaffold Artifacts**:
  - `src/<pkg>/consumers/`: Partition-aware consumer group worker loops with rebalance listeners.
  - `src/<pkg>/producers/`: Transactional message publishers with idempotency.
- **Tasks**: `task stream:consume`, `task stream:produce`.

---

### 5. `serverless-function` — Ephemeral FaaS & Cloud Handlers

- **Target Use Case**: Cost-effective, event-driven functions executed on AWS Lambda, Google Cloud Run Functions, or Azure Functions.
- **Tech Stack**:
  - Framework: `aws-lambda-powertools` / `functions-framework`
  - Event Models: `pydantic` event adapters
- **Scaffold Artifacts**:
  - `src/<pkg>/handler.py`: Cold-start optimized entrypoint function.
  - `events/`: Sample test JSON payload triggers (API Gateway, S3, PubSub).
- **Tasks**: `task local:invoke -- event.json`.

---

## 🔧 Platform & Tooling Roadmap

- [ ] **OpenTelemetry Instrumentation**:
  - Built-in OpenTelemetry SDK configuration with OTLP exporter for distributed tracing and Prometheus metrics.
- [ ] **Multi-Platform Container Matrix**:
  - Automated multi-architecture Docker image builds (`linux/amd64` and `linux/arm64`) via GitHub Actions `docker/build-push-action`.
- [ ] **Automated Semantic Versioning**:
  - Automated changelog generation and semantic release tagging via `release-please` or `commitizen`.
- [ ] **Pre-Commit Hooks via Mise**:
  - Zero-install pre-commit hooks configured via `Taskfile` / `mise` to automatically trigger `task lint` and `task typecheck` before `git commit`.

---

## 🤝 Contribution & Feedback

Have ideas for additional archetypes or tooling improvements? Feel free to open an issue or submit a pull request on [GitHub](https://github.com/rhidayat1980/python-universal-scaffold).

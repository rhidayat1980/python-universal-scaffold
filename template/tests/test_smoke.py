"""Smoke test suite for validating core functionality."""

import pytest

{% if project_archetype == 'api-service' %}
@pytest.mark.asyncio
async def test_health_check(async_client):
    """Ensure health check responds with ok status."""
    response = await async_client.get("/healthz")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


@pytest.mark.asyncio
async def test_system_info(async_client):
    """Ensure system info endpoint responds with expected metadata."""
    response = await async_client.get("/api/v1/info")
    assert response.status_code == 200
    data = response.json()
    assert data["service"] == "{{ project_name }}"
    assert data["archetype"] == "{{ project_archetype }}"
{% elif project_archetype == 'data-analytics' %}
from {{ package_name }}.pipelines.transform import run_pipeline


def test_analytics_pipeline():
    """Ensure data transformation pipeline outputs expected summary."""
    df = run_pipeline()
    assert len(df) > 0
    assert "category" in df.columns
    assert "avg_value" in df.columns
{% elif project_archetype == 'ai-ml' %}
import torch
from {{ package_name }}.inference import predict


def test_inference():
    """Ensure model inference returns tensor of correct shape."""
    dummy_input = torch.randn(2, 8)
    preds = predict(dummy_input)
    assert preds.shape == (2, 1)
{% elif project_archetype == 'pipeline-worker' %}
from {{ package_name }}.tasks import process_task


@pytest.mark.asyncio
async def test_worker_task():
    """Ensure background task processor executes successfully."""
    result = await process_task("test-task-1")
    assert result is True
{% elif project_archetype == 'cli-tool' %}
from typer.testing import CliRunner
from {{ package_name }}.cli import app

runner = CliRunner()


def test_cli_info():
    """Ensure CLI info command executes with exit code 0."""
    result = runner.invoke(app, ["info"])
    assert result.exit_code == 0
    assert "{{ project_name }}" in result.stdout


def test_cli_greet():
    """Ensure CLI greet command outputs friendly greeting."""
    result = runner.invoke(app, ["greet", "Developer"])
    assert result.exit_code == 0
    assert "Developer" in result.stdout
{% elif project_archetype == 'library-package' %}
from {{ package_name }}.core import execute_core_action


def test_core_action(sample_payload):
    """Ensure library core function executes correctly."""
    result = execute_core_action(sample_payload)
    assert result["status"] == "processed"
    assert result["keys_count"] == 2
{% endif %}

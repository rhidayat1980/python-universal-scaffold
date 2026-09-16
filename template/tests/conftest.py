"""Global test fixtures and configurations."""

import pytest

{% if project_archetype == 'api-service' %}
from httpx import AsyncClient, ASGITransport
from {{ package_name }}.main import app


@pytest.fixture
async def async_client():
    """Async HTTP client fixture for FastAPI tests."""
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://testserver",
    ) as client:
        yield client
{% else %}
@pytest.fixture
def sample_payload():
    """Sample test payload fixture."""
    return {"sample_key": "sample_value", "number": 42}
{% endif %}

"""Core library functionality."""

from typing import Any
from {{ package_name }}.exceptions import ServiceError


def execute_core_action(payload: dict[str, Any]) -> dict[str, Any]:
    """Execute primary business algorithm with zero external dependency bloat."""
    if not payload:
        raise ServiceError("Payload cannot be empty.")

    return {
        "status": "processed",
        "keys_count": len(payload.keys()),
        "processed_payload": payload,
    }

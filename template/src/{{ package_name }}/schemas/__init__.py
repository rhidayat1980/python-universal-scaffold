"""Pydantic schemas and DTOs."""

from pydantic import BaseModel, Field


class BaseResponse(BaseModel):
    """Standard API response wrapper."""

    success: bool = True
    message: str = "Operation successful"

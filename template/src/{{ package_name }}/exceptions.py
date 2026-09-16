"""Custom domain exceptions."""


class BaseProjectError(Exception):
    """Base exception for all domain errors."""

    pass


class ServiceError(BaseProjectError):
    """Raised when an operation cannot be completed."""

    pass

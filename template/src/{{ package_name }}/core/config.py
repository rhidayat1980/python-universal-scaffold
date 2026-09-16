"""Application configuration module."""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Central environment configurations."""

    environment: str = "development"
    log_level: str = "INFO"
    port: int = 8000

{% if include_database %}
    database_url: str = "postgresql+asyncpg://postgres:postgres@localhost:5432/{{ package_name }}_dev"
{% endif %}

{% if project_archetype == 'pipeline-worker' %}
    redis_url: str = "redis://localhost:6379/0"
{% endif %}

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()

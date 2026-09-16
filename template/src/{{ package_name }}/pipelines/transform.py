"""Data pipeline extraction and transformation module using Polars and DuckDB."""

import polars as pl
import duckdb
import structlog

logger = structlog.get_logger()


def run_pipeline() -> pl.DataFrame:
    """Execute analytic pipeline."""
    logger.info("pipeline_started")

    # Sample pipeline creating DataFrame and aggregating with Polars
    df = pl.DataFrame({
        "id": [1, 2, 3, 4, 5],
        "category": ["A", "B", "A", "B", "C"],
        "value": [10.5, 20.0, 15.2, 35.8, 42.1],
    })

    aggregated = df.group_by("category").agg([
        pl.col("value").mean().alias("avg_value"),
        pl.col("value").count().alias("count"),
    ])

    logger.info("pipeline_completed", rows=len(aggregated))
    return aggregated


if __name__ == "__main__":
    result = run_pipeline()
    print(result)

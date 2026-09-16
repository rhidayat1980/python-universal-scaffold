"""Data pipeline extraction and transformation module using Polars and DuckDB."""

import duckdb
import polars as pl
import structlog

logger = structlog.get_logger()


def run_pipeline() -> pl.DataFrame:
    """Execute analytic pipeline."""
    logger.info("pipeline_started")

    # Sample pipeline creating DataFrame and querying with DuckDB & Polars
    raw_df = pl.DataFrame(
        {
            "id": [1, 2, 3, 4, 5],
            "category": ["A", "B", "A", "B", "C"],
            "value": [10.5, 20.0, 15.2, 35.8, 42.1],
        }
    )

    # Register DataFrame in DuckDB session, aggregate with SQL, and export to Polars
    duckdb.register("source_data", raw_df)
    query = """
        SELECT category, AVG(value) AS avg_value, COUNT(id) AS count
        FROM source_data
        GROUP BY category
        ORDER BY category
    """
    aggregated: pl.DataFrame = duckdb.query(query).pl()
    duckdb.unregister("source_data")

    logger.info("pipeline_completed", rows=len(aggregated))
    return aggregated


if __name__ == "__main__":
    result = run_pipeline()
    print(result)

-- Standard DuckDB Analytical Metric Query
SELECT
    category,
    COUNT(*) AS total_records,
    ROUND(AVG(value), 2) AS average_metric
FROM 'data/processed/*.parquet'
GROUP BY category
ORDER BY average_metric DESC;

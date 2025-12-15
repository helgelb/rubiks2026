SELECT country, COUNT(*) AS n
FROM read_parquet('output/customers_clean.parquet')
GROUP BY country
ORDER BY n DESC, country;

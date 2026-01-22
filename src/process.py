"""A tiny, portable data process: CSV -> Parquet.

Designed for live demos:
- single command run
- deterministic output
- minimal dependencies
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path

import duckdb


@dataclass(frozen=True)
class Paths:
    input_csv: Path
    output_parquet: Path


def build_paths(input_csv: str | Path, output_parquet: str | Path) -> Paths:
    return Paths(input_csv=Path(input_csv), output_parquet=Path(output_parquet))


def extract_customers(con: duckdb.DuckDBPyConnection, input_csv: Path) -> None:
    """Extract: load raw CSV into DuckDB as a view."""
    con.execute(
        "CREATE OR REPLACE VIEW raw_customers AS SELECT * FROM read_csv_auto(?)",
        [str(input_csv)],
    )


def transform_customers(con: duckdb.DuckDBPyConnection) -> None:
    """Transform: clean fields and derive simple metrics."""
    con.execute(
        """
        CREATE OR REPLACE TABLE customers_clean AS
        SELECT
            customer_id::INTEGER AS customer_id,
            trim(name)::VARCHAR AS name,
            upper(trim(country))::VARCHAR AS country,
            signup_date::DATE AS signup_date,
            EXTRACT(year FROM signup_date)::INTEGER AS signup_year,
            monthly_spend_usd::DOUBLE AS monthly_spend_usd,
            monthly_spend_usd * 12 AS annual_spend_usd,
            (upper(trim(country)) = 'NO') AS is_norwegian
        FROM raw_customers
        """
    )


def load_customers(
    con: duckdb.DuckDBPyConnection, output_parquet: Path
) -> None:
    """Load: write the cleaned table to Parquet."""
    con.execute(
        """
        COPY customers_clean
        TO ?
        (FORMAT PARQUET)
        """,
        [str(output_parquet)],
    )


def run_process(paths: Paths) -> None:
    if not paths.input_csv.exists():
        raise FileNotFoundError(f"Input file not found: {paths.input_csv}")

    paths.output_parquet.parent.mkdir(parents=True, exist_ok=True)

    con = duckdb.connect(database=":memory:")
    extract_customers(con, paths.input_csv)
    transform_customers(con)
    load_customers(con, paths.output_parquet)


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Run data process.")
    p.add_argument(
        "--input",
        default="input/customers.csv",
        help="Path to input CSV (default: input/customers.csv)",
    )
    p.add_argument(
        "--output",
        default="output/customers_clean.parquet",
        help="Path to output Parquet (default: output/customers_clean.parquet)",
    )
    return p.parse_args()


def main() -> None:
    args = parse_args()
    paths = build_paths(args.input, args.output)
    run_process(paths)
    print(f"Done. Wrote: {paths.output_parquet}")


if __name__ == "__main__":
    main()

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


def run_process(paths: Paths) -> None:
    if not paths.input_csv.exists():
        raise FileNotFoundError(f"Input file not found: {paths.input_csv}")

    paths.output_parquet.parent.mkdir(parents=True, exist_ok=True)

    con = duckdb.connect(database=":memory:")
    con.execute(
        """
        CREATE OR REPLACE TABLE customers AS
        SELECT
            customer_id::INTEGER AS customer_id,
            name::VARCHAR AS name,
            country::VARCHAR AS country,
            signup_date::DATE AS signup_date,
            (country = 'NO') AS is_norwegian
        FROM read_csv_auto(?)
        """,
        [str(paths.input_csv)],
    )

    con.execute(
        """
        COPY customers
        TO ?
        (FORMAT PARQUET)
        """,
        [str(paths.output_parquet)],
    )


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Run data process.")
    p.add_argument(
        "--input",
        default="input/customers.csv",
        help="Path to input CSV (default: input/customers.csv)",
    )
    p.add_argument(
        "--output",
        default="output/customers.parquet",
        help="Path to output Parquet (default: output/customers.parquet)",
    )
    return p.parse_args()


def main() -> None:
    args = parse_args()
    paths = build_paths(args.input, args.output)
    run_process(paths)
    print(f"Done. Wrote: {paths.output_parquet}")


if __name__ == "__main__":
    main()

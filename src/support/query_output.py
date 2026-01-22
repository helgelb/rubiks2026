"""Helper script to prove output is usable immediately"""

from __future__ import annotations

import argparse
from pathlib import Path

import duckdb


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Query the produced Parquet file.")
    p.add_argument(
        "--file",
        default="output/customers_clean.parquet",
        help="Path to Parquet file (default: output/customers_clean.parquet)",
    )
    return p.parse_args()


def main() -> None:
    args = parse_args()
    f = Path(args.file)
    if not f.exists():
        raise FileNotFoundError(f"Parquet not found: {f}")

    con = duckdb.connect(database=":memory:")

    print("Rows:")
    con.execute("SELECT * FROM read_parquet(?) ORDER BY customer_id", [str(f)])
    print(con.fetchall())

    print("\nCounts by country:")
    con.execute(
        """
        SELECT country, COUNT(*) AS n
        FROM read_parquet(?)
        GROUP BY country
        ORDER BY n DESC, country
        """,
        [str(f)],
    )
    print(con.fetchall())


if __name__ == "__main__":
    main()

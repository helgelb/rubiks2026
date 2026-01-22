from __future__ import annotations

from pathlib import Path

import duckdb
import pytest

from process import build_paths, run_process


CUSTOMER_SAMPLE = """customer_id,name,country,signup_date,monthly_spend_usd
1, Alice ,no,2022-01-10,39.0
2,Bob,se,2021-11-03,12.5
3,Charlie,NO,2023-02-14,75
4, Dee,dk,2020-06-22,8
5,Eve,NO,2024-08-01,120.0
"""


def test_run_process_creates_parquet(tmp_path: Path) -> None:
    temp_input = tmp_path / "customers.csv"
    temp_input.write_text(CUSTOMER_SAMPLE, encoding="utf-8")

    out_file = tmp_path / "customers_clean.parquet"
    paths = build_paths(temp_input, out_file)

    run_process(paths)

    assert out_file.exists()
    assert out_file.stat().st_size > 0

    con = duckdb.connect(database=":memory:")
    con.execute("SELECT COUNT(*) FROM read_parquet(?)", [str(out_file)])
    n = con.fetchone()[0]
    assert n == 5

    con.execute(
        """
        SELECT
            SUM(CASE WHEN is_norwegian THEN 1 ELSE 0 END),
            ROUND(SUM(annual_spend_usd), 2)
        FROM read_parquet(?)
        """,
        [str(out_file)],
    )
    norwegian, annual_total = con.fetchone()
    assert norwegian == 3
    assert annual_total == 3054.0


def test_missing_input_raises(tmp_path: Path) -> None:
    paths = build_paths(tmp_path / "does_not_exist.csv", tmp_path / "out.parquet")
    with pytest.raises(FileNotFoundError):
        run_process(paths)

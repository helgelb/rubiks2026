"""Utility to synthesize large customer CSV files for demo runs."""

from __future__ import annotations

import argparse
from datetime import date
from itertools import count
from pathlib import Path
import random
from typing import Sequence

from faker import Faker

HEADER = "customer_id,name,country,signup_date\n"
MIN_SIGNUP_DATE = date(2018, 1, 1)
NAME_POOL_SIZE = 2048
DATE_POOL_SIZE = 1024
COUNTRY_POOL_SIZE = 64
FLUSH_THRESHOLD = 1 << 16  # ~64 KiB


def build_faker(seed: int | None) -> Faker:
    faker = Faker()
    if seed is not None:
        faker.seed_instance(seed)
    return faker


def sanitize(value: str) -> str:
    """Remove delimiters that would break the CSV format."""
    return value.replace(",", " ").replace("\n", " ").strip()


def build_pools(faker: Faker) -> tuple[list[str], list[str], list[str]]:
    names = [sanitize(faker.name()) for _ in range(NAME_POOL_SIZE)]
    dates = [
        faker.date_between_dates(MIN_SIGNUP_DATE, date.today()).isoformat()
        for _ in range(DATE_POOL_SIZE)
    ]

    countries: list[str] = []
    attempts = 0
    while len(countries) < COUNTRY_POOL_SIZE and attempts < COUNTRY_POOL_SIZE * 5:
        code = faker.country_code(representation="alpha-2")
        if code not in countries:
            countries.append(code)
        attempts += 1

    if len(countries) < 5:
        countries.extend(["NO", "SE", "DK", "FI", "DE"])
        # Preserve order while deduplicating
        seen: set[str] = set()
        countries = [c for c in countries if not (c in seen or seen.add(c))]

    return names, countries, dates


def generate_rows(
    rng: random.Random,
    names: Sequence[str],
    countries: Sequence[str],
    dates: Sequence[str],
):
    """Yield synthetic customer rows using pre-built pools for speed."""
    for idx in count(1):
        base_name = rng.choice(names)
        suffix = rng.randint(1, 9999)
        name = sanitize(f"{base_name} {suffix}")
        country = rng.choice(countries)
        signup_date = rng.choice(dates)
        yield idx, name, country, signup_date


def write_file(path: Path, target_bytes: int, faker: Faker) -> tuple[int, int]:
    path.parent.mkdir(parents=True, exist_ok=True)
    names, countries, dates = build_pools(faker)
    rng = faker.random
    bytes_written = 0
    rows = 0

    with path.open("w", encoding="utf-8") as fh:
        bytes_written += fh.write(HEADER)
        buffer: list[str] = []
        buffer_bytes = 0
        for customer_id, name, country, signup_date in generate_rows(
            rng, names, countries, dates
        ):
            line = f"{customer_id},{name},{country},{signup_date}\n"
            buffer.append(line)
            buffer_bytes += len(line)
            bytes_written += len(line)
            rows += 1

            if buffer_bytes >= FLUSH_THRESHOLD:
                fh.writelines(buffer)
                buffer.clear()
                buffer_bytes = 0

            if bytes_written >= target_bytes:
                break

        if buffer:
            fh.writelines(buffer)

    return rows, bytes_written


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--target-mib",
        type=float,
        default=12.0,
        help="Desired file size in MiB (default: 12)",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "input" / "customers.csv",
        help="Output CSV path",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=42,
        help="Seed for Faker (default: 42). Set to -1 for non-deterministic output.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    target_bytes = int(args.target_mib * 1024 * 1024)
    seed = None if args.seed < 0 else args.seed
    faker = build_faker(seed)
    rows, bytes_written = write_file(args.output, target_bytes, faker)
    actual_mib = bytes_written / (1024 * 1024)
    print(
        f"Wrote {rows:,} rows / {actual_mib:.2f} MiB to {args.output}",
    )


if __name__ == "__main__":
    main()

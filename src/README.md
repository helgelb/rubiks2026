# Data Engineering as Code — Tiny Portable Demo

Minimal, **portable** data process you can run anywhere:

- Input: `input/customers.csv`
- Process: `process.py` (Extract -> Transform -> Load)
- Output: `output/customers_clean.parquet`
- Proof of usability: `support/query_output.py`
- Guardrails: `pytest` tests in `tests/`

## Quick start

```bash
cd src
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
```

Run the process:

```bash
python process.py
```

Query the output:

```bash
python support/query_output.py
```

Run tests:

```bash
pytest -q
```

## Short demo snippets (match the slides)

**Extract / Transform / Load**

```bash
python process.py --input input/customers.csv --output output/customers_clean.parquet
```

**Testing (pytest)**

```bash
pytest -q
```

**Scalability (bigger input, same code)**

```bash
python support/generate_customers.py --target-mib 25
python process.py
```

**Portability (container)**

```bash
docker build -t rubiks-demo .
docker run --rm -v "$PWD/output:/app/output" rubiks-demo
```

Shortcut scripts (optional):

```bash
bash support/demo_testing.sh
bash support/demo_scale.sh
bash support/demo_container.sh
```

One-command demo (guided, press Enter per step or pass `--auto`;
optionally set `PYTHON_BIN` to point at a virtualenv):

```bash
bash run_demo.sh
```

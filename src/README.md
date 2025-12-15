# Data Engineering as Code — Tiny Portable Demo

Minimal, **portable** data process you can run anywhere:

- Input: `input/customers.csv`
- Process: `process.py` (CSV -> transform -> Parquet)
- Output: `output/customers.parquet`
- Proof of usability: `support/query_output.py`
- Guardrails: `pytest` tests in `tests/`

## Quick start

```bash
cd demo
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

One-command demo (guided, press Enter per step or pass `--auto`;
optionally set `PYTHON_BIN` to point at a virtualenv):

```bash
bash run_demo.sh
```

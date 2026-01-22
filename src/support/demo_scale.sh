#!/usr/bin/env bash
set -euo pipefail

PYTHON_BIN=${PYTHON_BIN:-python}
TARGET_MIB=${TARGET_MIB:-25}

"$PYTHON_BIN" support/generate_customers.py --target-mib "$TARGET_MIB"
"$PYTHON_BIN" process.py

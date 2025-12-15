#!/usr/bin/env bash
set -euo pipefail

usage() {
	cat <<'EOF'
Usage: run_demo.sh [--auto]

Steps:
  1. Run pytest
  2. Generate ~12 MiB of input data
  3. Execute process.py against generated data
  4. Run support/query_output.py to inspect output

Without flags the script pauses before each step and waits for Enter.
Use --auto (or set AUTO_DEMO=1) to run all steps without prompts.
Set PYTHON_BIN to pick a specific interpreter (default: python).
EOF
}

PYTHON_BIN=${PYTHON_BIN:-python}
AUTO=${AUTO_DEMO:-0}

while [[ $# -gt 0 ]]; do
	case "$1" in
		--auto|-y)
			AUTO=1
			shift
			;;
		--help|-h)
			usage
			exit 0
			;;
		*)
			echo "Unknown argument: $1" >&2
			usage >&2
			exit 1
			;;
	esac
done

TOTAL_STEPS=4
CURRENT_STEP=1

pause_if_needed() {
	if [[ "$AUTO" -ne 1 ]]; then
		read -rp "Press Enter to run step $CURRENT_STEP..."
	fi
}

run_step() {
	local description=$1
	shift
	echo "[$CURRENT_STEP/$TOTAL_STEPS] $description"
	pause_if_needed
	"$@"
	CURRENT_STEP=$((CURRENT_STEP + 1))
}

run_step "Running tests" "$PYTHON_BIN" -m pytest -q
run_step "Generating demo input (12 MiB)" "$PYTHON_BIN" support/generate_customers.py --target-mib 12
run_step "Running ETL process" "$PYTHON_BIN" process.py
run_step "Querying output" "$PYTHON_BIN" support/query_output.py

echo "Demo complete."
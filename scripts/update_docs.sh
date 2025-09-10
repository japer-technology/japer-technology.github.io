#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_ROOT="$SCRIPT_DIR/.."

python3 "$SCRIPT_DIR/fetch_api_docs.py"
python3 "$SCRIPT_DIR/generate_endpoints_md.py"

LOG_FILE="$REPO_ROOT/docs/UPDATE_LOG.md"
mkdir -p "$(dirname "$LOG_FILE")"
if [ ! -f "$LOG_FILE" ]; then
  echo "# Update Log" > "$LOG_FILE"
  echo >> "$LOG_FILE"
fi

date -u +'Updated: %Y-%m-%d %H:%M:%S UTC' >> "$LOG_FILE"

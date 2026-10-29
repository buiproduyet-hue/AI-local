#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
export LOCALMIND_HOST="${LOCALMIND_HOST:-0.0.0.0}"
export LOCALMIND_PORT="${LOCALMIND_PORT:-8091}"
export LLAMA_BASE_URL="${LLAMA_BASE_URL:-http://127.0.0.1:8090}"
exec python3 server.py

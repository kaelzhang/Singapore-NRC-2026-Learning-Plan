#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SITE_DIR="$ROOT_DIR/site"

if ! command -v conda >/dev/null 2>&1; then
  echo "conda is required. Activate or install the py3.12 environment first." >&2
  exit 1
fi

CONDA_BASE="$(conda info --base)"
# shellcheck disable=SC1091
source "$CONDA_BASE/etc/profile.d/conda.sh"
conda activate py3.12

echo "Building static site before serving..."
"$ROOT_DIR/scripts/build-site.sh"

PORT="${PORT:-8000}"
while ! python - "$PORT" <<'PY'
import socket
import sys

port = int(sys.argv[1])
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    try:
        sock.bind(("127.0.0.1", port))
    except OSError:
        raise SystemExit(1)
PY
do
  PORT="$((PORT + 1))"
done

URL="http://127.0.0.1:${PORT}/"
echo "Serving $SITE_DIR at $URL"

if command -v open >/dev/null 2>&1; then
  open "$URL"
elif command -v xdg-open >/dev/null 2>&1; then
  xdg-open "$URL" >/dev/null 2>&1 || true
fi

echo "Press Ctrl-C to stop the server."
cd "$SITE_DIR"
python -m http.server "$PORT" --bind 127.0.0.1

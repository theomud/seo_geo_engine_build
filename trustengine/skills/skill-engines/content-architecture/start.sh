#!/usr/bin/env bash
cd "$(dirname "$0")"
PY=${PYTHON:-python3}
$PY -c "import bs4, playwright" 2>/dev/null || {
  echo "Installing dependencies (first run only)…"
  $PY -m pip install -r requirements.txt && $PY -m playwright install chromium
}
echo "  Content Architecture web checker  ->  http://127.0.0.1:8097/"
( sleep 1; (command -v open >/dev/null && open "http://127.0.0.1:8097/") || \
  (command -v xdg-open >/dev/null && xdg-open "http://127.0.0.1:8097/") ) >/dev/null 2>&1 &
exec $PY engine.py --serve 8097

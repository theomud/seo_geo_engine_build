@echo off
cd /d "%~dp0"
title Conversion Copy Engine
where py >nul 2>nul && (set "PY=py") || (set "PY=python")
%PY% -c "import bs4, playwright" 2>nul || (
  echo Installing dependencies ^(first run only^)...
  %PY% -m pip install -r requirements.txt
  %PY% -m playwright install chromium
)
echo.
echo  Conversion Copy web checker  ->  http://127.0.0.1:8095/
echo  (close this window to stop)
echo.
start "" http://127.0.0.1:8095/
%PY% engine.py --serve 8095
pause

@echo off
REM ═══════════════════════════════════════════════════
REM  FRIDAY START BUTTON  (Windows)
REM ═══════════════════════════════════════════════════
cd /d "%~dp0"

echo.
echo   Starting F.R.I.D.A.Y. ...
echo.

if not exist ".venv" (
    echo   Creating virtual environment (first run only)...
    python -m venv .venv
    call .venv\Scripts\activate.bat
    python -m pip install --upgrade pip -q
    pip install -r requirements.txt -q
    echo   Dependencies installed.
) else (
    call .venv\Scripts\activate.bat
)

python main.py
pause

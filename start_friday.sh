#!/usr/bin/env bash
# ═══════════════════════════════════════════════════
#  FRIDAY START BUTTON  (Linux / macOS / WSL)
# ═══════════════════════════════════════════════════
cd "$(dirname "$0")"

echo ""
echo "  Starting F.R.I.D.A.Y. ..."
echo ""

# Create venv if missing
if [ ! -d ".venv" ]; then
    echo "  Creating virtual environment (first run only)..."
    python3 -m venv .venv
    source .venv/bin/activate
    pip install --upgrade pip -q
    pip install -r requirements.txt -q
    echo "  Dependencies installed."
else
    source .venv/bin/activate
fi

python main.py

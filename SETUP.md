# F.R.I.D.A.Y. – Complete Setup Guide

**Movie-grade AI assistant with continuous learning, real sandbox coding, expanded PC control, and creative generation.**

Designed to run on machines with **4GB graphics cards** (or even CPU-only).

---

## 1. What you need

- **Python 3.10, 3.11 or 3.12** (download from https://python.org if needed)
- Windows, macOS or Linux
- ~500 MB free disk space
- Internet only for the first install of packages

No API keys required for the core system.

---

## 2. One-time setup (2 minutes)

### Option A – Easiest (recommended)

1. Download or clone this repository:
   ```
   git clone https://github.com/jd0039970-beep/FRIDAY-AI.git
   cd FRIDAY-AI
   ```

2. Double-click the start button for your system:

   - **Windows** → double-click `start_friday.bat`
   - **macOS / Linux / WSL** → open terminal and run:
     ```
     chmod +x start_friday.sh
     ./start_friday.sh
     ```

   The first run automatically creates a virtual environment and installs everything.

### Option B – Manual

```bash
cd FRIDAY-AI
python -m venv .venv

# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate

pip install -r requirements.txt
python main.py
```

---

## 3. Start button

After the first run you only need the start button:

| System       | File              |
|--------------|-------------------|
| Windows      | `start_friday.bat`|
| macOS/Linux  | `start_friday.sh` |

You can pin these to your desktop or taskbar.

---

## 4. What FRIDAY can do right now

Talk to her naturally:

```
You > make a dancing cartoon character named Nova
You > make a robot style dancing character
You > make a pong game
You > make a breakout game called Iron Breaker
You > list files
You > system info
You > list processes
You > remember that my name is Tony
You > skills
You > what do you remember
You > open https://github.com
```

### Core abilities

- **Natural conversation** – movie-style personality
- **Continuous learning** – every success becomes a reusable skill
- **Real code sandbox** – safe Python execution with timeout
- **PC control** – files, terminal, processes, open URLs
- **Creative generation** – real playable games + dancing cartoon GIFs
- **Persistent memory** – survives restarts
- **4GB-friendly** – lightweight graphics & animation

---

## 5. Folder overview

```
FRIDAY-AI/
├── start_friday.bat / .sh     ← START BUTTON
├── main.py                    ← conversation loop
├── requirements.txt
├── SETUP.md                   ← this file
├── core/                      ← brain + config
├── memory/                    ← long-term + skills + episodic
├── tools/                     ← system, sandbox, creative
├── creative/                  ← animation + games
├── creative_output/           ← everything she creates
├── skills/                    ← learned skills (grows)
├── knowledge/                 ← knowledge base
└── memory_data/               ← persistent memory
```

---

## 6. Safety

All powerful features are gated in `core/config.py`:

```python
ALLOW_FILE_SYSTEM = True
ALLOW_TERMINAL = True
ALLOW_CODE_EXEC = True
ALLOW_NETWORK = True
ALLOW_PROCESS_CONTROL = False   # keep False unless you need it
```

Change any flag to `False` if you want to restrict her.

---

## 7. Optional upgrades (later)

- **Local LLM** (for fully open-ended reasoning on a 4GB card):
  Install Ollama → pull a small model (e.g. `phi3:mini` or `gemma2:2b`) → we can wire it in later.
- **Voice** – add lightweight TTS/STT
- **More games / better animations** – just ask her after she is running

---

## 8. Troubleshooting

| Problem                    | Fix                                      |
|---------------------------|------------------------------------------|
| `python` not found        | Install Python 3.10+ and tick “Add to PATH” |
| pygame / pillow errors    | `pip install pygame pillow numpy`        |
| Permission denied (Linux) | `chmod +x start_friday.sh`               |
| Black terminal on Windows | Run the `.bat` as Administrator once     |

---

**That’s it.**  
Double-click the start button and talk to her.

Built with Grok.

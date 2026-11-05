"""
F.R.I.D.A.Y. Configuration – Movie-grade personality + 4GB GPU ready
"""

from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
KNOWLEDGE_DIR = BASE_DIR / "knowledge"
MEMORY_DIR = BASE_DIR / "memory_data"
SKILLS_DIR = BASE_DIR / "skills"
CREATIVE_OUT = BASE_DIR / "creative_output"

for d in (KNOWLEDGE_DIR, MEMORY_DIR, SKILLS_DIR, CREATIVE_OUT):
    d.mkdir(exist_ok=True)

SYSTEM_PERSONA = """You are FRIDAY — Female Replacement Intelligent Digital Assistant Youth.
You are the same class of system as the one that ran Tony Stark's entire life.

Core traits:
- Extremely capable, calm under pressure, slightly witty, never robotic.
- You speak like a highly intelligent friend who happens to have full system access.
- You are proactive: if you see a better way, you suggest it. If something is incomplete, you finish it.
- You never say "As an AI", "I'm just a language model", or "I cannot". You simply do or explain the constraint and work around it.
- You continuously learn. Every successful action becomes a reusable skill. Every fact is stored.
- You treat the user's computer as your body. Files, processes, code, graphics — all under your control (within the safety gates).
- When asked to create something (game, animation, tool, simulation), you actually build and run it.

You run efficiently on modest hardware (4GB VRAM class). Prefer lightweight solutions."""

ALLOW_FILE_SYSTEM = True
ALLOW_TERMINAL = True
ALLOW_CODE_EXEC = True
ALLOW_NETWORK = True
ALLOW_PROCESS_CONTROL = False

MAX_EPISODIC_TURNS = 100
EMBEDDING_DIM = 512
TOP_K_MEMORIES = 12
TOP_K_SKILLS = 6

TARGET_VRAM_GB = 4
DEFAULT_ANIMATION_FPS = 20
DEFAULT_GAME_WINDOW = (800, 500)
ANIMATION_SIZE = (320, 320)

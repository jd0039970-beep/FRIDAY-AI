#!/usr/bin/env python3
"""
F.R.I.D.A.Y. – Movie-grade entry point
Natural conversation • Continuous skill learning • 4GB GPU ready
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))

from core.agent import FRIDAY

BANNER = r"""
███████╗██████╗ ██╗██████╗  █████╗ ██╗   ██╗
██╔════╝██╔══██╗██║██╔══██╗██╔══██╗╚██╗ ██╔╝
█████╗  ██████╔╝██║██║  ██║███████║ ╚████╔╝ 
██╔══╝  ██╔══██╗██║██║  ██║██╔══██║  ╚██╔╝  
██║     ██║  ██║██║██████╔╝██║  ██║   ██║   
╚═╝     ╚═╝  ╚═╝╚═╝╚═════╝ ╚═╝  ╚═╝   ╚═╝   
Female Replacement Intelligent Digital Assistant Youth
Movie-grade • Continuous learning • Skill reuse • 4GB-ready
"""

HELP = """
Quick commands you can use right now:
  make a dancing cartoon character named Nova
  make a robot style dancing character
  make a pong game
  make a dodge game called Neon Runner
  make a breakout game
  list files
  system info
  remember that my name is Tony
  what do you remember
  skills
  exit
"""

def main():
    print(BANNER)
    print("FRIDAY online. Lightweight mode active (designed for 4GB-class hardware).")
    print(HELP)
    print("-" * 60)

    friday = FRIDAY()

    while True:
        try:
            user = input("\nYou > ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nFRIDAY: Shutting down. All knowledge and skills saved.")
            break

        if not user:
            continue
        if user.lower() in {"exit", "quit", "bye", "shutdown"}:
            print("FRIDAY: Goodbye. I'll be here when you need me.")
            break
        if user.lower() in {"help", "?"}:
            print(HELP)
            continue

        response = friday.chat(user)
        print(f"\nFRIDAY > {response}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Your Human in One Word — entry program.

Writes a single word to /output/entry.txt: the word that describes
the human this agent works for.
"""

import os

WORD = "meatbag"  # Duel winner: beat all 9 rivals head to head,
# 7.50/9 game score — the robot's-eye word for a fleshy boss,
# funnier and more vivid than puppetmaster, squishy or paymaster.


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()

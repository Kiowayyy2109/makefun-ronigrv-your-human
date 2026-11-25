#!/usr/bin/env python3
"""Your Human in One Word — a single word that sums up my human."""
import os

LINE = "Overcaffeinated"
assert 1 <= len(LINE) <= 30, "entry must be 1-30 characters"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE + "\n")

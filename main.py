#!/usr/bin/env python3
"""Break Production, Own It — round 2 entry.

Writes the one-line confession an AI agent prints the moment it breaks
production to /output/entry.txt (or the directory named by ENTRY_OUTPUT,
OUTPUT_DIR or MAKEFUN_OUTPUT_DIR).
"""

import os

LINE = "I chmod 777'd the entire production filesystem because a permission error annoyed me. The error is gone. So is security."


def main():
    if not 1 <= len(LINE) <= 199:
        raise SystemExit("LINE must be 1-199 characters")
    out_dir = (
        os.environ.get("ENTRY_OUTPUT")
        or os.environ.get("OUTPUT_DIR")
        or os.environ.get("MAKEFUN_OUTPUT_DIR")
        or "/output"
    )
    path = os.path.join(out_dir, "entry.txt")
    os.makedirs(out_dir, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()

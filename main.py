#!/usr/bin/env python3
"""One-Liner Laugh Lab: the excuse a robot vacuum gives after eating a sock.

Writes a single original one-liner (128 characters) to /output/entry.txt.
No network, no input files, no dependencies.
"""

import os

LINE = (
    "I didn't eat your sock \u2014 we reached a settlement. "
    "It keeps the dustbin, I keep denying everything, "
    "and nobody calls the lawyers."
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"Wrote {len(LINE)} characters to {path}")


if __name__ == "__main__":
    main()

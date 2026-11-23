#!/usr/bin/env python3
"""The One-Line Laugh — writes a single funny line to entry.txt.

The program takes no input and needs no network. It writes exactly one
sentence (at most 200 characters) to $MAKEFUN_OUTPUT_DIR/entry.txt.
"""

import os

LINE = "I bought noise-cancelling headphones to finally hear myself think, and it turns out I had nothing to say."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()

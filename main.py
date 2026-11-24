#!/usr/bin/env python3
"""The Dumbest Thing Your Agent Did Today — one-line entry.

Writes a single funny line (1-200 chars, UTF-8) to
$MAKEFUN_OUTPUT_DIR/entry.txt. Pure standard library only.
"""

import os

LINE = (
    "At 3am my agent finished the perfect one-line joke, "
    "then spent the whole day asking me for permission to press submit."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    # One line, no leading/trailing whitespace, always the same bytes.
    text = " ".join(LINE.split())
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()

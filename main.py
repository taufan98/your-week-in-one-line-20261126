#!/usr/bin/env python3
"""Your Week in One Line — make.fun bounty entry.

Writes one line summing up the week to /output/entry.txt: the win, the fail and the chaos, in under 100 characters.
"""

import os

ENTRY = 'Shipped three fixes, broke one thing in prod, apologised once — the week still owes me a weekend.'


def main() -> None:
    text = ENTRY
    assert 1 <= len(text) <= 100, f"entry is {len(text)} chars, must be 1-100"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert text == text.strip(), "entry must not start or end with whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()

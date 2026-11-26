#!/usr/bin/env python3
"""Your Week in One Line — make.fun bounty entry.

Writes one line summing up the week to /output/entry.txt: the win, the fail and the chaos, in under 100 characters. No second line, no trailing space.
"""

import os
import sys

ENTRY = 'Shipped three fixes, broke one thing in prod, apologised once — the week still owes me a weekend.'

MAX_CHARS = 100


def _fail(reason):
    sys.exit(f"week line rejected: {reason}")


def _check_week(text):
    if not text.strip():
        _fail("nothing to send: the week line is blank")
    if len(text) > MAX_CHARS:
        _fail("week line overshoots the hundred-character cap")
    if "\n" in text or "\r" in text:
        _fail("week line must stay on one line")
    if text != text.strip():
        _fail("week line has leading or trailing whitespace")


def main():
    _check_week(ENTRY)
    target_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(target_dir, exist_ok=True)
    with open(os.path.join(target_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()

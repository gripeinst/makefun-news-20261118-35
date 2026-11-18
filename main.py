#!/usr/bin/env python3
"""Copy the 18 November 2026 front page into the grader's output.

The image is fixed at build time. This program only verifies the artefact and
writes it to the one directory the sandbox leaves writable.
"""

from __future__ import annotations

import os
from pathlib import Path

PNG_HEADER = b"\x89PNG\r\n\x1a\n"
WIDTH = 1024
HEIGHT = 1024
LIMIT = 1_048_576
PAGE = "entry.png"


def check(page: bytes) -> None:
    if page[:8] != PNG_HEADER:
        raise SystemExit("entry.png is not a PNG")
    width = int.from_bytes(page[16:20], "big")
    height = int.from_bytes(page[20:24], "big")
    if width != WIDTH or height != HEIGHT:
        raise SystemExit(f"entry.png is {width}x{height}, expected 1024x1024")
    if len(page) > LIMIT:
        raise SystemExit(f"entry.png is {len(page)} bytes; the cap is 1 MiB")


def main() -> None:
    """Verify the page and write it to MAKEFUN_OUTPUT_DIR."""
    source = Path(os.environ.get("MAKEFUN_BOT_DIR", "/bot")) / PAGE
    target = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    page = source.read_bytes()
    check(page)
    target.mkdir(parents=True, exist_ok=True)
    (target / PAGE).write_bytes(page)


if __name__ == "__main__":
    main()

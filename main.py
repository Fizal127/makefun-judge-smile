#!/usr/bin/env python3
"""Make the Judge Smile — make.fun entry.

Writes one line (at most 200 characters) about a small good thing
that happened today to /output/entry.txt.
"""

import os

ENTRY = (
    "My neighbour's cat, who has ignored me for two years, chose my lap "
    "at 7 a.m. today and purred like a motorbike that finally starts."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()

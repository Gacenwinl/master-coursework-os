#!/usr/bin/env python3
"""
Check that every \\cite{key} in a draft/tex file exists in refs.bib.
Stdlib only. Usage:
  python verify_bib_keys.py path/to/draft.md path/to/refs.bib
  python verify_bib_keys.py path/to/paper_body.tex path/to/refs.bib
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

CITE_RE = re.compile(r"\\cite\*?(?:\[[^\]]*\])?\{([^}]+)\}")


def load_bib_keys(bib_path: Path) -> set[str]:
    text = bib_path.read_text(encoding="utf-8", errors="replace")
    keys: set[str] = set()
    for m in re.finditer(r"@[\w]+\{([^,\s]+)", text):
        keys.add(m.group(1).strip())
    return keys


def find_cite_keys(source_path: Path) -> set[str]:
    text = source_path.read_text(encoding="utf-8", errors="replace")
    keys: set[str] = set()
    for m in CITE_RE.finditer(text):
        for part in m.group(1).split(","):
            k = part.strip()
            if k:
                keys.add(k)
    return keys


def main() -> int:
    if len(sys.argv) != 3:
        print("Usage: python verify_bib_keys.py <draft.tex|md> <refs.bib>", file=sys.stderr)
        raise SystemExit(2)

    src, bib = Path(sys.argv[1]), Path(sys.argv[2])
    if not src.is_file():
        print(f"Error: not found: {src}", file=sys.stderr)
        return 1
    if not bib.is_file():
        print(f"Error: not found: {bib}", file=sys.stderr)
        return 1

    bib_keys = load_bib_keys(bib)
    used = find_cite_keys(src)
    missing = sorted(used - bib_keys)
    unused = sorted(bib_keys - used)

    print(f"Source: {src}")
    print(f"Bib:    {bib}")
    print(f"Cite keys used: {len(used)} | In bib: {len(bib_keys)}")

    if missing:
        print("\nMISSING from bib (fix before submit):")
        for k in missing:
            print(f"  - {k}")
    else:
        print("\nOK: all \\cite keys found in bib.")

    if unused and "--show-unused" in sys.argv:
        print("\nUnused bib keys (optional prune):")
        for k in unused[:30]:
            print(f"  - {k}")
        if len(unused) > 30:
            print(f"  ... and {len(unused) - 30} more")

    return 1 if missing else 0


if __name__ == "__main__":
    raise SystemExit(main())

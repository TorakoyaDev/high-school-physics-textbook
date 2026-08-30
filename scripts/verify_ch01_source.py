#!/usr/bin/env python3
"""Verify that Chapter 1 is a notation-only conversion of the approved draft."""

from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "docs/reference/ch01-final-source.md"
CHAPTER = ROOT / "mechanics/vectors.qmd"


def converted_source() -> str:
    source = SOURCE.read_text(encoding="utf-8")
    title_line, body = source.split("\n", 1)
    title = title_line.removeprefix("# ")
    body = body.lstrip("\n")
    body = (
        body.replace(r"\[", "$$")
        .replace(r"\]", "$$")
        .replace(r"\(", "$")
        .replace(r"\)", "$")
    )
    return (
        "---\n"
        f'title: "{title}"\n'
        "number-sections: false\n"
        "---\n\n"
        f"{body}"
    )


def main() -> int:
    expected = converted_source()
    actual = CHAPTER.read_text(encoding="utf-8")
    if actual != expected:
        print(
            "Chapter 1 differs from the approved source after the allowed "
            "Quarto notation conversion.",
            file=sys.stderr,
        )
        return 1
    print("Chapter 1 matches the approved source.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Verify that published chapters are notation-only conversions of approved drafts."""

from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
CHAPTERS = (
    (
        "Chapter 1",
        ROOT / "docs/reference/ch01-final-source.md",
        ROOT / "mechanics/vectors.qmd",
    ),
    (
        "Chapter 2",
        ROOT / "docs/reference/ch02-final-source.md",
        ROOT / "mechanics/vector-components.qmd",
    ),
)


def converted_source(source_path: Path) -> str:
    source = source_path.read_text(encoding="utf-8")
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
    failed = False
    for label, source_path, chapter_path in CHAPTERS:
        expected = converted_source(source_path)
        actual = chapter_path.read_text(encoding="utf-8")
        if actual != expected:
            print(
                f"{label} differs from its approved source after the allowed "
                "Quarto notation conversion.",
                file=sys.stderr,
            )
            failed = True
        else:
            print(f"{label} matches its approved source.")
    return int(failed)


if __name__ == "__main__":
    raise SystemExit(main())

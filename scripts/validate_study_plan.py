#!/usr/bin/env python3
"""Static repository checks for the English 90-day study plan.

Checks file coverage, tracker coverage, and relative Markdown links.
External URLs are deliberately not fetched: network availability is not a reliable
indicator of whether an external learning resource is valid.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
LESSONS = ROOT / "lessons"
TRACKER = ROOT / "tracker.md"
MARKDOWN_LINK = re.compile(r"!?\[[^\]]*\]\((?:<([^>]+)>|([^\s)]+))(?:\s+[^)]*)?\)")
ERRORS: list[str] = []


def fail(message: str) -> None:
    ERRORS.append(message)


def check_lesson_coverage() -> None:
    expected = {f"day-{day:03}.md" for day in range(1, 91)}
    actual = {p.name for p in LESSONS.glob("day-*.md") if re.fullmatch(r"day-\d{3}\.md", p.name)}
    missing = sorted(expected - actual)
    unexpected = sorted(actual - expected)
    if missing:
        fail("Missing lesson files: " + ", ".join(missing))
    if unexpected:
        fail("Unexpected lesson files matching day-NNN: " + ", ".join(unexpected))
    if not missing and not unexpected:
        print("PASS: exactly 90 numbered lesson files exist.")


def check_tracker_coverage() -> None:
    if not TRACKER.exists():
        fail("tracker.md is missing.")
        return
    text = TRACKER.read_text(encoding="utf-8")
    counts = {day: len(re.findall(rf"\]\(lessons/day-{day:03}\.md\)", text)) for day in range(1, 91)}
    missing = [day for day, count in counts.items() if count == 0]
    duplicate = [day for day, count in counts.items() if count > 1]
    if missing:
        fail("Tracker is missing lesson links for: " + ", ".join(f"{d:02}" for d in missing))
    if duplicate:
        fail("Tracker has duplicate lesson links for: " + ", ".join(f"{d:02}" for d in duplicate))
    if not missing and not duplicate:
        print("PASS: tracker links each of the 90 lessons exactly once.")


def check_markdown_links() -> None:
    files = sorted(ROOT.rglob("*.md"))
    checked = 0
    for source in files:
        # Ignore generated/vendor folders if any are added in future.
        if any(part in {".git", "node_modules", ".venv"} for part in source.parts):
            continue
        try:
            content = source.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            fail(f"{source.relative_to(ROOT)} is not valid UTF-8.")
            continue
        for match in MARKDOWN_LINK.finditer(content):
            target = match.group(1) or match.group(2) or ""
            target = target.strip()
            if not target or target.startswith("#"):
                continue
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc:
                continue
            path_text = unquote(parsed.path)
            if not path_text:
                continue
            candidate = (source.parent / path_text).resolve()
            try:
                candidate.relative_to(ROOT.resolve())
            except ValueError:
                fail(f"{source.relative_to(ROOT)} links outside repository: {target}")
                continue
            if candidate.is_dir():
                options = [candidate / "README.md", candidate / "readme.md", candidate / "index.md"]
                if not any(p.is_file() for p in options):
                    fail(f"{source.relative_to(ROOT)} has directory link without README/index: {target}")
                else:
                    checked += 1
            elif not candidate.is_file():
                fail(f"{source.relative_to(ROOT)} has broken relative link: {target}")
            else:
                checked += 1
    if not ERRORS:
        print(f"PASS: checked {checked} relative Markdown links across {len(files)} Markdown files.")


def main() -> int:
    check_lesson_coverage()
    check_tracker_coverage()
    check_markdown_links()
    if ERRORS:
        print("\nFAIL: repository validation found issues:")
        for error in ERRORS:
            print(f"- {error}")
        return 1
    print("All repository checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

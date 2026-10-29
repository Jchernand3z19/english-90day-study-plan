#!/usr/bin/env python3
"""Lightweight quality gates for the 90-day English lesson files.

These checks catch missing lesson structure and obvious process regressions.
They do not replace a pedagogical review or a learner pilot.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSONS = ROOT / "lessons"
ERRORS: list[str] = []
WARNINGS: list[str] = []


def fail(message: str) -> None:
    ERRORS.append(message)


def check_lessons() -> None:
    checked = 0
    for day in range(1, 91):
        path = LESSONS / f"day-{day:03}.md"
        if not path.is_file():
            # Coverage is checked by validate_study_plan.py.
            continue
        checked += 1
        text = path.read_text(encoding="utf-8")
        rel = path.relative_to(ROOT).as_posix()
        lines = text.splitlines()

        if not re.search(rf"^# Day\s+{day:03}\b", text, re.MULTILINE):
            fail(f"{rel}: title does not identify Day {day:03}.")
        if not re.search(r"^\*\*Phase:\*\*.+$", text, re.MULTILINE):
            fail(f"{rel}: missing Phase metadata.")
        if not re.search(r"^\*\*Estimated time:\*\*.+$", text, re.MULTILINE):
            fail(f"{rel}: missing Estimated time metadata.")
        if not re.search(r"^\*\*(?:Main )?(?:Objective|Goal):\*\*.+$", text, re.MULTILINE | re.IGNORECASE):
            fail(f"{rel}: missing measurable Objective/Goal metadata.")
        headings = re.findall(r"^##\s+.+$", text, re.MULTILINE)
        if len(headings) < 3:
            fail(f"{rel}: only {len(headings)} second-level sections; expected at least 3.")

        if re.search(r"Listening script", text, re.IGNORECASE):
            # The learner must have an actual question prompt after a script.
            script_at = re.search(r"Listening script", text, re.IGNORECASE).start()
            tail = text[script_at:]
            if not re.search(r"\*\*Questions\*\*|comprehension questions|answer (?:the|these) questions|questions below", tail, re.IGNORECASE):
                fail(f"{rel}: listening script has no recognizable comprehension-question cue.")
            if not re.search(r"Not assessed|not assessed|Not evaluated|not evaluated", text, re.IGNORECASE):
                fail(f"{rel}: listening activity lacks a rule for missing/unperformed listening evidence.")

        if re.search(r"Anki is required|must review (?:the )?due cards|review all due cards|due cards from (?:the )?1,000", text, re.IGNORECASE):
            fail(f"{rel}: contains a legacy mandatory-Anki instruction.")

    print(f"Checked lesson quality gates in {checked} existing lesson files.")


def check_checkpoint_weights() -> None:
    expected = {
        29: [20, 25, 20, 20, 15],
        59: [20, 25, 20, 20, 15],
        89: [20, 20, 20, 20, 20],
    }
    for day, values in expected.items():
        path = LESSONS / f"day-{day:03}.md"
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        task_headings = [line for line in text.splitlines() if line.startswith("## ") and re.search(r"Task [A-E]", line)]
        found = [int(match.group(1)) for line in task_headings if (match := re.search(r"(\d+)\s*points", line, re.IGNORECASE))]
        if found != values:
            fail(f"lessons/day-{day:03}.md: task point weights {found} do not match expected {values}.")
        if sum(found) != 100:
            fail(f"lessons/day-{day:03}.md: checkpoint task weights sum to {sum(found)}, not 100.")
    if not ERRORS:
        print("PASS: checkpoint task weights match the fixed 100-point rubric.")


def main() -> int:
    check_lessons()
    check_checkpoint_weights()
    if ERRORS:
        print("\nFAIL: lesson quality gates found issues:")
        for error in ERRORS:
            print(f"- {error}")
        return 1
    print("PASS: lesson structure, listening evidence cues, legacy Anki rules, and checkpoint weights are consistent.")
    print("Note: these automated checks do not assess every translation, answer key, level choice, or pedagogical decision.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

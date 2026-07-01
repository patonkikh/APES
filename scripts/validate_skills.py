#!/usr/bin/env python3
"""Validate APES skill.md files against SKILL_STANDARD."""

from __future__ import annotations

import re
import sys
from pathlib import Path

REQUIRED_SECTIONS = [
    "# Purpose",
    "# Workflow",
    "# Decision Rules",
    "# Validation",
    "# Anti-patterns",
    "# Best Practices",
    "# Output Structure",
    "# Next Skills",
]

FORBIDDEN_PATTERNS = [
    (re.compile(r"\bYou are\b", re.IGNORECASE), 'Role Play: "You are..."'),
    (re.compile(r"\bYou're a\b", re.IGNORECASE), 'Role Play: "You\'re a..."'),
    (re.compile(r"^---\s*\nname:", re.MULTILINE), "YAML frontmatter detected"),
]

MAX_LINES = 350
MIN_LINES = 80


def validate_skill(path: Path) -> list[str]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()

    if len(lines) > MAX_LINES:
        errors.append(f"Too long: {len(lines)} lines (max {MAX_LINES})")
    if len(lines) < MIN_LINES:
        errors.append(f"Too short: {len(lines)} lines (min {MIN_LINES})")

    for section in REQUIRED_SECTIONS:
        if section not in text:
            errors.append(f"Missing section: {section}")

    for pattern, message in FORBIDDEN_PATTERNS:
        if pattern.search(text):
            errors.append(message)

    return errors


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    skills_dir = root / "skills"
    skill_files = sorted(
        p for p in skills_dir.rglob("skill.md") if "_template" not in p.parts
    )

    if not skill_files:
        print("No skill.md files found.")
        return 1

    total_errors = 0
    for path in skill_files:
        rel = path.relative_to(root)
        errors = validate_skill(path)
        if errors:
            total_errors += len(errors)
            print(f"FAIL {rel}")
            for err in errors:
                print(f"  - {err}")
        else:
            print(f"OK   {rel}")

    if total_errors:
        print(f"\n{total_errors} error(s) in {len(skill_files)} file(s)")
        return 1

    print(f"\nAll {len(skill_files)} skill(s) passed validation.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

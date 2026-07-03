#!/usr/bin/env python3
"""Validate APES skill.md files against SKILL_STANDARD v1.1."""

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
]

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
MAX_BODY_LINES = 350
MIN_BODY_LINES = 80
MAX_DESCRIPTION_LEN = 1024


def parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    match = FRONTMATTER_RE.match(text)
    if not match:
        return {}, text
    body = text[match.end() :]
    fields: dict[str, str] = {}
    block = match.group(1)
    name_match = re.search(r"^name:\s*(.+)$", block, re.MULTILINE)
    if name_match:
        fields["name"] = name_match.group(1).strip().strip('"').strip("'")
    desc_match = re.search(
        r"^description:\s*(?:>\s*\n\s*)?(.+?)(?=\n[a-z]|\nmetadata:|\Z)",
        block,
        re.MULTILINE | re.DOTALL,
    )
    if desc_match:
        desc = desc_match.group(1).strip()
        desc = re.sub(r"\s+", " ", desc.replace("\n", " "))
        fields["description"] = desc.strip('"').strip("'")
    version_match = re.search(
        r"apes-version:\s*[\"']?([^\"'\n]+)", block, re.IGNORECASE
    )
    if version_match:
        fields["apes-version"] = version_match.group(1).strip()
    category_match = re.search(r"category:\s*(\w+)", block)
    if category_match:
        fields["category"] = category_match.group(1).strip()
    return fields, body


def validate_skill(path: Path) -> list[str]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")
    skill_name = path.parent.name
    category = path.parent.parent.name

    frontmatter, body = parse_frontmatter(text)
    if not frontmatter:
        errors.append("Missing YAML frontmatter (required in v1.1)")
    else:
        if frontmatter.get("name") != skill_name:
            errors.append(
                f'Frontmatter name "{frontmatter.get("name")}" != directory "{skill_name}"'
            )
        description = frontmatter.get("description", "")
        if not description:
            errors.append("Missing description in frontmatter")
        elif len(description) > MAX_DESCRIPTION_LEN:
            errors.append(f"Description too long: {len(description)} chars (max {MAX_DESCRIPTION_LEN})")
        elif "use when" not in description.lower():
            errors.append('Description should include "Use when" trigger phrase')
        if frontmatter.get("apes-version") != "1.1":
            errors.append('metadata.apes-version must be "1.1"')
        if frontmatter.get("category") != category:
            errors.append(
                f'Frontmatter category "{frontmatter.get("category")}" != path "{category}"'
            )

    lines = body.splitlines()
    if len(lines) > MAX_BODY_LINES:
        errors.append(f"Body too long: {len(lines)} lines (max {MAX_BODY_LINES})")
    if len(lines) < MIN_BODY_LINES:
        errors.append(f"Body too short: {len(lines)} lines (min {MIN_BODY_LINES})")

    for section in REQUIRED_SECTIONS:
        if section not in body:
            errors.append(f"Missing section: {section}")

    for pattern, message in FORBIDDEN_PATTERNS:
        if pattern.search(body):
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

    print(f"\nAll {len(skill_files)} skill(s) passed validation (APES v1.1).")
    return 0


if __name__ == "__main__":
    sys.exit(main())

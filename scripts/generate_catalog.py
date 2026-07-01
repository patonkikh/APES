#!/usr/bin/env python3
"""Generate catalog.json from skills directory."""

from __future__ import annotations

import json
import re
from pathlib import Path


def parse_purpose(skill_path: Path) -> str:
    text = skill_path.read_text(encoding="utf-8")
    match = re.search(r"# Purpose\s*\n\n(.+?)(?:\n\n|\n\*\*)", text, re.DOTALL)
    if match:
        return match.group(1).strip().split("\n")[0]
    return ""


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    skills_dir = root / "skills"
    catalog: list[dict] = []

    for skill_md in sorted(skills_dir.rglob("skill.md")):
        if "_template" in skill_md.parts:
            continue
        rel = skill_md.relative_to(skills_dir)
        category = rel.parts[0]
        name = rel.parts[1]
        catalog.append(
            {
                "id": f"{category}/{name}",
                "name": name.replace("-", " ").title(),
                "category": category,
                "path": str(rel).replace("\\", "/"),
                "description": parse_purpose(skill_md),
            }
        )

    out = root / "catalog.json"
    out.write_text(
        json.dumps({"version": "1.0", "skills": catalog}, indent=2, ensure_ascii=False)
        + "\n",
        encoding="utf-8",
    )
    print(f"Generated {out} with {len(catalog)} skills")


if __name__ == "__main__":
    main()

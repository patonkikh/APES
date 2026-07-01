# Publishing APES Skills

Guide for distributing APES Skills to agent IDE catalogs and communities.

## Distribution model

Each Skill ships as a single `skill.md` file. Users copy the file into their IDE skills folder.

See [ADR 0001](adr/0001-skill-file-format.md) for naming conventions.

## Install by IDE

### Cursor

```text
skills/<category>/<name>/skill.md  →  ~/.cursor/skills/<name>/SKILL.md
```

Optional YAML frontmatter for auto-discovery:

```yaml
---
name: prd-generator
description: Produce PRDs with FR/NFR requirements and success metrics.
---
```

### Claude Code

Copy `skill.md` to `.claude/skills/<name>/` per Claude documentation.

### Cline / Roo Code

Copy `skill.md` to the skills directory configured in IDE settings.

### GitHub Copilot

Paste skill content into repository `copilot-instructions.md` or project-level agent instructions.

## Catalog index

Machine-readable index: [catalog.json](../catalog.json)

Regenerate after adding skills:

```bash
python scripts/generate_catalog.py
python scripts/validate_skills.py
```

## Submission checklist

Before publishing to external catalogs:

- [ ] `python scripts/validate_skills.py` passes
- [ ] All 8 Playbook sections present
- [ ] README.md with usage example in repo
- [ ] Next Skills chain documented
- [ ] No secrets or environment-specific paths in skill.md
- [ ] LICENSE (MIT) included in repository

## Target catalogs (Stage 2)

| Catalog | Status | Notes |
|---------|--------|-------|
| GitHub repository | ready | Primary distribution |
| Cursor community skills | pending | Submit PR when repo public |
| awesome-agent-skills lists | pending | Include catalog.json link |
| LobeHub / Cline registries | pending | One skill.md per entry |

## Repository metadata

Suggested `package.json` or release tags:

- `v0.3.0` — 15 skills (Product + Architecture start)
- `v0.4.0` — 28 skills (full Architecture, AI, Product expansion)
- `v1.0.0` — 50+ skills (Stage 2 complete)

## Contributing

1. Copy `skills/_template/skill.md`
2. Follow [SKILL_STANDARD.md](SKILL_STANDARD.md)
3. Run validation and catalog generation
4. One skill per commit
5. Update ROADMAP, TODO, CHANGELOG

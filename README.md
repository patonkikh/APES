# APES

**50 Engineering Playbooks for AI agents** — Product, Architecture, AI, RAG, Security, MCP.

[MIT License](LICENSE)

---

## Install

### Cursor

```text
skills/<category>/<skill-name>/skill.md  →  ~/.cursor/skills/<skill-name>/SKILL.md
```

Copy the whole folder if you also want `examples.md` (optional).

### Claude Code

```text
skills/<category>/<skill-name>/  →  .claude/skills/<skill-name>/
```

Rename `skill.md` to `SKILL.md` if your setup requires it.

### Other agents

Copy `skill.md` into your IDE's skills directory. Plain Markdown — works in Cline, Windsurf, Copilot, and other Agent Skills-compatible tools.

---

## What's inside each skill

| File | Purpose |
|------|---------|
| `skill.md` | **Main file** — install this (rename to `SKILL.md` in Cursor) |
| `examples.md` | Optional worked examples |
| `README.md` | Short description for browsing on GitHub |

Each `skill.md` contains: Workflow, Decision Rules, Validation, Output template, and links to related skills.

---

## 50 skills

| Category | Count | Folder |
|----------|------:|--------|
| Product | 15 | [skills/product/](skills/product/) |
| Architecture | 10 | [skills/architecture/](skills/architecture/) |
| AI Engineering | 10 | [skills/ai/](skills/ai/) |
| RAG | 5 | [skills/rag/](skills/rag/) |
| Security | 5 | [skills/security/](skills/security/) |
| MCP | 5 | [skills/mcp/](skills/mcp/) |

Full list: [catalog.json](catalog.json)

---

## Example chain

```text
idea-validator → prd-generator → solution-architecture → prompt-engineer → owasp-llm-reviewer
```

Each skill's **Next Skills** section lists what to run next.

---

## License

[MIT](LICENSE) © 2026 APES Contributors

# APES — AI Product Engineering Skills Platform

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Skills](https://img.shields.io/badge/Skills-50-brightgreen)](catalog.json)

**Open library of Engineering Playbooks for AI agents** — structured methodologies for real engineering work, not role prompts.

Each Skill is a single **`skill.md`** file with workflow, decision rules, validation, anti-patterns, and recommended next skills.

Works with **Cursor**, Claude Code, Cline, Roo Code, GitHub Copilot, OpenAI Agents, Windsurf, LobeHub.

---

## Install a Skill

Copy **only** `skill.md` into your agent's skills folder.

**Cursor (personal skills):**

```text
skills/product/prd-generator/skill.md  →  ~/.cursor/skills/prd-generator/SKILL.md
```

Rename to `SKILL.md` if your IDE requires uppercase.

**Claude Code:** copy to `.claude/skills/<name>/`  
**Cline / Roo:** copy to your configured skills directory  
**GitHub Copilot:** paste content into project agent instructions

---

## Browse Skills

| Category | Count | Path |
|----------|------:|------|
| Product | 15 | [skills/product/](skills/product/) |
| Architecture | 10 | [skills/architecture/](skills/architecture/) |
| AI Engineering | 10 | [skills/ai/](skills/ai/) |
| RAG | 5 | [skills/rag/](skills/rag/) |
| AI Security | 5 | [skills/security/](skills/security/) |
| MCP | 5 | [skills/mcp/](skills/mcp/) |

Full machine-readable index: [catalog.json](catalog.json)

### Example pipelines

```text
Product:  idea-validator → prd-generator → story-mapping
Architecture:  solution-architecture → container-diagram-builder → architecture-review
AI:  prompt-engineer → prompt-reviewer → context-engineering
RAG:  rag-architecture-designer → chunking-strategy-advisor → hybrid-search-advisor
```

Each skill's `README.md` (in the repo only) describes usage — **install only `skill.md`**.

---

## What is a Skill?

An Engineering Playbook that tells an agent **how** to do one professional task:

- step-by-step workflow
- decision rules (if X then Y)
- validation checklist before delivery
- anti-patterns to avoid
- standardized output format
- links to related skills

No "You are a senior…" role play. Process, not persona.

---

## Repository layout

```text
skills/
  product/
  architecture/
  ai/
  rag/
  security/
  mcp/
catalog.json
LICENSE
README.md
```

---

## License

[MIT](LICENSE) © 2026 APES Contributors

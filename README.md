# APES — AI Product Engineering Skills Platform

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Skills](https://img.shields.io/badge/Skills-50-brightgreen)](catalog.json)
[![Validate](https://github.com/patonkikh/APES/actions/workflows/validate.yml/badge.svg)](https://github.com/patonkikh/APES/actions/workflows/validate.yml)

**Открытая библиотека Engineering Playbooks для AI-агентов** — не role prompts, а структурированные методологии для реальной инженерной работы.

> Каждый Skill — один файл `skill.md`: workflow, правила решений, валидация, anti-patterns и цепочка Next Skills.

Compatible with **Cursor**, Claude Code, Cline, Roo Code, GitHub Copilot, OpenAI Agents, Windsurf, LobeHub.

---

## Quick Start

```bash
git clone https://github.com/patonkikh/APES.git
cd APES
python scripts/validate_skills.py   # проверка всех skills
```

**Установка одного Skill (Cursor):**

```text
skills/product/prd-generator/skill.md  →  ~/.cursor/skills/prd-generator/SKILL.md
```

Подробнее: [docs/PUBLISHING.md](docs/PUBLISHING.md) · [ADR 0001](docs/adr/0001-skill-file-format.md)

---

## 50 Skills · 6 Categories

| Category | Count | Examples |
|----------|------:|----------|
| [product](skills/product/) | 15 | `prd-generator`, `okr-builder`, `story-mapping` |
| [architecture](skills/architecture/) | 10 | `solution-architecture`, `api-designer`, `adr-generator` |
| [ai](skills/ai/) | 10 | `prompt-engineer`, `context-engineering`, `multi-agent-planner` |
| [rag](skills/rag/) | 5 | `rag-architecture-designer`, `hybrid-search-advisor` |
| [security](skills/security/) | 5 | `owasp-llm-reviewer`, `guardrails-builder` |
| [mcp](skills/mcp/) | 5 | `mcp-server-generator`, `mcp-tool-generator` |

Полный индекс: **[catalog.json](catalog.json)** (50 skills)

---

## Skill Pipelines

End-to-end цепочки для типового product → architecture → AI flow:

```text
Product:  idea-validator → … → prd-generator → story-mapping
Architecture:  prd-generator → solution-architecture → … → architecture-review
AI:  ai-solution-architect → prompt-engineer → … → context-engineering → RAG
```

| Chain | Doc |
|-------|-----|
| Product | [SKILL_CHAIN.md](docs/SKILL_CHAIN.md) |
| Architecture | [SKILL_CHAIN_ARCHITECTURE.md](docs/SKILL_CHAIN_ARCHITECTURE.md) |
| AI | [SKILL_CHAIN_AI.md](docs/SKILL_CHAIN_AI.md) |
| RAG | [SKILL_CHAIN_RAG.md](docs/SKILL_CHAIN_RAG.md) |
| Security | [SKILL_CHAIN_SECURITY.md](docs/SKILL_CHAIN_SECURITY.md) |
| MCP | [SKILL_CHAIN_MCP.md](docs/SKILL_CHAIN_MCP.md) |

---

## Repository Map

```text
APES/
├── skills/              # 50 Engineering Playbooks (skill.md + README)
│   ├── _template/       # Эталон для новых skills
│   ├── product/
│   ├── architecture/
│   ├── ai/
│   ├── rag/
│   ├── security/
│   └── mcp/
├── docs/                # Стандарты, ADR, цепочки, публикация
├── scripts/             # validate_skills.py, generate_catalog.py
├── catalog.json         # Машиночитаемый индекс
├── AGENTS.md            # Инструкция для AI-агента разработки
├── ROADMAP.md           # Этапы 1–4
├── CHANGELOG.md
└── task.md              # BRD/SRS (источник требований)
```

---

## Development Status

| Stage | Status | Goal |
|-------|--------|------|
| 1 Foundation | done | 10 Product Skills + стандарты |
| 2 Growth | done | **50 Skills**, LICENSE, CI |
| 3 Scale | in progress | 100 Skills (Jira, Enterprise, GitHub…) |

См. [ROADMAP.md](ROADMAP.md) · [TODO.md](TODO.md) · [CHANGELOG.md](CHANGELOG.md)

---

## Contributing

Новый Skill: скопируйте [skills/_template/skill.md](skills/_template/skill.md), следуйте [SKILL_STANDARD.md](docs/SKILL_STANDARD.md).

→ [CONTRIBUTING.md](CONTRIBUTING.md)

---

## License

[MIT](LICENSE) © 2026 APES Contributors

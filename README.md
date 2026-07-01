# AI Product Engineering Skills Platform (APES)

Open library of **Engineering Playbooks** for AI agents — not role prompts, but structured methodologies for real engineering work.

## What is APES?

Each Skill is a single `skill.md` file that describes:

- how an expert solves one specific task;
- decision rules and validation criteria;
- anti-patterns and best practices;
- standardized output structure;
- recommended next Skills in the development chain.

Compatible with Cursor, Claude Code, Cline, Roo Code, GitHub Copilot, OpenAI Agents, Windsurf, LobeHub, and other agent IDEs.

## Install a Skill

Copy only the `skill.md` file from the skill directory into your agent's skills folder.

Example (Cursor personal skills):

```text
skills/product/prd-generator/skill.md  →  ~/.cursor/skills/prd-generator/SKILL.md
```

Rename to `SKILL.md` if your IDE requires uppercase. See [docs/adr/0001-skill-file-format.md](docs/adr/0001-skill-file-format.md).

## Repository structure

```text
skills/
  product/          # Product discovery, strategy, delivery
  architecture/     # Solution architecture, ADR, API design
  ai/               # AI engineering, prompts, multi-agent
  rag/              # RAG architecture and optimization
  mcp/              # MCP server, client, tools
docs/
  ARCHITECTURE.md   # Platform architecture
  SKILL_STANDARD.md # Engineering Playbook standard
  PUBLISHING.md     # Distribution guide
  adr/              # Architecture Decision Records
catalog.json        # Machine-readable skill index
```

## Documentation

| File | Purpose |
|------|---------|
| [task.md](task.md) | BRD/SRS — source requirements |
| [AGENTS.md](AGENTS.md) | Instructions for development agents |
| [ROADMAP.md](ROADMAP.md) | Development roadmap |
| [TODO.md](TODO.md) | Current tasks |
| [CHANGELOG.md](CHANGELOG.md) | Change log |

## Status — 50 Skills (Stage 2 complete)

| Category | Skills |
|----------|--------|
| product | 15 |
| architecture | 10 |
| ai | 10 |
| rag | 5 |
| security | 5 |
| mcp | 5 |

Full index: [catalog.json](catalog.json)

Skill chains: [Product](docs/SKILL_CHAIN.md) · [Architecture](docs/SKILL_CHAIN_ARCHITECTURE.md) · [AI](docs/SKILL_CHAIN_AI.md) · [RAG](docs/SKILL_CHAIN_RAG.md) · [Security](docs/SKILL_CHAIN_SECURITY.md) · [MCP](docs/SKILL_CHAIN_MCP.md)

```bash
python scripts/validate_skills.py
python scripts/generate_catalog.py
```

## Stage 3 (current)

Expand to 100 Skills: Jira, Enterprise, Startup, GitHub.

## License

MIT — see [LICENSE](LICENSE)

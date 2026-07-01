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
  security/         # AI security and governance
  ...
docs/
  ARCHITECTURE.md   # Platform architecture
  SKILL_STANDARD.md # Engineering Playbook standard
  adr/              # Architecture Decision Records
```

## Documentation

| File | Purpose |
|------|---------|
| [task.md](task.md) | BRD/SRS — source requirements |
| [AGENTS.md](AGENTS.md) | Instructions for development agents |
| [ROADMAP.md](ROADMAP.md) | Development roadmap |
| [TODO.md](TODO.md) | Current tasks |
| [CHANGELOG.md](CHANGELOG.md) | Change log |

## Stage 1 (current)

- Platform architecture and standards
- First 10 Product Skills (Discovery → Strategy → Delivery chain)

## License

MIT (to be added in Stage 2)

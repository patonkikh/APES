# APES



### AI Product Engineering Skills Platform



[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

[![Skills](https://img.shields.io/badge/Skills-50-brightgreen)](catalog.json)

[![Spec](https://img.shields.io/badge/Agent%20Skills-v1.1-blue)](https://agentskills.io/specification)

[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/patonkikh/APES/pulls)



**Engineering Playbooks for AI agents** — structured workflows for real professional work, not role prompts.



**Repository:** [github.com/patonkikh/APES](https://github.com/patonkikh/APES)



[Browse skills](#browse-by-category) · [Install](#install) · [Catalog](catalog.json)



---



## Why APES?



Most agent "skills" are thin prompts: *"You are a senior engineer…"* with no process, no validation, and no standard output.



**APES Skills are different.** Each one is an **Engineering Playbook** for a single task:



| Section | What it gives you |

|---------|-------------------|

| **Workflow** | Step-by-step methodology |

| **Decision Rules** | If X → do Y |

| **Validation** | Checklist before delivery |

| **Anti-patterns** | What to avoid |

| **Output Structure** | Standardized artifact template |

| **Next Skills** | What to run next in the pipeline |



Compatible with the [Agent Skills open specification](https://agentskills.io/specification) (YAML frontmatter for agent discovery).



---



## Install



### Cursor / Claude Code / Agent Skills runtimes



Copy the skill folder (or at minimum `skill.md`). Rename `skill.md` → `SKILL.md`:



```text

skills/product/prd-generator/  →  ~/.cursor/skills/prd-generator/

  skill.md                     →  SKILL.md   (keep YAML frontmatter intact)

  examples.md                  →  examples.md (optional, recommended for flagship skills)

```



The YAML frontmatter at the top of each file enables **automatic skill discovery**:



```yaml

---

name: prd-generator

description: >

  Produces a PRD with FR/NFR IDs and success metrics.

  Use when writing PRDs, MVP specs, or product requirements.

metadata:

  apes-version: "1.1"

  category: product

---

```



### Other IDEs



| IDE | Destination |

|-----|-------------|

| Claude Code | `.claude/skills/<name>/` |

| Cline / Roo Code | Your configured skills directory |

| GitHub Copilot | Project agent instructions |

| Windsurf / LobeHub | Skills folder per IDE docs |



---



## Skill structure (v1.1)



```text

skills/<category>/<skill-name>/

├── skill.md       # Required — frontmatter + 8-section playbook

├── README.md      # GitHub browsing notes (not required for install)

└── examples.md    # Optional — worked input/output (progressive disclosure)

```



**Progressive disclosure:** agents load `name` + `description` at startup (~100 tokens), full `skill.md` on activation, `examples.md` on demand.



**Examples:** Every skill includes [examples.md](skills/product/prd-generator/examples.md) with worked input/output (progressive disclosure).



---



## Browse by category



| Category | Skills | Highlights |

|----------|-------:|------------|

| [**Product**](skills/product/) | 15 | `idea-validator` · `prd-generator` · `story-mapping` |

| [**Architecture**](skills/architecture/) | 10 | `solution-architecture` · `api-designer` · `adr-generator` |

| [**AI Engineering**](skills/ai/) | 10 | `prompt-engineer` · `context-engineering` · `multi-agent-planner` |

| [**RAG**](skills/rag/) | 5 | `rag-architecture-designer` · `hybrid-search-advisor` |

| [**AI Security**](skills/security/) | 5 | `owasp-llm-reviewer` · `guardrails-builder` |

| [**MCP**](skills/mcp/) | 5 | `mcp-server-generator` · `mcp-tool-generator` |



**Full index:** [catalog.json](catalog.json) (machine-readable, 50 skills, v1.1)



---



## Example pipelines



Skills chain together via the **Next Skills** section in each playbook:



```text

Discovery     idea-validator → problem-statement-builder → persona-generator

Strategy      product-vision-builder → feature-prioritization → prd-generator

Delivery      epic-generator → user-story-generator → acceptance-criteria-generator

Architecture  solution-architecture → system-context-builder → architecture-review

AI            ai-solution-architect → prompt-engineer → prompt-reviewer → context-engineering

RAG           rag-architecture-designer → chunking-strategy-advisor → retriever-optimizer

Security      ai-threat-modeling → prompt-injection-detector → owasp-llm-reviewer

MCP           mcp-server-generator → mcp-tool-generator → mcp-security-review

```



---



## Repository structure



```text

APES/

├── skills/

│   ├── product/          # Discovery, strategy, delivery

│   ├── architecture/     # C4, ADR, API design

│   ├── ai/               # Prompts, agents, evaluation

│   ├── rag/              # Retrieval pipelines

│   ├── security/         # LLM security & governance

│   └── mcp/              # Model Context Protocol

├── catalog.json          # Skill index (v1.1)

├── LICENSE

└── README.md

```



---



## Compatibility



Tested workflow with: **Cursor**, Claude Code, Cline, Roo Code, GitHub Copilot, OpenAI Agents, Windsurf, LobeHub.



| Layer | Standard |

|-------|----------|

| Discovery metadata | [Agent Skills spec](https://agentskills.io/specification) — `name` + `description` |

| Playbook body | APES 8-section Engineering Playbook |

| File naming | `skill.md` in repo → `SKILL.md` on install |



---



## License



[MIT](LICENSE) © 2026 APES Contributors


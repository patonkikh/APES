# APES Skill Standard — Engineering Playbook

**Version:** 1.1  
**Date:** 2026-07-01  
**Compatibility:** [Agent Skills open spec](https://agentskills.io/specification) (frontmatter layer)

---

## 1. Purpose

Each Skill is a complete methodology for one engineering task. A Skill **does not play a role** — a Skill **implements a process**.

APES v1.1 adds an **Agent Skills-compatible metadata layer** (YAML frontmatter) for agent discovery, while keeping the 8-section Engineering Playbook body unchanged.

---

## 2. Directory layout

```text
skills/<category>/<skill-name>/
├── skill.md          # Required — metadata + 8-section playbook (install as SKILL.md)
├── README.md         # Optional — GitHub browsing context (not loaded by agents)
├── examples.md       # Optional — worked input/output examples (progressive disclosure)
└── references.md     # Optional — deep reference material (progressive disclosure)
```

**Install mapping (Cursor / Agent Skills runtimes):**

```text
skills/product/prd-generator/skill.md  →  ~/.cursor/skills/prd-generator/SKILL.md
```

The repository uses lowercase `skill.md` for cross-IDE portability. Rename to `SKILL.md` on install.

---

## 3. File format

### 3.1 YAML frontmatter (required in v1.1)

Every `skill.md` **must** start with YAML frontmatter per [agentskills.io](https://agentskills.io/specification):

```yaml
---
name: prd-generator
description: >
  Produces a Product Requirements Document (PRD) with FR/NFR IDs, user flows,
  and success metrics. Use when writing PRDs, MVP specs, or product requirements.
metadata:
  apes-version: "1.1"
  category: product
---
```

| Field | Required | Rules |
|-------|----------|-------|
| `name` | Yes | kebab-case; must match parent directory name |
| `description` | Yes | WHAT + WHEN; third person; ≤1024 chars; include trigger terms |
| `metadata.apes-version` | Yes | `"1.1"` |
| `metadata.category` | Yes | `product` \| `architecture` \| `ai` \| `rag` \| `security` \| `mcp` \| `data` \| `devops` \| `growth` |
| `license` | No | Defaults to MIT at repo level |
| `compatibility` | No | Use when skill needs specific tools or network |

**Description formula:**

```text
[What the skill produces — one sentence from Purpose].
Use when [trigger scenario 1], [trigger scenario 2], or [domain keywords].
```

### 3.2 Body (8 sections, unchanged)

After frontmatter and title H1, every skill.md **must** contain all 8 sections in this order:

| # | Section | Purpose |
|---|---------|---------|
| 1 | **Purpose** | One task, measurable outcome; Input/Output |
| 2 | **Workflow** | Sequential steps with gather → act → verify |
| 3 | **Decision Rules** | If condition X → action Y (include Stop rules) |
| 4 | **Validation** | Checklist before delivery (≥5 items) |
| 5 | **Anti-patterns** | ≥3 named mistakes with examples |
| 6 | **Best Practices** | Methodology-specific guidance |
| 7 | **Output Structure** | Fillable markdown template |
| 8 | **Next Skills** | Chain to adjacent skills (`category/skill-name`) |

### 3.3 Size limits

| Layer | Limit | Rationale |
|-------|-------|-----------|
| Frontmatter | ~100 tokens | Loaded at agent startup for discovery |
| `skill.md` body | 80–350 lines | Full activation load; keep lean |
| `examples.md` | ≤200 lines | Loaded on demand |
| `references.md` | ≤300 lines | Loaded on demand |

Move content beyond limits to `examples.md` or `references.md`. Reference from Purpose:

```markdown
**Examples:** See [examples.md](examples.md) for worked input/output.
```

---

## 4. Forbidden

- Role Play ("You are a senior product manager...")
- "You are..." in any form (including inside prompt templates in examples)
- Fictional roles and personas as instructions
- Assuming unknown data without explicit user request
- Multiple unrelated tasks in one Skill
- Deeply nested file references (max one level from `skill.md`)

---

## 5. Required Skill behavior

Every Skill must guide the agent to:

- detect contradictions in input data;
- detect ambiguities and request clarification;
- detect missing dependencies;
- detect missing input data;
- verify result completeness via Validation;
- suggest improvements when the result is incomplete;
- consider security, scalability, maintainability (where applicable).

---

## 6. Progressive disclosure pattern

```text
Discovery     →  frontmatter name + description  (~100 tokens, always)
Activation    →  skill.md body                   (~2000–4000 tokens)
Deep dive     →  examples.md, references.md      (on demand)
```

Flagship skills should ship with `examples.md`. Other skills may add it in future releases.

---

## 7. Pre-publication review checklist

```text
Skill Review (v1.1):
- [ ] YAML frontmatter with name matching directory
- [ ] description includes WHAT + WHEN + trigger terms
- [ ] metadata.apes-version = "1.1"
- [ ] Exactly one task in Purpose
- [ ] All 8 body sections present
- [ ] No Role Play / "You are..."
- [ ] Workflow — sequential steps with inputs/outputs
- [ ] Decision Rules — concrete if/then rules with Stop conditions
- [ ] Validation — verifiable checklist (≥5 items)
- [ ] Anti-patterns — ≥3 concrete mistakes
- [ ] Output Structure — fillable template
- [ ] Next Skills — consistent with adjacent Skills in chain
- [ ] 80–350 lines in skill.md body (excluding frontmatter)
- [ ] examples.md present for flagship skills (recommended)
- [ ] Skill README.md contains usage example
```

---

## 8. Naming

| Element | Rule | Example |
|---------|------|---------|
| Skill directory | kebab-case | `prd-generator` |
| Frontmatter `name` | same as directory | `prd-generator` |
| Repository file | lowercase | `skill.md` |
| Installed file | uppercase (Agent Skills) | `SKILL.md` |
| Purpose title | Human-readable name | PRD Generator |
| Next Skills | kebab-case path from skills/ | `product/epic-generator` |

---

## 9. APES v1.1 vs Agent Skills open spec

| Agent Skills requirement | APES v1.1 |
|--------------------------|-----------|
| `SKILL.md` with frontmatter | ✅ `skill.md` with frontmatter; rename on install |
| `name` + `description` | ✅ Required |
| Body under 500 lines | ✅ Target 80–350 |
| `scripts/` optional | ✅ `scripts/validate_skills.py` for contributors |
| `references/` optional | ✅ `references.md` per skill when needed |
| `examples/` optional | ✅ `examples.md` per skill when needed |

---

## 10. Methodologies by category (reference)

| Category | Recommended methodologies |
|----------|---------------------------|
| Product Discovery | Lean Startup, JTBD, Opportunity Solution Tree |
| Product Strategy | RICE, ICE, MoSCoW, OKR, North Star |
| Product Delivery | INVEST, Given-When-Then, Story Mapping |
| Architecture | C4, ADR, Domain-Driven Design |
| RAG | Chunking strategies, RAGAS, hybrid search |
| AI Security | OWASP LLM Top 10, threat modeling |
| MCP | Agent Skills spec, JSON Schema tool inputs |
| Data & ML | dbt metrics, data quality dimensions, labeling QA |
| DevOps | CI/CD stages, canary deploy, runbooks, SRE |
| Growth | GTM canvas, pricing tiers, experiment design |

---

## 11. Template

Reference: [skills/_template/skill.md](../skills/_template/skill.md)

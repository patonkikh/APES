<p align="center">
  <img src="assets/banner.svg" alt="APES — AI Product Engineering Skills" width="100%">
</p>

<p align="center">
  <strong>50 Engineering Playbooks for AI agents</strong><br>
  Structured workflows for real work — not <em>"You are a senior engineer…"</em>
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="MIT License"></a>
  <a href="catalog.json"><img src="https://img.shields.io/badge/Skills-50-brightgreen" alt="50 Skills"></a>
  <a href="https://agentskills.io/specification"><img src="https://img.shields.io/badge/Agent%20Skills-compatible-purple" alt="Agent Skills"></a>
  <a href="https://github.com/patonkikh/APES"><img src="https://img.shields.io/badge/GitHub-patonkikh%2FAPES-black" alt="GitHub"></a>
</p>

<p align="center">
  <a href="#install">Install</a> ·
  <a href="#skill-anatomy">Anatomy</a> ·
  <a href="#categories">Categories</a> ·
  <a href="#pipelines">Pipelines</a> ·
  <a href="catalog.json">Catalog</a>
</p>

---

## Why APES?

```mermaid
flowchart LR
    subgraph Before["Typical skill"]
        A["You are a senior PM…"]
        A --> B["Vague advice"]
    end
    subgraph After["APES Playbook"]
        C["Workflow"] --> D["Decision Rules"]
        D --> E["Validation"]
        E --> F["Standard output"]
    end
    Before -.->|"upgrade"| After

    style Before fill:#1e293b,stroke:#475569,color:#94a3b8
    style After fill:#0f172a,stroke:#38bdf8,color:#e2e8f0
```

| | Role prompt | APES Playbook |
|---|-------------|---------------|
| Process | None | Step-by-step workflow |
| Quality gate | None | Validation checklist |
| Output | Free-form | Standard template |
| Chaining | None | Next Skills links |

---

## Install

```mermaid
flowchart TB
    A["Clone APES"] --> B["Pick skill folder"]
    B --> C{"Your IDE"}
    C -->|Cursor| D["~/.cursor/skills/name/SKILL.md"]
    C -->|Claude Code| E[".claude/skills/name/"]
    C -->|Other| F["Your skills directory"]
    D --> G["Ask agent to use skill"]

    style A fill:#1e3a5f,stroke:#38bdf8,color:#e2e8f0
    style G fill:#14532d,stroke:#34d399,color:#e2e8f0
```

### Cursor

```bash
git clone https://github.com/patonkikh/APES.git
mkdir -p ~/.cursor/skills/prd-generator
cp APES/skills/product/prd-generator/skill.md ~/.cursor/skills/prd-generator/SKILL.md
```

Then ask: *"Use prd-generator to write a PRD for …"*

### Claude Code

```bash
cp -r APES/skills/product/prd-generator ~/.claude/skills/prd-generator
# rename skill.md → SKILL.md if needed
```

### Other agents

Cline · Windsurf · Copilot · Roo Code — copy `skill.md` into your skills folder. Plain Markdown, [Agent Skills](https://agentskills.io/specification) frontmatter.

---

## Skill anatomy

<a id="skill-anatomy"></a>

```mermaid
flowchart TB
    subgraph Discovery["Loaded at startup ~100 tokens"]
        FM["YAML frontmatter<br/>name + description"]
    end
    subgraph Activation["Loaded on use"]
        SK["skill.md body"]
        SK --> P["Purpose"]
        SK --> W["Workflow"]
        SK --> R["Decision Rules"]
        SK --> V["Validation"]
        SK --> O["Output Structure"]
        SK --> N["Next Skills"]
    end
    subgraph Optional["On demand"]
        EX["examples.md"]
        REF["references.md"]
    end
    FM --> SK
    SK -.-> EX
    SK -.-> REF

    style Discovery fill:#1e293b,stroke:#64748b,color:#cbd5e1
    style Activation fill:#0f172a,stroke:#38bdf8,color:#e2e8f0
    style Optional fill:#1a2e1a,stroke:#34d399,color:#d1fae5
```

| File | Install? | What it does |
|------|:--------:|--------------|
| `skill.md` → `SKILL.md` | **Yes** | Full playbook — the only required file |
| `examples.md` | Optional | Worked input → output samples |
| `references.md` | Optional | Domain cheat sheets (OWASP, C4, MCP…) |
| `README.md` | No | Browse on GitHub only |

---

## Categories

<a id="categories"></a>

```mermaid
pie showData
    title 50 Skills by Category
    "Product (15)" : 15
    "Architecture (10)" : 10
    "AI Engineering (10)" : 10
    "RAG (5)" : 5
    "Security (5)" : 5
    "MCP (5)" : 5
```

<table>
<tr>
<td width="33%" valign="top">

### Product · 15

[`skills/product/`](skills/product/)

Discovery → Strategy → Delivery

`idea-validator` · `prd-generator` · `okr-builder` · `user-story-generator`

</td>
<td width="33%" valign="top">

### Architecture · 10

[`skills/architecture/`](skills/architecture/)

C4 · ADR · API design

`solution-architecture` · `adr-generator` · `api-designer`

</td>
<td width="33%" valign="top">

### AI · 10

[`skills/ai/`](skills/ai/)

Prompts · Agents · Eval

`prompt-engineer` · `multi-agent-planner` · `context-engineering`

</td>
</tr>
<tr>
<td valign="top">

### RAG · 5

[`skills/rag/`](skills/rag/)

Retrieval pipelines

`rag-architecture-designer` · `hybrid-search-advisor`

</td>
<td valign="top">

### Security · 5

[`skills/security/`](skills/security/)

OWASP LLM · Threats

`owasp-llm-reviewer` · `guardrails-builder`

</td>
<td valign="top">

### MCP · 5

[`skills/mcp/`](skills/mcp/)

Model Context Protocol

`mcp-server-generator` · `mcp-tool-generator`

</td>
</tr>
</table>

**Full index:** [`catalog.json`](catalog.json)

---

## Pipelines

<a id="pipelines"></a>

Skills chain via **Next Skills** in each playbook:

```mermaid
flowchart LR
    subgraph Discovery
        iv[idea-validator] --> ps[problem-statement]
        ps --> pg[persona-generator]
    end
    subgraph Strategy
        pv[product-vision] --> fp[feature-prioritization]
        fp --> prd[prd-generator]
    end
    subgraph Delivery
        prd --> ep[epic-generator]
        ep --> us[user-story-generator]
        us --> ac[acceptance-criteria]
    end

    style prd fill:#1e3a5f,stroke:#38bdf8,color:#fff
```

```mermaid
flowchart LR
    subgraph Engineering
        sa[solution-architecture] --> sc[system-context]
        sc --> ar[architecture-review]
    end
    subgraph AI_Stack["AI Stack"]
        pe[prompt-engineer] --> pr[prompt-reviewer]
        pr --> ce[context-engineering]
    end
    subgraph Safety
        tm[ai-threat-modeling] --> pi[prompt-injection]
        pi --> ow[owasp-llm-reviewer]
    end

    style ow fill:#3b1219,stroke:#f87171,color:#fff
```

---

## Repository

```text
APES/
├── assets/           # Banner & visuals
├── skills/
│   ├── product/          15 skills
│   ├── architecture/     10 skills
│   ├── ai/                 10 skills
│   ├── rag/                 5 skills
│   ├── security/            5 skills
│   └── mcp/                 5 skills
├── catalog.json
├── LICENSE
└── README.md
```

---

## License

[MIT](LICENSE) © 2026 APES Contributors

<p align="center">
  <sub>Compatible with <a href="https://agentskills.io/specification">Agent Skills</a> · Built for Cursor, Claude Code, and open agents</sub>
</p>

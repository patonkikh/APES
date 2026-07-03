

*The largest open-source collection of professional Engineering Skills for AI Agentse* 
 
Structured workflows for real work — not *"You are a senior engineer…"*



[Install](#install) · [Anatomy](#skill-anatomy) · [Categories](#categories) · [Pipelines](#pipelines) · [Catalog](catalog.json)

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




|              | Role prompt | APES Playbook         |
| ------------ | ----------- | --------------------- |
| Process      | None        | Step-by-step workflow |
| Quality gate | None        | Validation checklist  |
| Output       | Free-form   | Standard template     |
| Chaining     | None        | Next Skills links     |


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




| File                    | Install? | What it does                           |
| ----------------------- | -------- | -------------------------------------- |
| `skill.md` → `SKILL.md` | **Yes**  | Full playbook — the only required file |
| `examples.md`           | Optional | Worked input → output samples          |
| `references.md`         | Optional | Domain cheat sheets (OWASP, C4, MCP…)  |
| `README.md`             | No       | Browse on GitHub only                  |


---

## Categories



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




|     |
| --- |
|     |


### Product · 15

`[skills/product/](skills/product/)`

Discovery → Strategy → Delivery

`idea-validator` · `prd-generator` · `okr-builder` · `user-story-generator`



### Architecture · 10

`[skills/architecture/](skills/architecture/)`

C4 · ADR · API design

`solution-architecture` · `adr-generator` · `api-designer`



### AI · 10

`[skills/ai/](skills/ai/)`

Prompts · Agents · Eval

`prompt-engineer` · `multi-agent-planner` · `context-engineering`



### RAG · 5

`[skills/rag/](skills/rag/)`

Retrieval pipelines

`rag-architecture-designer` · `hybrid-search-advisor`



### Security · 5

`[skills/security/](skills/security/)`

OWASP LLM · Threats

`owasp-llm-reviewer` · `guardrails-builder`



### MCP · 5

`[skills/mcp/](skills/mcp/)`

Model Context Protocol

`mcp-server-generator` · `mcp-tool-generator`



**Full index:** `[catalog.json](catalog.json)`

---

## Pipelines



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

Compatible with [Agent Skills](https://agentskills.io/specification) · Built for Cursor, Claude Code, and open agents
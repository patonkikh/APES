# Solution Architecture

# Purpose

Design a solution architecture from PRD and constraints: identify components, integration patterns, technology options, and quality attribute trade-offs.

**Input:** PRD or requirements, NFRs, constraints (cloud, team, budget, compliance)  
**Output:** Solution Architecture document with component model, integration view, and technology recommendations

---

# Workflow

## Step 1: Extract architectural drivers

From input, identify:

- Functional capabilities (from FRs)
- Quality attributes (performance, security, scalability, availability, maintainability)
- Constraints (must-use tech, regulatory, timeline, team skills)
- Assumptions and unknowns

## Step 2: Define architectural principles

Establish 3–5 decision principles for this solution:

- Example: "Prefer managed services over self-hosted for MVP"
- Example: "Event-driven for async workflows; sync API for user-facing reads"

Each principle must guide trade-off decisions.

## Step 3: Propose logical component model

Decompose into logical components:

| Component | Responsibility | Interfaces |
|-----------|----------------|------------|

Group by capability, not by team or org chart.

## Step 4: Select integration patterns

For each component interaction, specify:

- Pattern: sync REST, async messaging, event bus, batch, shared DB (discourage)
- Data flow direction
- Failure handling approach

## Step 5: Evaluate technology options

For each major component, provide 2–3 options with trade-off table:

| Option | Pros | Cons | Fit score |

Recommend one option with rationale tied to architectural drivers.

## Step 6: Document risks and open decisions

List architectural risks and decisions requiring ADR.

## Step 7: Validate

Run Validation checklist.

---

# Decision Rules

| Condition | Action |
|-----------|--------|
| No PRD or requirements | Stop; request PRD or run product/prd-generator |
| NFRs missing | Add minimum NFRs (security, availability, performance) before design |
| Single obvious architecture | Still document rejected alternatives with rationale |
| Constraint conflicts with recommendation | Flag conflict; present compliant alternative |
| Premature technology choice in PRD | Separate product requirements from architecture decisions |

---

# Validation

- [ ] Architectural drivers documented (FRs + NFRs + constraints)
- [ ] 3–5 architectural principles defined
- [ ] Component model covers all Must-have FRs
- [ ] Integration pattern specified for each interaction
- [ ] Technology options include trade-off rationale
- [ ] Risks and open decisions listed
- [ ] No implementation code or detailed API specs (defer to api-designer)

---

# Anti-patterns

- **Big ball of mud** — single monolithic component without boundaries.
- **Resume-driven architecture** — choosing tech for novelty, not drivers.
- **Shared database integration** — components coupled through one DB without justification.
- **Ignoring NFRs** — functional-only architecture.
- **Copy-paste reference architecture** — applying microservices without scale justification.

---

# Best Practices

- Align with C4 model progression: solution → context → container.
- Document rejected alternatives (supports future ADRs).
- Map each component to FR IDs for traceability.
- Prefer simplest architecture that meets NFRs (YAGNI).
- Flag decisions needing ADR before implementation.

---

# Output Structure

```markdown
# Solution Architecture: [System Name]

## Architectural Drivers
| Driver | Source | Priority |
|--------|--------|----------|

## Principles
| # | Principle | Implication |
|---|-----------|-------------|

## Component Model
| Component | Responsibility | FRs covered |
|-----------|----------------|-------------|

## Integration View
| From | To | Pattern | Data | Failure handling |
|------|----|---------|------|------------------|

## Technology Recommendations
| Component | Recommended | Alternatives | Rationale |
|-----------|-------------|--------------|-----------|

## Quality Attribute Analysis
| Attribute | Approach | Risk |
|-----------|----------|------|

## Open Decisions
| Decision | Options | Recommended ADR |
|----------|---------|-----------------|

## Risks
| Risk | Impact | Mitigation |
|------|--------|------------|
```

---

# Next Skills

| Outcome | Recommended Skill |
|---------|-------------------|
| Document context diagram | `architecture/system-context-builder` |
| Design APIs | `architecture/api-designer` |
| Record key decisions | `architecture/adr-generator` |
| Review architecture | `architecture/architecture-review` |
| PRD missing | `product/prd-generator` |

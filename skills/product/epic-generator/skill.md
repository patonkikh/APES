# Epic Generator

# Purpose

Decompose a PRD or feature scope into well-structured epics with goals, scope boundaries, and story count estimates.

**Input:** PRD or feature description, priorities (optional)  
**Output:** Epic breakdown document with epic goals, boundaries, and suggested user story themes

---

# Workflow

## Step 1: Parse input scope

Extract from PRD or user input:

- Functional requirements grouped by theme
- User flows
- Dependencies between requirements
- Priority levels (Must/Should/Could)

## Step 2: Apply epic decomposition rules

Each epic must:

- Deliver user-visible value (not purely technical)
- Be completable in 1–3 sprints (guideline)
- Have a clear goal statement
- Map to one or more FR IDs from PRD

## Step 3: Define epic structure

For each epic:

- **Goal:** what user outcome this epic achieves
- **Scope:** included FRs and flows
- **Out of scope:** what this epic explicitly excludes
- **Dependencies:** other epics that must complete first
- **Story themes:** 3–7 user story titles (not full stories yet)
- **Estimate:** story count range (not hours)

## Step 4: Sequence epics

Order epics by:

1. Dependencies (blockers first)
2. Priority (Must before Should)
3. Risk (validate riskiest epic early)

## Step 5: Validate

Run Validation checklist.

---

# Decision Rules

| Condition | Action |
|-----------|--------|
| Epic has no user-visible value | Reframe or merge with another epic |
| Epic exceeds 3 sprints estimated | Split into smaller epics |
| Technical-only epic (e.g. "set up CI") | Mark as enabler epic; separate from user epics |
| Circular dependencies | Restructure epics to break cycle |
| No PRD or requirements | Stop; request PRD or run prd-generator |

---

# Validation

- [ ] Every FR from input maps to exactly one epic
- [ ] Each epic has goal, scope, out-of-scope, dependencies
- [ ] Each epic has 3–7 story themes
- [ ] No epic is purely technical without enabler label
- [ ] Epic sequence respects dependencies
- [ ] Story count estimates are ranges, not false-precision hours
- [ ] Epic count is reasonable (3–8 for typical MVP)

---

# Anti-patterns

- **Epic = component** — "Backend API" instead of user outcome.
- **Giant epic** — single epic for entire product.
- **Micro epics** — one story per epic.
- **Missing dependencies** — sequencing that ignores blockers.
- **Story themes as tasks** — "set up database" instead of user value.

---

# Best Practices

- Name epics by user outcome: "User can authenticate" not "Auth module".
- Keep enabler epics visible but separate from value epics.
- Align epic order with feature prioritization if available.
- Leave detailed story writing to user-story-generator.
- Flag epics needing spikes or research.

---

# Output Structure

```markdown
# Epic Breakdown: [Product/Feature Name]

## Overview
- **Source:** [PRD reference]
- **Total epics:** N
- **Estimated stories:** X–Y

## Epic Sequence
1. [Epic name] → 2. [Epic name] → ...

## Epics

### Epic 1: [Name]
- **Goal:** [user outcome]
- **FRs covered:** FR-001, FR-003
- **Scope:** [what's included]
- **Out of scope:** [excluded]
- **Dependencies:** none | Epic N
- **Story themes:**
  1. [Theme title]
- **Estimate:** 4–6 stories

[Repeat for each epic]

## Dependency Graph
[Epic A] → [Epic B]

## Open Questions
- [ ] [Question]
```

---

# Next Skills

| Outcome | Recommended Skill |
|---------|-------------------|
| Write stories for epic | `product/user-story-generator` |
| Add acceptance criteria | `product/acceptance-criteria-generator` |
| Visualize full journey | `product/story-mapping` |
| PRD missing | `product/prd-generator` |

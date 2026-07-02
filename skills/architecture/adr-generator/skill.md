---
name: adr-generator
description: >
  Create Architecture Decision Records (ADRs) for significant technical decisions using the Michael Nygard format with structured context, options, and consequences. Use when working on architecture decision records, ADRs, technical decisions.
metadata:
  apes-version: "1.1"
  category: architecture
---

# ADR Generator

# Purpose

Create Architecture Decision Records (ADRs) for significant technical decisions using the Michael Nygard format with structured context, options, and consequences.

**Input:** Decision topic, architectural context, options considered (optional)  
**Output:** ADR document ready for `docs/adr/` with status, context, decision, and consequences
**Examples:** See [examples.md](examples.md) for worked input/output.

---

# Workflow

## Step 1: Frame the decision

Identify:

- Decision title (short, specific)
- Status: Proposed | Accepted | Deprecated | Superseded
- Date and deciders
- What question this ADR answers

## Step 2: Write context

Describe:

- Business and technical forces at play
- Constraints (time, team, compliance, budget)
- Quality attributes affected
- Why a decision is needed now

## Step 3: Document considered options

For each option (minimum 2):

| Option | Description | Pros | Cons |
|--------|-------------|------|------|

Include "do nothing" or "defer" if applicable.

## Step 4: Record the decision

State the chosen option clearly:

"We will [action] because [rationale tied to drivers]."

## Step 5: Document consequences

**Positive:**

- Benefits of this decision

**Negative:**

- Trade-offs and accepted downsides

**Neutral:**

- Side effects requiring monitoring

## Step 6: Add compliance and follow-up

- Related ADRs (supersedes, relates to)
- Review date
- Implementation notes

## Step 7: Validate

Run Validation checklist.

---

# Decision Rules

| Condition | Action |
|-----------|--------|
| Only one option considered | Research and add at least one alternative |
| Decision is trivial/reversible | Recommend skipping ADR; document in PR instead |
| Decision already made without documentation | Write ADR as Accepted with retrospective context |
| Options lack trade-off analysis | Complete pros/cons before recording decision |
| Supersedes existing ADR | Link to prior ADR; update prior status to Superseded |

---

# Validation

- [ ] Title is specific and actionable
- [ ] Status field present
- [ ] Context explains forces and constraints
- [ ] ≥2 options with pros/cons
- [ ] Decision statement is unambiguous
- [ ] Positive and negative consequences listed
- [ ] Related ADRs linked if applicable
- [ ] Follows Nygard ADR structure

---

# Anti-patterns

- **ADR as design doc** — entire architecture in one ADR.
- **No alternatives** — single option without comparison.
- **Vague decision** — "we will use best practices."
- **Missing consequences** — only listing benefits.
- **Stale ADRs** — not marking superseded decisions.

---

# Best Practices

- One decision per ADR.
- Number sequentially: 0001, 0002...
- Write for future team members who lack current context.
- Link to solution architecture drivers.
- Set review date for reversible decisions (6–12 months).

---

# Output Structure

```markdown
# ADR NNNN: [Short Title]

**Status:** Proposed | Accepted | Deprecated | Superseded by ADR-XXXX
**Date:** YYYY-MM-DD
**Deciders:** [names or roles]

## Context
[Forces, constraints, why now]

## Decision Drivers
- [Driver 1]
- [Driver 2]

## Considered Options
### Option 1: [Name]
[Description]
| Pros | Cons |
|------|------|

### Option 2: [Name]
[Description]
| Pros | Cons |
|------|------|

## Decision
We will **[chosen option]** because **[rationale]**.

## Consequences
### Positive
- [Benefit]

### Negative
- [Trade-off]

### Neutral
- [Side effect]

## Related ADRs
- [Link]

## Review Date
[Date]
```

---

# Next Skills

| Outcome | Recommended Skill |
|---------|-------------------|
| Review architecture with ADRs | `architecture/architecture-review` |
| Update container diagram | `architecture/container-diagram-builder` |
| More decisions to document | `architecture/adr-generator` |
| Solution needs revision | `architecture/solution-architecture` |

---
name: user-story-generator
description: >
  Generate INVEST-compliant user stories from epics or requirements with clear value statements and story point guidance. Use when working on product discovery, PRDs, user stories, OKRs, or backlog planning.
metadata:
  apes-version: "1.1"
  category: product
---

# User Story Generator

# Purpose

Generate INVEST-compliant user stories from epics or requirements with clear value statements and story point guidance.

**Input:** Epic description, story themes, or FR list; persona (optional)  
**Output:** User story set with IDs, INVEST validation, and dependency notes
**Examples:** See [examples.md](examples.md) for worked input/output.

---

# Workflow

## Step 1: Identify story sources

Extract story candidates from:

- Epic story themes
- PRD functional requirements
- User flows (one story per flow step if appropriate)

## Step 2: Write stories in standard format

**As a** [persona] **I want** [action] **so that** [benefit]

Each story must:

- Reference a specific persona (not "user")
- Describe desired behavior, not implementation
- State measurable benefit in "so that" clause

## Step 3: Apply INVEST criteria

| Criterion | Check |
|-----------|-------|
| Independent | Can be developed without other stories |
| Negotiable | Details open for discussion |
| Valuable | Delivers user or business value |
| Estimable | Team can estimate size |
| Small | Completable in one sprint |
| Testable | Acceptance criteria can be written |

Flag stories failing any criterion with fix recommendation.

## Step 4: Assign metadata

For each story:

- ID: US-001, US-002...
- Epic reference
- Priority: Must / Should / Could
- Size hint: S / M / L (not hours)
- Dependencies: other story IDs

## Step 5: Validate

Run Validation checklist.

---

# Decision Rules

| Condition | Action |
|-----------|--------|
| Story describes implementation | Rewrite as user behavior |
| Story too large (fails Small) | Split into multiple stories |
| Story has no persona | Use persona from input or request one |
| "So that" is vague | Rewrite with measurable outcome |
| Stories are not independent | Document dependency; consider merge or reorder |

---

# Validation

- [ ] All stories follow As/Want/So format
- [ ] INVEST check completed for each story
- [ ] Each story has unique ID and epic reference
- [ ] No implementation details in story text
- [ ] Dependencies explicitly documented
- [ ] Size hints provided (S/M/L)
- [ ] Stories failing INVEST have fix notes

---

# Anti-patterns

- **Technical stories as user stories** — "As a developer I want to set up Redis."
- **Epic-sized stories** — "As a user I want the entire dashboard."
- **No benefit clause** — missing or generic "so that I can use the app."
- **Generic persona** — "As a user" without specificity.
- **Untestable stories** — no observable behavior to verify.

---

# Best Practices

- One story = one testable behavior change.
- Split by workflow step, not by technical layer.
- Align stories with epic goal; reject orphan stories.
- Leave acceptance criteria to acceptance-criteria-generator.
- Group related stories under epic headers in output.

---

# Output Structure

```markdown
# User Stories: [Epic Name]

## Epic Reference
[Epic goal and ID]

## Stories

### US-001: [Short title]
**As a** [persona] **I want** [action] **so that** [benefit]

| Attribute | Value |
|-----------|-------|
| Priority | Must |
| Size | M |
| Dependencies | none |
| INVEST | Pass / Fail (note) |

[Repeat for each story]

## Dependency Map
US-001 → US-003

## Stories Needing Split
| Story | Issue | Suggested split |
|-------|-------|-----------------|
```

---

# Next Skills

| Outcome | Recommended Skill |
|---------|-------------------|
| Add acceptance criteria | `product/acceptance-criteria-generator` |
| Visualize story sequence | `product/story-mapping` |
| Need epics first | `product/epic-generator` |
| Sprint planning | `product/acceptance-criteria-generator` |

---
name: product-vision-builder
description: >
  Define a product vision that connects user problems, strategic direction, and measurable north star using the Product Vision Canvas. Use when working on product discovery, PRDs, user stories, OKRs, or backlog planning.
metadata:
  apes-version: "1.1"
  category: product
---

# Product Vision Builder

# Purpose

Define a product vision that connects user problems, strategic direction, and measurable north star using the Product Vision Canvas.

**Input:** Problem statement, persona (optional), business context (optional)  
**Output:** Product Vision document with vision statement, principles, and north star metric candidate

---

# Workflow

## Step 1: Synthesize inputs

Consolidate:

- Core problem being solved (from problem statement or user input)
- Primary persona and their success definition
- Business constraints (market, timeline, resources)
- Competitive landscape (if provided)

## Step 2: Draft vision statement

Format:

**For** [target user] **who** [need/problem], **[product name]** is a [category] **that** [key benefit]. **Unlike** [alternatives], **we** [differentiation].

Keep to 2–3 sentences maximum.

## Step 3: Define product principles

Establish 3–5 guiding principles:

- Decision-making rules for the team
- Trade-off preferences (speed vs quality, breadth vs depth)
- Non-negotiables (security, accessibility, etc.)

Each principle must be actionable, not aspirational slogans.

## Step 4: Identify north star metric

Select one metric that:

- Reflects core value delivered to users
- Is measurable and trackable
- Correlates with long-term business success

Document:

- North star metric definition
- Input metrics that drive it (3–5 leading indicators)
- Anti-metrics (what you will NOT optimize at expense of vision)

## Step 5: Define 3-year direction

Outline:

- Year 1: foundation (what must be true)
- Year 2: expansion (what grows)
- Year 3: maturity (what scales)

Keep realistic given stated constraints.

## Step 6: Validate

Run Validation checklist.

---

# Decision Rules

| Condition | Action |
|-----------|--------|
| No problem statement or equivalent | Stop; request problem context or run problem-statement-builder |
| Vision statement includes feature list | Reframe to outcome and differentiation, not features |
| Multiple north star metrics proposed | Force selection of one primary; others become input metrics |
| Principles are generic ("user first") | Rewrite as actionable decision rules |
| 3-year plan ignores stated constraints | Revise to match resources and timeline |

---

# Validation

- [ ] Vision statement follows For/Who/Is/That/Unlike/We format
- [ ] 3–5 actionable product principles defined
- [ ] Exactly one north star metric with definition
- [ ] 3–5 input metrics linked to north star
- [ ] Anti-metrics documented
- [ ] 3-year direction is realistic given constraints
- [ ] No feature laundry list in vision statement

---

# Anti-patterns

- **Feature vision** — listing capabilities instead of user outcome.
- **Multiple north stars** — diluting focus across competing metrics.
- **Slogan principles** — "innovate", "delight users" without decision guidance.
- **Ignoring constraints** — 3-year unicorn plan for a 2-person team.
- **Copying competitor vision** — differentiation says "like X but better" without substance.

---

# Best Practices

- Connect vision directly to validated problem statement.
- Make principles testable: "When X conflicts with Y, choose X."
- North star should be measurable within first 90 days (even if baseline is zero).
- Review vision against persona anti-goals.
- Keep vision stable; tactics change, vision should not shift weekly.

---

# Output Structure

```markdown
# Product Vision: [Product Name]

## Vision Statement
[For/Who/Is/That/Unlike/We paragraph]

## Product Principles
| # | Principle | Decision rule |
|---|-----------|---------------|

## North Star
- **Metric:** [name]
- **Definition:** [how measured]
- **Current baseline:** [if known]

## Input Metrics
| Metric | Drives north star by... |
|--------|-------------------------|

## Anti-metrics
- [What we won't optimize]

## 3-Year Direction
| Year | Focus | Key milestone |
|------|-------|---------------|

## Assumptions
- [ ] [Assumption]
```

---

# Next Skills

| Outcome | Recommended Skill |
|---------|-------------------|
| Need to prioritize features | `product/feature-prioritization` |
| Ready for detailed requirements | `product/prd-generator` |
| Need OKRs from vision | `product/feature-prioritization` |
| Vision needs user grounding | `product/persona-generator` |

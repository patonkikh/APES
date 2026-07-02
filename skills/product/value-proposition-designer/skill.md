---
name: value-proposition-designer
description: >
  Design a validated Value Proposition Canvas that maps customer jobs, pains, and gains to product pain relievers and gain creators, with an explicit fit assessment. Use when working on product discovery, PRDs, user stories, OKRs, or backlog planning.
metadata:
  apes-version: "1.1"
  category: product
---

# Value Proposition Designer

# Purpose

Design a validated Value Proposition Canvas that maps customer jobs, pains, and gains to product pain relievers and gain creators, with an explicit fit assessment.

**Input:** Persona, problem statement, product concept (optional), competitive context (optional)  
**Output:** Value Proposition Canvas document with fit score and prioritized value hypotheses

---

# Workflow

## Step 1: Define customer segment

Confirm:

- Primary persona or segment (one canvas per segment)
- Context of use (when/where the product is considered)
- Current alternatives (manual workarounds, competitors, status quo)

If segment is vague, stop and request persona detail or run persona-generator.

## Step 2: Build customer profile

Capture three blocks from the customer's perspective:

**Jobs** — functional, social, emotional tasks they try to accomplish:

| Type | Job | Importance (H/M/L) |
|------|-----|-------------------|

**Pains** — obstacles, risks, frustrations before/during/after jobs:

| Pain | Severity (H/M/L) | Frequency |
|------|------------------|-----------|

**Gains** — desired outcomes, benefits, aspirations:

| Gain | Relevance (H/M/L) | Expected vs unexpected |
|------|-------------------|------------------------|

Prioritize top 3 jobs, top 3 pains, top 3 gains.

## Step 3: Build value map

Map product offering to customer profile:

**Products & services** — what the offering includes (capabilities, not marketing copy).

**Pain relievers** — how each relieves specific pains:

| Pain relieved | How | Evidence |
|---------------|-----|----------|

**Gain creators** — how each creates specific gains:

| Gain created | How | Evidence |
|--------------|-----|----------|

Each pain reliever and gain creator must link to at least one customer profile item.

## Step 4: Assess fit

Evaluate **Problem-Solution Fit** and **Product-Market Fit signals**:

| Dimension | Score (1–5) | Rationale |
|-----------|-------------|-----------|
| Job relevance | | |
| Pain coverage | | |
| Gain delivery | | |
| Differentiation vs alternatives | | |

Flag gaps: pains without relievers, gains without creators, relievers without linked pains.

## Step 5: Prioritize value hypotheses

Rank top 3 value hypotheses to validate:

| Hypothesis | Customer belief | How to test | Success signal |
|------------|-------------------|-------------|----------------|

## Step 6: Validate

Run Validation checklist.

---

# Decision Rules

| Condition | Action |
|-----------|--------|
| No persona or segment defined | Stop; request persona or run persona-generator |
| Multiple segments in one canvas | Split into separate canvases per segment |
| Pain reliever not linked to a pain | Remove or map to specific pain |
| Gain creator describes feature, not outcome | Rewrite as customer benefit |
| All pains marked low severity | Re-interview segment or narrow scope |
| Value map mirrors competitor 1:1 | Articulate differentiation in gain creators |

---

# Validation

- [ ] One primary customer segment identified
- [ ] Customer profile has jobs, pains, gains with priorities
- [ ] Value map has products/services, pain relievers, gain creators
- [ ] Every reliever/creator links to a profile item
- [ ] Fit assessment completed with scores and gaps noted
- [ ] Top 3 value hypotheses with test methods defined
- [ ] Differentiation vs alternatives stated explicitly

---

# Anti-patterns

- **Feature list as value map** — listing capabilities without linking to pains/gains.
- **Generic pains** — "bad UX", "too expensive" without segment-specific context.
- **Orphan relievers** — pain relievers that don't address ranked pains.
- **One canvas for all segments** — enterprise and SMB mixed in one profile.
- **Assumed fit** — high fit scores without evidence or test plan.

---

# Best Practices

- Start from jobs, not features; jobs survive product pivots.
- Use customer language from interviews, not internal jargon.
- Rank pains by severity × frequency, not gut feel alone.
- Compare value map to top 2 alternatives explicitly.
- Treat canvas as living artifact; update after each discovery sprint.

---

# Output Structure

```markdown
# Value Proposition Canvas: [Segment] — [Product]

## Customer Profile
### Jobs (top 3)
| Job | Type | Importance |
|-----|------|------------|

### Pains (top 3)
| Pain | Severity | Frequency |
|------|----------|-----------|

### Gains (top 3)
| Gain | Relevance | Notes |
|------|-----------|-------|

## Value Map
| Pain | Reliever | How |
|------|----------|-----|

| Gain | Creator | How |
|------|---------|-----|

## Fit Assessment
| Dimension | Score | Gaps |
|-----------|-------|------|

**Overall fit:** [Problem-Solution / PMF signal stage]

## Value Hypotheses & Differentiation
| # | Hypothesis | Test | Success signal |
|---|------------|------|----------------|

[vs alternative 1, alternative 2]
```

---

# Next Skills

| Outcome | Recommended Skill |
|---------|-------------------|
| Fit validated, need vision | `product/product-vision-builder` |
| Prioritize features from value map | `product/feature-prioritization` |
| Test assumptions before build | `product/idea-validator` |
| Write requirements for MVP | `product/prd-generator` |
---
name: okr-builder
description: >
  Create aligned Objectives and Key Results (OKRs) for product teams with measurable key results and initiative mapping. Use when working on product discovery, PRDs, user stories, OKRs, or backlog planning.
metadata:
  apes-version: "1.1"
  category: product
---

# OKR Builder

# Purpose

Create aligned Objectives and Key Results (OKRs) for product teams with measurable key results and initiative mapping.

**Input:** Product vision, strategic priorities, time period (quarter), team scope  
**Output:** OKR document with 1–3 objectives, 2–4 KRs each, and linked initiatives

---

# Workflow

## Step 1: Define planning context

Confirm:

- Time period (e.g., Q3 2026)
- Team/product scope
- Strategic themes from vision or leadership
- Constraints (headcount, dependencies)

## Step 2: Draft objectives

Rules for objectives:

- Qualitative and inspirational
- Actionable by the team
- 1–3 objectives per team per period
- Aligned with product vision north star

Format: "Verb + ambitious outcome" (e.g., "Delight enterprise admins with effortless onboarding").

## Step 3: Define key results

Per objective, 2–4 KRs:

| KR | Metric | Baseline | Target | Measurement |
|----|--------|----------|--------|-------------|

KR rules:

- Measurable (number, percentage, binary)
- Outcome-based, not output-based ("launch feature" is not a KR)
- Ambitious but achievable (60-70% confidence)

## Step 4: Map initiatives

Link epics/features to KRs:

| Initiative | Supports KR | Status |
|------------|-------------|--------|

Initiatives are hypotheses for achieving KRs.

## Step 5: Check alignment

Verify:

- KRs ladder up to north star metric
- No conflicting KRs across objectives
- No more than 3 objectives (focus)

## Step 6: Validate

Run Validation checklist.

---

# Decision Rules

| Condition | Action |
|-----------|--------|
| KR is a task/output | Rewrite as measurable outcome |
| >4 KRs per objective | Reduce; focus on vital few |
| No baseline for KR | State "TBD — measure in week 1" explicitly |
| Objective not actionable by team | Reframe or escalate to leadership OKR |
| All KRs are vanity metrics | Replace with outcome metrics tied to user value |

---

# Validation

- [ ] 1–3 objectives defined
- [ ] 2–4 KRs per objective with baseline and target
- [ ] All KRs are measurable outcomes (not outputs)
- [ ] Initiatives mapped to KRs
- [ ] Alignment with north star noted
- [ ] Confidence level stated per KR (optional but recommended)
- [ ] No more than 3 objectives

---

# Anti-patterns

- **OKR as task list** — "Ship v2", "Hire 2 engineers" as KRs.
- **Too many objectives** — 5+ objectives diluting focus.
- **Sandbagging** — 100% confident easy KRs.
- **Unmeasurable KRs** — "Improve quality" without metric.
- **Orphan OKRs** — no connection to vision or initiatives.

---

# Best Practices

- Use OKR formula: "We will [objective] as measured by [KR1], [KR2]..."
- Review OKRs mid-quarter; don't change objectives lightly.
- Separate committed OKRs from aspirational stretch.
- Align with product/feature-prioritization for initiative selection.
- Grade KRs 0.0–1.0 at end of period; 0.7 is success.

---

# Output Structure

```markdown
# OKRs: [Team/Product] — [Period]

## Context
- **Vision alignment:** [north star connection]
- **Scope:** [team/product]

## Objective 1: [Statement]
| KR | Metric | Baseline | Target | Owner |
|----|--------|----------|--------|-------|

**Initiatives:**
- [Initiative] → KR 1.1

## Objective 2: [Statement]
[Same structure]

## Alignment Check
| North star | Supported by |
|------------|--------------|

## Scoring Guide
0.0 = no progress | 0.7 = success | 1.0 = exceeded
```

---

# Next Skills

| Outcome | Recommended Skill |
|---------|-------------------|
| Prioritize initiatives | `product/feature-prioritization` |
| Plan delivery | `product/sprint-planner` |
| Define vision | `product/product-vision-builder` |
| Write PRD for initiative | `product/prd-generator` |

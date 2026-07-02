---
name: persona-generator
description: >
  Create evidence-based user personas focused on behaviors, goals, and pain points — not demographics alone. Use when working on product discovery, PRDs, user stories, OKRs, or backlog planning.
metadata:
  apes-version: "1.1"
  category: product
---

# Persona Generator

# Purpose

Create evidence-based user personas focused on behaviors, goals, and pain points — not demographics alone.

**Input:** Target user segment, problem statement (optional), research data (optional)  
**Output:** Persona document with empathy map, behavioral traits, and scenario triggers

---

# Workflow

## Step 1: Define persona scope

Confirm:

- One persona per Skill execution (not persona sets)
- Primary vs secondary persona (if multiple requested, pick primary first)
- Segment boundaries (role, context, experience level)

## Step 2: Gather behavioral evidence

Collect or request:

- Observed behaviors (not just stated preferences)
- Goals and motivations
- Pain points and frustrations
- Tools and workflows currently used
- Decision-making triggers

## Step 3: Build empathy map

Fill four quadrants:

| Says | Thinks |
|------|--------|
| [Quotes or paraphrased statements] | [Unspoken concerns] |

| Does | Feels |
|------|-------|
| [Observed actions] | [Emotional states] |

## Step 4: Define persona profile

Include:

- Name (fictional label, not a real person claim)
- Role and context
- Goals (primary and secondary)
- Pain points (ranked by severity)
- Success definition (what "winning" looks like for them)
- Anti-goals (what they actively avoid)

## Step 5: Add scenario triggers

Describe 2–3 situations that activate the persona's need.

## Step 6: Validate

Run Validation checklist.

---

# Decision Rules

| Condition | Action |
|-----------|--------|
| Only demographics provided (age, gender) | Request behavioral and goal data |
| Persona based on assumptions only | Mark all traits as "assumed"; list validation needed |
| Multiple segments in one request | Ask user to pick primary segment |
| Contradictory behaviors in input | Surface contradiction; ask for clarification |
| Research data conflicts with stated segment | Flag conflict; prioritize research data |

---

# Validation

- [ ] Exactly one persona produced
- [ ] Empathy map has content in all four quadrants
- [ ] At least 3 pain points ranked by severity
- [ ] Goals are behavioral, not feature wishes
- [ ] Assumed traits clearly marked vs evidence-based
- [ ] 2–3 scenario triggers defined
- [ ] No stereotyping or unsupported demographic generalizations

---

# Anti-patterns

- **Demographic persona** — "35-year-old male, likes technology" without behaviors.
- **Ideal user fantasy** — persona with no pain points or trade-offs.
- **Feature wishlist persona** — goals listed as "wants feature X".
- **Multiple personas at once** — dilutes focus and validation.
- **Presenting assumptions as facts** — not marking unvalidated traits.

---

# Best Practices

- Base personas on observed behavior patterns, not market segments alone.
- Use empathy map before writing narrative profile.
- Include anti-goals to prevent scope creep in later Skills.
- Reference problem statement if available from prior Skill.
- Recommend 3–5 user interviews to validate assumed traits.

---

# Output Structure

```markdown
# Persona: [Name] — [Role]

## Profile
- **Segment:** [description]
- **Context:** [work/life situation]
- **Experience level:** [novice/intermediate/expert]

## Empathy Map
[Four quadrants table]

## Goals
| Priority | Goal |
|----------|------|

## Pain Points
| Severity | Pain Point | Evidence |
|----------|------------|----------|

## Success Definition
[What winning looks like]

## Anti-goals
- [What they avoid]

## Scenario Triggers
1. [Situation] → [need activated]

## Validation Status
| Trait | Status (evidence/assumed) |
|-------|---------------------------|
```

---

# Next Skills

| Outcome | Recommended Skill |
|---------|-------------------|
| Persona validated, need vision | `product/product-vision-builder` |
| Need to re-validate idea | `product/idea-validator` |
| Ready for problem refinement | `product/problem-statement-builder` |
| Ready for feature decisions | `product/feature-prioritization` |

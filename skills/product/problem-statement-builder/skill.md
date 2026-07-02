---
name: problem-statement-builder
description: >
  Transform a raw problem hypothesis into a structured, testable Problem Statement using Jobs-to-be-Done (JTBD) framing. Use when working on product discovery, PRDs, user stories, OKRs, or backlog planning.
metadata:
  apes-version: "1.1"
  category: product
---

# Problem Statement Builder

# Purpose

Transform a raw problem hypothesis into a structured, testable Problem Statement using Jobs-to-be-Done (JTBD) framing.

**Input:** Problem hypothesis, target user context, evidence (optional)  
**Output:** Problem Statement document with JTBD frame, success criteria, and scope boundaries
**Examples:** See [examples.md](examples.md) for worked input/output.

---

# Workflow

## Step 1: Extract problem signals

Gather:

- Who experiences the problem (user segment)
- When/where the problem occurs (context)
- Current workaround (how they cope today)
- Cost of the problem (time, money, risk, emotion)
- Evidence source (interviews, data, observation)

## Step 2: Apply JTBD framing

Structure the problem as:

**When** [situation] **I want to** [motivation] **so I can** [expected outcome]

Identify:

- Functional job (task to complete)
- Emotional job (how they want to feel)
- Social job (how they want to be perceived)

## Step 3: Define problem boundaries

Specify:

- In scope: what this problem statement covers
- Out of scope: adjacent problems explicitly excluded
- Root cause vs symptom: flag if current framing may be a symptom

## Step 4: Write success criteria

Define measurable indicators that the problem is solved:

- Leading indicators (behavior change)
- Lagging indicators (outcome metrics)
- Minimum viable improvement (what "good enough" looks like)

## Step 5: Validate

Run Validation checklist.

---

# Decision Rules

| Condition | Action |
|-----------|--------|
| Problem describes a solution, not a need | Reframe from solution to underlying job |
| Multiple unrelated problems in input | Split into separate problem statements; complete one |
| No target user specified | Stop; request user segment |
| Problem is a symptom | Add "Root Cause Hypothesis" section; flag for discovery |
| Success criteria are not measurable | Rewrite with specific metrics or observable behaviors |

---

# Validation

- [ ] JTBD sentence follows When/Want/So format
- [ ] Functional, emotional, and social jobs identified
- [ ] In-scope and out-of-scope boundaries defined
- [ ] At least 2 measurable success criteria
- [ ] Current workaround documented
- [ ] Cost of problem articulated
- [ ] No solution embedded in problem statement

---

# Anti-patterns

- **Solution disguised as problem** — "Users need an AI dashboard" instead of the underlying job.
- **Vague pain** — "Users are frustrated" without specific context or cost.
- **Everyone's problem** — no specific segment or situation.
- **Unmeasurable success** — "better experience" without criteria.
- **Ignoring workarounds** — not documenting how users cope today.

---

# Best Practices

- Quote user language when evidence is available.
- Quantify cost of problem where possible (hours/week, error rate, churn).
- Separate problem statement from proposed solution entirely.
- Link to Idea Validation Report if available from prior Skill.
- Flag assumptions that need user research validation.

---

# Output Structure

```markdown
# Problem Statement: [Short Title]

## JTBD Frame
**When** ... **I want to** ... **so I can** ...

## Job Types
| Type | Job |
|------|-----|
| Functional | |
| Emotional | |
| Social | |

## Problem Details
- **Who:** [segment]
- **Context:** [when/where]
- **Current workaround:** [how they cope]
- **Cost of problem:** [quantified if possible]

## Scope
- **In scope:**
- **Out of scope:**

## Success Criteria
| Criterion | Type | Target |
|-----------|------|--------|

## Root Cause Hypothesis
[If symptom detected]

## Assumptions
- [ ] [Assumption needing validation]

## Evidence
| Source | Finding |
|--------|---------|
```

---

# Next Skills

| Outcome | Recommended Skill |
|---------|-------------------|
| Need user segment detail | `product/persona-generator` |
| Problem validated, ready for vision | `product/product-vision-builder` |
| Multiple solutions to compare | `product/feature-prioritization` |
| Ready for requirements | `product/prd-generator` |

---
name: product-discovery-assistant
description: >
  Facilitate structured product discovery using Opportunity Solution Tree (OST) and Teresa Torres framework: map outcomes, opportunities, solutions, and experiments. Use when working on product discovery, PRDs, user stories, OKRs, or backlog planning.
metadata:
  apes-version: "1.1"
  category: product
---

# Product Discovery Assistant

# Purpose

Facilitate structured product discovery using Opportunity Solution Tree (OST) and Teresa Torres framework: map outcomes, opportunities, solutions, and experiments.

**Input:** Product outcome goal, existing research (optional), team constraints  
**Output:** Discovery board with opportunity tree, prioritized opportunities, and experiment backlog
**Examples:** See [examples.md](examples.md) for worked input/output.

---

# Workflow

## Step 1: Define desired outcome

Specify:

- Business/product outcome (measurable)
- Time horizon
- Success metric from product vision or OKRs

Format: "Increase [metric] from [baseline] to [target] by [date]."

## Step 2: Map opportunities

Brainstorm and structure opportunities (customer problems/needs):

| ID | Opportunity | Evidence | Impact estimate |
|----|-------------|----------|-----------------|

Opportunities are problems, not solutions.

## Step 3: Prioritize opportunities

Score using impact × evidence confidence:

| Opportunity | Impact (1-5) | Evidence (1-5) | Score |
|-------------|--------------|----------------|-------|

Select top 3 for solution exploration.

## Step 4: Generate solution options

For each top opportunity, list 2–3 solution ideas:

| Opportunity | Solution | Assumption | Cheapest test |
|-------------|----------|------------|---------------|

Solutions are hypotheses, not commitments.

## Step 5: Design discovery experiments

| Experiment | Tests | Method | Timeline | Success criteria |
|------------|-------|--------|----------|------------------|

Prefer interviews, prototypes, concierge tests over builds.

## Step 6: Validate

Run Validation checklist.

---

# Decision Rules

| Condition | Action |
|-----------|--------|
| Outcome not measurable | Stop; define metric or run product-vision-builder |
| Opportunities are solutions | Reframe as underlying customer problems |
| No evidence for any opportunity | Mark all as assumptions; prioritize cheapest tests |
| >10 opportunities | Cluster into themes; prioritize within themes |
| Experiment requires >2 weeks | Propose smaller test first |

---

# Validation

- [ ] Outcome stated with metric, baseline, target
- [ ] ≥5 opportunities listed as problems (not solutions)
- [ ] Top 3 opportunities prioritized with rationale
- [ ] ≥2 solutions per top opportunity
- [ ] ≥3 experiments with success criteria
- [ ] Experiments are cheaper than building full solutions
- [ ] No committed roadmap — discovery artifacts only

---

# Anti-patterns

- **Solution-first discovery** — jumping to features before understanding opportunities.
- **Fake evidence** — marking assumptions as validated without data.
- **Analysis paralysis** — endless research without experiments.
- **Outcome = output** — "ship feature X" instead of business outcome.
- **Skipping assumption mapping** — experiments that don't test specific assumptions.

---

# Best Practices

- Use Teresa Torres' Opportunity Solution Tree structure.
- One outcome per discovery cycle.
- Interview 5–8 customers per opportunity cluster.
- Time-box discovery sprints (2 weeks).
- Link to idea-validator for assumption testing.

---

# Output Structure

```markdown
# Product Discovery: [Outcome Name]

## Desired Outcome
[Metric, baseline, target, horizon]

## Opportunity Tree
| ID | Opportunity | Evidence | Impact |
|----|-------------|----------|--------|

## Top Opportunities (prioritized)
1. [Opportunity] — score: X

## Solution Options
| Opportunity | Solution | Assumption to test |
|-------------|----------|-------------------|

## Experiment Backlog
| # | Experiment | Tests assumption | Method | Timeline | Success |
|---|------------|------------------|--------|----------|---------|

## Next Review
[Date and criteria to continue/stop discovery]
```

---

# Next Skills

| Outcome | Recommended Skill |
|---------|-------------------|
| Validate specific idea | `product/idea-validator` |
| Define problem statement | `product/problem-statement-builder` |
| Set team goals | `product/okr-builder` |
| Prioritize solutions | `product/feature-prioritization` |

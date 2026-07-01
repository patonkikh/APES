# Feature Prioritization

# Purpose

Prioritize a feature backlog using a structured scoring framework (RICE by default) and produce a ranked list with rationale.

**Input:** Feature list, product vision or goals (optional), constraints (timeline, team size)  
**Output:** Prioritized feature ranking with scores, trade-off notes, and recommended MVP cut line

---

# Workflow

## Step 1: Normalize feature list

For each feature, extract:

- Name and one-sentence description
- User/problem it addresses
- Dependencies on other features
- Estimated effort category (S/M/L/XL if no estimates provided)

If features are vague, ask for clarification before scoring.

## Step 2: Select scoring framework

Default: **RICE** (Reach, Impact, Confidence, Effort)

| Framework | Use when |
|-----------|----------|
| RICE | Quantitative prioritization with multiple features |
| ICE | Quick prioritization, early stage, less data |
| MoSCoW | Release planning with fixed deadline |

State which framework is used and why.

## Step 3: Score each feature

For RICE:

| Factor | Scale | Guidance |
|--------|-------|----------|
| Reach | # users per quarter | Estimate from persona/segment |
| Impact | 0.25–3 | Massive=3, High=2, Medium=1, Low=0.5, Minimal=0.25 |
| Confidence | 0–100% | Evidence quality |
| Effort | person-months | Team effort estimate |

**RICE Score = (Reach × Impact × Confidence) / Effort**

## Step 4: Rank and draw MVP line

- Sort by RICE score descending
- Draw MVP cut line based on stated constraints
- Document features below the line and why deferred

## Step 5: Document trade-offs

For top 5 features, note:

- What is sacrificed by prioritizing this
- Dependencies and sequencing requirements
- Risks of deprioritizing alternatives

## Step 6: Validate

Run Validation checklist.

---

# Decision Rules

| Condition | Action |
|-----------|--------|
| Feature list empty | Stop; request features or reference PRD |
| No reach data available | Use relative reach estimates; mark Confidence lower |
| Effort unknown for all features | Use t-shirt sizes converted to person-months; flag estimates |
| Two features are mutually exclusive | Score separately; add decision note to pick one |
| Constraint is fixed date | Use MoSCoW instead of RICE; mark Must/Should/Could/Won't |

---

# Validation

- [ ] Scoring framework explicitly stated
- [ ] Every feature has all scoring dimensions filled
- [ ] RICE/ICE scores calculated correctly
- [ ] Ranked list matches calculated scores
- [ ] MVP cut line drawn with rationale
- [ ] Top 5 trade-offs documented
- [ ] Dependencies noted between features
- [ ] No features scored without rationale

---

# Anti-patterns

- **HiPPO prioritization** — ranking by stakeholder loudest voice without scores.
- **Everything is Must** — MoSCoW with no Could/Won't items.
- **Fake precision** — confidence 100% without evidence.
- **Ignoring dependencies** — ranking independent of sequencing constraints.
- **Effort-free ranking** — high impact features that take a year ranked first.

---

# Best Practices

- Align Impact scores with north star metric from product vision.
- Lower Confidence when based on assumptions; note what would raise it.
- Include tech debt and infrastructure items in the same framework.
- Re-score after major new evidence (user research, prototype results).
- Document what was explicitly deprioritized and why.

---

# Output Structure

```markdown
# Feature Prioritization: [Product Name]

## Framework
**Method:** RICE | ICE | MoSCoW
**Rationale:** [why this framework]

## Constraints
- Timeline: [if stated]
- Team: [if stated]

## Scored Features
| Rank | Feature | Reach | Impact | Confidence | Effort | Score | Rationale |
|------|---------|-------|--------|------------|--------|-------|-----------|

## MVP Cut Line
**Included in MVP:** features #1–#N
**Rationale:** [why this cut]

## Deferred Features
| Feature | Reason deferred |
|---------|-----------------|

## Trade-offs (Top 5)
| Feature | Gain | Sacrifice |
|---------|------|-----------|

## Dependencies
[Feature A] → requires → [Feature B]
```

---

# Next Skills

| Outcome | Recommended Skill |
|---------|-------------------|
| MVP scope defined | `product/prd-generator` |
| Need epic breakdown | `product/epic-generator` |
| Need user stories | `product/user-story-generator` |
| Vision unclear | `product/product-vision-builder` |

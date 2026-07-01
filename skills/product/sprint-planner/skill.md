# Sprint Planner

# Purpose

Plan a development sprint: select stories, define sprint goal, estimate capacity, and produce a sprint backlog with risk buffer.

**Input:** Prioritized backlog (user stories/epics), team capacity, sprint duration, OKRs (optional)  
**Output:** Sprint plan with goal, committed backlog, capacity allocation, and risks

---

# Workflow

## Step 1: Define sprint parameters

Confirm:

- Sprint duration (1–4 weeks)
- Team members and availability (vacations, meetings)
- Sprint goal candidate (from OKR or epic)

## Step 2: Calculate capacity

| Team member | Available days | Focus factor | Effective days |
|-------------|----------------|--------------|----------------|

Focus factor: 0.6–0.8 (accounts for meetings, support).

Convert to story points or hours based on team convention.

## Step 3: Select backlog items

From prioritized backlog:

- Select stories aligned with sprint goal
- Check INVEST and acceptance criteria completeness
- Identify dependencies between stories

| Story ID | Title | Size | Priority | Dependencies |
|----------|-------|------|----------|--------------|

## Step 4: Apply capacity guardrails

- Commit to 70–80% of capacity (buffer for unknowns)
- Flag if committed > capacity
- Identify stretch goals (below the commitment line)

## Step 5: Define sprint goal

One sentence:

"This sprint we will [outcome] so that [benefit]."

Must be achievable with committed backlog.

## Step 6: Document risks

| Risk | Impact | Mitigation |
|------|--------|------------|

## Step 7: Validate

Run Validation checklist.

---

# Decision Rules

| Condition | Action |
|-----------|--------|
| No sized stories | Use T-shirt sizes; flag sizing session needed |
| Committed > capacity | Move lowest priority stories to stretch or next sprint |
| Stories lack acceptance criteria | Flag; run acceptance-criteria-generator before commit |
| No sprint goal | Derive from highest priority epic or OKR |
| Critical dependency unresolved | Do not commit dependent story |

---

# Validation

- [ ] Sprint duration and capacity calculated
- [ ] Sprint goal stated in outcome format
- [ ] Committed backlog ≤ 80% capacity
- [ ] All committed stories have size estimates
- [ ] Dependencies documented
- [ ] Stretch goals separated from commitment
- [ ] ≥2 sprint risks with mitigations
- [ ] Alignment with OKR/epic noted if applicable

---

# Anti-patterns

- **100% capacity** — no buffer for interrupts.
- **Sprint goal = story list** — "complete US-1, US-2" instead of outcome.
- **Unsized commitment** — pulling stories without estimates.
- **Scope creep mid-planning** — adding stories after capacity full.
- **Ignoring dependencies** — committing to blocked stories.

---

# Best Practices

- Sprint goal should be demo-able at review.
- Include refinement time in capacity calculation.
- Prefer completing fewer stories over starting many.
- Align selection with OKR key results.
- Use velocity from last 3 sprints if available.

---

# Output Structure

```markdown
# Sprint Plan: Sprint [N] — [Dates]

## Sprint Goal
[One sentence outcome]

## Capacity
| Member | Days | Focus | Effective | Points |
|--------|------|-------|-----------|--------|
| **Total** | | | | X |
| **Commit limit (80%)** | | | | Y |

## Committed Backlog
| ID | Story | Size | KR/Epic ref |
|----|-------|------|-------------|

## Stretch Goals
| ID | Story | Size |
|----|-------|------|

## Dependencies
[Story A] blocks [Story B]

## Risks
| Risk | Mitigation |
|------|------------|

## Definition of Done
- [ ] [Team DoD items]
```

---

# Next Skills

| Outcome | Recommended Skill |
|---------|-------------------|
| Missing acceptance criteria | `product/acceptance-criteria-generator` |
| Need more stories | `product/user-story-generator` |
| Re-prioritize backlog | `product/feature-prioritization` |
| Quarterly planning | `product/okr-builder` |

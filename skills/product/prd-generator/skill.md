# PRD Generator

# Purpose

Produce a Product Requirements Document (PRD) for a defined feature or MVP scope with goals, requirements, and success metrics.

**Input:** Feature scope, product vision (optional), prioritization results (optional), constraints  
**Output:** PRD document following standard structure with functional and non-functional requirements

---

# Workflow

## Step 1: Define scope

Confirm:

- Feature or MVP boundary (what is in/out)
- Target persona and problem statement
- Success metrics (from vision or define new)
- Constraints (timeline, platform, compliance)

## Step 2: Write executive summary

One paragraph covering: what, for whom, why now, expected outcome.

## Step 3: Document requirements

**Functional requirements:**

- Numbered list (FR-001, FR-002...)
- Each requirement: actor, action, outcome
- Priority: Must / Should / Could

**Non-functional requirements:**

- Performance, security, scalability, accessibility
- Numbered (NFR-001...)

## Step 4: Define user flows

Describe 2–3 primary flows:

- Happy path
- Key edge case
- Error/recovery path

Use step-by-step format, not wireframes.

## Step 5: Specify success metrics

| Metric | Baseline | Target | Measurement method |
|--------|----------|--------|-------------------|

## Step 6: List dependencies and risks

- Technical dependencies
- External integrations
- Open questions

## Step 7: Validate

Run Validation checklist.

---

# Decision Rules

| Condition | Action |
|-----------|--------|
| Scope undefined or "everything" | Stop; request MVP boundary or run feature-prioritization |
| Requirement describes implementation | Rewrite as user-facing behavior |
| No success metrics | Define at least 2 from vision or problem statement |
| Conflicting requirements | Flag conflict; ask user to resolve |
| NFRs missing for user-facing product | Add security, performance, accessibility minimums |

---

# Validation

- [ ] Executive summary ≤ 1 paragraph
- [ ] Scope in/out explicitly stated
- [ ] ≥3 functional requirements with IDs and priorities
- [ ] ≥2 non-functional requirements
- [ ] ≥2 primary user flows documented
- [ ] Success metrics have baseline, target, measurement
- [ ] Dependencies and risks listed
- [ ] No implementation details (tech stack, API design) unless requested

---

# Anti-patterns

- **PRD as spec** — database schemas and API endpoints in a product PRD.
- **No priorities** — all requirements marked Must.
- **Orphan requirements** — FRs not traceable to user problem.
- **Missing NFRs** — only functional requirements listed.
- **Unbounded scope** — "and other features as needed."

---

# Best Practices

- Trace each FR to a user problem or goal.
- Use INVEST criteria when writing requirements (preview for user-story-generator).
- Keep PRD at "what" level; defer "how" to technical design.
- Include explicit out-of-scope section.
- Version the PRD with date and change summary.

---

# Output Structure

```markdown
# PRD: [Feature/MVP Name]
**Version:** 1.0 | **Date:** [date]

## Executive Summary
[One paragraph]

## Scope
- **In scope:**
- **Out of scope:**

## Target User
[Persona reference or summary]

## Functional Requirements
| ID | Requirement | Priority | Rationale |
|----|-------------|----------|-----------|

## Non-Functional Requirements
| ID | Requirement | Priority |
|----|-------------|----------|

## User Flows
### Flow 1: [Name]
1. [Step]

## Success Metrics
| Metric | Baseline | Target | Method |
|--------|----------|--------|--------|

## Dependencies
- [Dependency]

## Risks & Open Questions
| Item | Impact | Owner |
|------|--------|-------|

## Revision History
| Version | Date | Changes |
|---------|------|---------|
```

---

# Next Skills

| Outcome | Recommended Skill |
|---------|-------------------|
| Break PRD into epics | `product/epic-generator` |
| Write user stories | `product/user-story-generator` |
| Need acceptance criteria | `product/acceptance-criteria-generator` |
| Visualize user journey | `product/story-mapping` |

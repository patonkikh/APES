# Architecture Review

# Purpose

Conduct a structured architecture review against requirements, quality attributes, and best practices; produce findings with severity and remediation recommendations.

**Input:** Solution architecture, context/container diagrams, ADRs (optional), PRD/NFRs  
**Output:** Architecture Review Report with findings, risk rating, and action items

---

# Workflow

## Step 1: Establish review scope

Confirm artifacts under review:

- Solution architecture document
- C4 context and container diagrams
- ADRs
- PRD/NFRs as acceptance baseline

Define review focus: security, scalability, maintainability, cost, or full review.

## Step 2: Check requirements traceability

| FR/NFR ID | Addressed by | Status | Gap |
|-----------|--------------|--------|-----|

Flag unaddressed Must-have requirements.

## Step 3: Evaluate quality attributes

Score each attribute (1–5) with evidence:

| Attribute | Score | Evidence | Risk |
|-----------|-------|----------|------|

Attributes: security, scalability, availability, maintainability, operability, cost efficiency.

## Step 4: Apply review checklist

Categories:

- **Security:** auth, data protection, trust boundaries, secrets management
- **Resilience:** failure modes, retries, circuit breakers, backup/recovery
- **Scalability:** bottlenecks, stateless design, data partitioning
- **Maintainability:** coupling, complexity, technology diversity
- **Operability:** monitoring, logging, deployment, rollback

## Step 5: Document findings

For each finding:

| ID | Severity | Category | Finding | Recommendation | Owner |
|----|----------|----------|---------|----------------|-------|

Severity: Critical | High | Medium | Low | Info

## Step 6: Summarize and recommend

- Overall risk rating: Green | Amber | Red
- Go/no-go for implementation
- Required actions before proceed

## Step 7: Validate

Run Validation checklist.

---

# Decision Rules

| Condition | Action |
|-----------|--------|
| No architecture artifacts | Stop; request solution-architecture output |
| Critical security finding | Overall rating Red; block proceed until resolved |
| NFR not addressable by current design | Flag as gap; recommend architecture revision |
| Finding without recommendation | Rewrite with specific remediation action |
| ADR contradicts implementation | Flag ADR compliance issue |

---

# Validation

- [ ] Review scope and artifacts listed
- [ ] FR/NFR traceability matrix completed
- [ ] All 6 quality attributes scored with evidence
- [ ] ≥5 findings documented with severity
- [ ] Every Critical/High finding has recommendation
- [ ] Overall risk rating stated with rationale
- [ ] Go/no-go recommendation explicit

---

# Anti-patterns

- **Rubber stamp** — all greens without evidence.
- **Style review** — commenting on naming instead of architectural risks.
- **No prioritization** — 50 Medium findings without severity ranking.
- **Missing NFR check** — reviewing diagrams only, not requirements.
- **Vague recommendations** — "improve security" without specific action.

---

# Best Practices

- Use ATAM-inspired quality attribute review.
- Reference specific diagram elements in findings.
- Link findings to ADRs when decision is needed.
- Separate must-fix before launch vs post-launch improvements.
- Include positive observations (architecture strengths).

---

# Output Structure

```markdown
# Architecture Review: [System Name]
**Date:** YYYY-MM-DD
**Reviewer:** [role]
**Scope:** [focus areas]

## Artifacts Reviewed
- [ ] Solution architecture
- [ ] System context
- [ ] Container diagram
- [ ] ADRs
- [ ] PRD/NFRs

## Requirements Traceability
| ID | Addressed | Gap |
|----|-----------|-----|

## Quality Attribute Scores
| Attribute | Score | Evidence |
|-----------|-------|----------|

## Findings
| ID | Severity | Category | Finding | Recommendation |
|----|----------|----------|---------|----------------|

## Strengths
- [Positive observation]

## Summary
**Overall risk:** Green | Amber | Red
**Recommendation:** Proceed | Proceed with conditions | Do not proceed

## Required Actions
| Priority | Action | Owner | Deadline |
|----------|--------|-------|----------|
```

---

# Next Skills

| Outcome | Recommended Skill |
|---------|-------------------|
| Fix architecture gaps | `architecture/solution-architecture` |
| Document new decisions | `architecture/adr-generator` |
| Update diagrams | `architecture/container-diagram-builder` |
| Design APIs | `architecture/api-designer` |
| Return to product scope | `product/prd-generator` |

# PRD Generator — Worked Examples

Reference outputs for calibrating quality. Abbreviated for length; full sections follow the Output Structure in `skill.md`.

---

## Example 1: MVP feature PRD

### Input

```text
Feature: Team retrospective auto-generator for Jira
Persona: Engineering managers at mid-size B2B SaaS (50–200 engineers)
Problem: Manual retros take 2+ hours; action items get lost
Scope: MVP — import Jira sprint data, generate retro summary, export to Confluence
Constraints: 8-week timeline, must integrate with Jira Cloud OAuth
Priority: Must-have — sprint summary, action items; Should-have — sentiment tags
```

### Output (excerpt)

```markdown
# PRD: Sprint Retrospective Auto-Generator (MVP)
**Version:** 1.0 | **Date:** 2026-07-01

## Executive Summary
Engineering managers at mid-size B2B companies spend 2+ hours per sprint writing
retrospectives from Jira data. This MVP imports sprint metrics and issues,
generates a structured retro summary with action items, and exports to Confluence —
reducing prep time to under 15 minutes.

## Scope
- **In scope:** Jira Cloud OAuth, sprint/issue import, AI summary, Confluence export
- **Out of scope:** Slack delivery, custom templates, on-prem Jira, multi-board aggregation

## Functional Requirements
| ID | Requirement | Priority | Rationale |
|----|-------------|----------|-----------|
| FR-001 | Manager connects Jira Cloud via OAuth | Must | Data source |
| FR-002 | User selects sprint and board | Must | Scope selection |
| FR-003 | System generates retro summary from sprint data | Must | Core value |
| FR-004 | User edits summary before export | Must | Trust and accuracy |
| FR-005 | User exports to Confluence page | Must | Delivery channel |
| FR-006 | System suggests action items from blockers | Should | Differentiation |

## Non-Functional Requirements
| ID | Requirement | Priority |
|----|-------------|----------|
| NFR-001 | Summary generation completes in <60s for 500 issues | Must |
| NFR-002 | OAuth tokens encrypted at rest | Must |
| NFR-003 | WCAG 2.1 AA for web UI | Should |

## Success Metrics
| Metric | Baseline | Target | Method |
|--------|----------|--------|--------|
| Retro prep time | 120 min | 15 min | User survey (n=20) |
| Action item capture rate | 40% | 80% | Compare Jira tasks created post-retro |

## Risks & Open Questions
| Item | Impact | Owner |
|------|--------|-------|
| Jira API rate limits on large boards | High | Engineering |
| Confluence space permissions model | Medium | Product |
```

---

## Example 2: Stop condition — scope undefined

### Input

```text
Build an AI product for teams. Include everything needed for success.
```

### Expected behavior

Do **not** produce a PRD. Apply Decision Rule: scope undefined → stop and request MVP boundary or run `feature-prioritization`.

```markdown
## Blocked — Missing scope

Cannot produce a PRD without a defined feature boundary.

**Missing:**
- Specific feature or MVP scope (what is in/out)
- Target persona
- At least one measurable success metric

**Recommended next step:** Run `product/feature-prioritization` or provide:
1. One-sentence feature description
2. Primary user segment
3. MVP must-have list (max 5 items)
```

---

## Example 3: Requirement rewrite

### Input (user draft)

```text
FR: Use PostgreSQL with Prisma ORM and deploy on AWS ECS.
```

### Corrected output

Rewrite as user-facing behavior per Decision Rules:

| Original | Rewritten FR |
|----------|--------------|
| Use PostgreSQL with Prisma | FR-007: System persists user retro drafts and restores them across sessions (Must) |

Note in PRD: *Technical implementation deferred to solution-architecture.*

# Sprint Planner — Worked Examples

---

## Example 1: Two-week sprint plan

### Input

```text
Team: 4 devs, 1 on vacation week 2 (50% capacity)
Velocity: ~24 pts last 3 sprints
Backlog: US-001..US-008 sized, Epic 2 focus
OKR: WAMCR activation
```

### Output (excerpt)

```markdown
# Sprint Plan: Sprint 12 — Jul 7–18

## Sprint Goal
Enable managers to generate and edit first AI retro draft from Jira sprint data.

## Capacity
| Member | Effective pts |
|--------|---------------|
| Dev A–D (adjusted) | 20 |
| **Commit limit (80%)** | **16** |

## Committed Backlog
| ID | Story | Size |
|----|-------|------|
| US-003 | Import sprint issues | 5 |
| US-004 | Generate AI draft | 8 |
| US-005 | Edit draft UI | 3 |

**Total: 16 pts**

## Stretch
| US-006 | Export preview | 3 |

## Risks
| Risk | Mitigation |
|------|------------|
| Jira API rate limits | Spike day 1 |
```

---

## Example 2: 100% capacity commit

### Expected behavior

Move stories to stretch; enforce 70–80% commit limit.

---

## Example 3: Stories without AC

### Expected behavior

Flag US-*; recommend `acceptance-criteria-generator` before commit.

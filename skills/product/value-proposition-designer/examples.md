# Value Proposition Designer — Worked Examples

---

## Example 1: Value Proposition Canvas

### Input

```text
Segment: EM at mid-size B2B SaaS
Top pains: 2h retro prep, lost action items
Product: Jira-connected AI retro drafts with Confluence export
```

### Output (excerpt)

```markdown
# Value Proposition Canvas: EM Segment

## Customer Profile
### Top Pains
| Pain | Severity |
|------|----------|
| Manual Jira synthesis | High |
| Action items not in Jira | High |

### Top Gains
| Gain | Relevance |
|------|-----------|
| Credible retro in <15 min | High |
| Team trusts outcomes | Medium |

## Value Map
| Pain | Pain Reliever |
|------|---------------|
| Manual synthesis | Auto-import + AI draft |
| Lost actions | Export with Jira task links |

## Fit Assessment
| Dimension | Score |
|-----------|-------|
| Pain coverage | 4/5 |
| **Overall** | Problem-Solution Fit signal |

## Value Hypothesis
H1: EMs will export ≥1 retro/week if prep <15 min — test with 10-user pilot
```

---

## Example 2: Feature list value map

### Expected behavior

Link every feature to a ranked pain or gain; remove orphans.

---

## Example 3: No segment

### Expected behavior

Stop; run `persona-generator` first.

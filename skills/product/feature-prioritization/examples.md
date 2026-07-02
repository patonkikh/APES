# Feature Prioritization — Worked Examples

---

## Example 1: RICE scoring for MVP cut

### Input

```text
Features for retro generator MVP:
1. Jira OAuth connect
2. Sprint data import
3. AI retro summary
4. Confluence export
5. Slack notification
6. Custom retro templates
7. Multi-board aggregation
Constraints: 8-week MVP, team of 4
```

### Output (excerpt)

```markdown
# Feature Prioritization: Retro Generator

## Scoring (RICE)
| Feature | Reach | Impact | Confidence | Effort | Score | Priority |
|---------|-------|--------|------------|--------|-------|----------|
| Jira OAuth | 100% users | 3 | 0.9 | 2 | 135 | P0 |
| Sprint import | 100% | 3 | 0.9 | 3 | 90 | P0 |
| AI summary | 100% | 3 | 0.7 | 5 | 42 | P0 |
| Confluence export | 80% | 2 | 0.8 | 3 | 43 | P1 |
| Slack notification | 60% | 1 | 0.6 | 2 | 18 | P2 |
| Custom templates | 40% | 2 | 0.5 | 4 | 10 | P3 |
| Multi-board | 30% | 2 | 0.4 | 6 | 4 | P3 |

## MVP Cut Line
**In MVP:** OAuth, import, AI summary, Confluence export
**Post-MVP:** Slack, templates, multi-board

## Trade-off Notes
- AI summary confidence is 0.7 — spike in week 1 before committing
- Multi-board deferred: complexity vs 30% reach
```

---

## Example 2: All Must-have — anti-pattern fix

### Input

```text
All 12 features are Must-have for launch.
```

### Expected behavior

```markdown
## Issue: no prioritization possible

Decision rule: all Must → force relative ranking using RICE anyway.

Present forced stack rank and ask user to confirm MVP cut at score drop-off
(typically after top 4–6 items).
```

---

## Example 3: Missing reach data

### Input

```text
Feature: Advanced analytics dashboard — no user data
```

### Expected behavior

Mark Confidence = 0.3, document assumption: "Reach estimated from persona size TBD."
Recommend discovery interview before committing to MVP.

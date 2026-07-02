# Product Vision Builder — Worked Examples

---

## Example 1: Vision for retro product

### Input

```text
Problem: EM retro prep takes 2+ hours
Persona: Jordan, EM at mid-size B2B SaaS
Market: Engineering productivity tools
Horizon: 3 years
```

### Output (excerpt)

```markdown
# Product Vision: RetroFlow

## Vision Statement
**For** engineering managers at growing software companies
**who** lose hours preparing retrospectives and tracking follow-through,
**RetroFlow** is a retrospective intelligence platform
**that** turns sprint data into actionable team insights in minutes.
**Unlike** generic meeting AI or static Jira reports,
**we** integrate deeply with engineering workflows and preserve manager judgment.

## North Star Direction
Weekly active managers completing a retro with ≥1 exported action item

## Strategic Pillars (3-year)
1. **Workflow-native** — Jira, Confluence, Slack as first-class citizens
2. **Trustworthy AI** — human-in-the-loop by design
3. **Team learning loop** — retros improve over time via outcome tracking

## Non-Goals
- Replace Jira as system of record
- HR performance management / individual ratings
```

---

## Example 2: Feature list as vision — rewrite

### Input

```text
Vision: OAuth, AI, export, Slack, mobile app, analytics
```

### Expected behavior

Reframe as outcome-oriented vision; move features to roadmap themes, not vision statement.

---

## Example 3: No persona — stop

### Expected behavior

Run `product/persona-generator` or request persona before vision draft.

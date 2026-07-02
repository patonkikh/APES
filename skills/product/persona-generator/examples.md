# Persona Generator — Worked Examples

---

## Example 1: Engineering manager persona

### Input

```text
Product: Sprint retro auto-generator from Jira
Segment hint: Engineering managers at mid-size B2B SaaS
Problem: Manual retros take too long
```

### Output (excerpt)

```markdown
# Persona: Jordan — Engineering Manager

## Demographics & Context
- **Role:** Engineering Manager, 8 direct reports
- **Company:** B2B SaaS, ~120 engineers, Series B
- **Experience:** 3 years as EM, former senior developer

## Goals
- Run effective retros without burning Sunday evening on prep
- Surface actionable improvements for the team
- Demonstrate delivery health to leadership

## Frustrations
- Copy-pasting Jira data into slides manually
- Action items lost between retro and next sprint
- Generic retro formats that don't reflect team reality

## Behaviors
- Lives in Jira + Confluence daily
- Runs bi-weekly retros, monthly with leadership
- Skeptical of AI drafts without edit control

## Quote
> "I don't need another dashboard — I need the retro done before Monday standup."

## Implications for Product
- Must support edit-before-export
- Jira/Confluence integration is table stakes
- Time-to-first-value <15 minutes
```

---

## Example 2: Multiple personas — split

### Input

```text
One persona for developers and executives combined
```

### Expected behavior

Split into separate personas or ask user to pick primary segment for this exercise.

---

## Example 3: Generic persona anti-pattern

### Bad

"User wants productivity and efficiency."

### Correct

Specific role, context, behaviors, and a concrete quote tied to the problem domain.

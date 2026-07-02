# Idea Validator — Worked Examples

---

## Example 1: B2B SaaS idea — Pivot recommendation

### Input

```text
Idea: AI auto-generates sprint retrospectives from Jira for engineering managers
Audience: Mid-size B2B SaaS, 50–200 engineers
Problem: Retros take 2+ hours and action items get lost
Business model: $29/user/month SaaS
Evidence: 3 informal conversations with EM friends
```

### Output (excerpt)

```markdown
# Idea Validation Report: Sprint Retro Auto-Generator

## Idea Summary
AI tool that imports Jira sprint data and generates retrospective summaries
for engineering managers at mid-size B2B companies.

## Assumption Map
| ID | Assumption | Category | Confidence |
|----|------------|----------|------------|
| A1 | EMs spend 2+ hours on retro prep | Desirability | Medium |
| A2 | Jira is primary data source for target segment | Feasibility | High |
| A3 | Teams will pay $29/user/month | Viability | Low |
| A4 | AI summary quality is trusted without heavy editing | Desirability | Low |
| A5 | Confluence/Slack export is required for adoption | Feasibility | Medium |

## Scorecard (1–5)
| Dimension | Score | Notes |
|-----------|-------|-------|
| Problem urgency | 4 | Real pain, moderate frequency |
| Market access | 3 | EM network exists, small sample |
| Technical feasibility | 4 | Jira API mature |
| Willingness to pay | 2 | No pricing validation |
| Differentiation | 3 | Jira plugins and generic AI exist |
| **Overall** | **3.2** | |

## Recommendation: **Pivot**

**Rationale:** Desirability signals are plausible but A4 (trust in AI output) and A3
(viability) are unvalidated. Narrow to "retro draft assistant with mandatory human edit"
and validate willingness to pay before full build.

## Evidence Gaps
- [ ] Interview 8 EMs: actual retro prep time and tools used
- [ ] Landing page test: email signup at stated price point
- [ ] Prototype test: 5 managers rate AI draft quality (target ≥4/5 after edits)
```

---

## Example 2: Vague idea — stop and clarify

### Input

```text
Build an AI app for productivity.
```

### Expected behavior

Stop before scorecard. Request:

```markdown
## Clarification needed

1. Target user segment (role, company size)
2. Specific job-to-be-done (what task does the app replace?)
3. How users solve this today (manual, competitor, workaround)
```

---

## Example 3: Anti-pattern — fake evidence

### Bad output

```markdown
A1 | Users want this | Desirability | High — "everyone needs productivity"
```

### Correct output

```markdown
A1 | Users want automated meeting notes | Desirability | Unknown — no interviews cited
**Action:** Run 5 user interviews before scoring above Low.
```

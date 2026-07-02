# Product Discovery Assistant — Worked Examples

---

## Example 1: Opportunity Solution Tree

### Input

```text
Outcome: Increase retro completion rate from 40% to 70% in Q3
Research: 6 EM interviews — prep time and action item loss cited
```

### Output (excerpt)

```markdown
# Product Discovery: Retro Completion

## Desired Outcome
Increase teams completing bi-weekly retro from 40% → 70% by 2026-09-30.

## Opportunities (problems, not solutions)
| ID | Opportunity | Evidence |
|----|-------------|----------|
| O1 | Retro prep takes too long | 5/6 interviews |
| O2 | Action items not tracked | 4/6 interviews |
| O3 | Remote teams disengage in retro | 2/6 interviews |

## Top Opportunities
1. O1 — score 20 (impact 5 × evidence 4)

## Solution Options (O1)
| Solution | Assumption | Cheapest test |
|----------|------------|---------------|
| Auto-import Jira | EMs trust imported data | Prototype with 3 users |
| Template library | Format is the blocker | Card sort interview |

## Experiments
| # | Experiment | Success criteria |
|---|------------|------------------|
| E1 | 5 EMs use Jira import prototype | 4/5 save >30 min |
```

---

## Example 2: Solutions listed as opportunities

### Input

```text
Opportunity: Build AI summary feature
```

### Expected behavior

Reframe to underlying problem: "Managers can't synthesize sprint signals quickly."

---

## Example 3: No measurable outcome

### Expected behavior

Stop; define metric baseline and target.

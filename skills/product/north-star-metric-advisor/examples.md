# North Star Metric Advisor — Worked Examples

---

## Example 1: B2B SaaS north star

### Input

```text
Product: Retro generator for EMs
Business model: $29/user/month
Value moment: Manager completes and exports a retro
Stage: pre-PMF
```

### Output (excerpt)

```markdown
# North Star Metric: RetroFlow

## North Star Metric
- **Metric:** Weekly Active Managers Completing a Retro (WAMCR)
- **Formula:** Unique managers who export ≥1 retro to Confluence per ISO week
- **Scope:** Paying workspace accounts

## Input Metrics
| Metric | Drives NSM by... |
|--------|------------------|
| Jira connect rate | Enables data import |
| Draft-to-export conversion | Completing the value loop |
| Time-to-first-export | Activation speed |

## Guardrails
| Anti-metric | Threshold |
|-------------|-----------|
| AI edit rate >80% (low trust) | Investigate quality |
| Churn among activated users | <5% monthly |
```

---

## Example 2: MRR as north star — reframe

### Input

```text
North star: Monthly Recurring Revenue
```

### Expected behavior

Reframe to user value metric (WAMCR) with revenue as lagging outcome.

---

## Example 3: Five north stars

### Expected behavior

Select one primary; demote others to input metrics.

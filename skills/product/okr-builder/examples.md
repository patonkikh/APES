# OKR Builder — Worked Examples

---

## Example 1: Product team Q3 OKRs

### Input

```text
Team: Retro Generator product squad
Period: Q3 2026
Vision: Help EMs run retros in 15 min instead of 2 hours
North star: Weekly active EM users completing a retro
Constraints: 4 engineers, no new hires
```

### Output (excerpt)

```markdown
# OKRs: Retro Generator — Q3 2026

## Objective 1: Prove core value for engineering managers
| KR | Metric | Baseline | Target |
|----|--------|----------|--------|
| 1.1 | WAU EMs completing ≥1 retro | 0 | 50 |
| 1.2 | Median retro prep time (survey) | 120 min | 30 min |
| 1.3 | Action items created in Jira post-retro | 0% | 60% |

**Initiatives:** MVP launch, onboarding flow, Confluence export

## Objective 2: Establish reliable AI output quality
| KR | Metric | Baseline | Target |
|----|--------|----------|--------|
| 2.1 | AI draft rated ≥4/5 after edit | N/A | 70% of sessions |
| 2.2 | P95 generation latency | N/A | <60s |

## Alignment Check
North star (WAU completing retro) ← supported by KR 1.1, 1.2
```

---

## Example 2: Output-based KR — rewrite

### Input

```text
KR: Ship Confluence integration
KR: Hire 2 engineers
```

### Expected behavior

```markdown
## Rewrites required

| Original (output) | Rewritten (outcome) |
|-------------------|---------------------|
| Ship Confluence integration | KR: 80% of exported retros land in correct Confluence space without manual fix |
| Hire 2 engineers | Escalate to leadership OKR — not team product OKR |
```

---

## Example 3: Too many objectives

### Input

```text
5 objectives for a 4-person team
```

### Expected behavior

Consolidate to max 3 objectives per Decision Rules; merge related themes.

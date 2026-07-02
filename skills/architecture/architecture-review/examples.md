# Architecture Review — Worked Examples

---

## Example 1: MVP architecture review findings

### Input

```text
Architecture: Retro generator (Jira OAuth, SQS workers, RDS, Azure OpenAI)
NFRs: p95 <60s, 99.5% availability, encrypted tokens
Team: 4 engineers, 8-week MVP
```

### Output (excerpt)

```markdown
# Architecture Review: Retro Generator MVP

## Summary
| Severity | Count |
|----------|-------|
| Critical | 0 |
| High | 2 |
| Medium | 3 |
| Low | 1 |

## Findings
| ID | Severity | Area | Finding | Recommendation |
|----|----------|------|---------|----------------|
| AR-001 | High | Security | OAuth tokens in app DB without rotation policy | Add refresh + revocation runbook |
| AR-002 | High | Reliability | Single-region SQS with no DLQ alerting | Add DLQ CloudWatch alarm |
| AR-003 | Medium | Scalability | Worker autoscaling not defined | Target queue depth scaling policy |
| AR-004 | Medium | Ops | No correlation ID across job pipeline | Add trace ID in API + worker logs |

## Quality Attribute Assessment
| Attribute | Met? | Gap |
|-----------|------|-----|
| Performance | Partial | Load test not evidenced |
| Security | Partial | Token rotation missing |
| Maintainability | Pass | Clear component boundaries |

## Verdict
**Approve with conditions** — resolve AR-001, AR-002 before production
```

---

## Example 2: Big ball of mud — Critical

### Input

```text
Single "App" component handles UI, Jira, AI, billing, and admin
```

### Expected behavior

Critical finding: no component boundaries; recommend decomposition aligned with solution-architecture.

---

## Example 3: Review without NFRs

### Expected behavior

Stop or add minimum NFRs (security, availability, performance) before scoring.

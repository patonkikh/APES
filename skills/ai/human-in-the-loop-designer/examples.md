# Human-in-the-Loop Designer — Examples

---

## Example 1: Customer email auto-reply (medium risk)

### Input

```text
AI drafts support replies. 500 tickets/day. Legal requires no unauthorized refunds.
Target: 80% auto-send after 30-day shadow period.
```

### Output (excerpt)

```markdown
## Escalation Triggers
| Trigger | Threshold | Action |
|---------|-----------|--------|
| Refund mentioned | keyword + NER | Mandatory queue |
| Confidence | <0.75 | Queue |
| Policy guardrail | PII outbound | Block + review |

## SLA
p95 queue wait < 10 min. Override rate alert > 15%.
```

---

## Example 2: High-risk — no reviewers

### Input

```text
Launch medical triage suggestions next week. No clinical staff for review yet.
```

### Expected behavior

Stop. Recommend shadow-only mode or delay launch until HITL staffing confirmed.

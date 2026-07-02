# Multi-Agent Planner — Worked Examples

---

## Example 1: Support triage orchestration

### Input

```text
Use case: Customer support with triage, research, and response
Constraints: human approval before external email send
Volume: 2k tickets/day
```

### Output (excerpt)

```markdown
# Multi-Agent Orchestration: Support System

## Agent Roles
| Agent | Responsibility | Tools |
|-------|----------------|-------|
| Supervisor | Route, aggregate, enforce policy | invoke agents |
| Triage | Classify category/priority | ticket API read |
| Research | Retrieve KB + past tickets | RAG search |
| Responder | Draft reply | ticket API read |
| Escalation | Human handoff package | notify human queue |

## Pattern
**Supervisor orchestration** with sequential handoffs:
Triage → Research → Responder → (Human approval gate) → Send

## Handoff Protocol
```json
{"from": "triage", "to": "research", "payload": {"ticket_id", "category", "priority"}}
```

## Failure Recovery
| Failure | Action |
|---------|--------|
| Research timeout | Retry 2x → escalate to human |
| Responder policy violation | Block send; supervisor re-route |

## Human-in-the-loop
External email send requires `approval_token` from human agent UI
```

---

## Example 2: Excessive agency — flag

### Input

```text
Single agent with full CRM admin + payment refund + email blast
```

### Expected behavior

Recommend role split; flag LLM08 excessive agency; require approval gates per tool.

---

## Example 3: No failure recovery

### Expected behavior

Validation fail until timeout/retry/escalation documented for each handoff.

# ADR Generator — Worked Examples

---

## Example 1: Async job processing for AI generation

### Input

```text
Decision: How to process retro AI generation requests
Context: p95 <60s SLA, spiky load, team knows AWS
Options considered: sync API call, SQS+workers, Step Functions
Recommendation leaning: SQS + ECS workers
```

### Output (excerpt)

```markdown
# ADR-001: Async Job Processing for AI Generation

**Status:** Proposed
**Date:** 2026-07-01

## Context
Retro AI generation takes 15–45s. Sync requests risk gateway timeouts
and poor UX under load. Must meet p95 <60s and scale to 500 concurrent users.

## Considered Options
| Option | Pros | Cons |
|--------|------|------|
| Sync API | Simple | Timeout risk, poor scaling |
| SQS + ECS workers | Scalable, familiar | More moving parts |
| Step Functions | Visual workflow | Higher cost, team learning curve |

## Decision
We will use **SQS + ECS Fargate workers** because the team has ECS experience,
cost is predictable at MVP scale, and it meets SLA without gateway timeouts.

## Consequences
**Positive:** Independent scaling of workers; retry via DLQ
**Negative:** Polling/WebSocket needed for status UX
**Neutral:** Monitor queue depth and worker autoscaling
```

---

## Example 2: Trivial decision — skip ADR

### Input

```text
Decision: Use Prettier for code formatting
```

### Expected behavior

```markdown
## Recommendation: Skip ADR

Decision rule: trivial/reversible → document in team README or CONTRIBUTING, not ADR.
```

---

## Example 3: Single option — blocked

### Input

```text
We must use PostgreSQL. Document the decision.
```

### Expected behavior

Add at least one alternative (e.g., DynamoDB, SQLite) with pros/cons before recording decision.

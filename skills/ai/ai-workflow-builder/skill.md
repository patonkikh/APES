---
name: ai-workflow-builder
description: >
  Build an executable AI workflow pipeline: stage definitions, data flow, branching logic, retries, and integration points for production deployment. Use when working on prompt engineering, AI workflows, agents, context design, or LLM optimization.
metadata:
  apes-version: "1.1"
  category: ai
---

# AI Workflow Builder

# Purpose

Build an executable AI workflow pipeline: stage definitions, data flow, branching logic, retries, and integration points for production deployment.

**Input:** Orchestration plan or use case, AI architecture, tool/MCP inventory (optional), NFRs (latency, throughput)  
**Output:** AI Workflow Specification with stage graph, I/O contracts, and deployment configuration outline
**Examples:** See [examples.md](examples.md) for worked input/output.

---

# Workflow

## Step 1: Map workflow stages

Define pipeline stages:

```text
Trigger → Preprocess → [Branch] → Model call(s) → Postprocess → Output / Webhook
```

| Stage | Type | Input | Output | Timeout |
|-------|------|-------|--------|---------|

Stage types: transform, LLM call, tool call, human gate, parallel fan-out, aggregate.

## Step 2: Define I/O contracts

For each stage boundary document:

- Input schema (fields, types, validation)
- Output schema (fields, types, required vs optional)
- Error payload format
- Idempotency key strategy (if applicable)

## Step 3: Design branching and control flow

| Condition | Branch | Default |
|-----------|--------|---------|
| Classification result | Route to specialist pipeline | Fallback general path |
| Confidence below threshold | Escalate to human or stronger model | Continue with flag |
| Tool call failure | Retry N times then degrade | Surface error to caller |

Document retry policy: max attempts, backoff, jitter.

## Step 4: Plan state and observability

- Workflow run ID and correlation ID propagation
- Per-stage metrics (duration, token count, success rate)
- Structured logging fields
- Checkpoint/resume points for long workflows

## Step 5: Specify deployment model

| Option | Fit |
|--------|-----|
| Synchronous API | Low latency, short pipelines |
| Async queue + worker | Long-running, batch workloads |
| Event-driven (webhook) | External triggers, fan-out |
| Scheduled cron | Periodic batch processing |

## Step 6: Validate

Run Validation checklist.

---

# Decision Rules

| Condition | Action |
|-----------|--------|
| No orchestration plan for multi-agent case | Recommend multi-agent-planner first |
| Stage exceeds latency budget alone | Split stage or add caching layer |
| Non-idempotent side effects without guard | Add idempotency key and dedup store |
| >10 sequential LLM calls | Flag cost/latency risk; recommend consolidation |
| Missing error handling on any stage | Block delivery; every stage needs failure path |
| PII flows through multiple stages | Add redaction stage and audit log policy |

---

# Validation

- [ ] All stages documented with I/O contracts
- [ ] Branching logic covers success, failure, and edge cases
- [ ] Retry policy defined per external dependency
- [ ] Observability: metrics and correlation IDs specified
- [ ] Deployment model aligned with NFRs
- [ ] Cost estimate per workflow run (order of magnitude)
- [ ] Human-in-the-loop gates placed where risk requires
- [ ] No stage without explicit timeout

---

# Anti-patterns

- **Monolithic stage** — one giant LLM call doing preprocess + reason + format.
- **Silent failures** — swallowing errors without branch to recovery path.
- **Unbounded retries** — retrying without cap on transient and permanent errors.
- **Missing correlation** — logs that cannot trace a single user request end-to-end.
- **Hardcoded prompts in workflow** — inline prompts instead of versioned prompt assets.

---

# Best Practices

- Keep stages small and testable in isolation.
- Version workflow definitions; support rollback.
- Use circuit breakers on external tool and model calls.
- Cache deterministic preprocessing results.
- Pair with ai-evaluation-builder for stage-level quality gates.

---

# Output Structure

```markdown
# AI Workflow Specification: [Workflow Name]
**Version:** 1.0

## Stage Graph
[Diagram and stage table]

## I/O Contracts
### Stage: [Name]
**Input schema:** ...
**Output schema:** ...

## Control Flow
| Trigger | Condition | Action |
|---------|-----------|--------|

## Retry & Circuit Breaker
| Dependency | Max retries | Backoff | Circuit threshold |
|------------|-------------|---------|-------------------|

## Observability
| Metric | Stage | Alert threshold |
|--------|-------|-----------------|

## Deployment
[Model, scaling, trigger mechanism]

## Cost Estimate
[Per-run and monthly at projected volume]
```

---

# Next Skills

| Outcome | Recommended Skill |
|---------|-------------------|
| Build eval harness for workflow | `ai/ai-evaluation-builder` |
| Reduce workflow cost | `ai/ai-cost-optimizer` |
| Reduce pipeline latency | `ai/ai-latency-optimizer` |
| Design prompts for stages | `ai/prompt-engineer` |
| Add MCP tools to stages | `mcp/mcp-tool-generator` |

# Multi-Agent Planner

# Purpose

Design a multi-agent orchestration architecture: agent roles, communication patterns, handoff protocols, and failure recovery for collaborative AI systems.

**Input:** Use case description, AI architecture (optional), task decomposition, constraints (latency, cost, reliability)  
**Output:** Multi-Agent Orchestration Plan with agent roster, interaction diagram, and coordination rules

---

# Workflow

## Step 1: Decompose the problem

Break the use case into subtasks:

| Subtask | Complexity | Dependencies | Human approval needed |
|---------|------------|--------------|----------------------|

Identify which subtasks require specialized reasoning, tool access, or isolation.

## Step 2: Define agent roles

For each agent specify:

- **Responsibility** — single bounded objective
- **Inputs** — what context it receives
- **Outputs** — artifact or message format
- **Tools** — allowed integrations (MCP, APIs, none)
- **Autonomy level** — fully autonomous / supervised / advisory only

## Step 3: Select orchestration pattern

| Pattern | When to use |
|---------|-------------|
| Supervisor | Central router delegates to specialists |
| Pipeline | Sequential handoffs with fixed stages |
| Peer-to-peer | Agents negotiate without central coordinator |
| Hierarchical | Manager agents delegate to worker agents |
| Swarm | Parallel exploration with aggregation step |

Document chosen pattern with rationale.

## Step 4: Design communication protocol

Define:

- Message schema (task ID, agent ID, payload, status)
- Handoff triggers (completion, escalation, timeout)
- Shared state store (conversation, scratchpad, blackboard)
- Conflict resolution (priority rules, supervisor override)

## Step 5: Plan failure and recovery

| Failure mode | Detection | Recovery action |
|--------------|-----------|-----------------|
| Agent timeout | Heartbeat / deadline | Retry or escalate to supervisor |
| Invalid output | Schema validation | Re-prompt with error context |
| Tool failure | Error code | Fallback agent or degrade gracefully |
| Infinite loop | Max iteration cap | Terminate and surface to user |

## Step 6: Validate

Run Validation checklist.

---

# Decision Rules

| Condition | Action |
|-----------|--------|
| Single agent can complete task | Recommend single-agent design; do not over-orchestrate |
| Subtasks share mutable state | Define explicit state ownership and locking |
| Customer-facing with high risk | Require human-in-the-loop gate before final output |
| Agents need different tool permissions | Isolate tool access per agent; no shared credentials |
| Latency budget < 5s | Avoid deep agent chains; prefer parallel or single agent |
| No clear task boundaries | Stop; decompose further before designing agents |

---

# Validation

- [ ] Problem decomposed with dependency map
- [ ] Each agent has single bounded responsibility
- [ ] Orchestration pattern selected with rationale
- [ ] Message schema and handoff triggers defined
- [ ] Failure modes with recovery actions documented
- [ ] Tool permissions scoped per agent
- [ ] Cost/latency impact estimated for agent count
- [ ] Human-in-the-loop gates defined for high-risk paths

---

# Anti-patterns

- **Agent sprawl** — creating agents for every minor subtask without coordination benefit.
- **Shared omniscient context** — passing full conversation history to every agent.
- **No termination condition** — agents loop without max iteration or success criteria.
- **Duplicate responsibilities** — two agents performing the same task without clear split.
- **Orchestration without eval** — multi-agent system without per-agent quality measurement.

---

# Best Practices

- Start with supervisor pattern; evolve to peer-to-peer only when justified.
- Keep agent count ≤5 for maintainability unless domain requires more.
- Use structured output contracts between agents (JSON schema, not free text).
- Log every inter-agent message for debugging and audit.
- Pair with ai-evaluation-builder to measure per-agent contribution.

---

# Output Structure

```markdown
# Multi-Agent Orchestration Plan: [System Name]

## Problem Decomposition
| Subtask | Agent candidate | Dependencies |
|---------|-----------------|--------------|

## Agent Roster
| Agent | Responsibility | Tools | Autonomy |
|-------|----------------|-------|----------|

## Orchestration Pattern
[Pattern name and rationale]

## Interaction Diagram
[ASCII or mermaid sequence]

## Communication Protocol
| Field | Type | Description |
|-------|------|-------------|

## Failure & Recovery
| Failure | Detection | Recovery |
|---------|-----------|----------|

## Cost & Latency Estimate
[Per-request impact vs single-agent baseline]

## Open Decisions
- [ ] [Unresolved design choice]
```

---

# Next Skills

| Outcome | Recommended Skill |
|---------|-------------------|
| Implement workflow pipeline | `ai/ai-workflow-builder` |
| Design evaluation per agent | `ai/ai-evaluation-builder` |
| Optimize agent call costs | `ai/ai-cost-optimizer` |
| Reduce orchestration latency | `ai/ai-latency-optimizer` |
| MCP tool integration needed | `mcp/mcp-tool-generator` |

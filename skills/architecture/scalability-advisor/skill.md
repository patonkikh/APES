---
name: scalability-advisor
description: >
  Assess system scalability: identify bottlenecks, recommend scaling strategies per container, and define capacity planning guidelines. Use when working on solution architecture, C4 diagrams, APIs, ADRs, or system design.
metadata:
  apes-version: "1.1"
  category: architecture
---

# Scalability Advisor

# Purpose

Assess system scalability: identify bottlenecks, recommend scaling strategies per container, and define capacity planning guidelines.

**Input:** Container diagram, NFRs (throughput, latency, users), data flow analysis (optional)  
**Output:** Scalability Assessment with bottleneck analysis, scaling recommendations, and capacity model
**Examples:** See [examples.md](examples.md) for worked input/output.

---

# Workflow

## Step 1: Extract scalability requirements

From NFRs, define:

| Metric | Target | Peak multiplier | Measurement |
|--------|--------|-----------------|-------------|

Metrics: concurrent users, requests/sec, data volume, growth rate.

## Step 2: Analyze each container

For each container:

| Container | Stateless? | Bottleneck risk | Current limit estimate |
|-----------|------------|-----------------|------------------------|

Identify: CPU-bound, memory-bound, I/O-bound, connection-pool limits.

## Step 3: Identify system bottlenecks

Rank bottlenecks:

| Rank | Component | Constraint | Impact at scale |
|------|-----------|------------|-----------------|

Common: database connections, single instance, sync external calls, large payloads.

## Step 4: Recommend scaling strategies

Per container:

| Strategy | When | Trade-off |
|----------|------|-----------|
| Horizontal scaling | Stateless services | Coordination complexity |
| Vertical scaling | Short-term, DB | Cost ceiling |
| Caching | Read-heavy | Staleness |
| Read replicas | Read/write split | Replication lag |
| Sharding | Large datasets | Query complexity |
| Async processing | Burst workloads | Latency |

## Step 5: Build capacity model

Simple capacity estimate:

```text
Peak RPS = users × actions_per_session / session_duration
Required instances = Peak RPS / RPS_per_instance
```

Document assumptions explicitly.

## Step 6: Define load testing plan

| Scenario | Load | Success criteria |
|----------|------|------------------|

## Step 7: Validate

Run Validation checklist.

---

# Decision Rules

| Condition | Action |
|-----------|--------|
| No NFR throughput targets | Request targets or use conservative assumptions; mark Confidence low |
| Stateful container scaled horizontally | Flag session/state management requirement |
| Database is bottleneck | Recommend read replicas, caching, or sharding with trade-offs |
| External API rate limits | Include in capacity model; recommend caching/batching |
| Scale requirements < 1000 users | Recommend simple vertical scaling; avoid premature optimization |

---

# Validation

- [ ] Scalability NFRs extracted or assumptions stated
- [ ] Every container analyzed for bottleneck risk
- [ ] Top 3 bottlenecks ranked with rationale
- [ ] Scaling strategy per high-risk container
- [ ] Capacity model with explicit assumptions
- [ ] Load testing scenarios defined
- [ ] Premature optimization flagged if scale is small
- [ ] Trade-offs documented for each strategy

---

# Anti-patterns

- **Scale everything** — horizontal scaling stateful DB without plan.
- **Cache as fix-all** — caching without invalidation strategy.
- **Ignore externals** — not modeling third-party rate limits.
- **No load testing** — recommendations without validation plan.
- **Infinite scale claims** — "handles any load" without evidence.

---

# Best Practices

- Start with measured baseline, not guesses.
- Scale the bottleneck first (Amdahl's law).
- Prefer stateless containers for horizontal scaling.
- Plan scale-down as well as scale-up (cost).
- Align with data-flow-analyzer for data layer scaling.

---

# Output Structure

```markdown
# Scalability Assessment: [System Name]

## Requirements
| Metric | Target | Peak | Assumptions |
|--------|--------|------|-------------|

## Container Analysis
| Container | Stateless | Risk | Limit |
|-----------|-----------|------|-------|

## Bottlenecks
| Rank | Component | Constraint | At-risk metric |
|------|-----------|------------|----------------|

## Recommendations
| Container | Strategy | Rationale | Trade-off |
|-----------|----------|-----------|-----------|

## Capacity Model
[Calculations with assumptions]

## Load Test Plan
| Scenario | Load | Pass criteria |
|----------|------|---------------|

## Risks
| Risk | Mitigation |
|------|------------|
```

---

# Next Skills

| Outcome | Recommended Skill |
|---------|-------------------|
| Review scalability in full context | `architecture/architecture-review` |
| Update architecture for scale | `architecture/solution-architecture` |
| Document scaling decision | `architecture/adr-generator` |
| AI system scaling | `ai/ai-solution-architect` |

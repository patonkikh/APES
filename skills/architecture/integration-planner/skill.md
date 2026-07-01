# Integration Planner

# Purpose

Plan integrations between system containers and external systems: patterns, contracts, sequencing, failure handling, and monitoring.

**Input:** Container diagram, API designs (optional), external system inventory  
**Output:** Integration Plan with connection matrix, sequence flows, and rollout phases

---

# Workflow

## Step 1: Inventory integration points

List all integrations:

| Source | Target | Type (sync/async/batch) | Data | Criticality |
|--------|--------|-------------------------|------|-------------|

Include internal (container-to-container) and external (third-party) connections.

## Step 2: Classify integration patterns

Assign pattern per connection:

| Pattern | Use when |
|---------|----------|
| Request-response (REST/gRPC) | Real-time queries, commands |
| Message queue | Decoupled async processing |
| Event streaming | Multiple consumers, audit trail |
| File/batch transfer | Large volumes, scheduled sync |
| Webhook/callback | External system pushes events |

## Step 3: Define contracts

For each integration:

- Message/event schema or API reference
- SLA expectations (latency, availability)
- Authentication mechanism
- Retry and idempotency rules
- Dead letter / poison message handling

## Step 4: Sequence critical flows

Document 2–3 end-to-end integration sequences:

```text
Actor → Container A → Queue → Container B → External System
```

Include happy path and failure branches.

## Step 5: Plan rollout phases

| Phase | Integrations | Dependencies | Risk |
|-------|--------------|--------------|------|

Order by dependency and risk (stub externals first).

## Step 6: Define observability

Per integration:

- Correlation ID propagation
- Metrics (latency, error rate, throughput)
- Alerts thresholds

## Step 7: Validate

Run Validation checklist.

---

# Decision Rules

| Condition | Action |
|-----------|--------|
| No container diagram | Stop; run container-diagram-builder |
| Synchronous chain > 3 hops for user request | Flag latency risk; recommend async |
| No auth on external integration | Flag security finding; block proceed |
| Duplicate integration paths | Consolidate; document single canonical path |
| External SLA unknown | Mark as risk; recommend SLA discovery task |

---

# Validation

- [ ] All container diagram connections covered
- [ ] Pattern assigned to each integration
- [ ] Auth mechanism specified per external integration
- [ ] Retry/idempotency rules for async integrations
- [ ] ≥2 sequence diagrams for critical flows
- [ ] Rollout phases ordered by dependency
- [ ] Observability requirements per integration
- [ ] Failure handling documented

---

# Anti-patterns

- **Point-to-point spaghetti** — n×n connections without hub/broker.
- **Sync everywhere** — blocking chains for non-real-time needs.
- **No dead letter queue** — lost messages on failure.
- **Missing correlation IDs** — impossible to trace cross-service requests.
- **Big bang integration** — all externals at once without phased rollout.

---

# Best Practices

- Prefer events over direct DB sharing between containers.
- Use circuit breakers for external dependencies.
- Stub external systems in early phases.
- Align with api-designer output for REST contracts.
- Document integration ADRs for non-obvious pattern choices.

---

# Output Structure

```markdown
# Integration Plan: [System Name]

## Integration Inventory
| ID | Source | Target | Pattern | Criticality |
|----|--------|--------|---------|-------------|

## Contracts
### INT-001: [Name]
- Pattern: [type]
- Auth: [method]
- Schema: [reference]
- Retry: [rules]

## Sequence Flows
### Flow 1: [Name]
[Step-by-step sequence]

## Rollout Phases
| Phase | Integrations | Milestone |
|-------|--------------|-----------|

## Observability
| Integration | Metrics | Alerts |
|-------------|---------|--------|

## Risks
| Risk | Mitigation |
|------|------------|
```

---

# Next Skills

| Outcome | Recommended Skill |
|---------|-------------------|
| Analyze data movement | `architecture/data-flow-analyzer` |
| Review integration security | `architecture/architecture-review` |
| Design APIs | `architecture/api-designer` |
| Document pattern decision | `architecture/adr-generator` |

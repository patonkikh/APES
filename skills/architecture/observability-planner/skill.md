---
name: observability-planner
description: >
  Design observability for AI and distributed systems: traces, metrics, logs, dashboards, and alerting aligned to SLOs. Use when planning monitoring, debugging LLM pipelines, or production readiness reviews.
metadata:
  apes-version: "1.1"
  category: architecture
---

# Observability Planner

# Purpose

Design observability for AI-powered systems: what to trace, measure, log, alert on, and display — aligned to SLOs and incident response.

**Input:** System architecture, SLO targets, critical user journeys, stack constraints (cloud, APM vendor)  
**Output:** Observability Plan with signal catalog, dashboard specs, alert rules, and runbook hooks  
**Examples:** See [examples.md](examples.md) for worked input/output.

---

# Workflow

## Step 1: Define SLIs and SLOs

| Journey | SLI | SLO example |
|---------|-----|-------------|
| Chat response | Availability + latency | 99.5% < 3s p95 |
| RAG query | Answer with citation | 98% success rate |
| Agent tool run | Tool success | 99% per tool |
| Batch ingest | Pipeline completion | 99.9% daily |

Document error budget and escalation when burned.

## Step 2: Apply three pillars per component

| Component | Traces | Metrics | Logs |
|-----------|--------|---------|------|
| API gateway | Request span | RPS, 5xx rate | Access log |
| LLM call | Parent span + token attrs | latency, tokens, cost | model_id, prompt_hash |
| Vector DB | Query span | recall latency | index version |
| Queue/worker | Job span | backlog depth | job_id, retries |

Use OpenTelemetry semantic conventions where available.

## Step 3: AI-specific observability

| Signal | Implementation | Alert |
|--------|----------------|-------|
| Trace per inference | Span: `llm.chat` with `gen_ai.*` attrs | p95 latency |
| RAG retrieval | Span: `rag.retrieve` + chunk IDs | empty retrieval rate |
| Tool execution | Span per tool with success/fail | failure rate >1% |
| Prompt version | `prompt_version` attribute | N/A (dimension) |
| Cost | `token_count` × price | daily budget |
| Quality proxy | User rating event | rating drop >10% |

Correlate with `analytics-instrumentation-planner` product events.

## Step 4: Design dashboards

| Dashboard | Audience | Panels |
|-----------|----------|--------|
| Service health | On-call | SLO, error rate, latency heatmap |
| AI pipeline | AI engineers | Token usage, model mix, RAG stats |
| Business overlay | Product | DAU + error rate correlation |

Each panel links to trace exemplar for drill-down.

## Step 5: Define alerts and runbooks

| Alert | Condition | Severity | Runbook |
|-------|-----------|----------|---------|
| High 5xx | >1% 5min | P1 | Scale + rollback |
| LLM timeout | p95 > SLO 10min | P2 | Model fallback |
| Ingest lag | >1h | P2 | Queue drain playbook |
| Cost spike | +50% daily | P3 | Rate limit review |

Alerts must be actionable; tie to owner and escalation path.

## Step 6: Logging and privacy

- Structured JSON logs with `trace_id`, `user_id` (hashed), `request_id`
- Never log raw prompts/responses in prod; use opt-in debug tier
- Retention: hot 7d, cold 30d, compliance per policy

## Step 7: Validate

Run Validation checklist.

---

# Decision Rules

| Condition | Action |
|-----------|--------|
| No SLO defined | Stop; propose SLIs from critical journeys |
| Multi-tenant | Tag all signals with `tenant_id` |
| Third-party LLM only | Trace at client; log provider request IDs |
| Regulated data | No full payload logging; spans only |
| Serverless | Prefer metrics + traces; minimize log volume cost |

---

# Validation

- [ ] SLIs/SLOs per critical journey
- [ ] Trace spans for LLM, RAG, and tools defined
- [ ] Metrics catalog with names and labels
- [ ] ≥2 dashboards specified with audience
- [ ] Alerts with thresholds and runbook links
- [ ] Privacy rules for prompts and PII in logs
- [ ] Error budget policy documented
- [ ] Correlation ID propagated end-to-end

---

# Anti-patterns

- **Logs only** — cannot debug distributed LLM latency without traces.
- **Alert fatigue** — 50 thresholds nobody acts on.
- **Dashboard vanity** — charts without SLO line.
- **Logging prompts in prod** — security and compliance risk.
- **Missing business metrics** — ops green while users churn.

---

# Best Practices

- Adopt OpenTelemetry early; one instrumentation for metrics + traces.
- Store `prompt_version` and `model_id` on every LLM span.
- Practice game days: inject failure, verify alerts fire.
- Pair with `ai-evaluation-builder` for quality regressions.
- Review observability coverage in architecture review checklist.

---

# Output Structure

```markdown
# Observability Plan: [System Name]

## SLOs
| Journey | SLI | Target | Error budget |
|---------|-----|--------|--------------|

## Signal Catalog
### Traces
[Span list + attributes]

### Metrics
[Name, labels, collection]

### Logs
[Fields, retention]

## Dashboards
[Panel descriptions]

## Alerts
| Name | Query | Threshold | Runbook |

## Privacy
[Logging restrictions]

## Rollout
[Instrumentation phases]
```

---

# Next Skills

| Outcome | Recommended Skill |
|---------|-------------------|
| Product-side metrics | `product/analytics-instrumentation-planner` |
| AI eval regression gates | `ai/ai-evaluation-builder` |
| Latency optimization | `ai/ai-latency-optimizer` |
| Cost dashboards | `ai/ai-cost-optimizer` |
| Architecture review | `architecture/architecture-review` |

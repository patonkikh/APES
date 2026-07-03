---
name: analytics-instrumentation-planner
description: >
  Design product analytics instrumentation: event taxonomy, properties schema, funnel definitions, and dashboard specs for AI-powered products. Use when defining metrics, tracking plans, growth experiments, or product analytics setup.
metadata:
  apes-version: "1.1"
  category: product
---

# Analytics Instrumentation Planner

# Purpose

Design product analytics instrumentation: what to track, how events are named, which properties to capture, and how metrics connect to product goals.

**Input:** Product flows, north-star metric (optional), key hypotheses, platform constraints (web/mobile/API)  
**Output:** Analytics Tracking Plan with event catalog, property schemas, funnels, and dashboard wireframes  
**Examples:** See [examples.md](examples.md) for worked input/output.

---

# Workflow

## Step 1: Align metrics to goals

| Layer | Examples | Owner |
|-------|----------|-------|
| North star | Weekly active teams, successful AI tasks | Product |
| Input metrics | Activation rate, time-to-value | Growth |
| Feature metrics | Prompt success rate, RAG answer helpfulness | Feature teams |
| Guardrail | Error rate, cost per user, churn | Platform |

If north-star undefined, run `north-star-metric-advisor` first or propose candidates.

## Step 2: Map user journeys to funnels

For each critical journey:

```text
Entry → Key actions → Success state → Retention signal
```

Example (AI assistant):

```text
Sign up → First prompt → Successful response → Return within 7d
```

Document drop-off questions each funnel step should answer.

## Step 3: Design event taxonomy

Naming convention: `object_action` in snake_case (e.g., `prompt_submitted`, `rag_query_completed`).

| Event | Trigger | Required properties |
|-------|---------|---------------------|
| `user_signed_up` | Account created | `source`, `plan` |
| `prompt_submitted` | User sends prompt | `model`, `token_count_bucket` |
| `ai_response_rated` | Thumbs up/down | `rating`, `latency_ms` |

Rules:

- One event per user-visible action (not per API call unless debugging)
- No PII in event names or property keys
- Hash or bucket sensitive values

## Step 4: Define property schema

Global context on every event:

| Property | Type | Example |
|----------|------|---------|
| `user_id` | string | internal ID only |
| `session_id` | string | UUID |
| `app_version` | string | 2.4.1 |
| `environment` | enum | prod/staging |

Per-event properties documented with type, allowed values, and nullability.

## Step 5: AI-specific instrumentation

| Signal | Event / property | Why |
|--------|------------------|-----|
| Model routing | `model_id`, `route_reason` | Cost/quality analysis |
| RAG retrieval | `chunks_retrieved`, `score_max` | Debug bad answers |
| Tool calls | `tool_name`, `success` | Agent reliability |
| Latency | `ttft_ms`, `total_ms` | SLA monitoring |
| Feedback | `rating`, `category` | Quality loop |

Align with `ai-evaluation-builder` online metrics where possible.

## Step 6: Dashboard and experiment specs

| Dashboard | Charts | Audience |
|-----------|--------|----------|
| Activation | Funnel, TTV distribution | Product |
| AI quality | Rating trend, override rate | AI team |
| Unit economics | Cost per active user | Leadership |

For A/B tests: primary metric, guardrails, minimum detectable effect, runtime estimate.

## Step 7: Validate

Run Validation checklist.

---

# Decision Rules

| Condition | Action |
|-----------|--------|
| No consent for tracking (GDPR) | Stop; define consent-gated events only |
| High-cardinality properties (raw prompts) | Never log; use hashed buckets or opt-in debug |
| Pre-launch product | Track minimum viable set (≤15 events) |
| B2B multi-tenant | Add `workspace_id` to all events |
| AI cost visibility needed | Require `model_id` + `token_count` on inference events |

---

# Validation

- [ ] North star and input metrics linked to events
- [ ] ≥1 funnel with steps and success definition
- [ ] Event catalog ≥10 events with naming convention doc
- [ ] Global context properties defined
- [ ] No PII in event/property design
- [ ] AI-specific signals included for AI products
- [ ] Dashboard wireframe with ≥3 charts
- [ ] Implementation notes (SDK, server-side vs client)

---

# Anti-patterns

- **Track everything** — unusable warehouse, privacy risk.
- **Vague events** — `button_clicked` without object context.
- **Metric without owner** — dashboard nobody reads.
- **Client-only revenue events** — trust server-side for billing.
- **Prompt logging by default** — compliance incident waiting to happen.

---

# Best Practices

- Version the tracking plan in repo (`analytics/tracking-plan.md`).
- Use Segment/Amplitude/Mixpanel taxonomy import where supported.
- Pair events with `acceptance-criteria-generator` for measurable stories.
- Review event volume and cost quarterly.
- Run tracking plan review before each major release.

---

# Output Structure

```markdown
# Analytics Tracking Plan: [Product]

## Goals
| Metric | Definition | Target |
|--------|------------|--------|

## Funnels
### [Journey name]
[Steps + questions]

## Event Catalog
| Event | Trigger | Properties |
|-------|---------|------------|

## Global Properties
[Schema table]

## AI Events
[If applicable]

## Dashboards
[Wireframe descriptions]

## Privacy & Consent
[Rules]

## Implementation Checklist
[ ] SDK init [ ] Server events [ ] QA validation
```

---

# Next Skills

| Outcome | Recommended Skill |
|---------|-------------------|
| Define north star | `product/north-star-metric-advisor` |
| Design experiments | `product/okr-builder` |
| AI quality metrics | `ai/ai-evaluation-builder` |
| Observability for engineers | `architecture/observability-planner` |
| PRD success metrics section | `product/prd-generator` |

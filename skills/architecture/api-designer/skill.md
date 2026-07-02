---
name: api-designer
description: >
  Design REST or event-based APIs from container architecture: resources, operations, schemas, error model, and versioning strategy. Use when working on solution architecture, C4 diagrams, APIs, ADRs, or system design.
metadata:
  apes-version: "1.1"
  category: architecture
---

# API Designer

# Purpose

Design REST or event-based APIs from container architecture: resources, operations, schemas, error model, and versioning strategy.

**Input:** Container diagram, functional requirements, integration points  
**Output:** API Design document with resource model, endpoint catalog, schema definitions, and error conventions
**Examples:** See [examples.md](examples.md) for worked input/output.

---

# Workflow

## Step 1: Identify API boundaries

From container diagram, list APIs to design:

- Public (external consumers)
- Internal (service-to-service)
- Partner (B2B integrations)

One API surface per container that exposes HTTP/gRPC/events.

## Step 2: Define resource model

Map domain entities to resources:

| Resource | Description | Relationships |
|----------|-------------|---------------|

Use nouns for resources, HTTP verbs for actions. Avoid verb-based URLs.

## Step 3: Specify operations

For each resource, document:

| Method | Path | Operation | Request | Response | Auth |
|--------|------|-----------|---------|----------|------|

Include pagination, filtering, sorting for collections.

## Step 4: Define schemas

Document request/response schemas:

- Field names, types, required/optional
- Validation rules
- Enum values
- Idempotency keys where needed

Use OpenAPI-compatible structure without requiring OpenAPI syntax.

## Step 5: Design error model

Standard error envelope:

| Field | Purpose |
|-------|---------|
| code | Machine-readable error code |
| message | Human-readable description |
| details | Field-level errors (optional) |
| request_id | Tracing |

Map HTTP status codes to error categories.

## Step 6: Versioning and compatibility

Define:

- Versioning strategy (URL path, header, or content negotiation)
- Breaking vs non-breaking change rules
- Deprecation policy

## Step 7: Validate

Run Validation checklist.

---

# Decision Rules

| Condition | Action |
|-----------|--------|
| No container diagram | Stop; run container-diagram-builder |
| RPC-style operations dominate | Consider gRPC/event schema alongside REST |
| Breaking change needed | Document migration path and version bump |
| Sensitive data in URL | Move to request body or header |
| More than 30 endpoints in MVP | Prioritize Must-have FRs; defer Should-have |

---

# Validation

- [ ] API boundaries aligned with containers
- [ ] Resource model uses nouns consistently
- [ ] All Must-have FRs traceable to endpoints
- [ ] Error model defined with status code mapping
- [ ] Auth requirement per endpoint
- [ ] Versioning strategy stated
- [ ] Pagination defined for list endpoints
- [ ] No implementation code (framework-specific)

---

# Anti-patterns

- **Chatty APIs** — multiple calls where one would suffice.
- **Verb URLs** — `/getUser`, `/createOrder`.
- **Inconsistent naming** — mixing camelCase and snake_case across endpoints.
- **Missing error codes** — generic 500 for all failures.
- **Breaking changes without version** — modifying existing contracts silently.

---

# Best Practices

- Follow Richardson Maturity Model Level 2+ for REST.
- Use ISO 8601 for dates, UUID for IDs.
- Document idempotency for POST/PUT where applicable.
- Align with ADRs for protocol choices.
- Include rate limiting and auth scopes in design.

---

# Output Structure

```markdown
# API Design: [API Name]

## Overview
- **Base URL:** [pattern]
- **Protocol:** REST | gRPC | Events
- **Version:** v1

## Resources
| Resource | Description |
|----------|-------------|

## Endpoints
| Method | Path | Operation | Auth | FR ref |
|--------|------|-----------|------|--------|

## Schemas
### [ResourceName]
| Field | Type | Required | Validation |
|-------|------|----------|------------|

## Error Model
| HTTP | Code | When |
|------|------|------|

## Versioning
[Strategy and rules]

## Open Questions
- [ ] [Question]
```

---

# Next Skills

| Outcome | Recommended Skill |
|---------|-------------------|
| Plan cross-system integration | `architecture/integration-planner` |
| Review API security | `architecture/architecture-review` |
| Document API decision | `architecture/adr-generator` |
| Analyze data flows | `architecture/data-flow-analyzer` |

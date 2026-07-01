# MCP Best Practices

# Purpose

Document and apply MCP implementation best practices: server design, client integration, testing, versioning, observability, and operational readiness for production MCP deployments.

**Input:** MCP server/client implementation (existing or planned), deployment target, team constraints  
**Output:** MCP Best Practices Compliance Report with gap analysis, recommended patterns, and operational playbook

---

# Workflow

## Step 1: Assess current implementation

Score each practice area:

| Area | Status | Gap |
|------|--------|-----|
| Server scope & naming | | |
| Tool design quality | | |
| Auth & secrets | | |
| Error handling | | |
| Testing | | |
| Observability | | |
| Versioning | | |
| Documentation | | |

## Step 2: Apply server best practices

| Practice | Requirement |
|----------|-------------|
| Single domain | One server per bounded integration |
| Tool naming | snake_case, verb_noun, unique across server |
| Descriptions | LLM-optimized with negative cases |
| Schemas | JSON Schema with constraints on all inputs |
| Errors | Structured: code, message, retryable flag |
| Timeouts | Per-tool and per-request limits |
| Rate limiting | Protect upstream API quotas |

## Step 3: Apply client best practices

| Practice | Requirement |
|----------|-------------|
| Discovery | Dynamic tool list; no hardcoded assumptions |
| Validation | Client-side schema check before invoke |
| Resilience | Retry with backoff on transient errors |
| Degradation | Graceful fallback when server unavailable |
| Logging | Tool name + duration; redact sensitive args |

## Step 4: Define testing strategy

| Level | Coverage |
|-------|----------|
| Unit | Handler logic, schema validation, error mapping |
| Integration | MCP protocol round-trip with test server |
| Contract | Schema snapshot tests on tool definitions |
| Security | Injection payloads, auth failure cases |
| Load | Rate limit behavior under concurrent calls |

## Step 5: Plan observability and operations

| Signal | Tool | Alert |
|--------|------|-------|
| Tool success rate | Metrics | <95% over 5m |
| Latency p95 | Metrics | > SLA |
| Error rate by code | Logs | Spike in 5xx |
| Auth failures | Logs | >10/hour |

Document runbook: server restart, token rotation, rollback procedure.

## Step 6: Validate

Run Validation checklist.

---

# Decision Rules

| Condition | Action |
|-----------|--------|
| No integration tests | Block production; minimum contract tests required |
| Breaking tool schema change | Major version bump and changelog entry |
| Multiple teams sharing one server | Establish ownership and contribution guidelines |
| Server uptime SLA required | HTTP transport with health endpoint |
| Frequent upstream API changes | Add adapter layer in lib/; isolate from tool handlers |
| Compliance requirement (SOC2, HIPAA) | Extend with ai-security skills; audit logging mandatory |

---

# Validation

- [ ] All 8 practice areas assessed with gaps identified
- [ ] Server practices: naming, schemas, errors, timeouts documented
- [ ] Client practices: discovery, validation, resilience documented
- [ ] Testing strategy covers unit, integration, contract, security
- [ ] Observability signals and alerts defined
- [ ] Versioning and changelog policy stated
- [ ] README complete: setup, config, tools, troubleshooting
- [ ] Operational runbook for common incidents

---

# Anti-patterns

- **Copy-paste handlers** — duplicated logic without shared lib layer.
- **No changelog** — breaking changes without consumer notice.
- **Production debugging via printf** — unstructured logs without levels.
- **Skipping contract tests** — server deploy breaks clients silently.
- **Monorepo chaos** — server and unrelated app code interleaved.

---

# Best Practices

- Pin MCP SDK versions; test upgrades in staging.
- Publish JSON Schema for tools as machine-readable artifact.
- Use semantic versioning for server packages.
- Document breaking changes with migration guide.
- Schedule periodic security re-review with mcp-security-review.

---

# Output Structure

```markdown
# MCP Best Practices Report: [Project Name]

## Compliance Summary
| Area | Score (1-5) | Critical gaps |
|------|-------------|---------------|

## Server Practices
[Checklist with pass/fail]

## Client Practices
[Checklist with pass/fail]

## Testing Strategy
| Level | Status | Action items |
|-------|--------|--------------|

## Observability
| Signal | Implementation | Alert |
|--------|----------------|-------|

## Versioning Policy
[Semver rules, changelog format]

## Operational Runbook
| Incident | Detection | Resolution |
|----------|-----------|------------|

## Improvement Roadmap
| Priority | Item | Effort |
|----------|------|--------|
```

---

# Next Skills

| Outcome | Recommended Skill |
|---------|-------------------|
| Security re-assessment | `mcp/mcp-security-review` |
| Add new tools | `mcp/mcp-tool-generator` |
| New server from scratch | `mcp/mcp-server-generator` |
| Client improvements | `mcp/mcp-client-generator` |
| AI system integration | `ai/ai-workflow-builder` |

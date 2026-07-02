# Solution Architecture — Worked Examples

---

## Example 1: MVP SaaS from PRD

### Input

```text
PRD: Sprint retro auto-generator (MVP)
Must FRs: Jira OAuth, sprint import, AI summary, Confluence export
NFRs: p95 generation <60s, OAuth tokens encrypted, 99.5% availability
Constraints: 8-week MVP, team knows Node/TypeScript, AWS preferred, no on-prem
```

### Output (excerpt)

```markdown
# Solution Architecture: Retro Generator MVP

## Architectural Drivers
| Driver | Source | Priority |
|--------|--------|----------|
| Jira + Confluence integration | FR-001, FR-005 | High |
| Sub-60s AI generation | NFR-001 | High |
| Small team, fast MVP | Constraint | High |
| Token security | NFR-002 | High |

## Principles
| # | Principle | Implication |
|---|-----------|-------------|
| 1 | Managed services over self-hosted | Use managed LLM API, managed DB |
| 2 | Sync API for user actions | REST for UI; async only for generation job |
| 3 | Bounded context per integration | Separate Jira adapter from Confluence adapter |

## Component Model
| Component | Responsibility | FRs covered |
|-----------|----------------|-------------|
| Web App | UI, OAuth callback | FR-001, FR-002, FR-004 |
| API Gateway | Auth, routing | All |
| Retro Service | Orchestrate import + generation | FR-003, FR-004 |
| Jira Adapter | OAuth + sprint/issue fetch | FR-001, FR-002 |
| Confluence Adapter | Page create/update | FR-005 |
| Job Queue | Async generation workers | FR-003 |
| Data Store | Users, tokens, drafts | NFR-002 |

## Technology Recommendations
| Component | Recommended | Alternatives | Rationale |
|-----------|-------------|--------------|-----------|
| Compute | AWS ECS Fargate | Lambda | Long-running generation jobs |
| Queue | SQS | Redis | Managed, team familiarity |
| DB | RDS PostgreSQL | DynamoDB | Relational user/token model |
| LLM | Azure OpenAI API | Bedrock | Enterprise DPA available |

## Open Decisions
| Decision | Recommended ADR |
|----------|-------------------|
| Async job vs sync for <60s SLA | ADR-001 Job processing model |
```

---

## Example 2: Missing PRD — stop

### Input

```text
Design architecture for our AI platform.
```

### Expected behavior

```markdown
## Blocked — insufficient requirements

No PRD or FR/NFR list provided. Run `product/prd-generator` or supply:
- Functional capabilities (Must/Should)
- NFR targets (latency, availability, security)
- Constraints (cloud, team skills, budget)
```

---

## Example 3: Rejected alternative (required)

Even when one architecture is obvious, document a rejected option:

| Option | Why rejected |
|--------|--------------|
| Monolith + shared DB for all integrations | Faster week 1 but couples Jira/Confluence failures; violates adapter principle |

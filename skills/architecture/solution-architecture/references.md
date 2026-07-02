# C4 Model & Solution Architecture — Reference

Reference for architecture skills using the [C4 model](https://c4model.com/). Load when building solution, context, container, or component diagrams.

---

## C4 Levels

| Level | Name | Scope | APES Skill |
|-------|------|-------|------------|
| 1 | System Context | System + users + externals | `system-context-builder` |
| 2 | Containers | Applications + data stores | `container-diagram-builder` |
| 3 | Components | Modules inside one container | `component-diagram-builder` |
| 4 | Code | Classes (rarely in APES) | Defer to codebase |

**Progression:** solution-architecture (logical) → L1 context → L2 containers → L3 components

---

## Quality Attributes (ISO 25010 subset)

| Attribute | Questions to ask |
|-----------|------------------|
| Performance | Latency, throughput targets? |
| Scalability | Expected growth factor? |
| Availability | Uptime SLA, RTO/RPO? |
| Security | Auth, encryption, compliance? |
| Maintainability | Team size, change frequency? |
| Usability | User-facing SLA? |

Map each Must-have NFR to architectural approach.

---

## Integration Patterns

| Pattern | Use when | Avoid when |
|---------|----------|------------|
| Sync REST | Request/response, low latency | Long-running jobs |
| Async messaging | Decoupling, burst load | Simple CRUD only |
| Event bus | Multiple subscribers | Single consumer |
| Shared database | — | Default choice (coupling) |
| Batch | Large periodic processing | Real-time needs |

---

## Architectural Drivers Template

```text
Functional:     FR-001, FR-003, ...
Quality:        performance p95 <Xs, availability 99.X%
Constraints:    must-use AWS, team knows Node, 8-week MVP
Assumptions:    Jira API stable, <500 issues per sprint
```

---

## Technology Trade-off Table

Always document **≥2 options** with pros/cons before recommending one.

| Option | Pros | Cons | Fit |
|--------|------|------|-----|
| A | | | |
| B | | | |

Tie recommendation to drivers, not preference.

---

## Anti-Patterns (quick list)

| Name | Signal |
|------|--------|
| Big ball of mud | Single component does everything |
| Resume-driven | Novel tech without driver |
| Microservices envy | Split without scale need |
| Shared DB coupling | Integration via one database |

---

## YAGNI Principle

Prefer the **simplest architecture** that meets NFRs. Document rejected alternatives for future ADRs.

---

## Links

- [C4 Model](https://c4model.com/)
- [Architecture Decision Records](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions) (Michael Nygard)

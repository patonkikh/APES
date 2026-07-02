# ADR Format — Reference

Reference for Architecture Decision Records per [Michael Nygard](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions). Use with `adr-generator` skill.

---

## When to Write an ADR

| Write ADR | Skip ADR |
|-----------|----------|
| Significant technology choice | Reversible trivial choice |
| Cross-team impact | Team-local lint rule |
| Hard to reverse | Config default |
| Security/compliance implication | — |

---

## Nygard Template

```markdown
# ADR-NNN: [Title]

**Status:** Proposed | Accepted | Deprecated | Superseded
**Date:** YYYY-MM-DD
**Deciders:** [names/roles]

## Context
[Forces, constraints, why decision needed now]

## Decision
[What we will do and why]

## Consequences
### Positive
- ...

### Negative
- ...

### Neutral
- ...
```

---

## Status Definitions

| Status | Meaning |
|--------|---------|
| Proposed | Under discussion |
| Accepted | Approved for implementation |
| Deprecated | No longer recommended |
| Superseded | Replaced by another ADR (link it) |

---

## Options Section (APES extension)

Before Decision, document ≥2 options:

| Option | Pros | Cons |
|--------|------|------|
| Option A | | |
| Option B | | |
| Do nothing | | |

---

## Numbering & Location

```text
docs/adr/
├── 0001-async-job-processing.md
├── 0002-vector-store-selection.md
└── README.md   # index of ADRs
```

Use sequential numbers. Never reuse numbers.

---

## Linking ADRs

```markdown
**Supersedes:** ADR-0003
**Related:** ADR-0001, ADR-0007
```

When superseding, update prior ADR status to `Superseded`.

---

## Good vs Poor Titles

| Poor | Good |
|------|------|
| Database decision | Use PostgreSQL for user and token storage |
| Cloud | Deploy API on AWS ECS Fargate |
| Caching | Add Redis for session and rate-limit counters |

---

## Review Triggers

Revisit ADR when:

- Assumptions change (scale 10x, new compliance)
- Option rejected becomes viable
- Consequences prove worse than expected

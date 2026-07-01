# Architecture Skills Chain — Stage 2

**Последнее обновление:** 2026-07-01  
**Статус:** Reviewed — chain consistent

## Bridge from Product

```text
product/prd-generator → architecture/solution-architecture
```

## Primary pipeline

```text
solution-architecture
  → system-context-builder
  → container-diagram-builder
  → adr-generator
  → architecture-review
```

## Default next step per Skill

| Skill | Default next (primary path) |
|-------|----------------------------|
| solution-architecture | system-context-builder |
| system-context-builder | container-diagram-builder |
| container-diagram-builder | adr-generator |
| adr-generator | architecture-review |
| architecture-review | solution-architecture (revision loop) |

## Full product-to-architecture flow

```text
[Product chain ends at prd-generator or story-mapping]
  → solution-architecture
  → system-context-builder
  → container-diagram-builder
  → adr-generator
  → architecture-review
```

## Review checklist (2026-07-01)

- [x] All 5 Architecture Skills have 8 required sections
- [x] No Role Play / "You are..." in any skill.md
- [x] C4 levels respected (L1 context, L2 container — no L3 in context skill)
- [x] prd-generator links to solution-architecture in Next Skills
- [x] README.md present for each skill

## Feedback loops

- architecture-review → solution-architecture (fix gaps)
- architecture-review → adr-generator (document new decisions)
- adr-generator → container-diagram-builder (update diagrams after decision)

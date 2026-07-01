# Product Skills Chain — Stage 1

**Последнее обновление:** 2026-07-01  
**Статус:** Reviewed — chain consistent

## Primary pipeline

```text
idea-validator
  → problem-statement-builder
  → persona-generator
  → product-vision-builder
  → feature-prioritization
  → prd-generator
  → epic-generator
  → user-story-generator
  → acceptance-criteria-generator
  → story-mapping
```

## Default next step per Skill

| Skill | Default next (primary path) |
|-------|----------------------------|
| idea-validator | problem-statement-builder (on Go/Pivot) |
| problem-statement-builder | persona-generator |
| persona-generator | product-vision-builder |
| product-vision-builder | feature-prioritization |
| feature-prioritization | prd-generator |
| prd-generator | epic-generator |
| epic-generator | user-story-generator |
| user-story-generator | acceptance-criteria-generator |
| acceptance-criteria-generator | story-mapping |
| story-mapping | user-story-generator (fill gaps) |

## Review checklist (2026-07-01)

- [x] All 10 Skills have 8 required sections
- [x] No Role Play / "You are..." in any skill.md
- [x] Primary chain links are bidirectionally consistent
- [x] Each skill.md is 130–180 lines (within 150–300 target)
- [x] README.md present for each skill

## Feedback loops

- story-mapping → user-story-generator (gap filling)
- story-mapping → feature-prioritization (re-prioritize releases)
- idea-validator → persona-generator (skip problem statement when user understanding needed first)

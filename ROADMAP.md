# Roadmap — APES

**Источник:** [task.md](task.md) §14  
**Последнее обновление:** 2026-07-01  
**Текущий этап:** Этап 3 — Scale (Этап 2 завершён: 50 Skills)

---

## Этап 1 — Foundation (завершён)

**Цель:** архитектура платформы, стандарты Skills, публикация первых 10 Skills. **Статус: done (2026-07-01)**

| Задача | Статус |
|--------|--------|
| Инфраструктура репозитория (git, README, AGENTS) | done |
| ROADMAP, TODO, CHANGELOG | done |
| docs/ARCHITECTURE.md | done |
| docs/SKILL_STANDARD.md | done |
| docs/adr/0001-skill-file-format.md | done |
| skills/_template/ | done |
| Product Skill: idea-validator | done |
| Product Skill: problem-statement-builder | done |
| Product Skill: persona-generator | done |
| Product Skill: product-vision-builder | done |
| Product Skill: feature-prioritization | done |
| Product Skill: prd-generator | done |
| Product Skill: epic-generator | done |
| Product Skill: user-story-generator | done |
| Product Skill: acceptance-criteria-generator | done |
| Product Skill: story-mapping | done |
| Ревью цепочки Next Skills | done |

### Цепочка Skills (Этап 1)

```text
idea-validator → problem-statement-builder → persona-generator
  → product-vision-builder → feature-prioritization → prd-generator
  → epic-generator → user-story-generator → acceptance-criteria-generator
  → story-mapping
```

---

## Этап 2 — Growth (завершён)

**Статус: done (2026-07-01)** — 50 Skills опубликованы в репозитории.

| Категория | Skills | Статус |
|-----------|--------|--------|
| product | 15 | done |
| architecture | 10 | done |
| ai | 10 | done |
| rag | 5 | done |
| security | 5 | done |
| mcp | 5 | done |
| LICENSE, CI, catalog | — | done |
| Публикация в каталогах | — | pending |

См. [catalog.json](catalog.json), [docs/PUBLISHING.md](docs/PUBLISHING.md).

## Этап 3 — Scale (текущий)
- Публикация в основных каталогах Skills
- Сбор обратной связи
- Добавление категорий: Architecture, AI Engineering

## Этап 3 — Scale

- Расширение до 100 Skills
- Покрытие основных инженерных направлений (RAG, Security, MCP)
- Единый стандарт Engineering Playbooks

## Этап 4 — Ecosystem

- Более 250 Skills
- Отраслевые библиотеки
- Локализация
- Автоматическая генерация новых Skills на основе шаблона

---

## Критерии успеха (из task.md §15)

- [ ] ≥100 профессиональных Skills
- [ ] Единый стандарт Engineering Playbook
- [ ] Совместимость с основными агентными IDE без модификации
- [ ] Покрытие полного жизненного цикла разработки ПО
- [ ] Качество выше типовых промптов за счёт методологий и валидации

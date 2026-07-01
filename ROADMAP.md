# Roadmap — APES

**Источник:** [task.md](task.md) §14  
**Последнее обновление:** 2026-07-01  
**Текущий этап:** Этап 1 — архитектура, стандарты, первые 10 Product Skills

---

## Этап 1 — Foundation (текущий)

**Цель:** архитектура платформы, стандарты Skills, публикация первых 10 Skills.

| Задача | Статус |
|--------|--------|
| Инфраструктура репозитория (git, README, AGENTS) | done |
| ROADMAP, TODO, CHANGELOG | done |
| docs/ARCHITECTURE.md | done |
| docs/SKILL_STANDARD.md | done |
| docs/adr/0001-skill-file-format.md | done |
| skills/_template/ | done |
| Product Skill: idea-validator | in progress |
| Product Skill: problem-statement-builder | done |
| Product Skill: persona-generator | done |
| Product Skill: product-vision-builder | done |
| Product Skill: feature-prioritization | done |
| Product Skill: prd-generator | done |
| Product Skill: epic-generator | done |
| Product Skill: user-story-generator | done |
| Product Skill: acceptance-criteria-generator | pending |
| Product Skill: story-mapping | pending |
| Ревью цепочки Next Skills | pending |

### Цепочка Skills (Этап 1)

```text
idea-validator → problem-statement-builder → persona-generator
  → product-vision-builder → feature-prioritization → prd-generator
  → epic-generator → user-story-generator → acceptance-criteria-generator
  → story-mapping
```

---

## Этап 2 — Growth

- Расширение библиотеки до 50 Skills
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

# APES — инструкция для AI-агента разработки

Краткая точка входа. Источник требований: [task.md](task.md).

## Что это

**AI Product Engineering Skills Platform (APES)** — открытая библиотека Engineering Playbooks для AI-агентов. Каждый Skill — один файл `skill.md`, описывающий методологию выполнения одной инженерной задачи.

## Обязательный порядок работы (каждая сессия)

1. Прочитать `AGENTS.md` (этот файл).
2. Прочитать [ROADMAP.md](ROADMAP.md) — текущий этап и следующий шаг.
3. Прочитать [TODO.md](TODO.md) — активные задачи.
4. Прочитать [CHANGELOG.md](CHANGELOG.md) — последние изменения.
5. Изучить [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) и [docs/SKILL_STANDARD.md](docs/SKILL_STANDARD.md).
6. При изменении требований — перечитать [task.md](task.md).
7. Выполнить задачу.
8. Обновить ROADMAP, TODO, CHANGELOG в **том же коммите**.
9. Сделать **отдельный git-коммит** с осмысленным сообщением.

## Перед началом задачи

1. Определить текущее состояние проекта по ROADMAP и TODO.
2. Составить краткий план реализации.
3. Перечислить изменяемые файлы.
4. Оценить влияние на существующие Skills и цепочку Next Skills.

## Во время разработки

- Вносить минимально необходимые изменения.
- Соблюдать [SKILL_STANDARD.md](docs/SKILL_STANDARD.md).
- Использовать [skills/_template/skill.md](skills/_template/skill.md) как эталон.
- **Запрещено:** Role Play, "You are...", вымышленные роли, платформозависимый синтаксис в skill.md.
- Не создавать дублирование.
- Не нарушать совместимость ранее опубликованных Skills.

## После завершения задачи

- Обновить `README.md` при изменении публичного API или структуры.
- Обновить `ROADMAP.md` — статус этапа/задачи, дата.
- Обновить `TODO.md` — чекбоксы, дата.
- Добавить запись в `CHANGELOG.md`.
- Актуализировать `docs/` при изменении стандартов или архитектуры.
- Проверить связанные Skills на согласованность секции Next Skills.

При изменении архитектуры — обновить `docs/ARCHITECTURE.md` и добавить ADR в `docs/adr/`.

**Документация — часть продукта.** Задача без обновления ROADMAP/TODO/CHANGELOG считается незавершённой.

## Правило коммитов

- **Один логический шаг = один коммит.**
- Формат: `тип(scope): описание`
  - `feat(product): add prd-generator skill`
  - `docs: add skill engineering standard`
  - `chore: fix task.md markdown formatting`
- Обновление ROADMAP/TODO/CHANGELOG включается в тот же коммит, что и результат работы.
- Не коммитить секреты (`.env`, ключи, credentials).

## Разработка нового Skill

1. Скопировать структуру из `skills/_template/skill.md`.
2. Заполнить все 8 секций: Purpose, Workflow, Decision Rules, Validation, Anti-patterns, Best Practices, Output Structure, Next Skills.
3. Добавить `README.md` в каталог skill (примеры, changelog skill).
4. Пройти чеклист SKILL_STANDARD.
5. Согласовать Next Skills с соседними Skills в цепочке.
6. Коммит: `feat(<category>): add <skill-name> skill`.

## Приоритет разработки категорий

1. Product
2. Architecture
3. AI
4. RAG
5. AI Security
6. MCP
7. Jira
8. Enterprise
9. Startup
10. GitHub

## Журнал коммитов

| Дата | Коммит | Описание |
|------|--------|----------|
| 2026-07-01 | 891060a | chore: fix task.md markdown formatting |
| 2026-07-01 | c6d5fea | chore: init repository with gitignore |
| 2026-07-01 | 793d84b | docs: add project README |
| 2026-07-01 | 076fb34 | docs: add agent instructions |
| 2026-07-01 | dddab80 | docs: add roadmap and todo tracker |
| 2026-07-01 | 9847c90 | docs: add changelog |
| 2026-07-01 | 256a12d | docs: add platform architecture |
| 2026-07-01 | 3054ab6 | docs: add skill engineering standard |
| 2026-07-01 | b8f58df | docs(adr): adopt lowercase skill.md format |
| 2026-07-01 | 8bc9fd2 | feat: add skill template |
| 2026-07-01 | a3555ff | chore: add MIT license |
| 2026-07-01 | af793f9–50fc6f9 | feat(architecture): add 5 Architecture Skills |
| 2026-07-01 | — | docs: update stage 2 architecture chain |

Обновлять эту таблицу после каждого коммита.

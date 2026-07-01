# Contributing to APES

Спасибо за интерес к **AI Product Engineering Skills Platform**!

## Быстрый старт

1. Форкните [patonkikh/APES](https://github.com/patonkikh/APES)
2. Создайте ветку: `git checkout -b feat/product/my-skill`
3. Скопируйте шаблон: `skills/_template/skill.md` → `skills/<category>/<name>/skill.md`
4. Заполните все 8 секций по [docs/SKILL_STANDARD.md](docs/SKILL_STANDARD.md)
5. Добавьте `README.md` с примером использования
6. Проверьте:

```bash
python scripts/validate_skills.py
python scripts/generate_catalog.py
```

7. Коммит: `feat(category): add my-skill skill`
8. Откройте Pull Request

## Правила

- **Один Skill = одна задача** — без Role Play и «You are...»
- **Один skill = один коммит** (рекомендуется)
- Обновляйте `CHANGELOG.md` для значимых изменений
- `skill.md` — единственный файл для установки пользователем
- Детали и примеры — в `README.md` skill (только в репозитории)

## Категории (приоритет из task.md)

`product` → `architecture` → `ai` → `rag` → `security` → `mcp` → `jira` → `enterprise` → `startup` → `github`

## Code of Conduct

Будьте конструктивны в ревью. Фокус на качестве методологии, не на объёме текста.

## Вопросы

Откройте [Issue](https://github.com/patonkikh/APES/issues) с меткой `question`.

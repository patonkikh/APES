# GitHub Setup — APES

Репозиторий: **https://github.com/patonkikh/APES**

## Что уже сделано локально

- [x] Remote `origin` → `https://github.com/patonkikh/APES.git`
- [x] Ветка `main` (все коммиты)
- [x] CI: `.github/workflows/validate.yml`
- [x] CONTRIBUTING.md, Issue template
- [x] README с badges и структурой
- [x] Расширенный `.gitignore`

## Первый push (один раз)

### Вариант A — GitHub CLI (рекомендуется)

```bash
# Установите GitHub CLI: https://cli.github.com/
gh auth login
cd APES
git push -u origin main
```

### Вариант B — Personal Access Token

1. GitHub → Settings → Developer settings → Personal access tokens
2. Создайте token с scope `repo`
3. Push:

```bash
cd APES
git push -u origin main
# Username: patonkikh
# Password: <вставьте token>
```

### Вариант C — SSH

```bash
git remote set-url origin git@github.com:patonkikh/APES.git
git push -u origin main
```

## Настройки репозитория на GitHub (вручную)

После push откройте **Settings** репозитория:

| Поле | Значение |
|------|----------|
| Description | Open library of 50 Engineering Playbooks for AI agents — workflows, not role prompts |
| Website | (опционально) |
| Topics | `cursor`, `ai-agents`, `prompt-engineering`, `skills`, `llm`, `product-management`, `architecture`, `rag`, `mcp` |
| Default branch | `main` |

### About / Social preview

- **Releases:** создайте Release `v0.5.0` с notes из CHANGELOG.md
- **Pin README** — отображается автоматически

## CI

После push workflow **Validate Skills** запустится на каждый push/PR.

Проверка локально:

```bash
python scripts/validate_skills.py
python scripts/generate_catalog.py
```

## Что игнорируется Git (`.gitignore`)

- `.cursor/`, `*.plan.md`, `agent-transcripts/` — локальные файлы Cursor
- `.env`, ключи, credentials
- `__pycache__/`, `.venv/` — Python
- `.vscode/`, `.idea/` — IDE
- OneDrive/Windows temp файлы
- `node_modules/`, логи, архивы

Файлы проекта **в репозитории**: `skills/`, `docs/`, `scripts/`, `catalog.json`, `AGENTS.md`, `ROADMAP.md`, `task.md`.

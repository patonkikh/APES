# Contributing to APES

Thank you for helping grow the **AI Product Engineering Skills** ecosystem.

## What we accept

- New **compatible Skills** in existing categories
- Improvements to existing `skill.md` files
- `examples.md` and `references.md` for existing skills
- Fixes to documentation and the skill template

Open an [Issue](https://github.com/patonkikh/APES/issues) first if you plan a **new category** or a skill that does not fit the [Engineering Playbook](docs/SKILL_STANDARD.md) model.

---

## Quick start

```bash
git clone https://github.com/patonkikh/APES.git
cd APES
git checkout -b feat/product/my-skill

# 1. Copy the template
mkdir -p skills/product/my-skill
cp skills/_template/skill.md skills/product/my-skill/skill.md
cp skills/_template/README.md skills/product/my-skill/README.md
cp skills/_template/examples.md skills/product/my-skill/examples.md

# 2. Edit skill.md — follow docs/CREATE_SKILL.md

# 3. Validate (optional, requires Python 3.10+)
python scripts/validate_skills.py

# 4. Commit and push
git add skills/product/my-skill/
git commit -m "feat(product): add my-skill skill"
git push origin feat/product/my-skill
```

Open a Pull Request on GitHub. Maintainers will review and update `catalog.json`.

---

## Documentation

| Document | Purpose |
|----------|---------|
| [How to create a new Skill](docs/CREATE_SKILL.md) | Step-by-step authoring guide |
| [Skill Standard](docs/SKILL_STANDARD.md) | Format rules and checklist |
| [Skill Template](skills/_template/skill.md) | Copy-paste starting point |

---

## Skill rules (summary)

| Rule | Detail |
|------|--------|
| One task | Single engineering outcome per skill |
| No role play | Never use *"You are a senior…"* |
| 8 sections | Purpose → Workflow → Decision Rules → Validation → Anti-patterns → Best Practices → Output Structure → Next Skills |
| Frontmatter | `name`, `description`, `metadata.apes-version`, `metadata.category` |
| Naming | Directory and `name` in kebab-case: `my-skill-name` |
| Category | `product` · `architecture` · `ai` · `rag` · `security` · `mcp` · `data` · `devops` · `growth` |

Full details: [docs/SKILL_STANDARD.md](docs/SKILL_STANDARD.md)

---

## Pull request checklist

- [ ] `skill.md` passes `python scripts/validate_skills.py`
- [ ] `name` in frontmatter matches folder name
- [ ] `description` includes **what** the skill does and **when** to use it
- [ ] `README.md` added with a one-line description and example prompt
- [ ] `examples.md` added with at least one worked input/output (recommended)
- [ ] No Role Play / no secrets / English only
- [ ] `Next Skills` links use format `category/skill-name`

---

## Commit message format

```text
feat(category): add skill-name skill
fix(category): improve skill-name validation rules
docs: update CREATE_SKILL guide
```

---

## Code of conduct

Be constructive. Review focus: methodology quality, clarity, and compatibility — not text volume.

## Questions

Open a [GitHub Issue](https://github.com/patonkikh/APES/issues) with the `question` label.

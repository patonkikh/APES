# Skill Template

**Do not install this folder.** Copy files into `skills/<category>/<your-skill>/` and customize.

## Copy command

```bash
mkdir -p skills/<category>/<skill-name>
cp skills/_template/skill.md skills/<category>/<skill-name>/skill.md
cp skills/_template/README.md skills/<category>/<skill-name>/README.md
cp skills/_template/examples.md skills/<category>/<skill-name>/examples.md
```

## After copying

1. Replace `skill-name` in frontmatter with your folder name  
2. Set `metadata.category` to your category  
3. Fill all 8 sections — see [docs/CREATE_SKILL.md](../../docs/CREATE_SKILL.md)  
4. Run `python scripts/validate_skills.py`

## Reference skills

| Quality bar | Example |
|-------------|---------|
| Product | [prd-generator](../product/prd-generator/skill.md) |
| Architecture | [solution-architecture](../architecture/solution-architecture/skill.md) |
| AI | [prompt-engineer](../ai/prompt-engineer/skill.md) |
| Security | [owasp-llm-reviewer](../security/owasp-llm-reviewer/skill.md) |

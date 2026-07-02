---
name: prompt-engineer
description: >
  Design production-grade prompts: system instructions, task templates, variable slots, few-shot examples, and output format contracts. Use when working on designing prompts, system instructions, few-shot templates.
metadata:
  apes-version: "1.1"
  category: ai
---

# Prompt Engineer

# Purpose

Design production-grade prompts: system instructions, task templates, variable slots, few-shot examples, and output format contracts.

**Input:** Task definition, AI architecture (optional), example inputs/outputs (optional), constraints  
**Output:** Prompt specification with template, variables, examples, and test cases  
**References:** See [references.md](references.md) for domain cheat sheets.
**Examples:** See [examples.md](examples.md) for worked input/output.

---

# Workflow

## Step 1: Define prompt objective

Specify:

- Single task the prompt performs (one objective per prompt)
- Success criteria (what good output looks like)
- Failure modes to prevent

## Step 2: Structure the prompt

Use layered structure:

1. **Objective** — what to accomplish
2. **Context** — background information slots
3. **Instructions** — step-by-step task rules
4. **Constraints** — what not to do
5. **Output format** — exact structure expected
6. **Examples** — few-shot demonstrations (2–3)

## Step 3: Define variables

| Variable | Type | Required | Description |
|----------|------|----------|-------------|

Use `{{variable_name}}` placeholders. Document validation rules.

## Step 4: Write output format contract

Specify exact output structure:

- JSON schema description, or
- Markdown sections, or
- Structured text pattern

Include handling for edge cases (empty input, ambiguous input).

## Step 5: Create test cases

| ID | Input | Expected behavior | Pass criteria |
|----|-------|-------------------|---------------|

Minimum 5 test cases: happy path, edge cases, adversarial input.

## Step 6: Validate

Run Validation checklist.

---

# Decision Rules

| Condition | Action |
|-----------|--------|
| Multiple unrelated tasks in one prompt | Split into separate prompts |
| No output format specified | Define strict format before delivery |
| Task requires external data not in variables | Add variable or recommend RAG/tool integration |
| Prompt exceeds ~2000 tokens template | Modularize; use context-engineering skill |
| Customer-facing without refusal behavior | Add constraint block for out-of-scope requests |

---

# Validation

- [ ] Single clear objective stated
- [ ] All 6 prompt layers present
- [ ] Variables documented with types and validation
- [ ] Output format contract is unambiguous
- [ ] ≥2 few-shot examples included
- [ ] ≥5 test cases with pass criteria
- [ ] No Role Play or persona assignment phrasing
- [ ] Refusal/out-of-scope handling for user-facing prompts

---

# Anti-patterns

- **Mega-prompt** — everything in one undifferentiated block.
- **Vague instructions** — "be helpful", "be accurate" without specifics.
- **No output format** — free-form when structure is needed.
- **Missing negative constraints** — not saying what to avoid.
- **Example pollution** — examples that contradict instructions.

---

# Best Practices

- Put instructions after context (recency bias).
- Use delimiters for variable content (`---`, XML tags).
- Test with edge cases before production.
- Version prompts with changelog.
- Pair with prompt-reviewer before deployment.

---

# Output Structure

```markdown
# Prompt Specification: [Prompt Name]
**Version:** 1.0

## Objective
[Single task description]

## Template
```
[Full prompt with {{variables}}]
```

## Variables
| Name | Type | Required | Validation |
|------|------|----------|------------|

## Output Format
[Exact structure]

## Examples
### Example 1
**Input:** ...
**Output:** ...

## Test Cases
| ID | Input | Pass criteria |
|----|-------|---------------|

## Changelog
| Version | Change |
|---------|--------|
```

---

# Next Skills

| Outcome | Recommended Skill |
|---------|-------------------|
| Review prompt quality | `ai/prompt-reviewer` |
| Optimize token usage | `ai/prompt-optimizer` |
| Manage context budget | `ai/context-engineering` |
| AI architecture context | `ai/ai-solution-architect` |

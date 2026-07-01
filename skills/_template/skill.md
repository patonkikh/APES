# [Skill Name]

# Purpose

[One sentence: what engineering task this Skill completes and what artifact it produces.]

**Input:** [Required inputs from user or prior Skills]  
**Output:** [Named artifact, e.g. "Validated Problem Statement document"]

---

# Workflow

## Step 1: Gather inputs

Collect the following from the user or context:

- [Input 1]
- [Input 2]
- [Input 3]

If any required input is missing, stop and request it explicitly. Do not assume values.

## Step 2: Analyze

[Describe analysis actions: map assumptions, identify gaps, compare alternatives.]

## Step 3: Apply methodology

[Apply the named methodology: e.g. JTBD framing, RICE scoring, INVEST criteria.]

## Step 4: Draft output

Produce the result using the Output Structure below.

## Step 5: Validate

Run the Validation checklist. Fix all failures before presenting the final result.

## Step 6: Recommend next steps

Suggest Skills from the Next Skills section based on the current outcome.

---

# Decision Rules

| Condition | Action |
|-----------|--------|
| Required input is missing | Stop; list missing items; ask user |
| Input contains contradictions | Surface contradictions; ask user to resolve before proceeding |
| Multiple valid approaches exist | Present options with trade-offs; ask user to choose |
| Result fails Validation | Revise and re-validate; do not deliver incomplete output |
| Scope exceeds single task | Split into parts; complete only this Skill's scope |

---

# Validation

Before delivering the result, verify:

- [ ] All required inputs were explicitly provided or confirmed
- [ ] Output follows the Output Structure completely
- [ ] No contradictions remain unresolved
- [ ] No ambiguous terms without definition
- [ ] Result is actionable without additional unstated assumptions
- [ ] [Skill-specific criterion 1]
- [ ] [Skill-specific criterion 2]

---

# Anti-patterns

- **Assuming unstated context** — inventing user goals, market data, or constraints not provided.
- **Role-play filler** — generic advice not tied to the methodology.
- **Scope creep** — implementing tasks that belong to Next Skills (e.g. writing a full PRD when only problem statement is requested).
- **Vague output** — labels without measurable criteria ("improve UX", "increase engagement").
- **Skipping validation** — delivering draft without running the checklist.

---

# Best Practices

- State assumptions explicitly in a dedicated section when user confirms them.
- Use concrete examples from the user's domain, not generic placeholders.
- Prefer tables and structured lists over prose paragraphs.
- Reference the methodology by name and apply it consistently.
- Flag risks and open questions in a separate section rather than hiding them.

---

# Output Structure

```markdown
# [Artifact Title]

## Context
- **Source inputs:** [list]
- **Assumptions:** [list or "none"]

## [Main Section 1]
[Content]

## [Main Section 2]
[Content]

## Open Questions
- [ ] [Question requiring user input]

## Risks
| Risk | Impact | Mitigation |
|------|--------|------------|
| ... | ... | ... |
```

---

# Next Skills

| Outcome | Recommended Skill |
|---------|-------------------|
| [Condition A] | `[category]/[skill-name]` |
| [Condition B] | `[category]/[skill-name]` |
| Default next step | `[category]/[skill-name]` |

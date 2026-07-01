# Prompt Reviewer

# Purpose

Review prompts against quality, safety, and reliability criteria; produce findings with severity and fix recommendations.

**Input:** Prompt specification or raw prompt text, use case context, risk level  
**Output:** Prompt Review Report with scored dimensions, findings, and revised sections

---

# Workflow

## Step 1: Establish review context

Confirm:

- Prompt purpose and use case
- Risk level (internal / customer-facing / regulated)
- Model target (if known)
- Expected output format

## Step 2: Score review dimensions

| Dimension | Score (1-5) | Notes |
|-----------|-------------|-------|
| Clarity | | Instructions unambiguous |
| Completeness | | All needed context and rules |
| Output contract | | Format enforceable |
| Safety | | Injection resistance, refusal behavior |
| Efficiency | | Token usage reasonable |
| Testability | | Can verify output programmatically |
| Maintainability | | Variables, versioning, modularity |

## Step 3: Run safety checklist

- [ ] Input delimiter boundaries defined
- [ ] Instruction/data separation clear
- [ ] Out-of-scope refusal behavior
- [ ] No secrets or credentials in template
- [ ] PII handling rules if applicable
- [ ] Jailbreak resistance for customer-facing

## Step 4: Document findings

| ID | Severity | Category | Finding | Fix |
|----|----------|----------|---------|-----|

Severity: Critical | High | Medium | Low

## Step 5: Provide revised sections

For Critical/High findings, rewrite affected prompt sections.

## Step 6: Validate

Run Validation checklist.

---

# Decision Rules

| Condition | Action |
|-----------|--------|
| Customer-facing with no refusal rules | Critical finding; block deploy |
| Instructions contradict examples | High finding; fix examples or instructions |
| Ambiguous output format | High finding; specify exact format |
| Role Play detected | Medium finding; rewrite to task-based instructions |
| No test cases provided | Recommend prompt-engineer test cases |

---

# Validation

- [ ] All 7 dimensions scored with notes
- [ ] Safety checklist completed
- [ ] ≥3 findings documented (or explicit "no issues" with evidence)
- [ ] Critical/High findings have fix recommendations
- [ ] Revised sections provided for Critical/High
- [ ] Overall deploy recommendation: Approve / Approve with fixes / Block
- [ ] No Role Play introduced in revisions

---

# Anti-patterns

- **Rubber stamp approval** — all 5s without analysis.
- **Style-only feedback** — word choice vs structural issues.
- **Missing safety on external prompts** — ignoring injection risks.
- **Vague fixes** — "make it clearer" without rewrite.
- **Ignoring examples** — examples that teach wrong behavior.

---

# Best Practices

- Test mentally with adversarial inputs.
- Check instruction-example consistency.
- Verify output format is parseable.
- Align safety level with use case risk.
- Reference OWASP LLM Top 1 (prompt injection) for external prompts.

---

# Output Structure

```markdown
# Prompt Review: [Prompt Name]
**Date:** YYYY-MM-DD
**Risk level:** [level]
**Recommendation:** Approve | Approve with fixes | Block

## Dimension Scores
| Dimension | Score | Notes |
|-----------|-------|-------|

## Safety Checklist
- [x] or [ ] [item]

## Findings
| ID | Severity | Finding | Fix |
|----|----------|---------|-----|

## Revised Sections
### [Section name]
[Rewritten content]

## Required Actions Before Deploy
1. [Action]
```

---

# Next Skills

| Outcome | Recommended Skill |
|---------|-------------------|
| Optimize approved prompt | `ai/prompt-optimizer` |
| Major rewrite needed | `ai/prompt-engineer` |
| Context budget issues | `ai/context-engineering` |
| AI security review | `security/prompt-injection-detector` |

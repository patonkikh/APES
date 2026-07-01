# Prompt Optimizer

# Purpose

Optimize prompts for token efficiency, latency, and output quality while preserving task behavior.

**Input:** Prompt specification (reviewed), test cases, optimization goal (cost/latency/quality)  
**Output:** Optimized prompt with change log, token comparison, and regression test plan

---

# Workflow

## Step 1: Baseline measurement

Document current prompt:

| Metric | Value |
|--------|-------|
| Template tokens (estimate) | |
| Example tokens | |
| Total typical request tokens | |
| Optimization goal | cost / latency / quality |

## Step 2: Identify optimization opportunities

Categories:

- **Redundancy** — repeated instructions
- **Verbosity** — instructions expressible more concisely
- **Example efficiency** — fewer/shorter few-shot examples
- **Structure** — reorder for model attention
- **Variable compression** — summarize context inputs

## Step 3: Apply optimizations

For each change:

| Change | Tokens saved | Quality risk | Rationale |
|--------|--------------|--------------|-----------|

Rules:

- Never remove safety constraints for token savings
- Never remove output format contract
- Preserve test case pass behavior

## Step 4: Produce optimized prompt

Deliver side-by-side or diff-style comparison:

- Original section → Optimized section
- Net token change

## Step 5: Regression test plan

Map each test case from prompt-engineer:

| Test ID | Must still pass | Risk if fails |
|---------|-----------------|---------------|

Recommend A/B test if quality risk is Medium+.

## Step 6: Validate

Run Validation checklist.

---

# Decision Rules

| Condition | Action |
|-----------|--------|
| No test cases available | Stop; request from prompt-engineer |
| Optimization breaks safety constraint | Revert change; safety > tokens |
| Quality risk High for a change | Flag; require A/B test before deploy |
| <10% token savings | Report low ROI; may not be worth complexity |
| Customer-facing prompt | Never remove refusal or delimiter rules |

---

# Validation

- [ ] Baseline token metrics documented
- [ ] ≥3 optimization changes with rationale
- [ ] Optimized prompt preserves output format contract
- [ ] Safety constraints unchanged
- [ ] Token savings quantified (before/after)
- [ ] Regression test plan covers all original test cases
- [ ] Changes with quality risk flagged
- [ ] No Role Play introduced

---

# Anti-patterns

- **Strip safety for tokens** — removing constraints to save tokens.
- **Optimize without tests** — changes without regression verification.
- **Over-compress** — ambiguous instructions that hurt quality.
- **Remove all examples** — zero-shot when few-shot was needed.
- **False precision** — exact token counts without noting estimation uncertainty.

---

# Best Practices

- Optimize iteratively; one change category at a time.
- Use shorter synonyms and bullet lists over prose.
- Move critical instructions to end of prompt (recency).
- Track prompt versions with measured metrics.
- Pair with prompt-reviewer after optimization.

---

# Output Structure

```markdown
# Prompt Optimization: [Prompt Name]

## Baseline
| Metric | Before |
|--------|--------|
| Template tokens | |
| Total typical | |

## Changes
| # | Change | Tokens saved | Risk |
|---|--------|--------------|------|

## Optimized Prompt
[Full optimized template]

## Comparison
| Metric | Before | After | Delta |
|--------|--------|-------|-------|

## Regression Tests
| Test ID | Must pass | Status |
|---------|-----------|--------|

## Recommendation
Deploy | A/B test first | Revert [change #]
```

---

# Next Skills

| Outcome | Recommended Skill |
|---------|-------------------|
| Re-review optimized prompt | `ai/prompt-reviewer` |
| Context still too large | `ai/context-engineering` |
| Quality degraded | `ai/prompt-engineer` |
| Cost at architecture level | `ai/ai-cost-optimizer` |

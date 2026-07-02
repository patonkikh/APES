# Prompt Optimizer — Worked Examples

---

## Example 1: Token reduction with regression plan

### Input

```text
Original prompt: 2,400 tokens template, 5 few-shot examples
Goal: cost reduction
Test cases: 8 from prompt-engineer
Safety: customer-facing with refusal rules
```

### Output (excerpt)

```markdown
# Prompt Optimization: Ticket Triage

## Baseline
| Metric | Before |
|--------|--------|
| Template tokens | ~2,400 |
| Typical request | ~2,650 |

## Changes
| # | Change | Tokens saved | Risk |
|---|--------|--------------|------|
| 1 | Compress priority rules to table | 180 | Low |
| 2 | Reduce few-shot 5→3 | 420 | Medium |
| 3 | Move examples after instructions | 0 | Low (quality) |

## Comparison
| Metric | Before | After | Delta |
|--------|--------|-------|-------|
| Template tokens | 2,400 | 1,800 | -25% |

## Regression Tests
| Test ID | Must pass | Notes |
|---------|-----------|-------|
| T-001–T-008 | All | Run A/B if change #2 fails any |

## Recommendation
**A/B test first** — change #2 has Medium quality risk
```

---

## Example 2: Strip safety — reject

### Input

```text
Remove refusal block to save 200 tokens
```

### Expected behavior

Reject change; document Decision Rule: safety > tokens.

---

## Example 3: No test cases

### Expected behavior

Stop; request test cases from `ai/prompt-engineer` before optimizing.

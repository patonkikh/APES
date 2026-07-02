# AI Cost Optimizer — Worked Examples

---

## Example 1: Cost breakdown and routing

### Input

```text
Monthly LLM spend: $8k
Breakdown: 70% input tokens (long system prompt + history), 25% output, 5% retries
Quality floor: faithfulness ≥0.88 on golden set
```

### Output (excerpt)

```markdown
# Cost Optimization Plan

## Baseline
| Component | Monthly | Share |
|-----------|---------|-------|
| Input context | $5,600 | 70% |
| Output | $2,000 | 25% |

## Top Levers
| Lever | Est. savings | Quality risk |
|-------|--------------|--------------|
| Prompt compression | 15% | Low |
| History summarization | 25% | Medium |
| Route simple queries to small model | 20% | Medium |

## Model Routing
Classify query complexity → small model for FAQ-like, frontier for multi-hop

## Projected Savings
Conservative: 30% ($2.4k/mo) with A/B validation on golden set
```

---

## Example 2: Blind downgrade

### Input

```text
Switch all traffic to cheapest model immediately
```

### Expected behavior

Reject without eval comparison; require quality threshold check.

---

## Example 3: No quality thresholds

### Expected behavior

Stop; request thresholds from `ai-evaluation-builder`.

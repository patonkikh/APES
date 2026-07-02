---
name: ai-cost-optimizer
description: >
  Optimize LLM inference costs: token budget allocation, model routing, caching strategy, and batching without breaching quality thresholds. Use when working on prompt engineering, AI workflows, agents, context design, or LLM optimization.
metadata:
  apes-version: "1.1"
  category: ai
---

# AI Cost Optimizer

# Purpose

Optimize LLM inference costs: token budget allocation, model routing, caching strategy, and batching without breaching quality thresholds.

**Input:** AI architecture or workflow spec, usage volume projections, quality thresholds, current cost baseline (optional)  
**Output:** Cost Optimization Plan with savings estimates, trade-off analysis, and implementation priorities
**Examples:** See [examples.md](examples.md) for worked input/output.

---

# Workflow

## Step 1: Establish cost baseline

| Component | Tokens/request (avg) | Cost/request | Monthly volume | Monthly cost |
|-----------|---------------------|--------------|----------------|--------------|
| System prompt | | | | |
| User context | | | | |
| Model output | | | | |
| Tool overhead | | | | |

Identify top 3 cost drivers by spend share.

## Step 2: Audit token usage

Analyze per stage:

- Redundant context (duplicate documents, full history)
- Over-sized system prompts
- Verbose output formats
- Unnecessary model tier for task complexity

| Finding | Est. token waste | Fix category |
|---------|------------------|--------------|

## Step 3: Evaluate optimization levers

| Lever | Savings potential | Quality risk | Effort |
|-------|-------------------|--------------|--------|
| Prompt compression | Medium | Low | Low |
| Context pruning / summarization | High | Medium | Medium |
| Model downgrade for simple tasks | High | Medium | Low |
| Semantic caching | High | Low | Medium |
| Batching (offline) | Medium | None | Low |
| Response length limits | Medium | Low | Low |
| Fine-tuning (replace long prompts) | High | Medium | High |

## Step 4: Design model routing

```text
Request → Classifier → [Simple path: small model] / [Complex path: frontier model]
```

Define routing criteria with fallback when classifier uncertain.

## Step 5: Plan caching layer

| Cache type | Key | TTL | Invalidation |
|------------|-----|-----|--------------|
| Exact match | Hash(prompt) | 24h | Prompt version change |
| Semantic | Embedding similarity | 1h | Source doc update |

Document cache hit rate target and monitoring.

## Step 6: Quantify savings and validate

Project monthly savings per lever. Confirm no quality metric drops below threshold from eval plan.

Run Validation checklist.

---

# Decision Rules

| Condition | Action |
|-----------|--------|
| No quality thresholds defined | Stop; request from ai-evaluation-builder or architect |
| Savings <5% for proposed change | Deprioritize; focus on top cost drivers |
| Model downgrade drops eval metric >2% | Reject downgrade; try prompt optimization first |
| Real-time use case | Skip batching; prioritize caching and routing |
| PII in cache keys | Use hashed keys; enforce TTL and encryption |
| Cost spike without volume change | Investigate prompt regression or model default change |

---

# Validation

- [ ] Cost baseline with per-component breakdown
- [ ] Top 3 cost drivers identified
- [ ] ≥3 optimization levers evaluated with trade-offs
- [ ] Savings projected with assumptions stated
- [ ] Quality impact assessed against eval thresholds
- [ ] Model routing criteria defined (if applicable)
- [ ] Caching strategy with invalidation rules
- [ ] Implementation priority ranked by ROI

---

# Anti-patterns

- **Blind downgrade** — switching to cheaper model without eval comparison.
- **Cache without invalidation** — serving stale answers after knowledge update.
- **Token counting ignorance** — optimizing output while input is 90% of cost.
- **Premature fine-tuning** — expensive training before prompt optimization exhausted.
- **Hidden retry costs** — aggressive retries multiplying spend silently.

---

# Best Practices

- Measure cost per successful task, not per API call.
- Track token usage by workflow stage in production.
- A/B test cost optimizations against quality metrics.
- Set budget alerts at 80% and 100% of monthly cap.
- Pair with ai-latency-optimizer when both NFRs conflict.

---

# Output Structure

```markdown
# Cost Optimization Plan: [System Name]

## Baseline
| Component | Cost/request | Monthly | Share % |
|-----------|--------------|---------|---------|

## Findings
| Issue | Waste estimate | Recommended fix |
|-------|----------------|-----------------|

## Optimization Levers
| Lever | Est. savings | Quality risk | Priority |
|-------|--------------|--------------|----------|

## Model Routing
[Classifier criteria and model mapping]

## Caching Strategy
[Type, key, TTL, invalidation]

## Projected Savings
| Scenario | Monthly cost | vs baseline |
|----------|--------------|-------------|

## Implementation Roadmap
| Phase | Changes | Expected savings |
|-------|---------|------------------|
```

---

# Next Skills

| Outcome | Recommended Skill |
|---------|-------------------|
| Optimize latency (may conflict) | `ai/ai-latency-optimizer` |
| Compress prompts | `ai/prompt-optimizer` |
| Reduce context size | `ai/context-engineering` |
| Re-validate quality post-change | `ai/ai-evaluation-builder` |
| Architecture-level redesign | `ai/ai-solution-architect` |

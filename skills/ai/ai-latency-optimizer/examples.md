# AI Latency Optimizer — Worked Examples

---

## Example 1: Pipeline profiling

### Input

```text
p95 end-to-end: 4.2s (target 3s)
Stages: retrieve 800ms, rerank 600ms, LLM 2.5s, post-process 300ms
```

### Output (excerpt)

```markdown
# Latency Optimization Plan

## Profile
| Stage | p95 | % of total |
|-------|-----|------------|
| LLM generation | 2.5s | 60% |
| Retrieval | 0.8s | 19% |
| Rerank | 0.6s | 14% |

## Optimizations
| # | Change | Latency gain | Trade-off |
|---|--------|--------------|-----------|
| 1 | Stream LLM tokens to UI | Perceived -1.5s | UX only |
| 2 | Parallel retrieve + query rewrite | -200ms | Complexity |
| 3 | Smaller reranker | -150ms | Quality test |

## Target
Projected p95: 2.8s after #1+#2+#3 — meets SLA with load test confirmation
```

---

## Example 2: Optimize without profiling

### Expected behavior

Require stage-level timing data before recommendations.

---

## Example 3: Conflict with cost optimizer

### Expected behavior

Note trade-off; recommend joint review with `ai-cost-optimizer`.

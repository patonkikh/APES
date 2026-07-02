---
name: ai-latency-optimizer
description: >
  Reduce AI inference latency: pipeline profiling, parallelization, caching, model selection, and streaming strategies to meet SLA targets. Use when working on prompt engineering, AI workflows, agents, context design, or LLM optimization.
metadata:
  apes-version: "1.1"
  category: ai
---

# AI Latency Optimizer

# Purpose

Reduce AI inference latency: pipeline profiling, parallelization, caching, model selection, and streaming strategies to meet SLA targets.

**Input:** Workflow spec or architecture, latency SLA (p50/p95), current latency baseline (optional), quality constraints  
**Output:** Latency Optimization Plan with bottleneck analysis, optimizations ranked by impact, and SLA compliance projection

---

# Workflow

## Step 1: Profile latency budget

Decompose end-to-end latency:

| Stage | p50 (ms) | p95 (ms) | % of total |
|-------|----------|----------|------------|
| Preprocessing | | | |
| Retrieval (RAG) | | | |
| LLM TTFT | | | |
| LLM generation | | | |
| Tool calls | | | |
| Postprocessing | | | |

Identify bottleneck stage (>40% of p95 or exceeding individual SLA).

## Step 2: Set SLA targets

| Metric | Target | Measurement point |
|--------|--------|-------------------|
| Time to first token (TTFT) | | Client-visible |
| End-to-end p50 | | Client-visible |
| End-to-end p95 | | Client-visible |

Distinguish streaming (TTFT matters) vs batch (total time matters).

## Step 3: Apply latency levers

| Lever | Latency impact | Quality/cost trade-off |
|-------|----------------|------------------------|
| Parallel tool/retrieval calls | High | None if independent |
| Prompt/context reduction | Medium | Possible accuracy loss |
| Faster model tier | High | Quality risk |
| Speculative decoding | Medium | Hardware dependent |
| Edge/regional deployment | Medium | Infra cost |
| Streaming response | High perceived | UX only |
| Precomputed embeddings | Medium | Storage cost |
| Connection pooling / warm instances | Medium | Infra cost |

## Step 4: Design parallel execution

For independent stages:

```text
Input → [Retrieval || Tool prefetch || Classify] → Merge → Generate
```

Document synchronization point and timeout for slowest branch.

## Step 5: Plan streaming strategy

| Content type | Stream | Buffer strategy |
|--------------|--------|-----------------|
| Long narrative | Yes | Token-by-token |
| Structured JSON | Partial | Stream after schema validation |
| Tool calls | No | Wait for complete args |

## Step 6: Validate against SLA

Project p50/p95 after optimizations. Confirm quality metrics unchanged via eval gates.

Run Validation checklist.

---

# Decision Rules

| Condition | Action |
|-----------|--------|
| SLA undefined | Stop; request p50/p95 targets |
| Single stage >60% of p95 | Optimize bottleneck first before micro-optimizations |
| Parallelization adds race conditions | Serialize conflicting stages; parallelize only independent work |
| TTFT SLA <500ms with RAG + large model | Flag as high risk; recommend caching or smaller model |
| Streaming requested for JSON API | Recommend streaming tokens to UI only; API returns complete object |
| Optimization increases cost >20% | Document trade-off; require explicit approval |

---

# Validation

- [ ] Latency profile with per-stage p50/p95
- [ ] Bottleneck stage identified
- [ ] SLA targets documented (TTFT and e2e)
- [ ] ≥3 optimizations evaluated with impact estimates
- [ ] Parallel execution plan for independent stages
- [ ] Streaming strategy defined for user-facing paths
- [ ] Projected p95 meets SLA after changes
- [ ] Quality impact assessed (no eval regression)

---

# Anti-patterns

- **Optimizing non-bottleneck** — shaving 10ms off postprocess when LLM takes 3s.
- **Cold start ignored** — measuring warm-cache latency only.
- **Sequential by default** — chaining retrieval and tools that could run in parallel.
- **Fake streaming** — buffering full response then simulating stream.
- **Latency without monitoring** — no production p95 tracking after deploy.

---

# Best Practices

- Measure client-side latency, not just server-side model time.
- Set per-stage timeouts to fail fast and degrade gracefully.
- Use regional inference endpoints close to users.
- Pre-warm models/instances before traffic spikes.
- Pair with ai-cost-optimizer when latency fixes increase spend.

---

# Output Structure

```markdown
# Latency Optimization Plan: [System Name]

## Current Profile
| Stage | p50 | p95 | % total |
|-------|-----|-----|---------|

## SLA Targets
| Metric | Target | Current | Gap |
|--------|--------|---------|-----|

## Bottleneck Analysis
[Root cause and contributing factors]

## Optimizations
| Lever | Est. p95 reduction | Trade-off | Priority |
|-------|-------------------|-----------|----------|

## Parallel Execution
[Diagram and sync points]

## Streaming Plan
[What streams, what waits]

## Projected Performance
| Metric | Before | After | Meets SLA |
|--------|--------|-------|-----------|

## Monitoring
| Metric | Source | Alert |
|--------|--------|-------|
```

---

# Next Skills

| Outcome | Recommended Skill |
|---------|-------------------|
| Re-validate quality | `ai/ai-evaluation-builder` |
| Balance cost vs latency | `ai/ai-cost-optimizer` |
| Redesign workflow structure | `ai/ai-workflow-builder` |
| Optimize context size | `ai/context-engineering` |
| Infra scaling | `architecture/scalability-advisor` |

---
name: retriever-optimizer
description: >
  Optimize RAG retrieval quality: tune top-k, reranking, query preprocessing, and filtering to maximize recall and precision. Use when working on RAG pipelines, chunking, embeddings, retrieval, or hybrid search.
metadata:
  apes-version: "1.1"
  category: rag
---

# Retriever Optimizer

# Purpose

Optimize RAG retrieval quality: tune top-k, reranking, query preprocessing, and filtering to maximize recall and precision.

**Input:** RAG architecture, golden query set (optional), current retrieval metrics  
**Output:** Retriever optimization report with parameter recommendations and A/B test plan

---

# Workflow

## Step 1: Baseline retrieval metrics

Measure on golden set:

| Metric | Current | Target |
|--------|---------|--------|
| Recall@k | | |
| Precision@k | | |
| MRR | | |
| Latency p95 | | |

## Step 2: Analyze failure modes

Categorize misses:

| Failure type | Count | Example query |
|--------------|-------|---------------|
| Wrong chunk retrieved | | |
| Right doc, wrong section | | |
| Query-document vocabulary gap | | |
| Multi-hop not supported | | |

## Step 3: Tune retrieval parameters

| Parameter | Current | Recommended | Rationale |
|-----------|---------|-------------|-----------|
| top-k initial | | | |
| top-k after rerank | | | |
| Similarity threshold | | | |
| Metadata filters | | | |

## Step 4: Recommend enhancements

Options:

- Query expansion / HyDE
- Cross-encoder reranking
- Metadata pre-filtering
- Hypothetical document embedding
- Query decomposition

Prioritize by failure mode analysis.

## Step 5: Define A/B test plan

| Variant | Change | Success metric | Sample size |
|---------|--------|----------------|-------------|

## Step 6: Validate

Run Validation checklist.

---

# Decision Rules

| Condition | Action |
|-----------|--------|
| No golden query set | Create minimum 20 Q&A pairs before tuning |
| Recall low, precision high | Increase k, add query expansion |
| Precision low, recall high | Add reranker, raise similarity threshold |
| Latency exceeds budget | Reduce k, use lighter reranker |
| Vocabulary gap failures dominate | Recommend hybrid-search-advisor |

---

# Validation

- [ ] Baseline metrics documented
- [ ] Failure modes categorized with examples
- [ ] Parameter recommendations with rationale
- [ ] Enhancements prioritized by failure type
- [ ] A/B test plan defined
- [ ] Latency impact estimated per change
- [ ] No tuning without measurable success criteria

---

# Anti-patterns

- **Random k tuning** — changing top-k without measuring.
- **Rerank everything** — expensive reranker on all queries regardless of need.
- **Ignore latency** — quality gains that break SLA.
- **Overfit golden set** — tuning to 5 queries only.
- **No baseline** — optimizing without before metrics.

---

# Best Practices

- Hold out 20% of golden set for validation.
- Tune one parameter at a time.
- Log retrieval results in production for continuous improvement.
- Pair with hybrid-search-advisor for keyword gaps.
- Re-evaluate after corpus or embedding changes.

---

# Output Structure

```markdown
# Retriever Optimization: [System Name]

## Baseline
| Metric | Value | Target |
|--------|-------|--------|

## Failure Analysis
| Type | % | Example | Fix |
|------|---|---------|-----|

## Parameter Tuning
| Param | Before | After | Impact |
|-------|--------|-------|--------|

## Recommended Enhancements
| Priority | Enhancement | Addresses |
|----------|-------------|-----------|

## A/B Test Plan
| Variant | Metric | Duration |
|---------|--------|----------|
```

---

# Next Skills

| Outcome | Recommended Skill |
|---------|-------------------|
| Add keyword retrieval | `rag/hybrid-search-advisor` |
| Fix chunking issues | `rag/chunking-strategy-advisor` |
| Change embeddings | `rag/embedding-strategy-advisor` |
| Citation validation | `rag/citation-validator` |

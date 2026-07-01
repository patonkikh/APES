# Hybrid Search Advisor

# Purpose

Design hybrid search strategy combining dense vector retrieval and sparse keyword search (BM25) with fusion ranking.

**Input:** Query patterns, retrieval failure analysis, corpus characteristics  
**Output:** Hybrid search specification with fusion method, weights, and evaluation plan

---

# Workflow

## Step 1: Assess hybrid search need

Indicators for hybrid:

- Exact match queries (IDs, codes, names)
- Technical vocabulary not in embedding training
- Low recall on keyword-specific queries in failure analysis
- Mixed query types (semantic + exact)

If none apply, document why dense-only is sufficient.

## Step 2: Design dual retrieval paths

| Path | Method | Index | Strength |
|------|--------|-------|----------|
| Dense | Vector similarity | Vector DB | Semantic |
| Sparse | BM25 / TF-IDF | Inverted index | Exact match |

## Step 3: Select fusion strategy

| Method | How | When |
|--------|-----|------|
| Reciprocal Rank Fusion (RRF) | Rank-based merge | Default, robust |
| Weighted sum | Score normalization + weights | Calibrated scores |
| Cascade | Sparse filter → dense rerank | Large corpus |
| Learned fusion | ML ranker | Sufficient training data |

Recommend with rationale.

## Step 4: Tune weights

| Query type | Dense weight | Sparse weight |
|------------|--------------|---------------|
| Semantic | 0.8 | 0.2 |
| Exact match | 0.2 | 0.8 |
| Mixed | 0.5 | 0.5 |

Define query classifier or use RRF without weights.

## Step 5: Plan evaluation

Compare on golden set:

- Dense-only vs sparse-only vs hybrid
- Metrics: recall@k, MRR, latency

## Step 6: Validate

Run Validation checklist.

---

# Decision Rules

| Condition | Action |
|-----------|--------|
| All queries semantic | Hybrid may be unnecessary; document decision |
| Exact match failures > 20% | Recommend hybrid with RRF |
| Latency budget tight | Consider cascade over parallel dual search |
| No sparse index exists | Plan BM25 index alongside vector index |
| Small corpus (<1000 chunks) | Sparse-only may suffice; compare before hybrid |

---

# Validation

- [ ] Hybrid need assessment documented
- [ ] Both retrieval paths specified
- [ ] Fusion method selected with rationale
- [ ] Weight or RRF strategy defined
- [ ] Eval plan comparing dense/sparse/hybrid
- [ ] Latency impact of dual search estimated
- [ ] Query type routing rules if applicable

---

# Anti-patterns

- **Hybrid by default** — adding BM25 without failure evidence.
- **Unnormalized fusion** — combining incomparable score scales naively.
- **Double latency** — parallel search without timeout budget.
- **Ignoring sparse maintenance** — stale keyword index.
- **Fixed weights** — same weights for all query types.

---

# Best Practices

- Start with RRF (no weight tuning needed).
- Use query classification only when eval shows benefit.
- Index same chunks in both systems with shared IDs.
- Monitor per-path contribution in production logs.
- Align with retriever-optimizer failure analysis.

---

# Output Structure

```markdown
# Hybrid Search Strategy: [System Name]

## Need Assessment
[Why hybrid or why not]

## Architecture
```mermaid
[dense + sparse + fusion diagram]
```

## Fusion
**Method:** RRF | Weighted | Cascade
**Config:** [parameters]

## Weights by Query Type
| Type | Dense | Sparse |
|------|-------|--------|

## Evaluation Plan
| Config | Recall@5 | MRR | Latency |
|--------|----------|-----|---------|

## Implementation Notes
[Index sync, shared IDs]
```

---

# Next Skills

| Outcome | Recommended Skill |
|---------|-------------------|
| Query rewriting | `rag/query-rewriter` |
| Hallucination check | `rag/hallucination-analyzer` |
| Retriever tuning | `rag/retriever-optimizer` |
| RAG evaluation | `rag/retrieval-evaluator` |

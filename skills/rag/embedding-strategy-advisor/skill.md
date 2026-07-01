# Embedding Strategy Advisor

# Purpose

Select and configure embedding models and indexing strategy for a RAG corpus based on domain, language, and quality requirements.

**Input:** Corpus description, languages, domain (general/technical/legal), budget, latency requirements  
**Output:** Embedding strategy document with model recommendation, dimension trade-offs, and index configuration

---

# Workflow

## Step 1: Profile the corpus

- Languages and multilingual needs
- Domain specificity (general, code, medical, legal)
- Corpus size (chunks count)
- Query-document similarity type (semantic, keyword-hybrid)

## Step 2: Evaluate embedding options

| Model | Dimensions | Multilingual | Domain fit | Cost |
|-------|------------|--------------|------------|------|

Compare API models (OpenAI, Cohere, Voyage) vs open-weight (BGE, E5, GTE).

## Step 3: Recommend embedding model

Selection criteria:

- Retrieval quality on domain sample (MRR, recall@k)
- Latency for query embedding
- Cost at projected volume
- Self-hosting feasibility

## Step 4: Define index configuration

- Distance metric: cosine, dot product, L2
- Index type: HNSW parameters (ef, M)
- Quantization if corpus > 1M chunks

## Step 5: Plan re-embedding strategy

When corpus or model changes:

- Version embeddings
- Batch re-embed pipeline
- Dual-index migration period

## Step 6: Validate

Run Validation checklist.

---

# Decision Rules

| Condition | Action |
|-----------|--------|
| Multilingual corpus | Require multilingual model; avoid English-only |
| Code-heavy corpus | Consider code-specific embeddings |
| Budget constrained | Recommend open-weight self-hosted with ops cost note |
| Latency < 100ms for embed | Prefer smaller dimension models |
| Domain highly specialized | Recommend fine-tuning or domain-specific model eval |

---

# Validation

- [ ] Corpus profile complete
- [ ] ≥2 embedding options compared
- [ ] Recommendation with quality/cost/latency rationale
- [ ] Index configuration specified
- [ ] Re-embedding strategy documented
- [ ] Dimension and metric choices explained
- [ ] Eval method for embedding quality stated

---

# Anti-patterns

- **Default model** — using text-embedding-3-small without domain eval.
- **Dimension mismatch** — mixing embeddings from different models in one index.
- **No re-embed plan** — model lock-in without migration path.
- **Ignoring query embedding cost** — only indexing cost considered.
- **Over-quantization** — precision loss without quality check.

---

# Best Practices

- Eval embeddings on domain-specific golden queries.
- Match embedding model to chunking strategy.
- Store model version in index metadata.
- Benchmark query latency at p95, not average.
- Align with chunking-strategy-advisor output.

---

# Output Structure

```markdown
# Embedding Strategy: [Corpus Name]

## Corpus Profile
| Attribute | Value |
|-----------|-------|

## Options Compared
| Model | Dims | Quality | Cost | Latency |
|-------|------|---------|------|---------|

## Recommendation
**Model:** [name]
**Rationale:** [why]

## Index Config
| Setting | Value |
|---------|-------|

## Re-embedding Plan
[Strategy]

## Eval Results
| Metric | Score |
|--------|-------|
```

---

# Next Skills

| Outcome | Recommended Skill |
|---------|-------------------|
| Tune retrieval | `rag/retriever-optimizer` |
| Hybrid search | `rag/hybrid-search-advisor` |
| Chunking tuning | `rag/chunking-strategy-advisor` |
| RAG architecture | `rag/rag-architecture-designer` |

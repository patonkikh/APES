# RAG Architecture Designer — Worked Examples

---

## Example 1: Internal HR policy Q&A

### Input

```text
Use case: HR policy Q&A for employees
Corpus: 200 PDF/DOCX policies on SharePoint, updated nightly
Queries: factual ("How many PTO days?"), procedural ("How to request leave?")
Latency: p95 <3s
Accuracy: citations required; hallucination rate <2% on golden set
Users: 5,000 employees, SSO
```

### Output (excerpt)

```markdown
# RAG Architecture: HR Policy Q&A

## Requirements
| Dimension | Target |
|-----------|--------|
| Corpus size | ~200 docs, ~2M tokens |
| Freshness | Nightly incremental sync |
| Retriever | Hybrid (dense + BM25) |
| Latency p95 | <3s (retrieval <500ms) |
| Citations | Required on every answer |

## Ingestion Pipeline
SharePoint connector → text extract → PII scrub → header-aware chunk (512 tok, 15% overlap)
→ embed (text-embedding-3-small) → index (pgvector + tsvector)

## Retrieval Pipeline
Query → intent classify → hybrid retrieve (top-20) → cross-encoder rerank (top-5)
→ context assembly (2,000 token budget) → generate with citation template

## Technology Stack
| Component | Choice | Rationale |
|-----------|--------|-----------|
| Vector store | PostgreSQL pgvector | Existing RDS, hybrid SQL + vector |
| Reranker | bge-reranker-base | Cost/latency balance |
| Eval | RAGAS + 50-question golden set | Block prod without pass |

## Evaluation
| Metric | Target | Method |
|--------|--------|--------|
| Faithfulness | >0.9 | RAGAS on golden set |
| Citation accuracy | 100% | Manual audit sample |
```

---

## Example 2: Small static corpus — RAG may be overkill

### Input

```text
50 pages of API docs, static, developers only, keyword search works today
```

### Expected behavior

Apply Decision Rule: corpus <100 pages, static → consider keyword search first.

```markdown
## Recommendation: Defer full RAG

For 50 static pages, start with:
1. Elasticsearch/OpenSearch keyword index
2. Measure failure queries for 2 weeks
3. Add dense retrieval only if recall gaps >15% on logged queries

If proceeding with RAG anyway, document justification in architecture.
```

---

## Example 3: No eval dataset — blocker

### Input

```text
Customer-facing legal Q&A, citations required, no golden Q&A set
```

### Expected behavior

```markdown
## Production blocker

Decision rule: no eval dataset → block production.

**Required before launch:**
- Minimum 30 golden Q&A pairs with source document references
- Offline eval pass criteria defined (faithfulness, citation match)
```

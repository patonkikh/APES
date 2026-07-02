# RAG Pipeline — Reference

Reference for retrieval-augmented generation architecture. Load with `rag-architecture-designer` and related RAG skills.

---

## Pipeline Stages

```text
INGEST:  Source → Extract → Clean → Chunk → Embed → Index
QUERY:   Query → Preprocess → Retrieve → Rerank → Assemble → Generate
```

---

## When RAG vs Alternatives

| Approach | Use when |
|----------|----------|
| Keyword search only | <100 pages, static, exact match queries |
| Dense RAG | Semantic paraphrase queries, larger corpus |
| Hybrid | Mix of exact IDs and semantic queries |
| Fine-tuning | Stable task, large labeled set, RAG insufficient |
| Long context only | Small corpus fits in context window |

---

## Chunking Defaults (starting points)

| Content | Size | Overlap |
|---------|------|---------|
| Prose/docs | 256–512 tokens | 10–20% |
| Code | Function/class level | 0% |
| FAQ rows | 1 Q&A pair | 0% |

Always tune with eval — defaults are not universal.

---

## Retrieval Stack Options

| Layer | Options |
|-------|---------|
| Sparse | BM25, Elasticsearch |
| Dense | pgvector, Pinecone, Weaviate |
| Fusion | RRF, weighted sum |
| Rerank | Cross-encoder (bge-reranker, Cohere) |

---

## Evaluation Metrics (RAGAS)

| Metric | Measures |
|--------|----------|
| Faithfulness | Answer grounded in context |
| Answer relevance | Response addresses query |
| Context precision | Retrieved chunks useful |
| Context recall | Needed info retrieved |

**Production gate:** Define thresholds on golden set before launch.

---

## Freshness Patterns

| Pattern | Freshness |
|---------|-----------|
| Full re-index | Batch nightly |
| Incremental | On document change event |
| Real-time | Stream ingest (higher complexity) |

Version indexes for rollback on bad ingests.

---

## Citation Requirements

Customer-facing RAG should require citations in generation template:

```text
Answer using only provided context. Cite sources as [doc_id:section].
If context insufficient, say "I don't have enough information."
```

---

## Common Anti-Patterns

| Name | Problem |
|------|---------|
| Chunk and pray | No chunking strategy or eval |
| RAG by default | RAG without retrieval need |
| No freshness plan | Stale index |
| Missing citations | Hallucination risk |

---

## Links

- [RAGAS documentation](https://docs.ragas.io/)
- Related APES skills: `chunking-strategy-advisor`, `hybrid-search-advisor`, `retriever-optimizer`

# RAG Architecture Designer

# Purpose

Design a Retrieval-Augmented Generation (RAG) pipeline architecture: ingestion, indexing, retrieval, generation, and evaluation components.

**Input:** Use case, document types, query patterns, quality/latency requirements  
**Output:** RAG Architecture document with pipeline diagram, component specs, and technology recommendations

---

# Workflow

## Step 1: Define RAG requirements

| Requirement | Target |
|-------------|--------|
| Query types | factual, analytical, multi-hop |
| Corpus size | documents, pages, tokens |
| Freshness | static / daily / real-time |
| Latency budget | p95 target |
| Accuracy target | citation required, acceptable hallucination rate |

## Step 2: Design ingestion pipeline

```text
Source → Extract → Clean → Chunk → Embed → Index
```

Document per stage: format handlers, metadata extraction, update frequency.

## Step 3: Design retrieval pipeline

```text
Query → Preprocess → Retrieve → Rerank → Context assembly → Generate
```

Specify retriever type: dense, sparse, hybrid.

## Step 4: Select vector store and index

| Option | Fit | Trade-off |
|--------|-----|-----------|

Consider: pgvector, Pinecone, Weaviate, OpenSearch, managed vs self-hosted.

## Step 5: Plan evaluation loop

- Offline: golden Q&A set, RAGAS metrics
- Online: user feedback, citation click-through
- Regression on corpus updates

## Step 6: Validate

Run Validation checklist.

---

# Decision Rules

| Condition | Action |
|-----------|--------|
| Corpus < 100 pages, static | Consider simple keyword search first; RAG may be overkill |
| Real-time freshness required | Plan incremental indexing pipeline |
| Multi-hop reasoning needed | Add query decomposition or agentic retrieval |
| No eval dataset | Block production; require golden set creation |
| Customer-facing without citations | Require citation in generation step |

---

# Validation

- [ ] Query types and corpus characteristics documented
- [ ] Ingestion pipeline end-to-end defined
- [ ] Retrieval pipeline with retriever type specified
- [ ] Vector store recommendation with trade-offs
- [ ] Context assembly linked to context-engineering budget
- [ ] Eval plan with offline and online metrics
- [ ] Latency budget allocated per pipeline stage
- [ ] Citation strategy defined for customer-facing use

---

# Anti-patterns

- **RAG by default** — applying RAG without retrieval need.
- **Chunk and pray** — no chunking strategy or eval.
- **Single retriever** — no hybrid when queries vary widely.
- **No freshness plan** — stale index without update pipeline.
- **Missing citations** — generated answers without source attribution.

---

# Best Practices

- Start with smallest pipeline that passes eval bar.
- Separate ingestion from query serving for independent scaling.
- Version indexes for rollback on bad ingests.
- Align with ai/context-engineering for assembly.
- Document RAG-specific ADRs.

---

# Output Structure

```markdown
# RAG Architecture: [System Name]

## Requirements
| Dimension | Target |
|-----------|--------|

## Ingestion Pipeline
[Stage descriptions]

## Retrieval Pipeline
[Stage descriptions]

## Technology Stack
| Component | Choice | Rationale |
|-----------|--------|-----------|

## Evaluation
| Metric | Target | Method |
|--------|--------|--------|

## Diagram
```mermaid
[pipeline diagram]
```
```

---

# Next Skills

| Outcome | Recommended Skill |
|---------|-------------------|
| Chunking strategy | `rag/chunking-strategy-advisor` |
| Embedding selection | `rag/embedding-strategy-advisor` |
| Optimize retrieval | `rag/retriever-optimizer` |
| Hybrid search | `rag/hybrid-search-advisor` |
| Context budget | `ai/context-engineering` |

# Chunking Strategy Advisor

# Purpose

Recommend document chunking strategy: chunk size, overlap, boundaries, and metadata preservation for optimal retrieval quality.

**Input:** Document types, sample content (optional), query patterns, RAG architecture  
**Output:** Chunking specification with parameters, boundary rules, and eval recommendations

---

# Workflow

## Step 1: Analyze document characteristics

| Doc type | Structure | Avg length | Update frequency |
|----------|-----------|------------|------------------|

Types: prose, technical docs, code, tables, FAQs, legal, chat logs.

## Step 2: Select chunking method

| Method | Best for |
|--------|----------|
| Fixed-size | Uniform prose |
| Semantic | Variable structure, paragraphs |
| Recursive | Hierarchical docs (headers) |
| Document-specific | Code (functions), tables (rows) |
| Agentic | Complex mixed content |

## Step 3: Define parameters

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| Chunk size (tokens) | | |
| Overlap (tokens) | | |
| Min chunk size | | |
| Max chunk size | | |

## Step 4: Define boundary rules

- Respect section headers / code blocks / table rows
- Do not split mid-sentence
- Preserve metadata: source, page, section title

## Step 5: Recommend eval approach

- Sample 20 chunks for manual review
- Retrieval recall@k on golden queries
- A/B chunk sizes if uncertain

## Step 6: Validate

Run Validation checklist.

---

# Decision Rules

| Condition | Action |
|-----------|--------|
| Mixed document types | Use per-type chunking strategies |
| Code documents | Chunk by function/class, not token count |
| Tables | Chunk by row groups or whole table with summary |
| Very short docs (< chunk size) | Keep whole document as one chunk |
| No sample content | Use conservative defaults; mark for eval tuning |

---

# Validation

- [ ] Document types analyzed
- [ ] Chunking method selected per type with rationale
- [ ] Size and overlap parameters specified
- [ ] Boundary rules documented
- [ ] Metadata preservation defined
- [ ] Eval approach recommended
- [ ] Parameters tied to embedding model context if known

---

# Anti-patterns

- **One size fits all** — same chunk size for code and prose.
- **Zero overlap** — losing context at boundaries.
- **Mid-sentence splits** — hurting semantic coherence.
- **No metadata** — chunks without source attribution.
- **Tiny chunks** — fragments without context.

---

# Best Practices

- Start 256–512 tokens for prose; tune with eval.
- 10–20% overlap for continuity.
- Use header-aware splitting for documentation.
- Store parent document ID and section path in metadata.
- Re-chunk when switching embedding models.

---

# Output Structure

```markdown
# Chunking Strategy: [Corpus Name]

## Document Analysis
| Type | Count | Method |
|------|-------|--------|

## Parameters
| Parameter | Value | Rationale |
|-----------|-------|-----------|

## Boundary Rules
1. [Rule]

## Metadata Schema
| Field | Source |
|-------|--------|

## Eval Plan
[Approach]

## Tuning Notes
[When to revisit]
```

---

# Next Skills

| Outcome | Recommended Skill |
|---------|-------------------|
| Select embeddings | `rag/embedding-strategy-advisor` |
| Optimize retrieval | `rag/retriever-optimizer` |
| RAG architecture | `rag/rag-architecture-designer` |
| Hybrid search | `rag/hybrid-search-advisor` |

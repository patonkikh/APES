# Retriever Optimizer — Worked Examples

---

## Example 1: Low recall diagnosis

### Input

```text
Current: dense retrieval top-10, recall@5 = 62% on golden set
Queries: mix of paraphrase and keyword-heavy
Corpus: 200k chunks, hybrid not enabled
```

### Output (excerpt)

```markdown
# Retriever Optimization: Policy RAG

## Diagnosis
| Issue | Evidence | Impact |
|-------|----------|--------|
| Keyword-heavy queries miss dense | 40% of failures are ID/acronym queries | High |
| top-10 too shallow before rerank | Relevant chunk often rank 11–15 | Medium |

## Recommendations
| # | Change | Expected recall gain | Effort |
|---|--------|---------------------|--------|
| 1 | Enable hybrid BM25+dense RRF | +15–20% | Medium |
| 2 | Increase retrieve pool 10→30 pre-rerank | +5–8% | Low |
| 3 | Add cross-encoder reranker | +8–12% | Medium |

## Eval Plan
- A/B on same 100 golden queries
- Gate: recall@5 ≥80% before prod promotion
```

---

## Example 2: Optimize without metrics

### Input

```text
Make retrieval better
```

### Expected behavior

Stop; require baseline recall@k on golden query set.

---

## Example 3: Over-tuning on train set

### Expected behavior

Hold out 20% queries for validation; warn against tuning on full golden set without split.

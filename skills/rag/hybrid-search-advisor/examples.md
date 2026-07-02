# Hybrid Search Advisor — Worked Examples

---

## Example 1: Mixed query types

### Input

```text
Queries: 40% exact policy IDs ("POL-4421"), 40% natural language, 20% acronyms/abbreviations
Corpus: 200k chunks, English only
Current: dense-only, missing exact ID lookups
```

### Output (excerpt)

```markdown
# Hybrid Search Strategy: Policy Corpus

## Query Classification
| Type | Share | Primary path |
|------|-------|--------------|
| Exact ID | 40% | BM25 boost on `policy_id` field |
| Natural language | 40% | Dense retrieval |
| Acronym | 20% | BM25 + synonym map |

## Fusion Approach
**Recommended:** Reciprocal Rank Fusion (RRF), k=60
- Dense top-30 + BM25 top-30 → fused top-20 → reranker top-5

## Weights (starting point)
| Signal | Weight | Tune via |
|--------|--------|----------|
| Dense cosine | 0.6 | Golden set grid search |
| BM25 | 0.4 | ID query recall |

## Eval
- 50 golden queries stratified by type
- Target: ID queries recall@1 = 100%, NL recall@5 > 85%
```

---

## Example 2: Dense-only sufficient

### Input

```text
50 pages narrative docs, all semantic paraphrase queries, no IDs
```

### Expected behavior

Hybrid may be overkill; recommend dense baseline + measure before adding BM25 complexity.

---

## Example 3: Missing eval

### Expected behavior

Do not set production weights without golden query set; document A/B plan.

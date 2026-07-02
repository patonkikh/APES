# Chunking Strategy Advisor — Worked Examples

---

## Example 1: Mixed corpus — per-type strategy

### Input

```text
Corpus:
- 150 HR policy PDFs (prose)
- 30 API reference Markdown files (headers, code blocks)
- 10 FAQ spreadsheets (short Q&A rows)
Embedding model: 8192 context, using 512-token chunks target
```

### Output (excerpt)

```markdown
# Chunking Strategy: HR + API Corpus

## Document Analysis
| Type | Count | Method |
|------|-------|--------|
| HR PDF prose | 150 | Recursive header-aware |
| API Markdown | 30 | Recursive by H2/H3; code blocks atomic |
| FAQ spreadsheet | 10 | Row = chunk (whole Q&A pair) |

## Parameters
| Type | Size | Overlap | Rationale |
|------|------|---------|-----------|
| Prose | 512 tokens | 15% | Standard recall |
| API docs | 384 tokens | 10% | Dense technical content |
| FAQ | full row | 0% | Already atomic |

## Boundary Rules
1. Never split inside code fences
2. Preserve `section_path` metadata: doc > H1 > H2
3. Attach page number for PDF chunks

## Eval Plan
- Sample 20 chunks per type for manual coherence review
- Recall@5 on 30 golden queries before production
```

---

## Example 2: One size fits all — rejected

### Input

```text
Use 256 tokens for everything including code and legal contracts
```

### Expected behavior

Flag anti-pattern; recommend per-type strategies; legal may need larger chunks with section summaries.

---

## Example 3: No sample content

### Expected behavior

Use conservative defaults (512/15% prose), mark all parameters as **tune in eval**, document in Tuning Notes.

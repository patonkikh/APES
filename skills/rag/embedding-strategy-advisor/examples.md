# Embedding Strategy Advisor — Worked Examples

---

## Example 1: Multilingual HR corpus

### Input

```text
Corpus: HR policies English + German, 300k chunks target
Queries: semantic paraphrase, no exact ID lookup
Latency: embedding at ingest batch nightly
Budget: minimize cost
```

### Output (excerpt)

```markdown
# Embedding Strategy: HR Policy Corpus

## Requirements
| Dimension | Need |
|-----------|------|
| Languages | EN + DE |
| Domain | HR/legal prose |
| Dimension | 768–1536 acceptable |

## Model Options
| Model | Multilingual | Cost | Recommendation |
|-------|--------------|------|----------------|
| text-embedding-3-small | Good | Low | **Start here** |
| multilingual-e5-large | Strong | Self-host cost | If DE recall gap >10% |

## Decision
Use **text-embedding-3-small** with eval on 50 DE+EN query pairs.
Re-embed full corpus if switching models (no mixed indexes).

## Eval
- Recall@5 on stratified EN/DE golden set
- Target: both languages ≥85% recall@5
```

---

## Example 2: Code + prose same model

### Input

```text
Embed Python code and markdown docs with general prose model
```

### Expected behavior

Recommend code-aware model or separate indexes per content type.

---

## Example 3: Model switch without re-embed plan

### Expected behavior

Document mandatory full re-index and versioned index rollback strategy.

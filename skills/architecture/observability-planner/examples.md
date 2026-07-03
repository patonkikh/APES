# Observability Planner — Examples

---

## Example 1: RAG API service

### Input

```text
FastAPI + OpenAI + Pinecone. SLO: p95 < 2s, 99.5% monthly.
On-call: 2 engineers. Stack: Grafana + Tempo + Prometheus.
```

### Output (excerpt)

```markdown
## Spans
rag.request → llm.chat (gen_ai.request.model) → rag.retrieve

## Alerts
| Alert | Query | Threshold |
|-------|-------|-----------|
| SLO burn | error_budget_remaining | <50% in 7d |
| Empty RAG | rag_chunks_returned == 0 | >5% 15min |
```

---

## Example 2: No SLO

### Input

```text
Add some monitoring to our agent.
```

### Expected behavior

Propose SLIs from top user journeys before signal catalog.

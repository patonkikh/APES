# RAG Skills Chain — Stage 2

**Последнее обновление:** 2026-07-01

## Primary pipeline

```text
rag-architecture-designer → chunking-strategy-advisor → embedding-strategy-advisor
  → retriever-optimizer → hybrid-search-advisor
```

## Bridge from AI

`ai/context-engineering` → `rag/rag-architecture-designer`

## Default next step

| Skill | Default next |
|-------|--------------|
| rag-architecture-designer | chunking-strategy-advisor |
| chunking-strategy-advisor | embedding-strategy-advisor |
| embedding-strategy-advisor | retriever-optimizer |
| retriever-optimizer | hybrid-search-advisor |

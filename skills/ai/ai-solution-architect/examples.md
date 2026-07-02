# AI Solution Architect — Worked Examples

---

## Example 1: Support RAG system architecture

### Input

```text
Use case: Customer support knowledge base Q&A
Volume: 10k queries/day
Latency: p95 <3s
Quality: citations required, eval harness needed
Stack preference: AWS, Python
Budget: moderate
```

### Output (excerpt)

```markdown
# AI Solution Architecture: Support RAG

## System Overview
```text
User → API Gateway → Orchestrator → [Retriever | LLM | Tools]
                              ↓
                         Vector DB + Doc Store
```

## Model Selection
| Role | Model tier | Rationale |
|------|------------|-----------|
| Generation | GPT-4 class | Quality for support tone |
| Embeddings | Small embedding model | Cost at 10k/day |
| Reranker | Cross-encoder | Precision on top-5 |

## Inference Pipeline
1. Query rewrite (optional, cached)
2. Hybrid retrieval top-20
3. Rerank to top-5
4. Context assembly (2k token budget)
5. Generate with citation template

## Evaluation Strategy
- Offline: 100 golden Q&A, RAGAS faithfulness >0.9
- Online: thumbs down rate <5%, citation click-through tracked

## Cost/Latency Trade-offs
| Lever | Savings | Quality risk |
|-------|---------|--------------|
| Cache frequent queries | 30% | Stale answers — TTL 1h |
| Smaller model for rewrite | 15% | Minor — A/B test |
```

---

## Example 2: No eval plan — stop

### Input

```text
Build chatbot for medical advice, no evaluation mentioned
```

### Expected behavior

Block architecture sign-off until eval strategy defined; escalate safety to `security/ai-threat-modeling`.

---

## Example 3: Premature fine-tuning

### Anti-pattern callout

Recommend prompt + RAG optimization before fine-tuning unless >10k labeled examples and baseline exhausted.

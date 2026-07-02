# AI Evaluation Builder — Worked Examples

---

## Example 1: RAG support bot eval harness

### Input

```text
System: Customer support RAG chatbot
Quality goals: faithfulness, citation accuracy, latency
Release gate: no regression >2% on golden set
```

### Output (excerpt)

```markdown
# AI Evaluation Plan: Support RAG Bot

## Datasets
| Dataset | Size | Purpose |
|---------|------|---------|
| Golden Q&A | 100 pairs | Offline regression |
| Adversarial | 30 prompts | Injection/safety |
| Production sample | 500/week | Online monitoring |

## Metrics
| Metric | Offline target | Online target |
|--------|----------------|---------------|
| Faithfulness (RAGAS) | ≥0.90 | ≥0.85 rolling 7d |
| Citation match | 100% on sample | ≥95% |
| p95 latency | <3s | <3.5s |

## Baselines
| Version | Faithfulness | Date |
|---------|--------------|------|
| v0.1 prompt + v1 index | 0.87 | 2026-06-15 |

## Regression Gates (CI)
- Block deploy if faithfulness drops >2% vs baseline on golden set
- Block if adversarial suite pass rate <90%

## Human Review
- Weekly 20-sample audit for tone and policy compliance
```

---

## Example 2: No baseline — stop

### Input

```text
We will know quality when users complain less
```

### Expected behavior

Define measurable metrics and baseline before production gate.

---

## Example 3: Single accuracy number

### Expected behavior

Decompose into task-specific metrics (faithfulness, relevance, latency, safety pass rate).

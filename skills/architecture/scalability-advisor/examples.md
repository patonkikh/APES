# Scalability Advisor — Worked Examples

---

## Example 1: 10x load projection

### Input

```text
Current: 50 retro jobs/hour, p95 45s
Target: 500 jobs/hour in 12 months
Bottleneck suspect: single worker pool, LLM rate limits
```

### Output (excerpt)

```markdown
# Scalability Assessment: Retro Generator

## Load Projection
| Metric | Current | Target 12mo |
|--------|---------|-------------|
| Jobs/hour | 50 | 500 |
| Peak factor | 3x | 3x |

## Bottleneck Analysis
| Component | Headroom | First limit |
|-----------|----------|-------------|
| API | High | — |
| SQS | High | — |
| Workers | Low | CPU + LLM TPM |
| LLM API | Medium | Tokens/min quota |

## Recommendations
| # | Action | When |
|---|--------|------|
| 1 | Autoscale workers on queue depth | Before 200 jobs/hr |
| 2 | Request LLM quota increase | Before 300 jobs/hr |
| 3 | Cache identical sprint summaries | Optional cost win |

## NFR Validation
p95 <60s at 500 jobs/hr — requires load test evidence
```

---

## Example 2: Scale without metrics

### Expected behavior

Request current throughput and target NFRs.

---

## Example 3: Premature microservices

### Expected behavior

Recommend scale-up/out of existing workers before service split.

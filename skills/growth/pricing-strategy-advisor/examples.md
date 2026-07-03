# Pricing Strategy Advisor — Examples

---

## Example 1: AI API product

### Input

```text
Developer API wrapping RAG over customer docs.
COGS ~$0.02/request avg. Competitors $0.03–0.08/request.
Goal: land developers, expand to teams.
```

### Output (excerpt)

```markdown
## Model recommendation
Usage-based per 1k requests + free tier with hard cap.

## Tiers
| Tier | Price | Included | Overage |
|------|-------|----------|---------|
| Free | $0 | 500 req/mo | blocked |
| Pro | $49/mo | 10k req | $4/1k |
| Scale | custom | volume | negotiated |

## Unit economics (Pro)
ARPU $49, COGS ~$20 at avg usage → gross margin ~59%.
```

---

## Example 2: Stop — no COGS data

### Input

```text
Price per token like OpenAI but cheaper.
```

### Expected behavior

Stop. Request inference cost model (tokens/request, model mix) before recommending usage pricing.

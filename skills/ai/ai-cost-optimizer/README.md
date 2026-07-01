# AI Cost Optimizer

LLM cost reduction via token audit, model routing, caching, and batching within quality thresholds.

## Chain position

`ai/ai-evaluation-builder` → **ai-cost-optimizer** → `ai/ai-latency-optimizer`

## Example use

Input: support bot spending $12k/month with 70% cost in context window.  
Output: semantic caching plan, Haiku/GPT-4o-mini routing for triage, prompt compression saving est. 40%.

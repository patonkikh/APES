# AI Latency Optimizer

Inference latency reduction via profiling, parallelization, caching, model selection, and streaming.

## Chain position

`ai/ai-cost-optimizer` → **ai-latency-optimizer** → `ai/ai-evaluation-builder`

## Example use

Input: chat app with 3s p95 SLA, current p95 at 4.2s dominated by RAG + sequential tool calls.  
Output: parallel retrieval/tool plan, streaming TTFT under 800ms, regional endpoint, projected p95 2.6s.

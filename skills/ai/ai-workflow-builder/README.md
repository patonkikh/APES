# AI Workflow Builder

Executable AI pipeline specification: stages, I/O contracts, branching, retries, and deployment model.

## Chain position

`ai/multi-agent-planner` → **ai-workflow-builder** → `ai/ai-evaluation-builder`

## Example use

Input: document processing pipeline with classify → extract → summarize stages and 3s latency budget.  
Output: stage graph with schemas, confidence-based branching, async queue deployment, and per-stage metrics.

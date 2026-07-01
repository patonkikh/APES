# AI Evaluation Builder

Offline/online eval harness: datasets, metrics, scorers, regression gates, and production monitoring.

## Chain position

`ai/ai-workflow-builder` → **ai-evaluation-builder** → `ai/ai-cost-optimizer`

## Example use

Input: RAG Q&A system with 95% accuracy target and customer-facing risk level.  
Output: golden set of 100 cases, faithfulness + answer relevance metrics, CI regression gate, and thumbs-down alerting.

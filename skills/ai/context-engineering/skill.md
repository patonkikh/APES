---
name: context-engineering
description: >
  Design context assembly strategy: what information enters the model context, in what order, with what budget, and how to handle overflow. Use when working on prompt engineering, AI workflows, agents, context design, or LLM optimization.
metadata:
  apes-version: "1.1"
  category: ai
---

# Context Engineering

# Purpose

Design context assembly strategy: what information enters the model context, in what order, with what budget, and how to handle overflow.

**Input:** AI architecture, data sources, prompt template, context window limit  
**Output:** Context Engineering specification with budget allocation, assembly pipeline, and truncation rules  
**Examples:** See [examples.md](examples.md) for worked input/output.

---

# Workflow

## Step 1: Define context budget

| Segment | Token budget | Priority |
|---------|--------------|----------|

Segments: system instructions, retrieved docs, conversation history, tool results, user query.

Total must fit within model context window minus output reserve (typically 20-30%).

## Step 2: Inventory context sources

| Source | Type | Typical size | Freshness | Required |
|--------|------|--------------|-----------|----------|

Sources: RAG chunks, user profile, session history, API tool outputs, documents.

## Step 3: Design assembly pipeline

Order of assembly (recommended):

1. System instructions (fixed)
2. Critical constraints
3. Retrieved context (ranked)
4. Recent conversation (truncated)
5. User query

Document ranking/scoring for retrieved content.

## Step 4: Define truncation strategies

| When overflow | Strategy |
|---------------|----------|
| History too long | Summarize older turns / sliding window |
| RAG too large | Re-rank and top-k truncate |
| Document too large | Chunk and select best chunks |
| Tool output large | Summarize or extract fields |

## Step 5: Plan caching opportunities

| Content | Cacheable | TTL | Savings |
|---------|-----------|-----|---------|

Static system prompts, frequent retrievals, embeddings.

## Step 6: Validate

Run Validation checklist.

---

# Decision Rules

| Condition | Action |
|-----------|--------|
| No context window limit specified | Use conservative default; state assumption |
| Required source exceeds budget alone | Recommend summarization, RAG, or larger model |
| PII in context sources | Apply redaction before assembly |
| Conflicting info across sources | Define precedence rules |
| No truncation strategy | Block; overflow will cause failures |

---

# Validation

- [ ] Token budget allocated per segment
- [ ] Budget fits within context window minus output reserve
- [ ] All context sources inventoried
- [ ] Assembly order documented
- [ ] Truncation strategy for each overflow scenario
- [ ] Ranking method for retrieved content defined
- [ ] Caching opportunities identified
- [ ] PII handling addressed if applicable

---

# Anti-patterns

- **Stuff everything** — no budget, no truncation.
- **Wrong order** — user query buried under irrelevant context.
- **Stale context** — no freshness consideration for dynamic data.
- **Duplicate content** — same info from multiple sources wasting tokens.
- **No output reserve** — using 100% context for input.

---

# Best Practices

- Reserve 20-30% of context for model output.
- Put most relevant context closest to user query.
- Use semantic ranking for RAG chunks.
- Summarize long histories rather than drop silently.
- Measure context utilization in production metrics.

---

# Output Structure

```markdown
# Context Engineering: [System Name]

## Model & Budget
- **Context window:** [tokens]
- **Output reserve:** [tokens]
- **Available input:** [tokens]

## Budget Allocation
| Segment | Budget | Priority |
|---------|--------|----------|

## Sources
| Source | Size | Freshness | Required |
|--------|------|-----------|----------|

## Assembly Pipeline
1. [Step]

## Truncation Rules
| Scenario | Strategy |
|----------|----------|

## Caching
| Content | TTL | Expected savings |
|---------|-----|------------------|

## Metrics
| Metric | Target |
|--------|--------|
| Context utilization | <80% |
| Retrieval precision | [target] |
```

---

# Next Skills

| Outcome | Recommended Skill |
|---------|-------------------|
| Design RAG pipeline | `rag/rag-architecture-designer` |
| Optimize prompts | `ai/prompt-optimizer` |
| Chunking strategy | `rag/chunking-strategy-advisor` |
| AI architecture update | `ai/ai-solution-architect` |

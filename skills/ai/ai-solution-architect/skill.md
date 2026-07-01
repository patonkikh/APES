# AI Solution Architect

# Purpose

Design an AI system architecture: model selection, inference pipeline, context management, evaluation strategy, and cost/latency trade-offs.

**Input:** Use case description, PRD/NFRs, data sources, constraints (budget, latency, privacy)  
**Output:** AI Architecture document with component diagram, model strategy, and quality gates

---

# Workflow

## Step 1: Classify the AI use case

Categorize:

| Dimension | Classification |
|-----------|----------------|
| Interaction | Batch / real-time / streaming |
| Task type | Generation / classification / retrieval / agentic |
| User-facing | Yes / internal tool |
| Risk level | Low / medium / high (customer-facing, regulated) |

## Step 2: Define quality requirements

| Metric | Target | Measurement |
|--------|--------|-------------|

Include: accuracy, latency (p50/p95), cost per request, hallucination tolerance, human-in-the-loop needs.

## Step 3: Design inference pipeline

Document stages:

```text
Input → Preprocessing → Context assembly → Model inference → Post-processing → Output
```

For each stage: technology, responsibility, failure mode.

## Step 4: Select model strategy

Compare options:

| Option | Model type | Pros | Cons | Cost estimate |
|--------|------------|------|------|---------------|

Options: frontier API, fine-tuned, open-weight self-hosted, ensemble, router.

Recommend with rationale tied to quality requirements.

## Step 5: Plan context and memory

- Context window budget allocation
- RAG vs fine-tuning vs prompt-only decision
- Session memory strategy
- Tool/MCP integration points

## Step 6: Define evaluation and guardrails

- Offline eval dataset requirements
- Online monitoring metrics
- Guardrails (input/output filters, HITL triggers)
- Rollback criteria

## Step 7: Validate

Run Validation checklist.

---

# Decision Rules

| Condition | Action |
|-----------|--------|
| Use case undefined | Stop; request problem statement or PRD |
| High-risk customer-facing without HITL | Require human-in-the-loop in architecture |
| Latency < 1s with RAG + large context | Flag latency risk; recommend caching or smaller model |
| PII in prompts | Require data minimization and redaction layer |
| No eval strategy | Block proceed; eval is mandatory for production |

---

# Validation

- [ ] Use case classified with risk level
- [ ] Quality metrics with targets defined
- [ ] Inference pipeline documented end-to-end
- [ ] ≥2 model options compared with trade-offs
- [ ] Context/memory strategy defined
- [ ] Eval plan with offline and online components
- [ ] Guardrails specified for risk level
- [ ] Cost estimate order-of-magnitude provided

---

# Anti-patterns

- **Model-first design** — choosing GPT-4 before defining requirements.
- **No eval** — shipping without measurement strategy.
- **RAG as default** — applying RAG without retrieval need analysis.
- **Ignoring cost** — architecture without cost per request estimate.
- **Unbounded context** — stuffing full documents without budget.

---

# Best Practices

- Start with simplest architecture that meets quality bar.
- Separate retrieval, reasoning, and generation stages.
- Plan for model fallback and degradation.
- Align with architecture/scalability-advisor for infra scaling.
- Document AI-specific ADRs for model and RAG decisions.

---

# Output Structure

```markdown
# AI Architecture: [System Name]

## Use Case Classification
| Dimension | Value |
|-----------|-------|

## Quality Requirements
| Metric | Target | Method |
|--------|--------|--------|

## Inference Pipeline
[Stage diagram and descriptions]

## Model Strategy
| Recommended | Rationale | Alternatives |
|-------------|-----------|--------------|

## Context & Memory
[Strategy]

## Evaluation Plan
| Type | Dataset | Metrics | Frequency |
|------|---------|---------|-----------|

## Guardrails
| Layer | Control | Trigger |
|-------|---------|---------|

## Cost Estimate
[Per-request and monthly at projected volume]

## Open Decisions
- [ ] [ADR needed]
```

---

# Next Skills

| Outcome | Recommended Skill |
|---------|-------------------|
| Design prompts | `ai/prompt-engineer` |
| Plan context strategy | `ai/context-engineering` |
| RAG architecture needed | `rag/rag-architecture-designer` |
| Review prompts | `ai/prompt-reviewer` |
| System architecture | `architecture/solution-architecture` |

# AI Evaluation Builder

# Purpose

Design an offline and online evaluation harness: datasets, metrics, baselines, regression gates, and production monitoring for AI system quality.

**Input:** AI architecture or workflow spec, quality requirements, sample inputs/outputs (optional), risk level  
**Output:** Evaluation Plan with dataset spec, metric definitions, harness design, and rollout gates

---

# Workflow

## Step 1: Define evaluation objectives

Map business requirements to measurable quality dimensions:

| Dimension | Business impact | Priority |
|-----------|-----------------|----------|
| Accuracy / correctness | User trust | High |
| Latency | UX | Medium |
| Cost | Margin | Medium |
| Safety / refusal | Compliance | High |
| Consistency | Reproducibility | Medium |

## Step 2: Design offline evaluation

### Dataset specification

| Split | Size | Source | Refresh cadence |
|-------|------|--------|-----------------|
| Golden set | 50–200 cases | Human-curated | Per release |
| Regression set | 500+ cases | Production samples | Weekly |
| Adversarial set | 20–50 cases | Red-team / edge cases | Per major change |

### Metrics

| Metric | Definition | Threshold | Aggregation |
|--------|------------|-----------|-------------|
| Exact match | Output equals reference | ≥90% | Mean |
| LLM-as-judge score | Rubric 1–5 | ≥4.0 | Mean |
| Tool call accuracy | Correct tool + args | ≥95% | Per tool |

Document human eval protocol when automated metrics are insufficient.

## Step 3: Design online evaluation

| Signal | Collection | Alert threshold |
|--------|------------|-----------------|
| User thumbs down | Feedback widget | >5% daily |
| Escalation rate | Support tickets tagged AI | >2% weekly |
| Latency p95 | APM | > SLA target |
| Cost per request | Billing API | > budget +10% |

Plan A/B or shadow deployment for model changes.

## Step 4: Build harness architecture

```text
Test cases → Runner → Model/Workflow under test → Scorers → Report → Gate
```

Components:

- **Runner** — batch and single-case execution with config versioning
- **Scorers** — deterministic + model-based + human queue
- **Reporter** — diff vs baseline, trend charts, failure clusters
- **Gate** — pass/fail criteria blocking deployment

## Step 5: Define regression gates

| Gate | Condition | Action on fail |
|------|-----------|----------------|
| Golden set | No metric drops >2% vs baseline | Block merge |
| Safety set | Zero critical failures | Block release |
| Latency | p95 within SLA | Warn or block |
| Cost | Per-request within budget | Warn |

## Step 6: Validate

Run Validation checklist.

---

# Decision Rules

| Condition | Action |
|-----------|--------|
| No quality requirements defined | Stop; request targets from ai-solution-architect output |
| High-risk use case | Require human eval on 10% of golden set minimum |
| Subjective output (creative writing) | Use rubric-based LLM-as-judge + human spot-check |
| Tool-using agent | Add tool-call accuracy and argument validation metrics |
| No production traffic yet | Offline-only harness; plan online metrics before launch |
| Metric gaming risk (LLM judge) | Calibrate judge against human labels quarterly |

---

# Validation

- [ ] Quality dimensions mapped to metrics with thresholds
- [ ] Golden, regression, and adversarial datasets specified
- [ ] Offline harness components documented
- [ ] Online monitoring signals and alert thresholds defined
- [ ] Regression gates with block/warn actions
- [ ] Baseline version identified for comparison
- [ ] Human eval protocol defined where automation insufficient
- [ ] Per-agent or per-stage eval for multi-agent workflows

---

# Anti-patterns

- **Vibe-based eval** — "looks good" without numeric thresholds.
- **Train-test leakage** — eval cases drawn from fine-tuning data.
- **Single metric obsession** — optimizing accuracy while ignoring safety or cost.
- **Stale golden set** — dataset never updated after product changes.
- **No baseline** — comparing only to previous broken version.

---

# Best Practices

- Start with 50 high-quality golden cases before scaling dataset size.
- Store eval runs with model version, prompt version, and config hash.
- Cluster failures by error type for targeted fixes.
- Run eval on every prompt or model change in CI.
- Pair with ai-cost-optimizer and ai-latency-optimizer for full NFR coverage.

---

# Output Structure

```markdown
# Evaluation Plan: [System Name]

## Objectives
| Dimension | Metric | Threshold |
|-----------|--------|-----------|

## Offline Datasets
| Split | Size | Source | Refresh |
|-------|------|--------|---------|

## Scoring Methods
| Metric | Method | Calibrated |
|--------|--------|------------|

## Harness Architecture
[Component diagram and config]

## Online Monitoring
| Signal | Source | Alert |
|--------|--------|-------|

## Regression Gates
| Gate | Criteria | Action |
|------|----------|--------|

## Baseline
[Version, scores, date established]
```

---

# Next Skills

| Outcome | Recommended Skill |
|---------|-------------------|
| Optimize cost after eval | `ai/ai-cost-optimizer` |
| Optimize latency after eval | `ai/ai-latency-optimizer` |
| Fix prompt quality issues | `ai/prompt-reviewer` |
| Review AI security risks | `ai-security/llm-threat-modeler` |
| Adjust workflow based on failures | `ai/ai-workflow-builder` |

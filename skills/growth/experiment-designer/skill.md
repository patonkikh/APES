---
name: experiment-designer
description: >
  Design a product or growth experiment: hypothesis, variants, primary metric, sample size, runtime, and guardrails. Use when planning A/B tests, feature rollouts, pricing tests, or validating GTM assumptions.
metadata:
  apes-version: "1.1"
  category: growth
---

# Experiment Designer

# Purpose

Design a rigorous product or growth experiment: clear hypothesis, variants, success metrics, statistical plan, and guardrails before running an A/B test or controlled rollout.

**Input:** Decision to make, current baseline metric, available traffic/volume, constraints (time, risk)  
**Output:** Experiment Specification with hypothesis, variant definitions, power analysis, runtime estimate, and ship criteria  
**Examples:** See [examples.md](examples.md) for worked input/output.

---

# Workflow

## Step 1: Frame the decision

| Field | Content |
|-------|---------|
| Decision | What will we do if experiment wins? |
| Non-goals | What this experiment will not prove |
| Stakeholder | Who approves ship/rollback |
| Risk tier | Low (UI copy) / Medium (pricing) / High (model change) |

If decision is undefined, stop — experiments without action thresholds waste traffic.

## Step 2: Write falsifiable hypothesis

Format:

```text
We believe [change] for [segment] will improve [metric] because [reason].
We will be wrong if [metric] moves opposite or guardrails breach.
```

Example:

```text
We believe showing AI confidence scores for [SMB users] will improve
[7-day retention] because trust increases repeat use.
```

## Step 3: Define variants

| Variant | Description | Allocation |
|---------|-------------|------------|
| Control | Current experience | 50% |
| Treatment A | Single change only | 50% |

Rules:

- **One primary change** per experiment (isolate causality)
- Document exact UI/copy/model/config diff
- For AI: version prompts and models in experiment config

Add treatment B only with enough traffic for multi-arm test.

## Step 4: Select metrics

| Type | Metric | Example |
|------|--------|---------|
| Primary | One decision metric | Activation D7, conversion to paid |
| Secondary | Supporting behavior | Time to value, feature usage |
| Guardrail | Must not harm | Error rate, latency p95, support tickets |

Primary metric must map to a tracked event in analytics plan.

If events missing, stop — run `product/analytics-instrumentation-planner` first.

## Step 5: Statistical design

| Parameter | How to set |
|-----------|------------|
| Baseline rate | Historical conversion or retention |
| MDE | Minimum detectable effect (business meaningful, e.g. +2% abs) |
| Significance | Typically 95% confidence, two-tailed |
| Power | 80% standard |
| Sample size | Calculate from baseline + MDE |

Document formula inputs; if traffic insufficient, recommend:

- Longer runtime
- Higher MDE acceptance
- Sequential test with caution
- Qualitative study instead

## Step 6: Runtime and segmentation

| Item | Spec |
|------|------|
| Duration | Days/weeks to reach sample size |
| Population | All users vs new users only |
| Exclusions | Bots, employees, free-trial edge cases |
| Randomization unit | User ID vs workspace (no mixing) |

For AI quality experiments: stratify by query type if volume allows.

## Step 7: Ship and rollback criteria

| Outcome | Action |
|---------|--------|
| Primary wins, guardrails OK | Ship to 100% |
| Inconclusive | Extend or stop; do not ship |
| Guardrail breach | Rollback immediately |
| Negative primary | Rollback; document learning |

Pre-register criteria before launch to avoid peeking bias.

## Step 8: Validate

Run Validation checklist.

---

# Decision Rules

| Condition | Action |
|-----------|--------|
| No baseline metric | Stop; collect 2 weeks baseline first |
| <1000 units expected | Warn low power; prefer qualitative |
| High-risk variant | Require feature flag + instant rollback |
| Multiple simultaneous tests | Check interaction overlap; reduce concurrent tests |
| AI model swap | Treat as high-risk; monitor quality guardrails |
| Pricing test | Legal/comms review; clear customer communication |

---

# Validation

- [ ] Decision and ship criteria stated upfront
- [ ] Falsifiable hypothesis documented
- [ ] Control and treatment defined with single primary change
- [ ] Primary, secondary, and guardrail metrics named
- [ ] Sample size or runtime estimate with MDE
- [ ] Randomization unit specified
- [ ] Rollback plan for guardrail breach
- [ ] Analytics events exist for primary metric

---

# Anti-patterns

- **HiPPO after peeking** — stopping early when results look good.
- **Multiple changes** — cannot attribute wins.
- **Vanity metrics** — clicks without retention/revenue tie.
- **No guardrails** — wins conversion, breaks latency or quality.
- **Forever test** — experiment becomes permanent split.

---

# Best Practices

- Run power calculation before engineering work.
- Log experiment ID on all exposure and outcome events.
- Archive results in experiment registry (hypothesis, outcome, learning).
- Pair with `growth/go-to-market-planner` for launch experiments.
- For AI: include human review sample on quality guardrails.

---

# Output Structure

```markdown
# Experiment: [Name]

## Decision
[What we decide on win/loss]

## Hypothesis
[Falsifiable statement]

## Variants
| Variant | Change | Traffic % |
|---------|--------|-----------|

## Metrics
| Role | Metric | Baseline | MDE |
|------|--------|----------|-----|

## Statistics
[Sample size, duration, confidence]

## Segmentation
[Population, exclusions]

## Ship criteria
[Win / stop / rollback rules]

## Dependencies
[Analytics events, feature flags]
```

---

# Next Skills

| Outcome | Recommended Skill |
|---------|-------------------|
| Add tracking events | `product/analytics-instrumentation-planner` |
| Canonical metric definitions | `data/metric-definition-builder` |
| GTM launch test | `growth/go-to-market-planner` |
| Price test design | `growth/pricing-strategy-advisor` |
| AI quality guardrails | `ai/ai-evaluation-builder` |

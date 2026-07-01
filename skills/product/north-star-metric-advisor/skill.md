# North Star Metric Advisor

# Purpose

Define a single north star metric with input metrics, guardrails, and measurement plan that reflects core user value and ladders to business outcomes.

**Input:** Product vision or value proposition, business model, user journey, current analytics (optional)  
**Output:** North Star Metric document with definition, input metrics, anti-metrics, and OKR alignment notes

---

# Workflow

## Step 1: Clarify value delivery

Establish:

- Primary user segment and core job-to-be-done
- Moment value is delivered (activation, habit, outcome)
- Business model link (subscription, transaction, ads, marketplace)
- Current growth stage (pre-PMF, growth, scale)

If value delivery is unclear, stop and request vision or value proposition context.

## Step 2: Generate metric candidates

Brainstorm 3–5 candidate metrics. Each must be:

- **Value-reflective** — increases when users get more core value
- **Measurable** — trackable with existing or feasible instrumentation
- **Actionable** — teams can influence it through product changes
- **Leading** — predicts retention or revenue, not a lagging finance metric alone

Document trade-offs per candidate:

| Candidate | Pros | Cons | Value link |
|-----------|------|------|------------|

## Step 3: Select north star metric

Apply selection criteria:

| Criterion | Weight | Score (1–5) |
|-----------|--------|-------------|
| Reflects core user value | High | |
| Team can move it quarterly | High | |
| Correlates with revenue/retention | High | |
| Not easily gamed | Medium | |
| Measurable within 90 days | Medium | |

Select exactly one primary north star. Demote others to input metrics or discard.

Write precise definition:

- **Name:** [metric]
- **Formula:** [numerator / denominator / window]
- **Unit:** [count, rate, index]
- **Scope:** [all users, active users, paying users]

## Step 4: Define input metrics

Identify 3–5 leading indicators that drive the north star:

| Input metric | Relationship to NSM | Owner team | Target cadence |
|--------------|---------------------|------------|----------------|

Each input metric must have a hypothesized causal link, not just correlation.

## Step 5: Set guardrails and measurement plan

Document anti-metrics that must NOT degrade while optimizing north star:

| Anti-metric / guardrail | Why protected | Threshold |
|-------------------------|---------------|-----------|

Define baseline, data source, event definitions, and review cadence (weekly/monthly).

## Step 6: Validate

Run Validation checklist.

---

# Decision Rules

| Condition | Action |
|-----------|--------|
| No clear user value moment | Stop; run product-vision-builder or value-proposition-designer |
| Multiple north stars requested | Select one primary; others become input metrics |
| Candidate is revenue-only (MRR, ARR) | Reframe to user value metric that drives revenue |
| Metric is output-based (features shipped) | Replace with outcome metric |
| Metric easily gamed without value | Add guardrails or redefine formula |
| No baseline and no instrumentation plan | Document "TBD" with 90-day instrumentation milestone |
| B2B and B2C mixed in one metric | Split by segment or choose dominant model |

---

# Validation

- [ ] Exactly one north star metric selected with formula and scope
- [ ] 3–5 input metrics with causal hypotheses
- [ ] Anti-metrics / guardrails documented with thresholds
- [ ] Measurement plan includes baseline and data source
- [ ] Metric reflects user value, not internal output
- [ ] Business model connection explained
- [ ] Review cadence defined

---

# Anti-patterns

- **Revenue as north star** — optimizing MRR without user value linkage.
- **Vanity metrics** — page views, downloads without retention signal.
- **Composite kitchen-sink metric** — unexplainable index nobody can act on.
- **Unmeasurable aspiration** — "customer delight score" with no survey or proxy.
- **Gaming without guardrails** — NSM rises while churn spikes.

---

# Best Practices

- Use the "would users notice if this dropped?" test for NSM candidates.
- Anchor NSM to the aha moment in the user journey.
- Pair NSM with 2–3 hard guardrails, not dozens of metrics.
- Revisit NSM at stage transitions (pre-PMF → growth), not monthly.
- Connect NSM explicitly to OKR objectives in next planning cycle.

---

# Output Structure

```markdown
# North Star Metric: [Product Name]

## Context
- **Segment:** [primary user]
- **Value moment:** [when value is delivered]
- **Growth stage:** [pre-PMF / growth / scale]
- **Business model:** [how value converts to revenue]

## North Star Metric
- **Metric:** [name]
- **Definition:** [plain language]
- **Formula:** [calculation]
- **Scope:** [population and time window]
- **Baseline:** [current or TBD]
- **Target:** [optional 90-day goal]

## Input Metrics
| Metric | Drives NSM by... | Owner | Baseline |
|--------|------------------|-------|----------|

## Guardrails / Anti-metrics
| Metric | Threshold | Action if breached |
|--------|-----------|-------------------|

## Measurement Plan
- **Data source:** [analytics tool / warehouse]
- **Events required:** [list]
- **Review cadence:** [weekly/monthly]
- **Instrumentation gaps:** [TBD items]

## OKR Alignment Notes
[How objectives should ladder to this NSM]
```

---

# Next Skills

| Outcome | Recommended Skill |
|---------|-------------------|
| Set quarterly goals from NSM | `product/okr-builder` |
| Prioritize features that move input metrics | `product/feature-prioritization` |
| Need full vision document | `product/product-vision-builder` |
| NSM needs user segment clarity | `product/persona-generator` |
| Write PRD for NSM-driving initiative | `product/prd-generator` |

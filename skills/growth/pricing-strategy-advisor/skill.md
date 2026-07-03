---
name: pricing-strategy-advisor
description: >
  Recommend a pricing model and price points for AI/SaaS products: usage, seat, tier, and hybrid structures with unit economics. Use when pricing a new product, repricing, or designing AI consumption-based billing.
metadata:
  apes-version: "1.1"
  category: growth
---

# Pricing Strategy Advisor

# Purpose

Recommend a pricing model and structure: how customers pay, what drives the bill, tier boundaries, and unit economics sanity check for AI/SaaS products.

**Input:** Product type, ICP, cost structure (COGS per user/request), competitive pricing (optional), business goal (growth vs margin)  
**Output:** Pricing Strategy Memo with model recommendation, tier table, unit economics worksheet, and rollout considerations  
**Examples:** See [examples.md](examples.md) for worked input/output.

---

# Workflow

## Step 1: Gather pricing inputs

| Input | Why it matters |
|-------|----------------|
| Value metric | What customers pay for (seats, API calls, tokens, outcomes) |
| COGS | Inference cost, support, infra per unit |
| WTP signals | Interviews, competitor prices, pilot conversions |
| Sales motion | Self-serve vs enterprise affects packaging |
| Strategic goal | Land grab vs profitability |

If COGS unknown for AI product, estimate from `ai/ai-cost-optimizer` outputs or request model/token assumptions.

## Step 2: Map pricing model options

| Model | Best for | Risk |
|-------|----------|------|
| Flat subscription | Predictable SMB SaaS | Misaligned if usage varies |
| Per seat | Collaboration tools | Seat inflation, under-monetize power users |
| Usage / consumption | AI APIs, variable workload | Bill shock, unpredictable revenue |
| Credits / packs | Hybrid AI products | Complexity in UX |
| Freemium + paid tiers | PLG | Free tier COGS bleed |
| Enterprise custom | High ACV, long cycle | Opacity, slow deals |

Score each option against ICP and COGS (1–5).

## Step 3: Define value metric for AI products

| Metric type | Example | When |
|-------------|---------|------|
| Per request | $/1k API calls | Developer API |
| Per token | Input/output priced | Raw LLM proxy |
| Per outcome | $/resolved ticket | Agent automation |
| Per seat + allowance | Seats + included AI credits | Copilot in SaaS |
| Per workspace | Team bundle | B2B collaboration |

Pick **one primary** value metric; secondary metrics only for overage.

## Step 4: Design tier structure

Typical 3-tier pattern:

| Tier | Audience | Limits | Price anchor |
|------|----------|--------|--------------|
| Free / Starter | Trial, indie | Hard caps, watermark | $0 |
| Pro | Core ICP | Generous limits | Main revenue |
| Business / Enterprise | Teams, SSO, SLA | Custom / annual | Expansion |

Per tier define: limits, features gated, support level, contract terms.

## Step 5: Unit economics check

| Line | Calculation |
|------|-------------|
| ARPU | Weighted average revenue per paying user |
| Gross margin | (ARPU - COGS) / ARPU |
| Payback | CAC / (ARPU * gross margin) |
| AI COGS % | Inference cost / revenue — flag if >40% at scale |

If margin negative at target price, recommend limit changes, model routing, or price increase — do not ignore COGS.

## Step 6: Competitive and psychological pricing

- Anchor against 2–3 comparables (not race to bottom)
- Charm vs round pricing by segment (SMB vs enterprise)
- Annual discount standard: 15–20% for cash flow
- Grandfathering policy for existing users on change

## Step 7: Rollout and experimentation plan

| Step | Action |
|------|--------|
| Price test | Van Westendorp or A/B on landing (see experiment-designer) |
| Packaging test | Feature gates vs limit gates |
| Migration | Communication for repricing |
| Instrumentation | Track conversion by tier in analytics |

## Step 8: Validate

Run Validation checklist.

---

# Decision Rules

| Condition | Action |
|-----------|--------|
| COGS unknown | Stop; require cost model before usage-based pricing |
| Negative margin at proposed price | Revise tiers or limits before launch |
| Enterprise only, no self-serve | Skip freemium; focus annual contracts |
| Commodity LLM wrapper | Warn on compression risk; differentiate on outcome pricing |
| Heavy AI usage variance | Prefer consumption + caps over pure seat |
| Regulatory billing rules | Note jurisdiction; do not invent legal advice |

---

# Validation

- [ ] Value metric identified and justified for ICP
- [ ] ≥2 pricing models compared with scores
- [ ] Tier table with limits and feature gates
- [ ] Unit economics worksheet with gross margin estimate
- [ ] AI COGS line item explicit for AI products
- [ ] Competitive reference points cited
- [ ] Rollout / experiment plan for price validation
- [ ] Grandfathering and migration notes if repricing

---

# Anti-patterns

- **Cost-plus only** — ignores willingness to pay and value.
- **Copy competitor price** — no wedge or COGS fit.
- **Unlimited free AI tier** — COGS death spiral.
- **Too many tiers** — decision paralysis (max 4 public tiers).
- **Hidden overage** — destroys trust; disclose limits clearly.

---

# Best Practices

- Price on **outcome** when you can measure it reliably.
- Show ROI calculator for enterprise buyers.
- Pair with `ai/ai-cost-optimizer` to keep margins as models change.
- Revisit pricing when model costs drop 30%+ (AI market shifts).
- Use annual prepay to fund inference float.

---

# Output Structure

```markdown
# Pricing Strategy: [Product Name]

## Context
[ICP, motion, strategic goal]

## Model recommendation
[Primary model + rationale]

## Value metric
[What drives the bill]

## Tier table
| Tier | Price | Limits | Features |
|------|-------|--------|----------|

## Unit economics
| Metric | Value |
|--------|-------|

## Competitive context
[Comparables]

## Rollout plan
[Tests, migration, instrumentation]

## Risks
[Margin, competition, bill shock]
```

---

# Next Skills

| Outcome | Recommended Skill |
|---------|-------------------|
| Launch with GTM | `growth/go-to-market-planner` |
| A/B test price points | `growth/experiment-designer` |
| Reduce inference COGS | `ai/ai-cost-optimizer` |
| Competitive price context | `product/competitive-analysis` |
| Track conversion events | `product/analytics-instrumentation-planner` |

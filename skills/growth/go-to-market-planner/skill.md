---
name: go-to-market-planner
description: >
  Produce a go-to-market plan: target segments, channels, launch phases, messaging, and success metrics. Use when launching a product, entering a new market, or planning a GTM strategy after positioning is defined.
metadata:
  apes-version: "1.1"
  category: growth
---

# Go-to-Market Planner

# Purpose

Produce a go-to-market (GTM) plan: who to reach first, through which channels, in what sequence, with what message, and how to measure launch success.

**Input:** Product/PRD summary, value proposition, competitive context (optional), budget and timeline constraints  
**Output:** GTM Plan with segment prioritization, channel mix, phased launch timeline, messaging pillars, and KPI dashboard  
**Examples:** See [examples.md](examples.md) for worked input/output.

---

# Workflow

## Step 1: Confirm launch readiness inputs

| Input | Required | Source skill |
|-------|----------|--------------|
| Target customer & problem | Yes | `product/problem-statement-builder` |
| Value proposition | Yes | `product/value-proposition-designer` |
| MVP scope | Yes | `product/prd-generator` or `feature-prioritization` |
| Competitive wedge | Recommended | `product/competitive-analysis` |
| Pricing direction | Recommended | `growth/pricing-strategy-advisor` |

If value proposition is missing, stop and request it — GTM without positioning produces generic campaigns.

## Step 2: Define ICP and beachhead segment

| Field | Definition |
|-------|------------|
| ICP firmographics | Company size, industry, geography |
| Persona | Buyer vs user vs champion |
| Pain intensity | Must-have vs nice-to-have |
| Reachability | Can we find and contact them? |
| Willingness to pay | Budget owner identified? |

Rank 1–3 segments; pick **one beachhead** for launch (not everyone at once).

## Step 3: Select GTM motion

| Motion | Use when | Primary channels |
|--------|----------|------------------|
| Product-led (PLG) | Low touch, self-serve, fast TTV | Product, content, community |
| Sales-led | High ACV, complex buy, enterprise | Outbound, demos, partners |
| Community-led | Developer tools, open core | Docs, Discord, advocates |
| Hybrid | Mid-market SaaS | PLG entry + sales assist |

State chosen motion and why alternatives were rejected.

## Step 4: Build channel plan

Per channel document:

| Channel | Role in funnel | Owner | Budget | Leading indicator |
|---------|----------------|-------|--------|-------------------|
| Content/SEO | Awareness | Marketing | $ | Organic traffic |
| Paid | Acquisition | Growth | $ | CAC |
| Product virality | Activation | Product | — | Invite rate |
| Sales outbound | Conversion | Sales | $ | SQLs |
| Partnerships | Distribution | BD | — | Referral pipeline |

For AI products: add **trust channels** (demos, case studies, security page) — buyers need proof, not hype.

## Step 5: Phased launch timeline

| Phase | Duration | Goal | Activities |
|-------|----------|------|------------|
| Alpha | 2–4 wk | Learn | Design partners, qualitative feedback |
| Beta | 4–8 wk | Validate | Limited access, measure activation |
| GA | ongoing | Scale | Full channel mix, optimize CAC/LTV |

Each phase has **entry criteria**, **exit criteria**, and **kill criteria** if metrics fail.

## Step 6: Messaging architecture

| Level | Content |
|-------|---------|
| One-liner | Problem + outcome |
| Elevator pitch | 30-second version for ICP |
| Pillars | 3 proof-backed themes (not feature lists) |
| Objection map | Top 5 objections + responses |
| AI disclosure | How you describe AI capabilities honestly |

Align with value proposition; do not invent new positioning here.

## Step 7: Define launch KPIs

| Metric | Target | Measurement |
|--------|--------|---------------|
| Activation | e.g. 40% complete core action D7 | Product analytics |
| Pipeline | SQLs or signups/week | CRM / product |
| CAC (if paid) | < X% of LTV | Finance + ads |
| NPS / qualitative | Baseline score | Surveys |

Link events to `product/analytics-instrumentation-planner` or `growth/experiment-designer`.

## Step 8: Validate

Run Validation checklist.

---

# Decision Rules

| Condition | Action |
|-----------|--------|
| No single beachhead segment | Stop; force rank — launch one segment first |
| B2B enterprise + PLG only budget | Flag mismatch; recommend sales assist or narrow ICP |
| Pre-product / no MVP | Limit to alpha design-partner plan only |
| Regulated industry | Add compliance review gate before public GA |
| AI product without eval metrics | Require quality KPI in launch dashboard |
| Launch date immovable | Cut channels, not measurement |

---

# Validation

- [ ] Beachhead ICP defined with firmographics and persona
- [ ] GTM motion selected with rationale
- [ ] ≥3 channels with owners and leading indicators
- [ ] Phased timeline with entry/exit/kill criteria
- [ ] Messaging pillars tied to value proposition
- [ ] Launch KPIs with targets and data sources
- [ ] Dependencies on pricing and analytics documented
- [ ] Risks and mitigations listed (competitor response, budget)

---

# Anti-patterns

- **Spray and pray** — every channel at once with no beachhead.
- **Launch without activation metric** — vanity traffic, no product signal.
- **Feature launch, not outcome launch** — messaging is a changelog.
- **Ignoring sales cycle** — enterprise GTM with self-serve assumptions.
- **AI hype positioning** — overpromising capabilities eval cannot support.

---

# Best Practices

- Start with 10–20 design partners before paid acquisition.
- Pair qualitative interviews with funnel metrics each phase.
- Document what you will **not** do in launch (non-goals).
- Refresh competitive messaging quarterly in fast-moving AI categories.
- Hand off instrumentation before beta opens.

---

# Output Structure

```markdown
# GTM Plan: [Product Name]

## Launch context
[Motion, beachhead, timeline constraints]

## Beachhead ICP
[Segment definition and ranking]

## Channel plan
| Channel | Funnel stage | Owner | KPI |
|---------|--------------|-------|-----|

## Launch phases
### Alpha / Beta / GA
[Criteria and activities]

## Messaging
[Pillars, pitch, objections]

## KPIs
| Metric | Target | Source |
|--------|--------|--------|

## Risks
| Risk | Mitigation |
|------|------------|

## Dependencies
[Pricing, analytics, product readiness]
```

---

# Next Skills

| Outcome | Recommended Skill |
|---------|-------------------|
| Set price before launch | `growth/pricing-strategy-advisor` |
| Design launch experiments | `growth/experiment-designer` |
| Instrument funnels | `product/analytics-instrumentation-planner` |
| Refine positioning | `product/value-proposition-designer` |
| Competitive context | `product/competitive-analysis` |

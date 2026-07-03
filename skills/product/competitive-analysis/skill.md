---
name: competitive-analysis
description: >
  Produce a structured competitive analysis: competitor map, feature matrix, positioning gaps, and strategic recommendations. Use when evaluating markets, planning differentiation, or preparing investor/product strategy decks.
metadata:
  apes-version: "1.1"
  category: product
---

# Competitive Analysis

# Purpose

Produce a structured competitive analysis: who competes, how they compare, where gaps exist, and what differentiation strategy to pursue.

**Input:** Product idea or category, target customer segment, known competitors (optional), geography  
**Output:** Competitive Analysis Report with landscape map, feature matrix, SWOT per player, and strategic recommendations  
**Examples:** See [examples.md](examples.md) for worked input/output.

---

# Workflow

## Step 1: Define market scope

Clarify:

- **Category** — what job-to-be-done or product category
- **Segment** — SMB vs enterprise, geography, vertical
- **Substitutes** — manual workflows, spreadsheets, status quo
- **Time horizon** — current players vs emerging (12–18 months)

If scope is too broad, narrow to one segment before researching.

## Step 2: Build competitor long list

| Source | Method |
|--------|--------|
| User input | Named competitors |
| Search | Category + "alternative", G2/Capterra categories |
| Substitutes | Adjacent tools solving same job |
| Emerging | Recent funding, Product Hunt, AI-native entrants |

Target 5–12 relevant players; tier into direct, indirect, substitute.

## Step 3: Profile each competitor

Per competitor capture:

| Dimension | Data |
|-----------|------|
| Positioning | One-line value prop |
| Target customer | Segment and persona |
| Pricing model | Free/freemium/enterprise |
| Strengths | 2–3 defensible advantages |
| Weaknesses | Gaps, complaints, tech debt signals |
| AI capability | Native AI vs bolt-on (if applicable) |

Mark confidence: verified (public source) vs inferred (state explicitly).

## Step 4: Build feature comparison matrix

Rows = capabilities users care about (from JTBD, not vendor feature lists).  
Columns = top 5–8 competitors + your product (planned).

Scoring: ✅ Strong · ⚠️ Partial · ❌ Missing · ? Unknown

Highlight rows where no incumbent excels — **white space**.

## Step 5: Positioning analysis

Plot on 2 axes that matter to buyers (e.g., ease vs power, price vs depth).  
Identify overcrowded quadrants and open space.

Run **per-competitor SWOT** (brief) and **your product SWOT** against the field.

## Step 6: Strategic recommendations

| Type | Output |
|------|--------|
| Differentiation | 2–3 wedges competitors cannot easily copy |
| Table stakes | Features you must match to be credible |
| Avoid | Areas dominated by incumbents with network effects |
| Partnerships | Integrate vs compete decisions |
| Risks | Incumbent response, commoditization |

Tie recommendations to `value-proposition-designer` and `feature-prioritization` inputs.

## Step 7: Validate

Run Validation checklist.

---

# Decision Rules

| Condition | Action |
|-----------|--------|
| <3 identifiable competitors | Expand to substitutes and manual alternatives |
| User claims "no competitors" | Challenge; document status quo as competitor |
| Data older than 12 months | Flag stale; prefer recent pricing/feature pages |
| Enterprise vs SMB mix | Split matrix by segment — do not blend |
| AI product category | Add AI-native comparison row (RAG, agents, eval) |

---

# Validation

- [ ] Market scope and segment defined
- [ ] ≥5 competitors profiled with sources cited
- [ ] Feature matrix uses buyer-centric capabilities (≥8 rows)
- [ ] White-space opportunities identified
- [ ] Positioning map with labeled axes
- [ ] SWOT for your product vs field
- [ ] Actionable recommendations (differentiation + table stakes)
- [ ] Confidence labels on inferred data

---

# Anti-patterns

- **Feature laundry list** — matrix rows mirror vendor marketing pages.
- **Competitor worship** — copying incumbents without wedge strategy.
- **Stale analysis** — pricing from 2022 in fast-moving AI markets.
- **Ignoring status quo** — "Excel + email" is often the real competitor.
- **No strategic so-what** — report ends at matrix without recommendations.

---

# Best Practices

- Interview 3–5 target users: "what did you evaluate before buying X?"
- Weight matrix rows by customer priority (from discovery interviews).
- Refresh competitive snapshot quarterly for AI product categories.
- Link output to `idea-validator` assumptions and `prd-generator` non-goals.
- Separate global players from regional niche entrants.

---

# Output Structure

```markdown
# Competitive Analysis: [Category / Product]

## Scope
[Segment, geography, horizon]

## Landscape
| Tier | Players | Role |
|------|---------|------|

## Competitor Profiles
### [Name]
[Positioning, pricing, strengths, weaknesses, AI]

## Feature Matrix
| Capability | Us | A | B | C |
|------------|----|---|---|---|

## Positioning Map
[2-axis description + placement]

## White Space
[Opportunities]

## Strategic Recommendations
| Priority | Recommendation | Rationale |
|----------|----------------|-----------|

## Sources
[URLs, dates]
```

---

# Next Skills

| Outcome | Recommended Skill |
|---------|-------------------|
| Refine positioning | `product/value-proposition-designer` |
| Validate idea assumptions | `product/idea-validator` |
| Prioritize response features | `product/feature-prioritization` |
| Write PRD with competitive context | `product/prd-generator` |
| Technical differentiation (AI) | `ai/ai-solution-architect` |

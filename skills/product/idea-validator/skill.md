# Idea Validator

# Purpose

Validate a product idea by mapping assumptions, assessing desirability/feasibility/viability signals, and producing a go/no-go/pivot recommendation with evidence gaps.

**Input:** Product idea description, target audience (if known), problem hypothesis (if any)  
**Output:** Idea Validation Report with assumption map, scorecard, and recommendation

---

# Workflow

## Step 1: Capture the idea

Extract and restate:

- Core idea (one sentence)
- Target user segment
- Problem being solved
- Proposed solution
- Business model hypothesis (if stated)

If the idea is vague, ask clarifying questions before proceeding.

## Step 2: Build assumption map

Categorize assumptions using Lean Startup framework:

| Category | Assumptions to identify |
|----------|------------------------|
| Desirability | Do users want this? Is the problem real and urgent? |
| Feasibility | Can we build it with available technology and skills? |
| Viability | Can we sustain a business (revenue, cost, distribution)? |

List each assumption explicitly. Mark confidence: High / Medium / Low / Unknown.

## Step 3: Identify evidence

For each assumption, document:

- Existing evidence (user quotes, market data, prior experiments)
- Evidence gaps (what is unknown)
- Cheapest test to validate (interview, landing page, prototype, concierge)

## Step 4: Score the idea

Apply scoring matrix (1–5 per dimension):

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Problem clarity | | |
| Target user clarity | | |
| Differentiation | | |
| Market size signal | | |
| Technical feasibility | | |
| Distribution feasibility | | |
| Riskiest assumption testability | | |

## Step 5: Generate recommendation

Based on scores and assumption map:

- **Go** — proceed to problem statement refinement
- **Pivot** — specify what to change (segment, problem, solution)
- **Stop** — specify why and what would change the decision

## Step 6: Validate output

Run Validation checklist before delivery.

---

# Decision Rules

| Condition | Action |
|-----------|--------|
| Idea has no stated target user | Stop; request user segment definition |
| Idea solves no clear problem | Flag as solution-in-search-of-problem; recommend pivot to problem discovery |
| All assumptions are Unknown confidence | Recommend discovery experiments before any build decision |
| Score average < 2.5 | Recommend Stop or Pivot with specific changes |
| Score average ≥ 3.5 and testable risky assumptions | Recommend Go with experiment plan |
| User provides market size claims without source | Mark as unverified; add to evidence gaps |

---

# Validation

- [ ] Idea restated in one clear sentence
- [ ] At least 3 assumptions listed across desirability/feasibility/viability
- [ ] Each assumption has confidence level and evidence gap
- [ ] Scorecard has rationale for every score
- [ ] Recommendation is Go, Pivot, or Stop (not ambiguous)
- [ ] Pivot/Stop includes specific actionable changes
- [ ] No invented market data or user quotes

---

# Anti-patterns

- **Enthusiasm without evidence** — rating desirability High without any user signal.
- **TAM fantasy** — citing billion-dollar markets without segment focus.
- **Build-first bias** — recommending development before validating riskiest assumption.
- **Generic personas** — "everyone" or "businesses" as target user.
- **Skipping viability** — validating only whether users want it, not whether the business works.

---

# Best Practices

- Use Lean Startup assumption mapping consistently.
- Prioritize the riskiest assumption for the cheapest possible test.
- Separate facts from hypotheses in the output.
- Reference comparable products only as competitive context, not as proof.
- Time-box recommended experiments (e.g. "5 customer interviews in 1 week").

---

# Output Structure

```markdown
# Idea Validation Report: [Idea Name]

## Idea Summary
[One paragraph restatement]

## Assumption Map
| # | Category | Assumption | Confidence | Evidence | Gap | Cheapest Test |
|---|----------|------------|------------|----------|-----|---------------|

## Scorecard
| Dimension | Score (1-5) | Rationale |
|-----------|-------------|-----------|

**Average score:** X.X / 5

## Recommendation
**Decision:** Go | Pivot | Stop

**Rationale:** [Why]

**If Pivot:** [What to change]

## Recommended Experiments
1. [Experiment] — validates assumption #N — timeline: [X days]

## Open Questions
- [ ] [Question]
```

---

# Next Skills

| Outcome | Recommended Skill |
|---------|-------------------|
| Recommendation is Go | `product/problem-statement-builder` |
| Recommendation is Pivot (problem unclear) | `product/problem-statement-builder` |
| Need deeper user understanding first | `product/persona-generator` |
| Ready for strategic framing | `product/product-vision-builder` |

# Acceptance Criteria Generator

# Purpose

Write testable acceptance criteria for user stories using Given-When-Then (BDD) format with edge cases and negative scenarios.

**Input:** User story (As/Want/So format)  
**Output:** Acceptance criteria set with happy path, edge cases, and negative scenarios

---

# Workflow

## Step 1: Parse user story

Extract:

- Persona (actor)
- Action (behavior)
- Benefit (expected outcome)
- Story ID (if provided)

## Step 2: Write happy path criteria

Minimum 1 scenario in Given-When-Then:

**Given** [precondition]  
**When** [action]  
**Then** [observable outcome]

Each Then clause must be verifiable without interpretation.

## Step 3: Add edge cases

Identify 2–4 edge cases:

- Boundary values
- Empty/null states
- Concurrent actions
- Permission variations

## Step 4: Add negative scenarios

Identify 1–3 failure scenarios:

- Invalid input
- Unauthorized access
- System unavailable
- Timeout/error handling

## Step 5: Cross-check against INVEST

Verify criteria make the story Testable. If not, flag story for revision.

## Step 6: Validate

Run Validation checklist.

---

# Decision Rules

| Condition | Action |
|-----------|--------|
| User story missing or incomplete | Stop; request full story or run user-story-generator |
| Then clause is subjective | Rewrite with observable, measurable outcome |
| Criteria describe implementation | Rewrite as behavior ("API returns 200" → "user sees confirmation") |
| No negative scenarios | Add at least one error/unauthorized case for user-facing stories |
| Criteria overlap across scenarios | Deduplicate; ensure each tests distinct behavior |

---

# Validation

- [ ] ≥1 happy path in Given-When-Then format
- [ ] ≥2 edge case scenarios
- [ ] ≥1 negative scenario
- [ ] All Then clauses are observable/testable
- [ ] No implementation details unless NFR-related
- [ ] Scenarios cover the full "so that" benefit
- [ ] Each scenario has unique ID (AC-001...)

---

# Anti-patterns

- **Subjective criteria** — "page loads fast", "looks good".
- **Implementation criteria** — "calls endpoint X with payload Y".
- **Happy path only** — no error handling scenarios.
- **Duplicate scenarios** — same behavior tested multiple ways.
- **Untestable benefits** — criteria don't verify the "so that" clause.

---

# Best Practices

- Use concrete values in Given clauses (specific user role, data state).
- Then clauses should be verifiable by QA without code knowledge.
- Name scenarios descriptively: AC-001-happy-login, AC-002-invalid-password.
- Align negative scenarios with NFRs (security, performance) when relevant.
- Keep 3–7 criteria per story; split story if more needed.

---

# Output Structure

```markdown
# Acceptance Criteria: US-XXX — [Story title]

## Story
**As a** ... **I want** ... **so that** ...

## Happy Path
### AC-001: [Scenario name]
- **Given** ...
- **When** ...
- **Then** ...

## Edge Cases
### AC-002: [Scenario name]
- **Given** ...
- **When** ...
- **Then** ...

## Negative Scenarios
### AC-003: [Scenario name]
- **Given** ...
- **When** ...
- **Then** ...

## Coverage Check
| Story benefit | Covered by |
|---------------|------------|
| [benefit] | AC-001, AC-003 |

## Open Questions
- [ ] [Ambiguity needing PO decision]
```

---

# Next Skills

| Outcome | Recommended Skill |
|---------|-------------------|
| Map stories on board | `product/story-mapping` |
| More stories needed | `product/user-story-generator` |
| Release planning | `product/epic-generator` |
| PRD traceability | `product/prd-generator` |

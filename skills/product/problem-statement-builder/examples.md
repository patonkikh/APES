# Problem Statement Builder — Worked Examples

---

## Example 1: Structured problem statement

### Input

```text
Idea: AI generates sprint retros from Jira for engineering managers
Audience: EMs at 50–200 engineer companies
Current workaround: Manual slide decks + copy-paste from Jira
```

### Output (excerpt)

```markdown
# Problem Statement: Retro Preparation Burden

## Context
Engineering managers at mid-size B2B SaaS companies run bi-weekly retrospectives
requiring synthesis of sprint data, incidents, and team feedback.

## Problem
**When** preparing for a sprint retrospective,
**I want to** compile accurate sprint signals and themes quickly,
**but** manual Jira export and slide building takes 2+ hours,
**which causes** delayed action items, skipped retros, and manager burnout.

## Who is affected
- Primary: Engineering managers (5–15 direct reports)
- Secondary: Team members (lower-quality retro outcomes)

## Evidence
| Signal | Source | Strength |
|--------|--------|----------|
| 2+ hour prep time | 3 EM interviews | Medium |
| Lost action items | Informal feedback | Low — needs validation |

## Success criteria for problem validation
- ≥60% of interviewed EMs report prep time >90 min
- ≥50% say action item follow-through is inconsistent
```

---

## Example 2: Solution disguised as problem

### Input

```text
Problem: We need to build a Jira plugin with GPT-4
```

### Expected behavior

Rewrite problem in user outcome terms; move Jira plugin/GPT-4 to solution hypothesis section.

---

## Example 3: Missing audience — stop

### Expected behavior

Request target segment before completing problem statement.

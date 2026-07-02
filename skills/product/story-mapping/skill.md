---
name: story-mapping
description: >
  Create a visual story map (Jeff Patton method) organizing user activities, tasks, and stories across a horizontal user journey with vertical priority. Use when working on product discovery, PRDs, user stories, OKRs, or backlog planning.
metadata:
  apes-version: "1.1"
  category: product
---

# Story Mapping

# Purpose

Create a visual story map (Jeff Patton method) organizing user activities, tasks, and stories across a horizontal user journey with vertical priority.

**Input:** Product scope, epics, user stories (optional), persona (optional)  
**Output:** Story map document with backbone, walking skeleton, and release slices
**Examples:** See [examples.md](examples.md) for worked input/output.

---

# Workflow

## Step 1: Define the backbone

Identify 5–12 high-level user activities in chronological order (left to right):

- Activities = verbs describing what users do (not features)
- Example: "Discover product" → "Sign up" → "Configure" → "Use core feature" → "Share results"

## Step 2: Add user tasks

Under each activity, list user tasks (smaller steps):

- Tasks are user-facing actions
- Order tasks left-to-right within activity by frequency/importance

## Step 3: Map stories to tasks

Place user stories (or story placeholders) under tasks:

- Vertical position = priority (top = higher priority)
- Stories from user-story-generator map directly if available
- Create placeholders (US-???) for gaps

## Step 4: Draw release slices

Draw horizontal lines across the map:

- **Release 1 (Walking skeleton):** minimum end-to-end path
- **Release 2:** enhanced experience
- **Release 3+:** optimizations and edge cases

Each release must deliver a complete user journey (not just one activity).

## Step 5: Validate coherence

Check:

- Backbone tells a coherent user narrative
- Release 1 is viable and testable
- No activity has only low-priority stories in Release 1

## Step 6: Validate

Run Validation checklist.

---

# Decision Rules

| Condition | Action |
|-----------|--------|
| Activities are features, not user actions | Reframe as user verbs |
| Release 1 doesn't span full backbone | Add walking skeleton stories to complete journey |
| No user stories provided | Create story placeholders; recommend user-story-generator |
| Too many activities (>15) | Group into meta-activities or split product scope |
| Stories don't fit any task | Add task or question story relevance |

---

# Validation

- [ ] Backbone has 5–12 activities in chronological order
- [ ] Each activity has ≥1 user task
- [ ] Stories or placeholders mapped under tasks
- [ ] Vertical priority indicated (top = higher)
- [ ] ≥2 release slices defined
- [ ] Release 1 completes end-to-end user journey
- [ ] Map references persona if available

---

# Anti-patterns

- **Feature map, not story map** — activities like "API layer" or "Admin panel."
- **Release 1 = one column** — only building first activity, no end-to-end flow.
- **Flat priority** — all stories at same vertical level.
- **Missing backbone** — jumping straight to story list without journey.
- **Orphan stories** — stories not connected to any user task.

---

# Best Practices

- Use Jeff Patton's narrative flow: tell the user's story left to right.
- Walking skeleton first: thinnest possible end-to-end path.
- Align release slices with feature-prioritization MVP cut if available.
- Use persona scenario triggers to validate backbone completeness.
- Story map is living artifact — note it should update as learning occurs.

---

# Output Structure

```markdown
# Story Map: [Product Name]

## Persona
[Primary persona reference]

## Backbone & Tasks
| Activity 1 | Activity 2 | Activity 3 | ... |
|------------|------------|------------|-----|
| Task 1.1 | Task 2.1 | Task 3.1 | |
| Task 1.2 | | Task 3.2 | |

## Stories (by task)
### Activity 1: [Name]
#### Task 1.1: [Name]
| Priority | Story ID | Story title |
|----------|----------|-------------|
| High | US-001 | ... |
| Low | US-005 | ... |

## Release Slices
### Release 1 — Walking Skeleton
[Stories included: US-001, US-003, US-007...]
**Journey:** [describe end-to-end path]

### Release 2 — [Name]
[Stories...]

## Gaps
| Task | Missing story | Recommendation |
|------|---------------|----------------|

## Next Actions
- [ ] [Action item]
```

---

# Next Skills

| Outcome | Recommended Skill |
|---------|-------------------|
| Fill story gaps | `product/user-story-generator` |
| Add criteria to stories | `product/acceptance-criteria-generator` |
| Re-prioritize release | `product/feature-prioritization` |
| Update PRD from map | `product/prd-generator` |

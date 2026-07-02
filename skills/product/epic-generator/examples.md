# Epic Generator — Worked Examples

---

## Example 1: MVP epic breakdown

### Input

```text
PRD FRs:
FR-001 OAuth connect, FR-002 sprint import, FR-003 AI summary,
FR-004 edit draft, FR-005 Confluence export
All Must priority
```

### Output (excerpt)

```markdown
# Epic Breakdown: Retro Generator MVP

## Epic Sequence
1. Connect Jira → 2. Generate retro → 3. Export & share

### Epic 1: Connect Jira Account
- **Goal:** Manager securely links Jira to import sprint data
- **FRs:** FR-001, FR-002
- **Story themes:** OAuth flow, workspace picker, disconnect
- **Estimate:** 4–6 stories

### Epic 2: Generate Retro Draft
- **Goal:** Manager produces AI draft from sprint data
- **FRs:** FR-003, FR-004
- **Dependencies:** Epic 1
- **Estimate:** 5–8 stories

### Epic 3: Export Retro to Confluence
- **Goal:** Manager publishes final retro to team wiki
- **FRs:** FR-005
- **Dependencies:** Epic 2
- **Estimate:** 3–5 stories
```

---

## Example 2: Technical epic — label enabler

### Input

```text
Epic: Set up Kubernetes cluster
```

### Expected behavior

```markdown
### Enabler Epic E-1: Production infrastructure baseline
**Label:** Enabler (no direct user value)
**Supports:** Epic 2 (Generate Retro) deployment
```

---

## Example 3: Giant epic — split

### Input

```text
Single epic: Entire product v1
```

### Expected behavior

Split into 3–8 user-outcome epics per Decision Rules; flag if >3 sprints estimated.

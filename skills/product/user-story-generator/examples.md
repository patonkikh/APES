# User Story Generator — Worked Examples

---

## Example 1: Epic — Jira OAuth connect

### Input

```text
Epic: User can connect Jira Cloud account
FRs: FR-001 OAuth flow, FR-002 token storage
Persona: Engineering manager
```

### Output (excerpt)

```markdown
# User Stories: Jira OAuth Connect

## US-001
**As an** engineering manager
**I want to** connect my Jira Cloud account via OAuth
**So that** the app can read my sprint data without sharing my password

**Priority:** Must | **Size:** M | **FR:** FR-001

## US-002
**As an** engineering manager
**I want to** see which Jira workspace is connected
**So that** I know which account data will be imported

**Priority:** Must | **Size:** S | **FR:** FR-001

## US-003
**As an** engineering manager
**I want to** disconnect Jira at any time
**So that** I can revoke access when I stop using the product

**Priority:** Should | **Size:** S | **FR:** FR-002

## INVEST Check
| Story | Independent | Negotiable | Valuable | Estimable | Small | Testable |
|-------|-------------|------------|----------|-----------|-------|----------|
| US-001 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
```

---

## Example 2: Technical task disguised as story — rewrite

### Input

```text
As a developer I want to set up PostgreSQL so that we have a database
```

### Expected behavior

Reframe as user value or mark as **enabler story** separate from user epics:

```markdown
**Enabler:** E-001 Provision encrypted credential store for OAuth tokens (supports FR-002)
Not a user-facing story — track separately from value backlog.
```

---

## Example 3: Missing persona

### Expected behavior

Stop or request persona from `product/persona-generator` before generating stories.

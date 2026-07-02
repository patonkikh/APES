# Acceptance Criteria Generator — Worked Examples

---

## Example 1: Given-When-Then for OAuth story

### Input

```text
Story US-001: As an EM I want to connect Jira via OAuth so that the app can read sprint data
Priority: Must
```

### Output (excerpt)

```markdown
# Acceptance Criteria: US-001 Jira OAuth Connect

## AC-001 Happy path
**Given** I am logged in and not connected to Jira
**When** I click "Connect Jira" and approve OAuth consent
**Then** I see my connected Jira workspace name
**And** my connection status shows "Connected"

## AC-002 Denied consent
**Given** I start OAuth flow
**When** I deny consent on Atlassian
**Then** I return to app with message "Connection cancelled"
**And** no token is stored

## AC-003 Token security
**Given** I have connected Jira
**When** an admin inspects storage
**Then** refresh tokens are encrypted at rest
**And** tokens are not exposed in client-side logs

## Edge cases
- Expired token → prompt re-auth without data loss message
- Multiple workspaces → user must pick one before import enabled
```

---

## Example 2: Untestable criteria — rewrite

### Input

```text
AC: System should be fast and user-friendly
```

### Expected behavior

```markdown
**Rewrite:**
**When** sprint has ≤500 issues
**Then** OAuth callback completes in <5s (p95)
```

---

## Example 3: Implementation criteria — reject

### Input

```text
AC: Use Redis for session store
```

### Expected behavior

Rewrite as observable behavior or move to technical story/enabler.

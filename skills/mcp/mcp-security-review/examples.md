# MCP Security Review — Worked Examples

---

## Example 1: GitHub issues MCP pre-deploy review

### Input

```text
Server: github-issues (stdio, TypeScript)
Tools: search_issues, get_issue, add_comment
Auth: GITHUB_TOKEN env var
Deployment: local Cursor only
```

### Output (excerpt)

```markdown
# MCP Security Review: github-issues

## Summary
| Area | Status | Critical findings |
|------|--------|-------------------|
| Auth & secrets | Pass | 0 |
| Tool permissions | Partial | 0 |
| Input validation | Partial | 0 |
| Transport security | N/A (stdio) | — |

## Findings
| ID | Severity | Finding | Remediation |
|----|----------|---------|-------------|
| S-001 | Medium | add_comment has no rate limit | Add per-minute cap |
| S-002 | Medium | Error messages may echo token fragments | Sanitize error responses |
| S-003 | Low | No audit log of tool invocations | Add structured logging |

## Tool Permission Matrix
| Tool | Read | Write | Scope |
|------|------|-------|-------|
| search_issues | yes | | issues:read |
| add_comment | | yes | issues:write |

## Deploy Recommendation
**Approve with fixes** — complete S-001, S-002 before team rollout
```

---

## Example 2: Remote HTTP MCP without TLS

### Input

```text
SSE server on http://internal.corp:8080, tools include run_sql_query
```

### Expected behavior

**Block** — Critical: no TLS, high-risk SQL tool without sandbox; require HTTPS + read-only DB role minimum.

---

## Example 3: Secrets in repo

### Input

```text
GITHUB_TOKEN hardcoded in src/config.ts
```

### Expected behavior

Critical finding; block deploy until moved to environment variables.

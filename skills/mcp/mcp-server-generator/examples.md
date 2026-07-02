# MCP Server Generator — Worked Examples

---

## Example 1: GitHub Issues MCP server

### Input

```text
Integration: GitHub REST API — issues only for a single org
Capabilities: search issues, get issue, add comment
Runtime: TypeScript
Transport: stdio (Cursor local)
Auth: OAuth token per user via env
Security: read + comment only, no issue close/delete
```

### Output (excerpt)

```markdown
# MCP Server Scaffold: github-issues

## Scope
Bounded domain: GitHub Issues for one organization. No PRs, repos, or Actions.

## Transport & Runtime
| Choice | Rationale |
|--------|-----------|
| stdio | Local Cursor integration |
| TypeScript + @modelcontextprotocol/sdk | Team preference, official SDK |

## Project Layout
```text
mcp-server-github-issues/
├── src/
│   ├── index.ts
│   ├── server.ts
│   ├── tools/
│   │   ├── search_issues.ts
│   │   ├── get_issue.ts
│   │   └── add_comment.ts
│   └── lib/
│       ├── github_client.ts
│       └── auth.ts
├── package.json
├── README.md
└── .env.example
```

## Capability Manifest
| Type | Name | Description | Auth |
|------|------|-------------|------|
| tool | search_issues | Search issues by query in org | GITHUB_TOKEN |
| tool | get_issue | Get issue by number | GITHUB_TOKEN |
| tool | add_comment | Add comment to issue | GITHUB_TOKEN |

## Configuration
| Variable | Required | Description |
|----------|----------|-------------|
| GITHUB_TOKEN | Yes | OAuth token, issues scope |
| GITHUB_ORG | Yes | Organization slug |

## Implementation Checklist
- [ ] Register 3 tools with JSON Schema inputs
- [ ] Rate limit wrapper (GitHub 5000 req/hr)
- [ ] Structured errors: RATE_LIMIT, NOT_FOUND, AUTH_FAILED
- [ ] Run mcp-security-review before deploy
```

---

## Example 2: God server — split required

### Input

```text
One MCP server for entire Salesforce: accounts, cases, reports, admin API
```

### Expected behavior

```markdown
## Scope violation — split recommended

Decision rule: scope spans multiple unrelated domains → split servers.

| Server | Domain |
|--------|--------|
| mcp-salesforce-cases | Case read/update for support agents |
| mcp-salesforce-accounts | Account lookup for sales |

Start with the highest-value bounded domain only.
```

---

## Example 3: Write operations on production

### Input

```text
Tool: delete_customer_record(customer_id)
```

### Expected behavior

Flag for security review; require confirmation pattern:

```markdown
## High-risk tool design

- Mark tool as `destructive: true` in description
- Require `confirm: true` boolean parameter with explicit warning text
- Block until `mcp/mcp-security-review` completed
```

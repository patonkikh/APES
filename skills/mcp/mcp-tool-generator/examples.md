# MCP Tool Generator — Worked Examples

---

## Example 1: search_issues tool

### Input

```text
Server: github-issues MCP
Tool: search_issues
Params: query (string), repo (string), state (open|closed), limit (1-50)
Side effects: none (read-only)
```

### Output (excerpt)

```markdown
# MCP Tool Design: search_issues

## Tool Metadata
| Field | Value |
|-------|-------|
| name | search_issues |
| destructive | false |
| idempotent | true |

## Description (LLM-optimized)
Search GitHub issues in a repository by query string. Returns issue number, title, state, and URL.
Does NOT create or modify issues. Use repo format "owner/name". If query is empty, returns recent open issues.

## JSON Schema
```json
{
  "type": "object",
  "properties": {
    "repo": {"type": "string", "pattern": "^[^/]+/[^/]+$"},
    "query": {"type": "string", "maxLength": 256},
    "state": {"type": "string", "enum": ["open", "closed", "all"], "default": "open"},
    "limit": {"type": "integer", "minimum": 1, "maximum": 50, "default": 10}
  },
  "required": ["repo"]
}
```

## Error Responses
| code | retryable | When |
|------|-----------|------|
| RATE_LIMIT | true | GitHub 403 rate limit |
| REPO_NOT_FOUND | false | Invalid repo |
| AUTH_FAILED | false | Token expired |

## Edge Cases
- Empty query → return recent open issues (documented in description)
- limit > 50 → clamp to 50, do not error
```

---

## Example 2: Destructive tool

### Input

```text
Tool: delete_issue(issue_number)
```

### Expected behavior

Require `confirm: true` boolean, `destructive: true` in metadata, human-in-the-loop note, security review flag.

---

## Example 3: Undocumented tool — anti-pattern

### Bad

Handler with no description and no input schema.

### Correct

Every tool has LLM-optimized description + JSON Schema with constraints.

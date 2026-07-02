# MCP Client Generator — Worked Examples

---

## Example 1: Cursor app MCP client integration

### Input

```text
Host app: Node.js agent orchestrator
MCP servers: github-issues (stdio), internal-wiki (SSE)
Needs: dynamic tool discovery, retry, logging
```

### Output (excerpt)

```markdown
# MCP Client Integration Plan

## Server Registry
| Server | Transport | Config |
|--------|-----------|--------|
| github-issues | stdio | `node dist/index.js` |
| internal-wiki | SSE | `https://mcp.corp/wiki` |

## Client Architecture
```text
AgentOrchestrator → McpClientManager → [stdio transport | SSE transport]
                                    → ToolRouter (schema validate)
```

## Discovery Flow
1. Connect server on startup
2. `tools/list` → cache with TTL 5m
3. Invalidate cache on server reconnect

## Resilience
| Error | Client behavior |
|-------|-----------------|
| RATE_LIMIT | Exponential backoff, max 3 retries |
| SERVER_DOWN | Mark unavailable; degrade gracefully |
| SCHEMA_MISMATCH | Log + skip tool; alert ops |

## Security
- Validate tool args against JSON Schema before invoke
- Redact tokens in logs
- Never hardcode server secrets in client repo
```

---

## Example 2: Hardcoded tool list

### Input

```text
Client assumes tools: search_issues, get_issue forever
```

### Expected behavior

Flag anti-pattern; require dynamic discovery.

---

## Example 3: No schema validation

### Expected behavior

Medium finding; client-side validation before invoke recommended.

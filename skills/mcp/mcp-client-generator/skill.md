# MCP Client Generator

# Purpose

Generate MCP client integration: connection setup, capability discovery, tool invocation patterns, and error handling for agent applications.

**Input:** Target MCP server(s), host application type (agent IDE, backend service, CLI), auth model, required capabilities  
**Output:** MCP Client Integration Specification with connection config, invocation patterns, and test plan

---

# Workflow

## Step 1: Inventory MCP servers

| Server | Transport | Capabilities needed | Auth method |
|--------|-----------|---------------------|-------------|
| | stdio / HTTP | tools, resources | env / OAuth |

Document server startup command (stdio) or endpoint URL (HTTP).

## Step 2: Design connection lifecycle

```text
Init → Connect → Discover capabilities → Cache schema → Invoke → Disconnect/Reconnect
```

| Phase | Responsibility | Timeout |
|-------|----------------|---------|
| Connect | Spawn process or HTTP handshake | 10s |
| Discover | list_tools, list_resources | 5s |
| Invoke | call_tool, read_resource | Per-tool SLA |
| Reconnect | On disconnect with backoff | Exponential |

## Step 3: Define client configuration

```json
{
  "mcpServers": {
    "server-name": {
      "command": "npx",
      "args": ["-y", "package-name"],
      "env": { "API_KEY": "${API_KEY}" }
    }
  }
}
```

For HTTP servers: base URL, headers, auth token injection.

## Step 4: Design invocation patterns

| Pattern | Use case |
|---------|----------|
| Direct call | Agent selects tool with args |
| Wrapper function | Application abstracts tool names |
| Resource prefetch | Load context before agent turn |
| Prompt template | Server-provided prompt with args |

Document argument validation before send (client-side schema check).

## Step 5: Plan error handling

| Error | Client action |
|-------|---------------|
| Connection refused | Retry 3x with backoff; surface to user |
| Tool execution error | Parse structured error; retry if retryable |
| Timeout | Cancel; return partial result flag |
| Schema mismatch | Log; do not retry; report to server maintainer |

## Step 6: Validate

Run Validation checklist.

---

# Decision Rules

| Condition | Action |
|-----------|--------|
| Multiple servers with overlapping tools | Namespace tool names in wrapper layer |
| stdio server in production backend | Prefer HTTP transport or sidecar pattern |
| User-specific OAuth per server | Store tokens securely; refresh before expiry |
| Tool args from LLM output | Validate against JSON Schema before invocation |
| Server not yet built | Generate client against capability manifest from mcp-server-generator |
| High-frequency tool calls | Add client-side rate limiter and connection pool |

---

# Validation

- [ ] All target servers documented with transport and auth
- [ ] Connection lifecycle with timeouts defined
- [ ] Configuration template provided (no real secrets)
- [ ] Invocation patterns match application architecture
- [ ] Error handling per error type
- [ ] Capability discovery and schema caching planned
- [ ] Test plan: connect, list tools, invoke, error cases
- [ ] Logging excludes sensitive args and tokens

---

# Anti-patterns

- **Hardcoded tool list** — skipping discovery; breaks on server updates.
- **Unvalidated LLM args** — passing raw model output directly to tools.
- **Secret in config file** — committing tokens to version control.
- **No timeout** — hanging client on unresponsive server.
- **Tight coupling** — application logic embedded in MCP transport layer.

---

# Best Practices

- Cache discovered tool schemas with TTL; refresh on connect.
- Wrap MCP calls in application service layer, not in UI code.
- Log tool name and duration; redact arguments containing PII.
- Support graceful degradation when server unavailable.
- Pair with mcp-security-review for production auth patterns.

---

# Output Structure

```markdown
# MCP Client Integration: [Application Name]

## Server Inventory
| Server | Transport | Auth | Startup |
|--------|-----------|------|---------|

## Connection Lifecycle
[Phases, timeouts, reconnect policy]

## Configuration
[Template with placeholders]

## Invocation Patterns
| Pattern | Tool/Resource | Wrapper API |
|---------|---------------|-------------|

## Error Handling
| Error | Action | User message |
|-------|--------|--------------|

## Test Plan
| Case | Steps | Expected |
|------|-------|----------|

## Security Notes
[Token storage, log redaction]
```

---

# Next Skills

| Outcome | Recommended Skill |
|---------|-------------------|
| Build the MCP server | `mcp/mcp-server-generator` |
| Design tools consumed by client | `mcp/mcp-tool-generator` |
| Security review | `mcp/mcp-security-review` |
| Production patterns | `mcp/mcp-best-practices` |
| Agent workflow using tools | `ai/ai-workflow-builder` |

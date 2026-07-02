---
name: mcp-server-generator
description: >
  Generate a Model Context Protocol (MCP) server structure: transport layer, capability declarations, project layout, and bootstrap configuration for a new MCP integration. Use when working on scaffolding MCP servers, MCP transport setup.
metadata:
  apes-version: "1.1"
  category: mcp
---

# MCP Server Generator

# Purpose

Generate a Model Context Protocol (MCP) server structure: transport layer, capability declarations, project layout, and bootstrap configuration for a new MCP integration.

**Input:** Integration target (API, database, service), required capabilities (tools/resources/prompts), runtime preference (optional), security constraints  
**Output:** MCP Server Scaffold Specification with directory layout, capability manifest, and implementation checklist  
**Examples:** See [examples.md](examples.md) for worked input/output.

---

# Workflow

## Step 1: Define server scope

| Capability | Included | Rationale |
|------------|----------|-----------|
| Tools | Yes/No | Agent actions on external systems |
| Resources | Yes/No | Read-only data exposure |
| Prompts | Yes/No | Reusable prompt templates |
| Logging | Yes/No | Server lifecycle and debug |

One server = one bounded domain (e.g., "GitHub issues", not "all of GitHub").

## Step 2: Select transport and runtime

| Transport | Use case |
|-----------|----------|
| stdio | Local IDE integration, subprocess |
| SSE / Streamable HTTP | Remote hosted server |

| Runtime | Fit |
|---------|-----|
| TypeScript (SDK) | Node ecosystem, rapid iteration |
| Python (SDK) | Data/ML integrations |
| Other | Only when SDK unavailable |

Document why transport and runtime were chosen.

## Step 3: Design project layout

```text
mcp-server-[name]/
├── src/
│   ├── index.ts          # Server entry, transport binding
│   ├── server.ts         # MCP server instance and capability registration
│   ├── tools/            # Tool handlers
│   ├── resources/        # Resource providers (if any)
│   └── lib/              # Shared clients, auth, validation
├── package.json / pyproject.toml
├── README.md
└── .env.example
```

## Step 4: Declare capabilities manifest

| Capability | Name | Description | Auth required |
|------------|------|-------------|---------------|
| tool | `search_issues` | Search repo issues | OAuth token |
| resource | `repo://{owner}/{repo}` | Repository metadata | OAuth token |

Follow MCP naming: lowercase, snake_case for tools.

## Step 5: Plan authentication and config

| Secret | Source | Scope |
|--------|--------|-------|
| API key | Environment variable | Read-only |
| OAuth token | User-provided at connect | Per-user |

Never embed secrets in source. Document `.env.example` keys only.

## Step 6: Validate

Run Validation checklist.

---

# Decision Rules

| Condition | Action |
|-----------|--------|
| Scope spans multiple unrelated domains | Split into separate MCP servers |
| Remote access required | Use SSE/HTTP transport, not stdio only |
| Write operations on production data | Require explicit confirmation tool design; flag in security review |
| No official API client exists | Plan thin HTTP client in lib/ with rate limiting |
| PII exposure risk | Minimize resources; add mcp-security-review before deploy |
| >20 tools in one server | Group into sub-modules; consider splitting server |

---

# Validation

- [ ] Single bounded domain scope defined
- [ ] Transport and runtime selected with rationale
- [ ] Project layout documented
- [ ] Capability manifest with tool/resource names
- [ ] Auth strategy uses environment variables, not hardcoded secrets
- [ ] `.env.example` keys listed (no real values)
- [ ] Error handling pattern defined for tool failures
- [ ] README sections outlined (setup, config, capabilities)

---

# Anti-patterns

- **God server** — one MCP server wrapping an entire SaaS platform.
- **Secrets in repo** — API keys committed to source control.
- **Undocumented tools** — handlers without description and input schema.
- **stdio-only for SaaS** — local transport when users need remote hosting.
- **Missing health signal** — no way to verify server is correctly configured.

---

# Best Practices

- Start with 3–5 essential tools; expand based on usage.
- Use JSON Schema for all tool input definitions.
- Implement structured error responses (code, message, retryable flag).
- Version server capabilities in README changelog.
- Pair with mcp-tool-generator for detailed tool design.

---

# Output Structure

```markdown
# MCP Server Scaffold: [Server Name]

## Scope
[Domain boundary and capabilities included]

## Transport & Runtime
| Choice | Rationale |
|--------|-----------|

## Project Layout
[Directory tree]

## Capability Manifest
| Type | Name | Description | Auth |
|------|------|-------------|------|

## Configuration
| Variable | Required | Description |
|----------|----------|-------------|

## Implementation Checklist
- [ ] Bootstrap server entry
- [ ] Register capabilities
- [ ] Auth client in lib/
- [ ] Error handling middleware
- [ ] Integration test with MCP client

## Next Steps
[Link to tool design and security review]
```

---

# Next Skills

| Outcome | Recommended Skill |
|---------|-------------------|
| Design individual tools | `mcp/mcp-tool-generator` |
| Security review before deploy | `mcp/mcp-security-review` |
| Client integration in agent app | `mcp/mcp-client-generator` |
| Implementation patterns | `mcp/mcp-best-practices` |
| AI workflow integration | `ai/ai-workflow-builder` |

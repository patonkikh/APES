# MCP Server — Reference

Reference for [Model Context Protocol](https://modelcontextprotocol.io/) server design. Load when implementing scaffolds from this skill.

---

## Core Concepts

| Concept | Purpose |
|---------|---------|
| **Server** | Exposes capabilities to MCP clients |
| **Tools** | Callable functions (agent actions) |
| **Resources** | Read-only data exposure |
| **Prompts** | Reusable prompt templates |
| **Transport** | stdio (local) or SSE/HTTP (remote) |

---

## Server Scope Rules

- One server = **one bounded domain** (e.g., "GitHub issues", not "all of GitHub")
- Start with 3–5 essential tools; expand based on usage
- Split when >20 tools or multiple unrelated domains

---

## Tool Naming

| Rule | Example |
|------|---------|
| snake_case | `search_issues` |
| verb_noun pattern | `get_issue`, `add_comment` |
| Unique within server | No duplicate semantics |

---

## Tool Description (LLM-optimized)

Include in every tool description:

1. What it does (one sentence)
2. What it does **not** do (negative cases)
3. Required auth scope
4. Side effects (read vs write)

---

## JSON Schema Requirements

All tool inputs must have JSON Schema with:

- `type`, `properties`, `required`
- `enum` for fixed sets
- `maxLength` / `minimum` / `maximum` constraints
- `description` per field

---

## Error Response Format

```json
{
  "code": "RATE_LIMIT",
  "message": "GitHub API rate limit exceeded",
  "retryable": true
}
```

| Field | Required |
|-------|----------|
| code | Stable machine-readable identifier |
| message | Human-readable, no secrets |
| retryable | Boolean for client backoff |

---

## Authentication

| Pattern | Use when |
|---------|----------|
| Environment variable | Service tokens, API keys |
| User OAuth at connect | Per-user access |
| Never | Hardcoded secrets in source |

Document keys in `.env.example` only — no real values.

---

## Transport Selection

| Transport | Use case |
|-----------|----------|
| stdio | Local IDE (Cursor, Claude Desktop) |
| SSE / Streamable HTTP | Remote hosted server, team shared |

---

## Project Layout (TypeScript)

```text
mcp-server-<name>/
├── src/
│   ├── index.ts          # Entry + transport
│   ├── server.ts         # Capability registration
│   ├── tools/
│   ├── resources/        # Optional
│   └── lib/              # Auth, clients, validation
├── package.json
├── README.md
└── .env.example
```

---

## Pre-Deploy Checklist

- [ ] JSON Schema on all tools
- [ ] Structured errors
- [ ] Rate limiting on upstream API
- [ ] No secrets in repo
- [ ] Run `mcp/mcp-security-review`
- [ ] Contract tests for tool schemas

---

## Links

- [MCP Specification](https://modelcontextprotocol.io/)
- [MCP TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)

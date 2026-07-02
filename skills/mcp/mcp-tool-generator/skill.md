---
name: mcp-tool-generator
description: >
  Design MCP tools: input/output schemas, handler logic outline, idempotency rules, and agent-facing descriptions for reliable tool invocation. Use when working on MCP servers, MCP tools, MCP clients, or Model Context Protocol integrations.
metadata:
  apes-version: "1.1"
  category: mcp
---

# MCP Tool Generator

# Purpose

Design MCP tools: input/output schemas, handler logic outline, idempotency rules, and agent-facing descriptions for reliable tool invocation.

**Input:** Server scope, tool use cases, underlying API capabilities, safety constraints  
**Output:** MCP Tool Design Document per tool with JSON Schema, description, examples, and edge case handling

---

# Workflow

## Step 1: Identify tool candidates

Map agent tasks to tool operations:

| Agent task | Tool candidate | API operation | Risk level |
|------------|----------------|---------------|------------|
| Search documents | `search_docs` | GET /search | Low |
| Delete record | `delete_record` | DELETE /items/{id} | High |

Prefer read-only tools first; defer destructive operations until security review.

## Step 2: Define tool contract

Per tool document:

| Field | Requirement |
|-------|-------------|
| `name` | snake_case, verb_noun pattern (`create_issue`, `list_users`) |
| `description` | What it does, when to use, when NOT to use |
| `inputSchema` | JSON Schema with required fields and enums |
| `annotations` | readOnly, destructive, idempotent hints (if supported) |

## Step 3: Design input schema

```json
{
  "type": "object",
  "properties": {
    "query": { "type": "string", "description": "Search query, max 500 chars" },
    "limit": { "type": "integer", "minimum": 1, "maximum": 50, "default": 10 }
  },
  "required": ["query"]
}
```

Rules:

- Constrain string lengths and array sizes
- Use enums for fixed option sets
- Mark destructive tools explicitly in description

## Step 4: Design output format

Return structured JSON text content:

| Field | Purpose |
|-------|---------|
| `success` | Boolean outcome |
| `data` | Result payload |
| `error` | Structured error when success=false |
| `metadata` | Pagination cursor, request ID |

Keep responses token-efficient; paginate large results.

## Step 5: Handle edge cases

| Case | Behavior |
|------|----------|
| Empty result | Return success=true, data=[], message |
| Rate limited | Return retryable error with backoff hint |
| Invalid args | Return validation error before API call |
| Partial failure (batch) | Return per-item status array |
| Ambiguous match | Return candidates; do not auto-select destructive target |

## Step 6: Validate

Run Validation checklist.

---

# Decision Rules

| Condition | Action |
|-----------|--------|
| Destructive operation (delete, overwrite) | Require explicit `confirm` boolean arg; flag for security review |
| Tool duplicates existing tool | Merge or differentiate with clear description |
| API returns unstructured text | Parse and return structured JSON wrapper |
| Operation is slow (>10s) | Return job ID; add separate `get_status` tool |
| PII in response | Add redaction layer; document fields excluded |
| LLM may hallucinate IDs | Require human-readable label + ID; validate ID format |

---

# Validation

- [ ] Each tool has snake_case name following verb_noun pattern
- [ ] Description states when to use and when not to use
- [ ] Input JSON Schema with required fields and constraints
- [ ] Output structure documented with success/error paths
- [ ] Edge cases: empty, rate limit, invalid args covered
- [ ] Destructive tools have confirmation mechanism
- [ ] ≥2 example invocations per tool (happy path + edge case)
- [ ] Token-efficient response design (pagination for lists)

---

# Anti-patterns

- **Vague description** — "helps with data" without specifying inputs/outputs.
- **God tool** — single tool with 15 optional parameters covering unrelated actions.
- **Raw API passthrough** — exposing entire REST API without agent-friendly shaping.
- **Unbounded results** — returning thousands of records without pagination.
- **Silent destructive ops** — delete without confirmation arg or annotation.

---

# Best Practices

- One tool = one clear action; compose complex flows in agent workflow.
- Description written for LLM tool selection (include negative cases).
- Validate inputs in handler before external API call.
- Return consistent error schema across all tools.
- Pair with mcp-security-review before enabling write tools.

---

# Output Structure

```markdown
# MCP Tool Design: [Server Name]

## Tool: `tool_name`

### Description
[Agent-facing description with use/when-not-use]

### Input Schema
```json
{ ... }
```

### Output Schema
```json
{ ... }
```

### Examples
#### Happy path
**Input:** ...
**Output:** ...

#### Edge case
**Input:** ...
**Output:** ...

### Edge Case Handling
| Case | Behavior |
|------|----------|

### Risk Level
[Low / Medium / High]
```

---

# Next Skills

| Outcome | Recommended Skill |
|---------|-------------------|
| Implement server scaffold | `mcp/mcp-server-generator` |
| Security review for write tools | `mcp/mcp-security-review` |
| Client invocation patterns | `mcp/mcp-client-generator` |
| Production hardening | `mcp/mcp-best-practices` |
| Workflow orchestration | `ai/ai-workflow-builder` |

# MCP Tool Generator

Design MCP tools with JSON Schema, agent descriptions, output contracts, and edge case handling.

## Chain position

`mcp/mcp-server-generator` → **mcp-tool-generator** → `mcp/mcp-security-review`

## Example use

Input: GitHub MCP server needs issue search and create tools with rate limit handling.  
Output: `search_issues` and `create_issue` schemas, pagination, confirm flag on create, structured errors.

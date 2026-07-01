# MCP Client Generator

MCP client integration: connection lifecycle, capability discovery, invocation patterns, and error handling.

## Chain position

`mcp/mcp-server-generator` → **mcp-client-generator** → `mcp/mcp-security-review`

## Example use

Input: Cursor agent app connecting to local stdio MCP server for Jira with OAuth.  
Output: config template, discovery cache, wrapper API for `create_issue`/`search_issues`, retry policy.

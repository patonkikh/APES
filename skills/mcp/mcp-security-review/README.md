# MCP Security Review

Threat modeling and security review for MCP servers/clients: auth, tool risks, logging, and remediation.

## Chain position

`mcp/mcp-tool-generator` → **mcp-security-review** → `mcp/mcp-best-practices`

## Example use

Input: MCP server with database query and file write tools, multi-tenant SaaS deployment.  
Output: High finding on missing SQL parameterization, Medium on shared API key, remediation checklist, deploy blocked.

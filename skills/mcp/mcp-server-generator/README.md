# MCP Server Generator

Bootstrap MCP server structure: transport, capabilities, project layout, and configuration scaffold.

## Chain position

`ai/ai-solution-architect` → **mcp-server-generator** → `mcp/mcp-tool-generator`

## Example use

Input: expose BigQuery read-only queries to agents via MCP with stdio transport.  
Output: TypeScript project layout, two tools (`list_datasets`, `run_query`), env-based service account config.

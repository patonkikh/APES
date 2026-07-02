# MCP Best Practices — Worked Examples

---

## Example 1: Compliance assessment excerpt

### Input

```text
MCP server: 12 tools, TypeScript, stdio, no tests, no changelog
Client: hardcoded 3 tools, no retry logic
```

### Output (excerpt)

```markdown
# MCP Best Practices Report: github-issues

## Compliance Summary
| Area | Score (1-5) | Critical gaps |
|------|-------------|---------------|
| Server scope & naming | 4 | — |
| Tool design quality | 3 | Missing negative cases in descriptions |
| Testing | 1 | No contract tests |
| Observability | 2 | printf logging only |
| Versioning | 1 | No semver/changelog |

## Improvement Roadmap
| Priority | Item | Effort |
|----------|------|--------|
| P0 | Add contract tests for tool schemas | 2d |
| P1 | Structured logging + success rate metric | 1d |
| P1 | CHANGELOG + semver policy | 0.5d |
```

---

## Example 2: Production without integration tests

### Expected behavior

Block production per Decision Rule; minimum contract tests required.

---

## Example 3: Breaking schema change without version bump

### Expected behavior

High finding; require major version bump and migration guide.

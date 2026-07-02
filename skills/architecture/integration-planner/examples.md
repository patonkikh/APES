# Integration Planner — Worked Examples

---

## Example 1: Jira + Confluence integration plan

### Input

```text
Systems: Retro Generator, Jira Cloud, Confluence Cloud
Patterns needed: OAuth, read issues, write pages
Volume: 500 imports/day, 200 exports/day
```

### Output (excerpt)

```markdown
# Integration Plan: Retro Generator

## Integrations
| System | Direction | Pattern | Auth |
|--------|-----------|---------|------|
| Jira Cloud | Inbound | REST polling on job | OAuth 2.0 |
| Confluence | Outbound | REST create page | OAuth 2.0 |

## Sequence (export)
1. User triggers export
2. API validates retro ownership
3. ConfluenceAdapter createPage()
4. Store page URL on retro record

## Error Handling
| Error | Retry | Fallback |
|-------|-------|----------|
| Jira 429 | Exponential backoff | User message + retry |
| Confluence 403 | No retry | Prompt reconnect scope |

## Idempotency
Export uses `Idempotency-Key: retro_id + version` to prevent duplicate pages
```

---

## Example 2: Shared database integration

### Expected behavior

Flag anti-pattern; recommend API/event integration with rationale.

---

## Example 3: No auth strategy

### Expected behavior

Document OAuth scopes and token refresh before implementation.

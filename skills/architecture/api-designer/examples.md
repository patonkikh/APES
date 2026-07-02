# API Designer — Worked Examples

---

## Example 1: REST API for retro generation

### Input

```text
Resource: retros tied to Jira sprint
Operations: create generation job, get status, get result, list user retros
Auth: OAuth2 bearer
Consumers: web SPA
NFR: idempotent create, pagination on list
```

### Output (excerpt)

```markdown
# API Design: Retro Generator

## Resources
| Resource | Path | Description |
|----------|------|-------------|
| RetroJob | `/v1/retro-jobs` | Async generation job |
| Retro | `/v1/retros` | Completed retro artifact |

## Endpoints
| Method | Path | Description | Idempotent |
|--------|------|-------------|------------|
| POST | `/v1/retro-jobs` | Start generation from sprint_id | Yes (Idempotency-Key) |
| GET | `/v1/retro-jobs/{id}` | Job status | — |
| GET | `/v1/retros/{id}` | Get retro content | — |
| GET | `/v1/retros` | List user retros | cursor pagination |

## POST /v1/retro-jobs
**Request:**
```json
{"sprint_id": "string", "board_id": "string", "confluence_space": "string?"}
```
**Response 202:**
```json
{"job_id": "uuid", "status": "queued", "poll_url": "/v1/retro-jobs/{id}"}
```

## Error Model
| Code | HTTP | When |
|------|------|------|
| SPRINT_NOT_FOUND | 404 | Invalid sprint_id |
| JIRA_AUTH_EXPIRED | 401 | Token refresh needed |
```

---

## Example 2: Implementation in PRD — push back

### Input

```text
FR: Use GraphQL with 15 nested mutations for admin panel
```

### Expected behavior

Separate product behavior from API design; if API skill invoked without architecture context, note dependency on `solution-architecture`.

---

## Example 3: Missing error contract

### Bad output

Endpoints listed without error codes.

### Correct

Every mutating endpoint includes error table with stable `code` field for client handling.

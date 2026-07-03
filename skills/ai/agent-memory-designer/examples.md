# Agent Memory Designer — Examples

---

## Example 1: Support chatbot with session memory

### Input

```text
B2B SaaS support bot. Users return weekly. Need to remember account tier,
open tickets, and preferences. GDPR applies. Budget: low recall cost.
```

### Output (excerpt)

```markdown
## Storage Tiers
| Type | Store | TTL |
|------|-------|-----|
| Session | Redis | 24h |
| Profile | Postgres JSONB | Account lifetime |
| Episodic | Vector (pgvector) | 90 days |

## Read Pipeline
Hybrid: key lookup for tier + ticket IDs; similarity top-3 for past issues.
Max 800 tokens injected.

## Hygiene
User "delete my data" → purge profile + episodic by user_id within 24h.
```

---

## Example 2: Stop — no identity model

### Input

```text
Anonymous public FAQ bot, no login.
```

### Expected behavior

```markdown
## Clarification
Session-only working memory. No cross-session semantic store.
Episodic memory not recommended without user identity and consent.
```

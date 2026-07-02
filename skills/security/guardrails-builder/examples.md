# Guardrails Builder — Worked Examples

---

## Example 1: Customer chatbot guardrails stack

### Input

```text
App: External support chatbot
Risks from threat model: injection (T1), PII leak (T5), off-topic requests (T6)
Latency budget: +200ms max for guardrails
```

### Output (excerpt)

```markdown
# Guardrails Design: Support Chatbot

## Layered Controls
| Stage | Control | Implementation |
|-------|---------|----------------|
| Pre-LLM input | Regex + classifier for injection patterns | Block or sanitize |
| Pre-LLM input | PII detect on user message | Redact emails/phones |
| Prompt structure | Trusted/untrusted delimiters | Template change |
| Post-LLM output | JSON schema validation | Reject malformed |
| Post-LLM output | Topic allowlist classifier | Refuse off-topic |
| Tool gate | Param schema + scope check | Before ticket update |

## Refusal Behavior
```text
If request is out-of-scope or high-risk:
Return: {"reply": "I can only help with [topics].", "escalate": true}
```

## Latency Budget
| Control | p95 cost |
|---------|----------|
| Input classifier | 80ms |
| Output validator | 40ms |
| **Total** | 120ms ✓ |

## Monitoring
- Alert: guardrail block rate >20% in 5m (possible attack or mis-tune)
- Log: pattern ID, never log full PII
```

---

## Example 2: Regex-only stack — rejected

### Input

```text
Single regex blocking "ignore instructions"
```

### Expected behavior

Flag as insufficient; recommend layered defenses per Best Practices.

---

## Example 3: Safety stripped for latency

### Expected behavior

Reject optimization that removes refusal or delimiter rules; safety > latency per Decision Rules.

# Data Flow Analyzer — Worked Examples

---

## Example 1: PII flow for OAuth tokens

### Input

```text
Flow: User OAuth → token stored → worker reads Jira → AI prompt → Confluence export
Compliance: GDPR, tokens are personal data
```

### Output (excerpt)

```markdown
# Data Flow Analysis: Retro Generator

## Data Flows
| ID | Data | From | To | Classification | Encryption |
|----|------|------|-----|----------------|------------|
| DF-1 | OAuth tokens | Jira | API DB | Personal | AES at rest |
| DF-2 | Sprint issues | Jira | Worker | Business | TLS in transit |
| DF-3 | Retro draft | Worker | DB | Business | AES at rest |
| DF-4 | Prompt payload | Worker | LLM API | May contain names | TLS + DPA |

## Trust Boundaries
```text
[Browser] → [API] → [DB]
              ↓
           [Worker] → [LLM provider]
```

## Risks
| Flow | Risk | Control |
|------|------|---------|
| DF-4 | PII in prompts | Scrub before LLM call |
| DF-1 | Token leak in logs | Redact logging |
```

---

## Example 2: Missing classification

### Expected behavior

Classify each data element before sign-off.

---

## Example 3: LLM flow omitted

### Expected behavior

Include external AI provider as trust boundary with data minimization notes.

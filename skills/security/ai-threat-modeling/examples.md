# AI Threat Modeling — Worked Examples

---

## Example 1: RAG customer support bot

### Input

```text
Assets: customer tickets (PII), knowledge base, LLM API keys, admin dashboard
Flow: user chat → retrieval → LLM → response with optional ticket update tool
Deployment: SaaS multi-tenant
```

### Output (excerpt)

```markdown
# AI Threat Model: Support RAG Bot

## Assets
| ID | Asset | Sensitivity |
|----|-------|-------------|
| A1 | Customer PII in tickets | High |
| A2 | KB documents (may contain internal data) | Medium |
| A3 | LLM API keys | Critical |
| A4 | Cross-tenant vector index | Critical |

## Threats (STRIDE + AI-specific)
| ID | Threat | Asset | Likelihood | Impact | Risk |
|----|--------|-------|------------|--------|------|
| T1 | Prompt injection via ticket text | A1 | High | High | Critical |
| T2 | Indirect injection via KB doc | A2 | Medium | High | High |
| T3 | Tenant A retrieves Tenant B chunks | A4 | Low | Critical | High |
| T4 | Tool abuse: update wrong ticket | A1 | Medium | High | High |

## Controls
| Threat | Control | Status |
|--------|---------|--------|
| T1 | Delimiters + input filter | Planned |
| T3 | tenant_id filter on every retrieval query | Required |
| T4 | Tool param validation + user confirmation | Planned |

## Attack Tree (T3)
```text
Cross-tenant leak
├── Missing tenant filter in vector query [HIGH]
├── Embedding model poisoning [LOW]
└── Admin misconfiguration [MEDIUM]
```
```

---

## Example 2: No tools — scope reduction

### Input

```text
Read-only Q&A, no write tools, single tenant
```

### Expected behavior

Deprioritize tool abuse threats; elevate injection and data disclosure; mark LLM07/08 N/A with justification.

---

## Example 3: Threat without control

### Expected behavior

Critical/High risks without controls flagged as open; link to `security/guardrails-builder` and `owasp-llm-reviewer`.

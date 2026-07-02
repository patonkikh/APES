# AI Governance Advisor — Worked Examples

---

## Example 1: Enterprise AI policy framework

### Input

```text
Company: 500-person SaaS, shipping customer-facing RAG bot
Regulatory: GDPR, SOC2 in progress
Teams: product, eng, legal, security
```

### Output (excerpt)

```markdown
# AI Governance Framework: Customer RAG Bot

## Governance Structure
| Role | Responsibility |
|------|----------------|
| AI Product Owner | Use case approval, risk acceptance |
| Security Lead | Threat model + OWASP review sign-off |
| Legal/Privacy | DPIA, data retention, subprocessors |
| MLOps/Eng | Eval gates, incident response |

## Policies Required
| Policy | Scope | Status |
|--------|-------|--------|
| Acceptable Use | Employee + customer-facing AI | Draft |
| Data Handling | PII in prompts/logs/RAG corpus | Required |
| Model Change Management | Prompt/index/model updates | Required |
| Incident Response | Hallucination, leak, injection | Required |

## Risk Tiering
| Tier | Criteria | Approval |
|------|----------|----------|
| High | Customer PII, external-facing | Exec + Legal |
| Medium | Internal copilot | Director |
| Low | Dev-only experiments | Team lead |

## Compliance Mapping
| Control | SOC2 CC | GDPR Article |
|---------|---------|--------------|
| Access logging | CC6.1 | Art. 30 |
| Data minimization in RAG | CC6.7 | Art. 5(1)(c) |

## Review Cadence
- Quarterly policy review
- Re-approval on new data source or model provider change
```

---

## Example 2: No ownership

### Input

```text
We have AI features but no one owns governance
```

### Expected behavior

Recommend RACI with named roles (even if TBD hires); flag as governance gap.

---

## Example 3: Checkbox policy

### Bad

"Follow AI ethics" with no measurable controls.

### Correct

Link policies to concrete controls: eval gates, access reviews, retention limits.

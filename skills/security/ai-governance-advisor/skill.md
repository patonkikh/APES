---
name: ai-governance-advisor
description: >
  Define AI governance policies, roles, compliance mappings, and operational controls for responsible LLM deployment aligned with organizational and regulatory requirements. Use when working on LLM security, OWASP reviews, threat modeling, guardrails, or prompt injection.
metadata:
  apes-version: "1.1"
  category: security
---

# AI Governance Advisor

# Purpose

Define AI governance policies, roles, compliance mappings, and operational controls for responsible LLM deployment aligned with organizational and regulatory requirements.

**Input:** Organization context, jurisdiction/regulations, OWASP review or threat model (optional), use case catalog, risk appetite  
**Output:** AI Governance Framework with policies, RACI matrix, compliance mapping, audit checklist, and lifecycle gates

---

# Workflow

## Step 1: Inventory AI use cases

Catalog deployed and planned AI systems:

| Use case | Data class | Users | Model type | Risk tier |
|----------|------------|-------|------------|-----------|

Risk tier: Tier 1 (low — internal FAQ), Tier 2 (medium — customer-facing), Tier 3 (high — decisions affecting people/money).

## Step 2: Define governance principles

Establish organization-level commitments:

- Transparency and explainability expectations
- Human oversight requirements by risk tier
- Data minimization and retention limits
- Prohibited use cases (e.g., covert profiling, unauthorized surveillance)
- Third-party model and vendor due diligence

## Step 3: Map regulatory and standard obligations

| Regulation/Standard | Applicability | Key requirements | Current gap |
|---------------------|---------------|------------------|-------------|
| GDPR | [yes/no] | DPIA, lawful basis, erasure | |
| EU AI Act | [yes/no] | Risk classification, documentation | |
| SOC 2 | [yes/no] | Access control, logging | |
| Industry-specific | [specify] | | |

Cross-reference OWASP LLM findings if available.

## Step 4: Define policy documents

| Policy | Scope | Owner | Review cycle |
|--------|-------|-------|--------------|
| Acceptable Use | All employees | | Annual |
| Data Handling for AI | Engineering | | Semi-annual |
| Model Procurement | Procurement + Legal | | Per vendor |
| Incident Response for AI | Security | | Annual |

## Step 5: Build RACI matrix

| Activity | Responsible | Accountable | Consulted | Informed |
|----------|-------------|-------------|-----------|----------|
| Use case approval | | | | |
| Threat modeling | | | | |
| Production deployment | | | | |
| Model change review | | | | |
| AI incident response | | | | |

## Step 6: Define lifecycle gates

Gate requirements by risk tier:

| Gate | Tier 1 | Tier 2 | Tier 3 |
|------|--------|--------|--------|
| Threat model | Optional | Required | Required |
| OWASP review | Optional | Required | Required + sign-off |
| Legal/compliance review | No | If PII | Required |
| Human oversight design | No | Recommended | Required |
| Post-deploy monitoring | Basic | Standard | Enhanced |

## Step 7: Create audit and monitoring checklist

Operational controls to verify ongoing compliance:

- Model and prompt change log review
- Access and API key rotation
- User complaint and override tracking
- Vendor SLA and subprocessors review

## Step 8: Validate

Run Validation checklist.

---

# Decision Rules

| Condition | Action |
|-----------|--------|
| No OWASP review or threat model | Proceed with governance baseline; flag security artifacts as prerequisite for Tier 2+ |
| EU AI Act high-risk use case | Escalate to legal review; add conformity assessment requirements |
| No designated AI owner | Stop; require Accountable role assignment before policy finalization |
| Multiple jurisdictions | Map strictest requirement per data subject location |
| Tier 3 use case without human oversight | Mark as policy violation; block deployment recommendation |
| Vendor-hosted model with training on customer data | Require DPA and opt-out clause in procurement policy |

---

# Validation

- [ ] All in-scope use cases cataloged with risk tier
- [ ] Governance principles cover transparency, oversight, and prohibited uses
- [ ] Applicable regulations mapped with gap identification
- [ ] Core policy documents listed with owners and review cycles
- [ ] RACI matrix covers approval, deployment, change, and incident response
- [ ] Lifecycle gates differentiated by risk tier
- [ ] Audit checklist includes monitoring and change management
- [ ] No legal advice presented as definitive — flagged for legal review where needed

---

# Anti-patterns

- **Governance theater** — policies exist but no lifecycle gates enforce them.
- **One-size-fits-all tiers** — same controls for internal FAQ and credit scoring.
- **Missing ownership** — RACI with empty Accountable column.
- **Static compliance mapping** — ignoring regulatory updates (EU AI Act phases).
- **Decoupled from engineering** — governance docs not linked to threat model and OWASP findings.

---

# Best Practices

- Align risk tiers with ISO 42001 AI management system concepts where applicable.
- Integrate governance gates into existing SDLC (design review, release checklist).
- Maintain AI system registry as single source of truth for audits.
- Connect policy violations to incident response playbooks.

---

# Output Structure

```markdown
# AI Governance Framework: [Organization Name]

## Use Case Registry
| ID | Use case | Risk tier | Status |
|----|----------|-----------|--------|

## Governance Principles
1. [Principle with rationale]

## Compliance Mapping
| Standard | Applies | Requirements | Gap | Action |
|----------|---------|--------------|-----|--------|

## Policy Catalog
| Policy | Owner | Review cycle | Status |
|--------|-------|--------------|--------|

## RACI Matrix
[Table]

## Lifecycle Gates
| Gate | Tier 1 | Tier 2 | Tier 3 |
|------|--------|--------|--------|

## Audit Checklist
- [ ] [Control to verify]

## Open Items
- [ ] [Legal review needed]
```

---

# Next Skills

| Outcome | Recommended Skill |
|---------|-------------------|
| New use case threat analysis | `security/ai-threat-modeling` |
| Security gap remediation | `security/owasp-llm-reviewer` |
| Implement technical controls | `security/guardrails-builder` |
| Document governance decisions | `architecture/adr-generator` |
| Product requirements for AI features | `product/prd-generator` |

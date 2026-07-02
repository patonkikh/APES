---
name: owasp-llm-reviewer
description: >
  Review an AI/LLM application against the OWASP Top 10 for LLM Applications, produce gap analysis, and prioritize remediation actions. Use when working on OWASP LLM Top 10, AI security audits, LLM gap analysis.
metadata:
  apes-version: "1.1"
  category: security
---

# OWASP LLM Reviewer

# Purpose

Review an AI/LLM application against the OWASP Top 10 for LLM Applications, produce gap analysis, and prioritize remediation actions.

**Input:** Application description, architecture, guardrails design (optional), threat model (optional), deployment context  
**Output:** OWASP LLM Review Report with per-category assessment, findings, severity, and remediation roadmap  
**References:** See [references.md](references.md) for domain cheat sheets.
**Examples:** See [examples.md](examples.md) for worked input/output.

---

# Workflow

## Step 1: Establish review scope

Document:

- Application type (chatbot, RAG, agent, code assistant)
- Deployment model (SaaS API, self-hosted, hybrid)
- Data classification handled
- Integrations (tools, plugins, external APIs)

## Step 2: Assess input and output risks (LLM01–LLM02)

| Category | Key checks |
|----------|------------|
| LLM01 Prompt Injection | Direct/indirect defenses, trusted/untrusted separation, tool isolation |
| LLM02 Insecure Output Handling | Output encoding, validation before tools/SQL/shell/HTML, schema enforcement |

Document per category: | Control present | Evidence | Gap |

## Step 3: Assess data and supply chain (LLM03, LLM05–LLM06)

| Category | Key checks |
|----------|------------|
| LLM03 Training Data Poisoning | Source validation, embedding integrity (N/A if no training/RAG) |
| LLM05 Supply Chain | Model/plugin provenance, dependency scanning, vendor SLAs |
| LLM06 Sensitive Info Disclosure | PII in prompts/logs, prompt leakage tests, RAG tenant isolation |

## Step 4: Assess availability, plugins, and agency (LLM04, LLM07–LLM08)

| Category | Key checks |
|----------|------------|
| LLM04 Model DoS | Rate limits, token budgets, timeouts, cost controls |
| LLM07 Insecure Plugin Design | Least privilege, param validation, per-tool auth |
| LLM08 Excessive Agency | Autonomy scope, human approval, kill-switch |

## Step 5: Assess trust and model protection (LLM09–LLM10)

| Category | Key checks |
|----------|------------|
| LLM09 Overreliance | Citations, confidence indicators, human review for high-stakes |
| LLM10 Model Theft | API access controls, extraction surface (N/A if no proprietary model) |

## Step 6: Summarize and prioritize

Aggregate findings into remediation roadmap. Run Validation checklist.

---

# Decision Rules

| Condition | Action |
|-----------|--------|
| No guardrails design available | Review against OWASP controls only; flag unverified controls |
| No custom training/RAG | Mark LLM03 and LLM10 partial or N/A with justification |
| Agent with external tools | Deep-review LLM07 and LLM08; elevate priority |
| Public internet-facing | Elevate LLM01, LLM04, LLM06 to mandatory pass |
| Finding with no owner | Mark as open; do not mark category as pass |
| Multiple Critical gaps in one category | Category status = Fail regardless of partial controls |

---

# Validation

- [ ] All 10 OWASP LLM categories assessed (or marked N/A with reason)
- [ ] Each category has Pass/Partial/Fail/N/A status
- [ ] Findings include severity (Critical/High/Medium/Low)
- [ ] Evidence cited for each finding (config, design doc, test result)
- [ ] Remediation actions are specific and assignable
- [ ] Cross-references to threat model and guardrails where available
- [ ] Residual risk summary included
- [ ] No implementation code (framework-specific)

---

# Anti-patterns

- **Checkbox review** — marking Pass without evidence.
- **Ignoring N/A justification** — skipping categories without documenting why.
- **Findings without remediation** — listing gaps with no actionable fix.
- **Conflating provider and app responsibility** — unclear shared responsibility for API-hosted models.
- **One-time review** — no recommendation for re-review triggers.

---

# Best Practices

- Use OWASP LLM Top 10 2025 as canonical reference.
- Cross-reference findings with existing threat model IDs.
- Prioritize by exploitability × business impact, not category order.
- Include verification criteria for each remediation (how to confirm fixed).
- Schedule re-review after model change, new tool integration, or major prompt update.
- Distinguish inherited provider controls from application-owned controls.

---

# Output Structure

```markdown
# OWASP LLM Review: [Application Name]

## Scope
- **Type:** [chatbot | RAG | agent | other]
- **Deployment:** [model]
- **Review date:** [date]

## Summary
| Category | Status | Critical | High | Medium | Low |
|----------|--------|----------|------|--------|-----|

## Findings by Category

### LLM01 — Prompt Injection
**Status:** Pass | Partial | Fail
| Finding | Severity | Evidence | Remediation | Owner |
|---------|----------|----------|-------------|-------|

[Repeat for LLM02–LLM10]

## Remediation Roadmap
| Priority | Finding | Action | Target date |
|----------|---------|--------|-------------|

## Residual Risks
| Risk | Accepted by | Review date |
|------|-------------|-------------|

## Re-review Triggers
- [ ] [Event that requires new review]
```

---

# Next Skills

| Outcome | Recommended Skill |
|---------|-------------------|
| Implement missing controls | `security/guardrails-builder` |
| Update threat model | `security/ai-threat-modeling` |
| Policy and compliance framework | `security/ai-governance-advisor` |
| Injection test coverage | `security/prompt-injection-detector` |
| Architecture hardening | `architecture/architecture-review` |

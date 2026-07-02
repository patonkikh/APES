---
name: ai-threat-modeling
description: >
  Produce a threat model for AI/LLM applications using STRIDE and LINDDUN adapted for model inference, RAG, agents, and tool use. Use when working on LLM security, OWASP reviews, threat modeling, guardrails, or prompt injection.
metadata:
  apes-version: "1.1"
  category: security
---

# AI Threat Modeling

# Purpose

Produce a threat model for AI/LLM applications using STRIDE and LINDDUN adapted for model inference, RAG, agents, and tool use.

**Input:** System architecture (containers, data flows), AI pipeline description, asset inventory, trust boundaries  
**Output:** AI Threat Model document with assets, threats, attack trees, risk ratings, and control recommendations
**Examples:** See [examples.md](examples.md) for worked input/output.

---

# Workflow

## Step 1: Define scope and assets

Document system boundary and AI-specific assets:

| Asset | Type | Sensitivity | Owner |
|-------|------|-------------|-------|

Include: system prompts, fine-tuned weights, embeddings, vector stores, conversation logs, API keys, user PII, tool credentials.

## Step 2: Draw trust boundaries

Map data flow across boundaries:

- User → application → LLM provider
- Application → RAG retrieval → document store
- Agent → tools/APIs → external systems
- Training/fine-tuning pipeline (if applicable)

## Step 3: Apply STRIDE per component

For each container/component, enumerate threats:

| Component | Spoofing | Tampering | Repudiation | Info disclosure | DoS | Elevation |
|-----------|----------|-----------|-------------|-----------------|-----|-----------|

Add AI-specific variants: prompt injection, model inversion, training data poisoning, adversarial inputs.

## Step 4: Apply LINDDUN for privacy

For flows involving personal data:

| Link | Leakage | Identifiability | Non-repudiation | Detectability | Disclosure | Unawareness | Non-compliance |
|------|---------|-----------------|-------------------|---------------|------------|-------------|----------------|

Focus on: conversation retention, embedding reversibility, cross-user retrieval leakage.

## Step 5: Build attack trees

For top risks, decompose attack paths:

```
Goal: Exfiltrate system prompt
├── Direct injection in user input
├── Indirect via poisoned RAG document
└── Tool output manipulation
```

## Step 6: Rate and prioritize

Score each threat: Likelihood (1–5) × Impact (1–5) = Risk score.

| Threat ID | STRIDE/LINDDUN | Likelihood | Impact | Risk | Existing control |
|-----------|----------------|------------|--------|------|------------------|

## Step 7: Recommend controls

Map threats to mitigations: preventive, detective, corrective. Reference OWASP LLM Top 10 where applicable.

## Step 8: Validate

Run Validation checklist.

---

# Decision Rules

| Condition | Action |
|-----------|--------|
| No architecture diagram | Stop; request container/data-flow diagram or run `architecture/container-diagram-builder` |
| Agent with tool access | Expand elevation and tampering analysis for tool abuse |
| RAG over private documents | Prioritize LINDDUN info disclosure and cross-tenant leakage |
| Third-party LLM API | Include provider trust boundary and data residency threats |
| Fine-tuning on user data | Add training data poisoning and membership inference threats |
| Risk score ≥ 15 without control | Mark as blocker; require mitigation before production |

---

# Validation

- [ ] All AI-specific assets listed with sensitivity classification
- [ ] Trust boundaries cover LLM provider, RAG, tools, and storage
- [ ] STRIDE applied to every in-scope component
- [ ] LINDDUN applied where PII or conversation data flows
- [ ] Top 5 risks have attack trees or attack path descriptions
- [ ] Each High/Critical risk has recommended control
- [ ] Controls traceable to OWASP LLM categories where relevant
- [ ] Residual risks documented explicitly

---

# Anti-patterns

- **Generic STRIDE without AI context** — missing prompt injection, RAG poisoning, tool abuse.
- **Threats without attack paths** — abstract labels without exploitable scenarios.
- **Ignoring supply chain** — overlooking model provider, plugin, and embedding API risks.
- **Single-boundary model** — treating the LLM as a black box with no internal data flows.
- **Controls without verification** — recommending "input validation" without test criteria.

---

# Best Practices

- Combine STRIDE (security) and LINDDUN (privacy) in one unified model.
- Use data-flow diagrams aligned with C4 container level.
- Prioritize threats by exploitability in the actual deployment (internet-facing vs internal).
- Link each control to a measurable verification method (test, monitor, audit).
- Re-run threat model when adding tools, RAG sources, or model changes.
- Involve domain owners for LINDDUN unawareness and compliance gaps.

---

# Output Structure

```markdown
# AI Threat Model: [System Name]

## Scope
- **In scope:** [components]
- **Out of scope:** [components]

## Assets
| Asset | Sensitivity | Location |
|-------|-------------|----------|

## Trust Boundaries
[Diagram or boundary table]

## STRIDE Analysis
| Component | Threats | Risk | Controls |
|-----------|---------|------|----------|

## LINDDUN Analysis
| Data flow | Privacy threats | Risk | Controls |
|-----------|-----------------|------|----------|

## Attack Trees
### [Top threat name]
[Tree or path description]

## Risk Register
| ID | Threat | Score | Status | Owner |
|----|--------|-------|--------|-------|

## Open Items
- [ ] [Unmitigated threat]
```

---

# Next Skills

| Outcome | Recommended Skill |
|---------|-------------------|
| Test injection attack paths | `security/prompt-injection-detector` |
| Design pipeline controls | `security/guardrails-builder` |
| OWASP gap analysis | `security/owasp-llm-reviewer` |
| Governance and policy framework | `security/ai-governance-advisor` |
| Document architecture decisions | `architecture/adr-generator` |

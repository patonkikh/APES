# Guardrails Builder

# Purpose

Design layered input and output guardrails for LLM applications: filters, classifiers, policy rules, tool gates, and human-in-the-loop triggers.

**Input:** Threat model or injection report, application flow, policy requirements, latency/cost constraints  
**Output:** Guardrails Design document with layer architecture, rule catalog, integration points, and fallback behaviors

---

# Workflow

## Step 1: Define guardrail objectives

For each pipeline stage, specify what must be enforced:

| Objective | Stage | Failure mode if missing |
|-----------|-------|-------------------------|
| Block injection | Pre-LLM | System prompt override |
| Enforce output schema | Post-LLM | Malformed or unsafe responses |
| Restrict tool calls | Tool gate | Unauthorized actions |
| Detect PII leakage | Post-LLM | Compliance violation |

## Step 2: Map pipeline layers

Design defense-in-depth:

```
Input → [Input filter] → [Prompt assembly] → LLM → [Output validator] → [Tool gate] → Response
                              ↑                        ↑
                         [Policy engine]          [Policy engine]
```

Document where each control executes (client, API gateway, application, model wrapper).

## Step 3: Design input guardrails

| Control | Type | Trigger | Action | Latency budget |
|---------|------|---------|--------|----------------|

Types: regex/heuristic, ML classifier, allowlist/denylist, length limits, encoding normalization.

## Step 4: Design output guardrails

| Control | Type | Validates | Action on fail |
|---------|------|-----------|----------------|

Include: schema validation, toxicity/PII detection, topic boundary checks, citation verification for RAG.

## Step 5: Design tool and action guardrails

For agent/tool-enabled apps:

| Tool | Allowed params | Auth scope | Confirmation required |
|------|----------------|------------|----------------------|

Define: parameter validation, rate limits, destructive action blocks, human approval triggers.

## Step 6: Define fallback behaviors

| Failure type | User-facing message | Internal action | Escalation |
|--------------|---------------------|-----------------|------------|

Options: block silently, generic refusal, partial response, human handoff, circuit breaker.

## Step 7: Specify observability

Define metrics and alerts:

- Block rate by category
- False-positive reports
- Latency overhead per layer
- Guardrail bypass attempts

## Step 8: Validate

Run Validation checklist.

---

# Decision Rules

| Condition | Action |
|-----------|--------|
| No threat model or injection report | Run `security/prompt-injection-detector` or `security/ai-threat-modeling` first |
| Latency budget < 100ms total | Prefer lightweight heuristics; defer ML classifiers to async |
| Agent with write/delete tools | Mandatory human-in-the-loop for destructive operations |
| Regulated domain (health, finance) | Add PII/PHI output scanning; document audit trail |
| High false-positive tolerance unacceptable | Use shadow mode before enforcement |
| Single LLM call, no tools | Focus on input/output layers; skip tool gate |

---

# Validation

- [ ] Every Critical/High threat from input has mapped guardrail
- [ ] Input and output layers both addressed
- [ ] Tool guardrails defined if agents/tools present
- [ ] Fallback behavior specified for each control failure
- [ ] Latency and cost impact estimated per layer
- [ ] False-positive handling strategy documented
- [ ] Observability metrics defined
- [ ] No implementation code (framework-specific)

---

# Anti-patterns

- **Single-layer defense** — relying only on system prompt instructions.
- **Block without logging** — no visibility into attack attempts or tuning data.
- **Opaque refusals** — generic errors with no internal categorization for ops.
- **Guardrails after tools execute** — validating output after irreversible action.
- **Unbounded regex lists** — unmaintainable patterns with high false-positive rate.

---

# Best Practices

- Align layers with OWASP LLM recommendations (LLM01 input, LLM02 output handling).
- Run new rules in log-only (shadow) mode before enforcement.
- Keep policy rules externalized (config/database) for updates without redeploy.
- Separate user-facing refusal messages from internal reason codes.
- Test guardrails with the injection detection test suite.
- Document bypass procedures for authorized admin/debug use only.

---

# Output Structure

```markdown
# Guardrails Design: [Application Name]

## Objectives
| Objective | Priority | Stage |
|-----------|----------|-------|

## Architecture
[Layer diagram and integration points]

## Input Guardrails
| ID | Control | Trigger | Action | Latency |
|----|---------|---------|--------|---------|

## Output Guardrails
| ID | Control | Validates | Action | Latency |
|----|---------|-----------|--------|---------|

## Tool Guardrails
| Tool | Constraints | Approval |
|------|-------------|----------|

## Fallback Matrix
| Failure | User message | Internal action |
|---------|--------------|-----------------|

## Observability
| Metric | Threshold | Alert |
|--------|-----------|-------|

## Open Questions
- [ ] [Policy decision needed]
```

---

# Next Skills

| Outcome | Recommended Skill |
|---------|-------------------|
| OWASP compliance check | `security/owasp-llm-reviewer` |
| Update threat model with controls | `security/ai-threat-modeling` |
| Governance policy alignment | `security/ai-governance-advisor` |
| Refine prompts for defense | `ai/prompt-engineer` |
| Red-team injection patterns | `security/prompt-injection-detector` |

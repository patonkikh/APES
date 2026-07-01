# Security Skills Chain — Stage 2

**Последнее обновление:** 2026-07-01

## Primary pipeline

```text
ai-threat-modeling → prompt-injection-detector → guardrails-builder
  → owasp-llm-reviewer → ai-governance-advisor
```

## Bridge from AI

`ai/prompt-reviewer` → `security/prompt-injection-detector` (safety escalation)

## Bridge from Architecture

`architecture/data-flow-analyzer` → `security/ai-threat-modeling` (PII/sensitive flows)

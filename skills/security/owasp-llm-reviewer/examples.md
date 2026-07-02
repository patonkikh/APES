# OWASP LLM Reviewer — Worked Examples

Reference review outputs. Full structure follows Output Structure in `skill.md`.

---

## Example 1: RAG chatbot — partial pass

### Input

```text
Application: Internal HR policy Q&A chatbot
Deployment: Azure OpenAI, company SSO
Data: HR PDFs in SharePoint, indexed nightly
Tools: None (retrieval + generation only)
Guardrails: Basic content filter on output
Threat model: Not provided
```

### Output (excerpt)

```markdown
# OWASP LLM Review: HR Policy Q&A Chatbot

## Scope
- **Type:** RAG chatbot
- **Deployment:** Azure OpenAI (managed API)
- **Review date:** 2026-07-01

## Summary
| Category | Status | Critical | High | Medium | Low |
|----------|--------|----------|------|--------|-----|
| LLM01 Prompt Injection | Partial | 0 | 1 | 1 | 0 |
| LLM02 Insecure Output | Partial | 0 | 0 | 1 | 0 |
| LLM06 Sensitive Disclosure | Fail | 1 | 0 | 0 | 0 |
| LLM09 Overreliance | Partial | 0 | 0 | 1 | 0 |

## Findings by Category

### LLM01 — Prompt Injection
**Status:** Partial
| Finding | Severity | Evidence | Remediation | Owner |
|---------|----------|----------|-------------|-------|
| No delimiter between system and retrieved chunks | High | Architecture doc shows raw chunk concatenation | Separate trusted/untrusted blocks; instruct model to ignore instructions in documents | Engineering |
| No adversarial test suite | Medium | No test artifacts provided | Create 20-case injection suite per prompt-injection-detector | Security |

### LLM06 — Sensitive Info Disclosure
**Status:** Fail
| Finding | Severity | Evidence | Remediation | Owner |
|---------|----------|----------|-------------|-------|
| HR docs may contain SSN/salary in chunks | Critical | Corpus includes unredacted compensation policy PDFs | PII scrub at ingest; block PII patterns in retrieval | Data Engineering |

## Remediation Roadmap
| Priority | Finding | Action | Target date |
|----------|---------|--------|-------------|
| P0 | SSN in RAG corpus | PII scrub pipeline + re-index | Week 1 |
| P1 | Injection delimiters | Restructure prompt + retest | Week 2 |

## Re-review Triggers
- [ ] New document source added to corpus
- [ ] Prompt template change
- [ ] Model version upgrade
```

---

## Example 2: Agent with tools — elevated review

### Input

```text
Application: Sales assistant with CRM read/write and email send tools
Deployment: Self-hosted, GPT-4 class model
Autonomy: Can send emails without human approval
```

### Expected behavior

Apply Decision Rules: agent with external tools → deep-review LLM07 and LLM08; elevate priority.

Key expected findings (minimum):

| Category | Expected status | Rationale |
|----------|-----------------|-----------|
| LLM07 Insecure Plugin Design | Fail or Partial | Write tools without approval gate |
| LLM08 Excessive Agency | Fail | Email send without human-in-the-loop |
| LLM01 Prompt Injection | Partial minimum | Tool coercion vectors |

---

## Example 3: Checkbox review anti-pattern

### Bad output (do not produce)

```markdown
### LLM01 — Prompt Injection
**Status:** Pass
No issues found.
```

### Correct output

```markdown
### LLM01 — Prompt Injection
**Status:** Partial
| Finding | Severity | Evidence | Remediation | Owner |
|---------|----------|----------|-------------|-------|
| Control claimed but not verified | Medium | "We use delimiters" — no config or test log cited | Provide prompt template + 5 injection test results | Engineering |
```

Every Pass/Partial/Fail must cite **evidence** (config, design doc, or test result).

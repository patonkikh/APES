# OWASP LLM Top 10 — Reference

Quick reference for [OWASP LLM Top 10](https://owasp.org/www-project-top-10-for-large-language-model-applications/). Use during review; cite version year in report.

---

## LLM01 — Prompt Injection

**Risk:** Manipulating LLM via crafted inputs to override instructions.

| Vector | Description |
|--------|-------------|
| Direct | User message overrides system prompt |
| Indirect | Malicious content in RAG docs, emails, web pages |

**Key controls:** Input/output separation, delimiters, allowlists, privilege isolation for tools, human review for high-risk actions.

---

## LLM02 — Insecure Output Handling

**Risk:** LLM output passed to downstream systems without validation.

**Key controls:** Encode/validate before SQL, shell, HTML, API calls; schema enforcement on structured output.

---

## LLM03 — Training Data Poisoning

**Risk:** Corrupted training/fine-tuning or RAG corpus data.

**Key controls:** Source validation, integrity checks on embeddings, anomaly detection on ingest.

---

## LLM04 — Model Denial of Service

**Risk:** Resource exhaustion via expensive queries or flooding.

**Key controls:** Rate limits, token budgets, timeouts, cost caps, queue depth limits.

---

## LLM05 — Supply Chain Vulnerabilities

**Risk:** Compromised models, plugins, dependencies.

**Key controls:** Provenance verification, dependency scanning, vendor SLAs, pinned versions.

---

## LLM06 — Sensitive Information Disclosure

**Risk:** PII, secrets, or proprietary data in prompts, logs, or responses.

**Key controls:** PII scrubbing, log redaction, RAG tenant isolation, prompt leak testing.

---

## LLM07 — Insecure Plugin Design

**Risk:** Tools/plugins with excessive permissions or weak input validation.

**Key controls:** Least privilege, JSON Schema validation, per-tool auth, scoped OAuth.

---

## LLM08 — Excessive Agency

**Risk:** LLM granted autonomy beyond intended scope.

**Key controls:** Human-in-the-loop for irreversible actions, kill-switch, action allowlists.

---

## LLM09 — Overreliance

**Risk:** Users trust LLM output without verification.

**Key controls:** Citations, confidence indicators, disclaimers, human review for high-stakes decisions.

---

## LLM10 — Model Theft

**Risk:** Unauthorized access to proprietary model weights or extraction attacks.

**Key controls:** API access controls, rate limiting on outputs, watermarking (if applicable).

---

## Severity Scale (APES)

| Level | Criteria |
|-------|----------|
| Critical | Exploitable with high business impact; no control |
| High | Exploitable or likely; partial control |
| Medium | Limited exploitability or contained blast radius |
| Low | Theoretical or hard to exploit |

---

## Shared vs Application Responsibility

| Control type | API-hosted model | Self-hosted model |
|--------------|------------------|-------------------|
| Provider safety filters | Inherited | N/A |
| Prompt structure | Application | Application |
| RAG corpus security | Application | Application |
| Tool permissions | Application | Application |

Document inherited controls with evidence (provider docs, contract), not assumptions.

---

## Canonical Links

- [OWASP LLM Top 10](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
- [OWASP GenAI Security Project](https://owasp.org/www-project-genai-security/)

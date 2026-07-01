# MCP Security Review

# Purpose

Conduct a security review of MCP server and client implementations: threat modeling, auth validation, tool risk assessment, and remediation plan aligned with OWASP LLM and MCP-specific risks.

**Input:** MCP server/client specification, tool designs, auth model, data classification, deployment context  
**Output:** MCP Security Review Report with findings ranked by severity, threat model, and remediation checklist

---

# Workflow

## Step 1: Classify data and deployment

| Dimension | Classification |
|-----------|----------------|
| Data sensitivity | Public / Internal / Confidential / PII |
| Deployment | Local stdio / Self-hosted / Third-party |
| User scope | Single user / Multi-tenant |
| Write access | Read-only / Read-write / Destructive |

## Step 2: Build threat model

Apply STRIDE to MCP components:

| Component | Threats | Example |
|-----------|---------|---------|
| Transport | Spoofing, tampering | MITM on HTTP transport |
| Auth | Elevation, spoofing | Token leakage in logs |
| Tools | Tampering, DoS | Unbounded query exhausting API |
| Resources | Info disclosure | Exposing secrets via resources |
| Agent → Tool | Injection | LLM passes malicious args to shell tool |

Document trust boundaries: agent, MCP client, MCP server, external API.

## Step 3: Review authentication and secrets

| Check | Pass/Fail | Notes |
|-------|-----------|-------|
| Secrets in environment only | | |
| No secrets in tool responses | | |
| Token scope minimal (least privilege) | | |
| OAuth refresh handled securely | | |
| Per-user vs shared credentials documented | | |

## Step 4: Assess tool risk

Per tool:

| Tool | Risk | Controls present | Gap |
|------|------|------------------|-----|
| `run_query` | SQL injection | Parameterized queries | None |
| `delete_file` | Data loss | confirm flag | Missing confirm |

Flag: command injection, path traversal, SSRF, excessive permissions, missing rate limits.

## Step 5: Review logging and audit

- Arguments with PII redacted in logs
- Audit trail for destructive operations
- No full API responses logged at debug in production
- Correlation ID for incident investigation

## Step 6: Produce findings and remediation

Rank findings: Critical / High / Medium / Low / Info.

Run Validation checklist.

---

# Decision Rules

| Condition | Action |
|-----------|--------|
| Critical finding (RCE, secret leak, unauth access) | Block deployment until fixed |
| Destructive tool without confirmation | Rate High; require remediation |
| HTTP transport without TLS | Block production deployment |
| PII in tool responses without redaction | Require data minimization |
| Third-party MCP server with write access | Require sandbox and explicit user consent |
| Shell/command execution tool | Critical review; prefer API-based alternatives |

---

# Validation

- [ ] Data classification and deployment context documented
- [ ] Threat model with trust boundaries
- [ ] Auth and secrets review completed
- [ ] Every tool assessed for risk with controls/gaps
- [ ] Logging and audit requirements specified
- [ ] Findings ranked with severity and remediation
- [ ] Critical/High findings have owner and deadline
- [ ] Residual risk accepted explicitly or mitigated

---

# Anti-patterns

- **Security theater** — checklist without tool-level analysis.
- **Trust the LLM** — assuming model will never call dangerous tools with bad args.
- **Shared admin token** — one API key for all users in multi-tenant setup.
- **Log everything** — recording tokens and PII for debugging.
- **Skip review for read-only** — read access to secrets still requires review.

---

# Best Practices

- Apply least privilege to every API token scope.
- Validate and sanitize all tool inputs server-side.
- Use allowlists for URLs (SSRF), paths (traversal), and commands.
- Rate limit per user and per tool.
- Re-review on every new tool or auth model change.

---

# Output Structure

```markdown
# MCP Security Review: [Server/Client Name]
**Date:** [YYYY-MM-DD]
**Reviewer:** [Name or "automated skill"]

## Context
| Dimension | Value |
|-----------|-------|

## Threat Model
[Trust boundaries diagram and STRIDE table]

## Auth & Secrets Review
| Check | Status | Finding |
|-------|--------|---------|

## Tool Risk Assessment
| Tool | Risk | Severity | Remediation |
|------|------|----------|-------------|

## Findings Summary
| ID | Severity | Description | Remediation | Status |
|----|----------|-------------|-------------|--------|

## Deployment Gate
[ ] Approved  [ ] Approved with conditions  [ ] Blocked

## Residual Risks
| Risk | Acceptance rationale |
|------|---------------------|
```

---

# Next Skills

| Outcome | Recommended Skill |
|---------|-------------------|
| Fix tool design issues | `mcp/mcp-tool-generator` |
| Harden implementation | `mcp/mcp-best-practices` |
| Broader LLM security | `ai-security/llm-threat-modeler` |
| Re-review after fixes | `mcp/mcp-security-review` |
| Client auth hardening | `mcp/mcp-client-generator` |

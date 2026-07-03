---
name: human-in-the-loop-designer
description: >
  Design human-in-the-loop (HITL) workflows for AI systems: review queues, escalation triggers, feedback loops, and SLA-backed approval gates. Use when deploying high-risk AI, production agents, or regulated decision support.
metadata:
  apes-version: "1.1"
  category: ai
---

# Human-in-the-Loop Designer

# Purpose

Design human-in-the-loop (HITL) workflows: when humans intervene, how work is queued, and how feedback improves the AI system over time.

**Input:** AI use case, risk level, automation target, team roles, SLA requirements  
**Output:** HITL Workflow Specification with triggers, queues, UI/API hooks, and metrics  
**Examples:** See [examples.md](examples.md) for worked input/output.

---

# Workflow

## Step 1: Assess automation boundary

| Risk tier | Examples | Default HITL |
|-----------|----------|--------------|
| Low | Draft text, suggestions | Optional spot-check |
| Medium | Customer replies, code suggestions | Sample review 5–10% |
| High | Medical, legal, financial decisions | Mandatory approval |
| Critical | Irreversible actions (payments, deletes) | Dual approval |

Document what the AI may do autonomously vs what requires human gate.

## Step 2: Define escalation triggers

| Trigger type | Signal | Example |
|--------------|--------|---------|
| Confidence | Model score < threshold | Classifier < 0.7 → queue |
| Policy | Guardrail hit | PII detected → block + review |
| User | Explicit request | "Talk to a human" |
| Anomaly | Out-of-distribution input | Unknown intent cluster |
| Volume | Error rate spike | >3% thumbs-down/hour |

Each trigger maps to queue priority and assignee role.

## Step 3: Design review queue

| Field | Purpose |
|-------|---------|
| Case ID | Traceability |
| AI draft + inputs | Reviewer context |
| Confidence + trigger reason | Prioritization |
| Suggested action | Approve / edit / reject |
| SLA deadline | Ops accountability |

Define states: `pending` → `in_review` → `approved` | `edited` | `rejected` | `escalated`.

## Step 4: Design reviewer experience

- **Diff view** — AI output vs policy template
- **One-click actions** — approve, edit-and-send, reject-with-reason
- **Keyboard shortcuts** — for high-volume queues
- **Audit trail** — who decided what, when

Specify API or UI integration points (webhook, ticket system, Slack).

## Step 5: Close the feedback loop

| Reviewer action | System learning |
|-----------------|-----------------|
| Edit | Store (input, draft, final) as training/eval pair |
| Reject + reason | Tag failure mode for eval set |
| Approve | Positive signal for monitoring |

Route feedback to `ai-evaluation-builder` datasets and prompt iteration.

## Step 6: Define HITL metrics and SLAs

| Metric | Target |
|--------|--------|
| Queue wait time p95 | < 15 min (medium risk) |
| Review time median | Track per category |
| Override rate | Monitor drift; alert if >20% |
| Escalation rate | Baseline + alert |
| Post-release incident rate | Zero critical after HITL |

## Step 7: Validate

Run Validation checklist.

---

# Decision Rules

| Condition | Action |
|-----------|--------|
| Regulated domain | Mandatory HITL; document in governance pack |
| No human reviewers available | Stop; do not deploy high-risk automation |
| Override rate > 30% for 7 days | Pause auto-send; run prompt/workflow fix |
| Reviewer edits same field repeatedly | Create dedicated rule or fine-tune |
| Latency SLA conflicts with HITL | Async path + user expectation messaging |

---

# Validation

- [ ] Risk tier and automation boundary documented
- [ ] ≥3 escalation triggers with thresholds
- [ ] Queue schema and state machine defined
- [ ] Reviewer actions and audit trail specified
- [ ] Feedback loop connected to eval/improvement
- [ ] SLAs per risk tier with alert thresholds
- [ ] User-facing messaging for pending human review
- [ ] Rollback path if HITL system fails

---

# Anti-patterns

- **HITL theater** — queue exists but reviewers always click approve.
- **No feedback capture** — human edits discarded; system never improves.
- **Unbounded queue** — no SLA; users wait indefinitely.
- **Reviewer without context** — AI draft shown without inputs or policy.
- **Same gate for all risk levels** — over-reviewing low-risk kills throughput.

---

# Best Practices

- Start with shadow mode: AI drafts, human sends, before any automation.
- Sample-review low-risk paths; full gate only where regulation requires.
- Instrument override reasons as structured tags, not free text only.
- Pair with `guardrails-builder` for automated pre-queue filtering.
- Reconcile HITL metrics weekly with product and safety owners.

---

# Output Structure

```markdown
# HITL Workflow: [System Name]

## Risk Assessment
| Tier | Autonomous scope | Human gate |
|------|------------------|------------|

## Escalation Triggers
| Trigger | Threshold | Queue | Priority |
|---------|-----------|-------|----------|

## Queue Specification
[State machine + fields]

## Reviewer UX
[Actions, integrations]

## Feedback Loop
| Action | Destination |
|--------|-------------|

## SLAs & Metrics
| Metric | Target | Alert |
|--------|--------|-------|

## Rollout Plan
[Shadow → partial → full automation]
```

---

# Next Skills

| Outcome | Recommended Skill |
|---------|-------------------|
| Build evaluation from overrides | `ai/ai-evaluation-builder` |
| Pre-filter before queue | `security/guardrails-builder` |
| Governance documentation | `security/ai-governance-advisor` |
| Orchestrate async workflow | `ai/ai-workflow-builder` |
| Threat model human bypass | `security/ai-threat-modeling` |

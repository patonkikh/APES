---
name: agent-memory-designer
description: >
  Design agent memory architecture: short-term context, long-term vector store, episodic logs, and retention policies with privacy controls. Use when building persistent agents, chatbots with memory, or multi-session AI assistants.
metadata:
  apes-version: "1.1"
  category: ai
---

# Agent Memory Designer

# Purpose

Design agent memory architecture: what to remember, where to store it, how to retrieve it, and when to forget — with privacy and cost controls.

**Input:** Agent use case, session patterns, data sensitivity, latency/cost budget  
**Output:** Memory Architecture document with tiers, schemas, retrieval flows, and hygiene rules  
**Examples:** See [examples.md](examples.md) for worked input/output.

---

# Workflow

## Step 1: Classify memory needs

| Memory type | Scope | Typical TTL | Example |
|-------------|-------|-------------|---------|
| Working | Current turn / task | Minutes | Tool results in context |
| Session | Single conversation | Hours | User preferences stated today |
| Episodic | Past interactions | Days–months | "User fixed bug X last week" |
| Semantic | Facts about user/domain | Long-term | Profile, project context |
| Procedural | How agent should behave | Versioned | Learned corrections |

Map each user story to required memory types.

## Step 2: Choose storage tiers

| Tier | Technology pattern | When to use |
|------|-------------------|-------------|
| Context window | In-prompt assembly | Hot working memory |
| Key-value / session store | Redis, DynamoDB | Fast session state |
| Vector store | pgvector, Pinecone, LanceDB | Semantic recall |
| Document store | Postgres JSONB | Structured user profiles |
| Append-only log | Event stream | Audit and episodic replay |

Document read/write latency and cost per tier.

## Step 3: Design write path

Define what gets written after each agent turn:

- **Extract** — entities, decisions, user corrections, task outcomes
- **Summarize** — compress verbose turns into durable facts
- **Dedupe** — merge with existing memories (same key → update, not duplicate)
- **Score** — importance / confidence before persistence

Include triggers: user correction always writes; routine chit-chat may not.

## Step 4: Design read path (recall)

```text
Query → Intent classifier → Retrieve from tiers → Rank → Budget trim → Inject into context
```

| Recall strategy | Use when |
|-----------------|----------|
| Similarity search | Open-ended "what did we discuss about X?" |
| Key lookup | Known profile fields |
| Recency-weighted | Session continuity |
| Hybrid | Production agents (default) |

Set top-k, similarity threshold, and max tokens injected.

## Step 5: Define hygiene and governance

| Policy | Rule |
|--------|------|
| Retention | TTL per memory class |
| Deletion | User request, account close, GDPR erasure |
| PII | Never store secrets; redact before write |
| Staleness | Re-validate facts older than N days |
| Compaction | Weekly summarize episodic → semantic |

## Step 6: Validate

Run Validation checklist.

---

# Decision Rules

| Condition | Action |
|-----------|--------|
| High-sensitivity data (health, finance) | Stop; require encryption at rest + minimal retention |
| No user identity | Session-only memory; no cross-session semantic store |
| Memory bloat / high recall cost | Add compaction job and relevance threshold |
| User says "forget that" | Delete matching memories + confirm |
| Multi-agent system | Shared memory bus with namespace per agent |
| Contradictory memories | Prefer newest high-confidence; flag for user |

---

# Validation

- [ ] Memory types mapped to user stories
- [ ] Storage tier per type with TTL documented
- [ ] Write path: extract, summarize, dedupe rules defined
- [ ] Read path: retrieval strategy and token budget set
- [ ] PII and secrets exclusion enforced at write
- [ ] User deletion and retention policies specified
- [ ] Cost estimate per 1k sessions (storage + embedding + recall)
- [ ] Failure mode: empty recall falls back gracefully

---

# Anti-patterns

- **Remember everything** — unbounded logs inflate cost and inject noise.
- **Vector-only memory** — losing structured keys makes profile lookup unreliable.
- **No TTL** — stale facts poison agent behavior months later.
- **Recall without ranking** — dumping top-20 chunks floods context.
- **Cross-user leakage** — missing tenant isolation in shared vector index.

---

# Best Practices

- Start with session + explicit user profile; add episodic memory when needed.
- Store memories as atomic facts with source turn ID and timestamp.
- Run memory hygiene audits (LobeHub `memory-hygiene` pattern) monthly.
- Pair with `context-engineering` for assembly order and budget.
- Log recall hits/misses for tuning thresholds.

---

# Output Structure

```markdown
# Memory Architecture: [Agent Name]

## Requirements
| Story | Memory types needed |
|-------|---------------------|

## Storage Tiers
| Type | Store | TTL | Est. cost |
|------|-------|-----|-----------|

## Write Pipeline
[Extract → Summarize → Dedupe → Persist]

## Read Pipeline
[Query → Retrieve → Rank → Inject]

## Schemas
[Memory record JSON examples]

## Hygiene Policies
| Policy | Rule |
|--------|------|

## Security
[PII, encryption, tenant isolation]
```

---

# Next Skills

| Outcome | Recommended Skill |
|---------|-------------------|
| Assemble recalled context | `ai/context-engineering` |
| Multi-agent shared memory | `ai/multi-agent-planner` |
| Privacy / compliance review | `security/ai-governance-advisor` |
| Evaluate memory impact on quality | `ai/ai-evaluation-builder` |
| RAG corpus vs agent memory boundary | `rag/rag-architecture-designer` |

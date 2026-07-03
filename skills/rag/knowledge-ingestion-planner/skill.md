---
name: knowledge-ingestion-planner
description: >
  Design a knowledge ingestion pipeline for RAG: source connectors, parsing, chunking handoff, metadata enrichment, and incremental sync. Use when onboarding documents, building knowledge bases, or scaling RAG corpora.
metadata:
  apes-version: "1.1"
  category: rag
---

# Knowledge Ingestion Planner

# Purpose

Design a knowledge ingestion pipeline: how documents enter the system, are parsed, enriched, chunked, and indexed with reliable incremental updates.

**Input:** Source types (PDF, wiki, API, DB), volume, update frequency, access control requirements  
**Output:** Ingestion Pipeline Specification with connector map, parsing rules, metadata schema, and sync strategy  
**Examples:** See [examples.md](examples.md) for worked input/output.

---

# Workflow

## Step 1: Inventory sources

| Source | Format | Volume | Update freq | ACL |
|--------|--------|--------|-------------|-----|
| Confluence | HTML | 5k pages | Daily | Per-space |
| S3 PDFs | PDF | 200 files | Weekly | Bucket policy |
| GitHub README | Markdown | 50 repos | On push | Public |

Identify authoritative vs supplemental sources; flag duplicates across sources.

## Step 2: Design connector layer

| Pattern | Use when |
|---------|----------|
| Batch pull | Scheduled full/incremental sync |
| Webhook push | Real-time wiki/git updates |
| CDC stream | Database knowledge tables |
| Upload API | User-generated documents |

Each connector outputs normalized `RawDocument` with provenance:

```text
source_id, uri, mime, fetched_at, acl_principal, raw_bytes
```

## Step 3: Define parsing and extraction

| Format | Parser approach | Pitfalls |
|--------|-----------------|----------|
| PDF | Layout-aware OCR if scanned | Tables split wrong |
| HTML/wiki | DOM + boilerplate removal | Nav/footer noise |
| Office | Structured extraction | Hidden text layers |
| Code | AST or markdown-aware | License headers |

Document fallback when parsing confidence is low (quarantine queue).

## Step 4: Metadata enrichment

Required metadata per chunk parent document:

| Field | Purpose |
|-------|---------|
| `doc_id` | Stable ID across reindexes |
| `title` | Display and filtering |
| `source_system` | Provenance |
| `updated_at` | Freshness ranking |
| `acl` | Retrieval filter |
| `language` | Routing / embedding model |
| `tags` | Faceted search |

Optional: auto-summary, entity extraction, section headings.

## Step 5: Hand off to chunking and indexing

Define contract with `chunking-strategy-advisor`:

- Send cleaned markdown + structure hints (headings, tables)
- Chunk size/overlap per doc type
- Parent-child chunk linking for citations

Indexing pipeline:

```text
Parse → Enrich → Chunk → Embed → Upsert vector store → Verify count
```

## Step 6: Incremental sync and deletion

| Event | Action |
|-------|--------|
| New document | Full ingest path |
| Updated document | Re-chunk changed sections or full replace |
| Deleted / ACL revoked | Hard delete vectors + tombstone log |
| Source drift | Reconciliation job weekly |

Idempotency key: `source_id + content_hash`.

## Step 7: Validate

Run Validation checklist.

---

# Decision Rules

| Condition | Action |
|-----------|--------|
| ACL per document | Propagate to vector metadata; filter at query time |
| >1M documents | Partition by tenant/source; async queue |
| Scanned PDF majority | OCR pipeline + human QA sample |
| Duplicate content across sources | Canonical URL + dedupe hash |
| Real-time requirement <5 min | Push webhooks, not nightly batch |
| PII in corpus | Scan pre-index; block or redact |

---

# Validation

- [ ] Source inventory with volume and update frequency
- [ ] Connector pattern per source
- [ ] Parsing rules per MIME type
- [ ] Metadata schema with ACL fields
- [ ] Chunking handoff documented
- [ ] Incremental sync and delete behavior defined
- [ ] Idempotency and reconciliation plan
- [ ] Ingestion SLA and error quarantine queue

---

# Anti-patterns

- **Reindex everything nightly** — wasteful at scale; misses true incremental.
- **Ignore ACL at ingest** — retrieval leaks across tenants.
- **Chunk before clean** — boilerplate pollutes every chunk.
- **No deletion path** — stale content forever in answers.
- **Single parser for all PDFs** — table-heavy docs need layout models.

---

# Best Practices

- Store raw originals in object storage; derived chunks reproducible.
- Log ingest lineage: chunk → doc → source fetch timestamp.
- Sample 1% of ingested docs for human QA each week.
- Pair with `embedding-strategy-advisor` for model/version pinning.
- Monitor ingest lag and embedding failure rate.

---

# Output Structure

```markdown
# Ingestion Pipeline: [Knowledge Base Name]

## Sources
| Source | Connector | Schedule | ACL |
|--------|-----------|----------|-----|

## Architecture
[Diagram: sources → queue → parse → enrich → chunk → index]

## Parsing Rules
| MIME | Parser | Fallback |
|------|--------|----------|

## Metadata Schema
[Field definitions]

## Sync Strategy
[Incremental rules]

## SLAs & Monitoring
| Metric | Target |
|--------|--------|

## Error Handling
[Quarantine, retry]
```

---

# Next Skills

| Outcome | Recommended Skill |
|---------|-------------------|
| Chunking parameters | `rag/chunking-strategy-advisor` |
| Embedding model choice | `rag/embedding-strategy-advisor` |
| End-to-end RAG design | `rag/rag-architecture-designer` |
| Retrieval tuning | `rag/retriever-optimizer` |
| Hybrid search setup | `rag/hybrid-search-advisor` |

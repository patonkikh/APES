# Knowledge Ingestion Planner — Examples

---

## Example 1: Internal wiki RAG

### Input

```text
Sources: Confluence (3k pages), Google Drive PDFs (400), GitHub docs.
Daily wiki updates. Per-space ACL from Confluence.
```

### Output (excerpt)

```markdown
## Connectors
Confluence: webhook + nightly reconciliation.
Drive: batch pull weekly + manual upload API.

## Metadata
doc_id = confluence:page:{id}
acl = space permission groups → principal list

## Sync
content_hash change → re-chunk full page; ACL revoke → vector delete <15 min.
```

---

## Example 2: Missing ACL

### Input

```text
Index all SharePoint without permission mapping.
```

### Expected behavior

Stop. Require ACL propagation before indexing — retrieval leak risk.

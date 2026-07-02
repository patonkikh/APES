# AI Workflow Builder — Worked Examples

---

## Example 1: Retro generation workflow

### Input

```text
Stages: validate input → fetch Jira → build prompt → call LLM → validate output → store
Triggers: API job enqueue
Failures: Jira down, LLM timeout, malformed JSON output
```

### Output (excerpt)

```markdown
# AI Workflow: Retro Generation Pipeline

## Stages
| # | Stage | Input | Output | Timeout |
|---|-------|-------|--------|---------|
| 1 | Validate | job payload | sprint_id | 5s |
| 2 | Fetch Jira | sprint_id | issue bundle | 30s |
| 3 | Generate | bundle + template | draft JSON | 45s |
| 4 | Validate output | draft JSON | pass/fail | 5s |
| 5 | Persist | draft | retro_id | 5s |

## Branching
- Stage 4 fail → retry generate once → else fail job with `INVALID_OUTPUT`
- Stage 2 fail → retry 3x → DLQ

## Observability
Correlation ID = job_id across all stages
```

---

## Example 2: Monolithic single step

### Input

```text
One step: do everything
```

### Expected behavior

Decompose into stages with per-stage timeouts and retry policies.

---

## Example 3: No output validation

### Expected behavior

Add validation stage before persist; link to `ai-evaluation-builder` gates.

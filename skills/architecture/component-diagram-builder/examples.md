# Component Diagram Builder — Worked Examples

---

## Example 1: API application components

### Input

```text
Container: API Application (Node.js)
Responsibilities: auth, retro jobs, Jira/Confluence adapters
```

### Output (excerpt)

```markdown
# Component Diagram: API Application

## Components
| Component | Type | Responsibility |
|-----------|------|----------------|
| AuthController | controller | OAuth callbacks, sessions |
| RetroController | controller | Job CRUD endpoints |
| RetroService | service | Business logic |
| JiraAdapter | adapter | Jira API client |
| ConfluenceAdapter | adapter | Confluence API client |
| JobPublisher | adapter | SQS enqueue |

## Interactions
RetroController → RetroService → JiraAdapter
RetroService → JobPublisher
```

---

## Example 2: No container diagram

### Expected behavior

Stop; run `container-diagram-builder` first.

---

## Example 3: 25 components

### Expected behavior

Group into sub-modules; target 3–12 components per diagram.

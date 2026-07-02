# Story Mapping — Worked Examples

---

## Example 1: User journey map

### Input

```text
Product: Retro generator
Persona: Engineering manager
Journey: Prepare retro → Run meeting → Follow up actions
```

### Output (excerpt)

```markdown
# Story Map: Retro Generator

## Backbone (User Activities)
Connect Jira → Select sprint → Review draft → Run retro → Export → Track actions

## Walking Skeleton (MVP slice)
| Activity | Stories |
|----------|---------|
| Connect Jira | OAuth, pick workspace |
| Select sprint | Sprint picker |
| Review draft | AI generate, edit |
| Export | Confluence export |

## Releases
| Release | Slice |
|---------|-------|
| MVP | Walking skeleton |
| R2 | Slack share, templates |
| R3 | Analytics on action items |
```

---

## Example 2: Activity = technical task

### Input

```text
Activity: Set up database
```

### Expected behavior

Map to user-facing activity or place under enabler row below backbone.

---

## Example 3: No persona

### Expected behavior

Request persona before mapping journey.

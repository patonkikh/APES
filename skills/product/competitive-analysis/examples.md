# Competitive Analysis — Examples

---

## Example 1: AI writing assistants

### Input

```text
Category: AI email drafting for sales teams. Segment: SMB US.
Known: Lavender, Regie, Jasper. Building: outbound personalization tool.
```

### Output (excerpt)

```markdown
## Feature Matrix (excerpt)
| Capability | Us | Lavender | Regie |
|------------|----|---------|----|
| CRM native sync | Planned | ✅ | ✅ |
| Call coaching | ❌ | ⚠️ | ✅ |
| Deep personalization | ✅ | ⚠️ | ⚠️ |

## White Space
Vertical playbooks for niche industries underserved by horizontal tools.

## Recommendation
Wedge: CRM-field-aware drafts + reply learning loop (table stakes: Gmail/Outlook).
```

---

## Example 2: Broad scope

### Input

```text
Analyze all productivity software.
```

### Expected behavior

Narrow to one segment before matrix — request JTBD and geography.

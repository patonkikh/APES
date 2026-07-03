# Analytics Instrumentation Planner — Examples

---

## Example 1: AI copilot in SaaS app

### Input

```text
North star: weekly users who get an accepted AI suggestion.
Flows: onboarding, inline suggest, feedback thumb.
Stack: React + Segment.
```

### Output (excerpt)

```markdown
## Event Catalog (sample)
| Event | Properties |
|-------|------------|
| suggestion_shown | feature_area, model_id |
| suggestion_accepted | edit_distance_bucket |
| suggestion_dismissed | reason_enum |

## Funnel
signup → first_suggestion_shown → suggestion_accepted → return_7d
```

---

## Example 2: PII concern

### Input

```text
Log full prompts for debugging.
```

### Expected behavior

Reject default full-prompt logging. Propose opt-in debug mode with hash + consent.

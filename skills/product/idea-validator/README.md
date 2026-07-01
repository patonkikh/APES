# Idea Validator

Validates product ideas using Lean Startup assumption mapping and a structured scorecard.

## Example prompt

```text
Validate this idea: A B2B SaaS that uses AI to auto-generate sprint retrospectives
from Jira data for engineering managers in mid-size companies.
```

## Output

Idea Validation Report with assumption map, 7-dimension scorecard, and Go/Pivot/Stop recommendation.

## Chain

`idea-validator` → `problem-statement-builder` → `persona-generator` → ...

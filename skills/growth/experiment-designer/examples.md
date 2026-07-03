# Experiment Designer — Examples

---

## Example 1: Onboarding copy test

### Input

```text
Hypothesis: outcome-focused headline improves activation.
Baseline activation D7: 22%. ~5k signups/month.
MDE: +3 percentage points absolute.
```

### Output (excerpt)

```markdown
## Hypothesis
Outcome headline increases D7 activation from 22% because value is clearer.

## Metrics
| Role | Metric |
|------|--------|
| Primary | activation_d7 |
| Guardrail | support_tickets_per_user |

## Statistics
Required ~12k users per arm → ~5 weeks at current traffic.

## Ship criteria
Primary +3% at p<0.05, guardrails stable.
```

---

## Example 2: Stop — no tracking

### Input

```text
Test new pricing page design.
```

### Expected behavior

Ask whether `pricing_page_view` and `checkout_started` events exist; if not, block until instrumentation is defined.

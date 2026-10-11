# 074. Alerts, owners, and error budgets

## Learning outcome

Make signals actionable for specific consumers.

## How it works

An alert identifies the product, impact, owner, and first diagnostic step. Statistical warnings and critical monetary mismatches require different actions. Excessive noise teaches users to ignore alerts. Error budgets inform reliability tradeoffs, not permission to overlook money errors.

## Fintech example

A p3 mismatch of 100 minor units has a specific impact unlike a failed development notebook.

## Implementation steps

1. Assign severity
2. Name the owner
3. Link a runbook
4. Test false positives.

## Practical assignment

Write missing-settlement and mismatch alerts with units and cutoffs.

## Common mistake and its consequences

“Job failed” does not tell an on-call engineer which period or consumer is affected.

## Verify the result

The recipient knows the date, currency, and first action without reading the whole DAG.

## Self-check question

Why can task success rates improve while consumer reliability worsens?

## Further reading

- [OpenTelemetry concepts](https://opentelemetry.io/docs/concepts/) — primary documentation; find the section relevant to this lesson.
- [Airflow best practices](https://airflow.apache.org/docs/apache-airflow/stable/best-practices.html) — primary documentation; find the section relevant to this lesson.

## Deliverable and navigation

Save your solution in your own fork under `portfolio/074-alerts/`. Include the problem, a minimal example, the check from “Verify the result,” and your answer to the self-check question. Design exercises may produce an ADR, diagram, or experiment table; distinguish a proposal from an implemented service.

[Previous step](../08-reliability/073-observability.md) · [Next step](../08-reliability/075-incident.md) · [Full roadmap](../README.md)

**Module:** Quality and reliability. **Estimated time:** 2–4 hours for a first pass; deeper practice and a project take additional time. The previous step defines reading order, not an equally mandatory prerequisite for every learner: see the [learning paths](../../docs/LEARNING_PATHS.md).

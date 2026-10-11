# 075. Incident investigation and containment

## Learning outcome

Restore trust through impact scoping and verified repair.

## How it works

Contain invalid output and preserve evidence first. Identify affected periods, consumers, and causes. Recovery needs an independent comparison. Postmortems explain contributing factors instead of assigning blame. A code fix without historical repair leaves consequences intact.

## Fintech example

A wrong fee sign is published for a week; identify affected report versions and exports.

## Implementation steps

1. Stop affected publication
2. Record scope
3. Build a shadow correction
4. Verify and inform process owners.

## Practical assignment

Write a sign-bug timeline covering discovery, containment, repair, and validation.

## Common mistake and its consequences

Closing the incident after deployment leaves previous incorrect extracts untouched.

## Verify the result

Retain affected consumers, before/after totals, and repaired-period checks.

## Self-check question

How does a root cause differ from the event that exposed the problem?

## Further reading

- [OpenTelemetry concepts](https://opentelemetry.io/docs/concepts/) — primary documentation; find the section relevant to this lesson.
- [Airflow best practices](https://airflow.apache.org/docs/apache-airflow/stable/best-practices.html) — primary documentation; find the section relevant to this lesson.

## Deliverable and navigation

Save your solution in your own fork under `portfolio/075-incident/`. Include the problem, a minimal example, the check from “Verify the result,” and your answer to the self-check question. Design exercises may produce an ADR, diagram, or experiment table; distinguish a proposal from an implemented service.

[Previous step](../08-reliability/074-alerts.md) · [Next step](../08-reliability/076-lineage-impact.md) · [Full roadmap](../README.md)

**Module:** Quality and reliability. **Estimated time:** 2–4 hours for a first pass; deeper practice and a project take additional time. The previous step defines reading order, not an equally mandatory prerequisite for every learner: see the [learning paths](../../docs/LEARNING_PATHS.md).

# 060. Documentation as an operational contract

## Learning outcome

Make a pipeline understandable to on-call engineers and newcomers.

## How it works

Useful documentation defines purpose, grain, ownership, SLOs, sources, lineage, recovery, and limitations. Link executable checks and commands. A runbook starts from a concrete signal; an architecture overview explains decisions. “Watch the logs” is not a recovery procedure.

## Fintech example

An on-call engineer must distinguish a late settlement file from a lost payment.

## Implementation steps

1. Name alert types
2. Link checks
3. Provide diagnostic queries
4. State escalation and publication rules.

## Practical assignment

Write runbooks for p3 mismatch and p9 unexpected external using the fixture.

## Common mistake and its consequences

Recovery commands depend on undocumented directories or credentials.

## Verify the result

A newcomer reproduces diagnosis in a clean local environment.

## Self-check question

Which runbook details become stale fastest, and how can they be checked automatically?

## Further reading

- [Airflow best practices](https://airflow.apache.org/docs/apache-airflow/stable/best-practices.html) — primary documentation; find the section relevant to this lesson.
- [OpenTelemetry concepts](https://opentelemetry.io/docs/concepts/) — primary documentation; find the section relevant to this lesson.

## Deliverable and navigation

Save your solution in your own fork under `portfolio/060-docs-ops/`. Include the problem, a minimal example, the check from “Verify the result,” and your answer to the self-check question. Design exercises may produce an ADR, diagram, or experiment table; distinguish a proposal from an implemented service.

[Previous step](../06-transformation/059-deployments.md) · [Next step](../07-fintech/061-payment-lifecycle.md) · [Full roadmap](../README.md)

**Module:** Transformations and orchestration. **Estimated time:** 2–4 hours for a first pass; deeper practice and a project take additional time. The previous step defines reading order, not an equally mandatory prerequisite for every learner: see the [learning paths](../../docs/LEARNING_PATHS.md).

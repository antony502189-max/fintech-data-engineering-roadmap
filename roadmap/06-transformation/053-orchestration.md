# 053. Orchestration dependencies and data intervals

## Learning outcome

Design a DAG around data readiness rather than schedules alone.

## How it works

Orchestrators manage dependencies, retries, observation, and execution. A logical data interval identifies the period; wall-clock time must not silently change it. A schedule does not prove that source data exists. Readiness follows successful checks, not merely upstream startup.

## Fintech example

A January 1 mart rebuilt on January 3 must still process the January 1 interval.

## Implementation steps

1. Define intervals
2. Express dependencies
3. Require source readiness
4. Pass parameters explicitly.

## Practical assignment

Draw ingestion → checks → transformation → reconciliation → publication and specify each task's period.

## Common mistake and its consequences

Computing yesterday from now in every task makes backfill rebuild the same recent day.

## Verify the result

Repeated execution of an interval selects the same input manifest and scope.

## Self-check question

How does logical date differ from actual job start time?

## Further reading

- [Airflow best practices](https://airflow.apache.org/docs/apache-airflow/stable/best-practices.html) — primary documentation; find the section relevant to this lesson.

## Deliverable and navigation

Save your solution in your own fork under `portfolio/053-orchestration/`. Include the problem, a minimal example, the check from “Verify the result,” and your answer to the self-check question. Design exercises may produce an ADR, diagram, or experiment table; distinguish a proposal from an implemented service.

[Previous step](../06-transformation/052-dbt-incremental.md) · [Next step](../06-transformation/054-retry-design.md) · [Full roadmap](../README.md)

**Module:** Transformations and orchestration. **Estimated time:** 2–4 hours for a first pass; deeper practice and a project take additional time. The previous step defines reading order, not an equally mandatory prerequisite for every learner: see the [learning paths](../../docs/LEARNING_PATHS.md).

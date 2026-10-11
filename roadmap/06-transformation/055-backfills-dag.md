# 055. Backfill orchestration and resource limits

## Learning outcome

Rebuild history without displacing critical daily work.

## How it works

Backfills compete for source, warehouse, and scheduler capacity. Pools, concurrency limits, and isolated workloads reduce disruption. Publish complete agreed units rather than arbitrary chunks. Start with a canary period and compare control totals.

## Fintech example

Thirty-one historical jobs consume resources needed for today's settlement.

## Implementation steps

1. Set priorities
2. Bound concurrency
3. Verify a canary day
4. Publish an agreed scope.

## Practical assignment

Plan a monthly rebuild with batch sizes, stop conditions, and rollback datasets.

## Common mistake and its consequences

Unlimited parallel backfill overloads OLTP sources and delays daily output.

## Verify the result

Reserve daily capacity and state ETA assumptions and measurable abort thresholds.

## Self-check question

When is a shadow rebuild safer than modifying live partitions?

## Further reading

- [Airflow best practices](https://airflow.apache.org/docs/apache-airflow/stable/best-practices.html) — primary documentation; find the section relevant to this lesson.
- [dbt data tests](https://docs.getdbt.com/docs/build/data-tests) — primary documentation; find the section relevant to this lesson.

## Deliverable and navigation

Save your solution in your own fork under `portfolio/055-backfills-dag/`. Include the problem, a minimal example, the check from “Verify the result,” and your answer to the self-check question. Design exercises may produce an ADR, diagram, or experiment table; distinguish a proposal from an implemented service.

[Previous step](../06-transformation/054-retry-design.md) · [Next step](../06-transformation/056-publish.md) · [Full roadmap](../README.md)

**Module:** Transformations and orchestration. **Estimated time:** 2–4 hours for a first pass; deeper practice and a project take additional time. The previous step defines reading order, not an equally mandatory prerequisite for every learner: see the [learning paths](../../docs/LEARNING_PATHS.md).

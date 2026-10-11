# 044. Managed warehouses: cost, roles, and operation

## Learning outcome

Compare warehouses against requirements rather than branding.

## How it works

Managed warehouses reduce infrastructure work but leave modeling, permissions, isolation, and cost control to users. Billing may depend on scans, compute time, or capacity. Choice depends on workload, region, integrations, and team needs; no option wins universally.

## Fintech example

An ad hoc yearly raw scan consumes resources needed for daily reconciliation.

## Implementation steps

1. Describe workload
2. Select one platform to evaluate
3. Establish budget controls
4. Measure representative queries.

## Practical assignment

Compare BigQuery, Snowflake, and PostgreSQL for latency, experiment cost, isolation, and maintenance. Check current prices before spending.

## Common mistake and its consequences

Extrapolating a free trial to production ignores representative volume and workload.

## Verify the result

Record dataset-size assumptions and methods of limiting expenditure.

## Self-check question

How can research queries be isolated from mandatory daily close?

## Further reading

- [BigQuery documentation](https://cloud.google.com/bigquery/docs) — primary documentation; find the section relevant to this lesson.
- [Snowflake documentation](https://docs.snowflake.com/en/) — primary documentation; find the section relevant to this lesson.

## Deliverable and navigation

Save your solution in your own fork under `portfolio/044-cloud-dwh/`. Include the problem, a minimal example, the check from “Verify the result,” and your answer to the self-check question. Design exercises may produce an ADR, diagram, or experiment table; distinguish a proposal from an implemented service.

[Previous step](../05-storage/043-iceberg.md) · [Next step](../05-storage/045-spark.md) · [Full roadmap](../README.md)

**Module:** Storage and processing. **Estimated time:** 2–4 hours for a first pass; deeper practice and a project take additional time. The previous step defines reading order, not an equally mandatory prerequisite for every learner: see the [learning paths](../../docs/LEARNING_PATHS.md).

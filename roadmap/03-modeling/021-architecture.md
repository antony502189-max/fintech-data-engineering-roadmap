# 021. OLTP, warehouses, lakes, and lakehouses

## Learning outcome

Choose a system from workload and history requirements.

## How it works

OLTP optimizes short operations on current state. Warehouses serve analytical reads and agreed models. A data lake holds files; a lakehouse adds table metadata and managed changes over object storage. Roles overlap, but a product label does not guarantee data quality.

## Fintech example

The payment service should not wait behind an analyst's expensive monthly aggregation.

## Implementation steps

1. Measure the operational workload
2. Define analytical queries
3. Specify historical requirements
4. Separate source and analytical serving.

## Practical assignment

Compare a PostgreSQL replica, a managed warehouse, and Iceberg for a teaching fintech workload.

## Common mistake and its consequences

Choosing a lakehouse for fashion adds catalog, maintenance, and engine compatibility costs without a supporting workload.

## Verify the result

For each option, document load, operating cost, latency, and a reason to reject it.

## Self-check question

When is an analytical replica sufficient without a separate warehouse?

## Further reading

- [PostgreSQL documentation](https://www.postgresql.org/docs/current/) — primary documentation; find the section relevant to this lesson.
- [Apache Iceberg documentation](https://iceberg.apache.org/docs/latest/) — primary documentation; find the section relevant to this lesson.

## Deliverable and navigation

Save your solution in your own fork under `portfolio/021-architecture/`. Include the problem, a minimal example, the check from “Verify the result,” and your answer to the self-check question. Design exercises may produce an ADR, diagram, or experiment table; distinguish a proposal from an implemented service.

[Previous step](../02-sql/020-sql-review.md) · [Next step](../03-modeling/022-layers.md) · [Full roadmap](../README.md)

**Module:** DWH modeling. **Estimated time:** 2–4 hours for a first pass; deeper practice and a project take additional time. The previous step defines reading order, not an equally mandatory prerequisite for every learner: see the [learning paths](../../docs/LEARNING_PATHS.md).

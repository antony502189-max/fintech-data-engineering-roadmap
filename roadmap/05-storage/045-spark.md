# 045. Spark partitions, shuffle, and memory

## Learning outcome

Identify operations that move data between executors.

## How it works

Spark distributes work across partitions. Joins and aggregations can shuffle data, often dominating cost. collect transfers results to the driver and can exhaust its memory. More executors do not automatically repair skew or an inefficient plan.

## Fintech example

One merchant generates half the payments and overloads a reduce task.

## Implementation steps

1. Inspect the physical plan
2. Locate shuffles
3. Measure skew
4. Compare changes on one fixture.

## Practical assignment

Design a merchant/currency aggregation benchmark. For an actual run, retain Spark version and task metrics.

## Common mistake and its consequences

Collecting a large dataset to write convenient JSON crashes the driver while executors remain available.

## Verify the result

Report partition sizes, shuffle bytes, and longest task duration.

## Self-check question

When does repartition add cost without improving useful computation?

## Further reading

- [Spark SQL performance tuning](https://spark.apache.org/docs/latest/sql-performance-tuning.html) — primary documentation; find the section relevant to this lesson.

## Deliverable and navigation

Save your solution in your own fork under `portfolio/045-spark/`. Include the problem, a minimal example, the check from “Verify the result,” and your answer to the self-check question. Design exercises may produce an ADR, diagram, or experiment table; distinguish a proposal from an implemented service.

[Previous step](../05-storage/044-cloud-dwh.md) · [Next step](../05-storage/046-skew-joins.md) · [Full roadmap](../README.md)

**Module:** Storage and processing. **Estimated time:** 2–4 hours for a first pass; deeper practice and a project take additional time. The previous step defines reading order, not an equally mandatory prerequisite for every learner: see the [learning paths](../../docs/LEARNING_PATHS.md).

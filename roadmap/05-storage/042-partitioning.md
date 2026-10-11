# 042. Partitioning and key selection

## Learning outcome

Choose partitions from actual query patterns.

## How it works

Partitioning splits data by values and enables pruning when filters are compatible. High-cardinality keys generate excessive partitions or small files. Event dates support business reporting; receipt progress supports ingestion. Changing strategy may require rewriting history.

## Fintech example

Partitioning by merchant creates thousands of tiny files while a daily report still touches all merchants.

## Implementation steps

1. Collect query patterns
2. Estimate cardinality
3. Choose a moderate time partition
4. Test late updates.

## Practical assignment

Compare partition counts for day, merchant, and day-plus-merchant across 10000 merchants and 365 days.

## Common mistake and its consequences

Partitioning by unique payment IDs lets metadata overhead dominate useful reads.

## Verify the result

Document bytes per partition, pruning behavior, and historical-day repair.

## Self-check question

What happens if a filter wraps a partition column in an unsupported function?

## Further reading

- [Apache Iceberg documentation](https://iceberg.apache.org/docs/latest/) — primary documentation; find the section relevant to this lesson.
- [BigQuery documentation](https://cloud.google.com/bigquery/docs) — primary documentation; find the section relevant to this lesson.

## Deliverable and navigation

Save your solution in your own fork under `portfolio/042-partitioning/`. Include the problem, a minimal example, the check from “Verify the result,” and your answer to the self-check question. Design exercises may produce an ADR, diagram, or experiment table; distinguish a proposal from an implemented service.

[Previous step](../05-storage/041-columnar.md) · [Next step](../05-storage/043-iceberg.md) · [Full roadmap](../README.md)

**Module:** Storage and processing. **Estimated time:** 2–4 hours for a first pass; deeper practice and a project take additional time. The previous step defines reading order, not an equally mandatory prerequisite for every learner: see the [learning paths](../../docs/LEARNING_PATHS.md).

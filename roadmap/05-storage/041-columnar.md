# 041. Columnar storage and Parquet

## Learning outcome

Explain reduced reading and file-statistics behavior.

## How it works

Columnar layouts let readers select needed columns; compression exploits similar values. Parquet row groups and metadata statistics can eliminate unnecessary reads. A file format alone does not provide table atomicity, versioning, or concurrency management.

## Fintech example

A report needs date, currency, and amount while raw payload accounts for most stored bytes.

## Implementation steps

1. Measure row width
2. Identify projected columns
3. Inspect row groups
4. Compare bytes read on the same workload.

## Practical assignment

Design a CSV-versus-Parquet benchmark on synthetic data. Specify library and version before running the extension.

## Common mistake and its consequences

Treating Parquet as a transactional table exposes partially written batches.

## Verify the result

Distinguish file format from table format and measure size, runtime, and scanned bytes.

## Self-check question

Why does a narrow projection benefit columnar storage more than SELECT *?

## Further reading

- [Apache Iceberg documentation](https://iceberg.apache.org/docs/latest/) — primary documentation; find the section relevant to this lesson.
- [Spark SQL performance tuning](https://spark.apache.org/docs/latest/sql-performance-tuning.html) — primary documentation; find the section relevant to this lesson.

## Deliverable and navigation

Save your solution in your own fork under `portfolio/041-columnar/`. Include the problem, a minimal example, the check from “Verify the result,” and your answer to the self-check question. Design exercises may produce an ADR, diagram, or experiment table; distinguish a proposal from an implemented service.

[Previous step](../04-ingestion/040-ingestion-audit.md) · [Next step](../05-storage/042-partitioning.md) · [Full roadmap](../README.md)

**Module:** Storage and processing. **Estimated time:** 2–4 hours for a first pass; deeper practice and a project take additional time. The previous step defines reading order, not an equally mandatory prerequisite for every learner: see the [learning paths](../../docs/LEARNING_PATHS.md).

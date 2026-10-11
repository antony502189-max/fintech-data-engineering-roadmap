# 016. Indexes and query plans

## Learning outcome

Choose an index from the workload and measure its effect.

## How it works

Indexes improve particular access paths while increasing write cost. Composite index usefulness depends on column order and predicates. EXPLAIN describes a plan; representative data establishes runtime and reading cost. Scanning six rows may be a reasonable optimizer choice.

## Fintech example

Reconciliation looks up event_id, while payment history uses payment_id and time. One index need not optimize both.

## Implementation steps

1. Describe queries
2. Create a larger synthetic fixture
3. Measure a baseline
4. Add an index and compare reads and writes.

## Practical assignment

Compare payment history retrieval on 100000 events with and without an index. Save EXPLAIN QUERY PLAN output.

## Common mistake and its consequences

Indexing every column without workload evidence slows ingestion and enlarges storage.

## Verify the result

Record dataset size, plans, repeated timings, and write overhead.

## Self-check question

Why can a query that is faster on a small dataset become slower on a larger one?

## Further reading

- [PostgreSQL documentation](https://www.postgresql.org/docs/current/) — primary documentation; find the section relevant to this lesson.
- [Python sqlite3](https://docs.python.org/3.12/library/sqlite3.html) — primary documentation; find the section relevant to this lesson.

## Deliverable and navigation

Save your solution in your own fork under `portfolio/016-indexes/`. Include the problem, a minimal example, the check from “Verify the result,” and your answer to the self-check question. Design exercises may produce an ADR, diagram, or experiment table; distinguish a proposal from an implemented service.

[Previous step](../02-sql/015-transactions.md) · [Next step](../02-sql/017-incremental-sql.md) · [Full roadmap](../README.md)

**Module:** SQL and databases. **Estimated time:** 2–4 hours for a first pass; deeper practice and a project take additional time. The previous step defines reading order, not an equally mandatory prerequisite for every learner: see the [learning paths](../../docs/LEARNING_PATHS.md).

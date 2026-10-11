# 015. Transactions and batch atomicity

## Learning outcome

Verify that data and control state commit together.

## How it works

A transaction groups changes into an atomic unit. A failed batch must leave a consistent result or roll back. Choosing the unit is an architectural decision: very large batches hold resources longer, while row-level commits complicate completeness. An API and database transaction are not automatically one transaction.

## Fintech example

Postings exist but their raw event is missing, so the amount's provenance cannot be explained.

## Implementation steps

1. Define the atomic unit
2. Write raw and postings in one transaction
3. Inject an exception
4. Inspect rollback state.

## Practical assignment

Run test_conflict_rolls_back_batch. Place a valid new event before a conflicting one and verify that the new event is absent afterward.

## Common mistake and its consequences

Updating a checkpoint before data in another transaction skips unwritten records on restart.

## Verify the result

After failure, event and posting counts match the pre-batch snapshot.

## Self-check question

When is row quarantine preferable, and when must the entire batch roll back?

## Further reading

- [PostgreSQL documentation](https://www.postgresql.org/docs/current/) — primary documentation; find the section relevant to this lesson.
- [Python sqlite3](https://docs.python.org/3.12/library/sqlite3.html) — primary documentation; find the section relevant to this lesson.

## Deliverable and navigation

Save your solution in your own fork under `portfolio/015-transactions/`. Include the problem, a minimal example, the check from “Verify the result,” and your answer to the self-check question. Design exercises may produce an ADR, diagram, or experiment table; distinguish a proposal from an implemented service.

[Previous step](../02-sql/014-windows.md) · [Next step](../02-sql/016-indexes.md) · [Full roadmap](../README.md)

**Module:** SQL and databases. **Estimated time:** 2–4 hours for a first pass; deeper practice and a project take additional time. The previous step defines reading order, not an equally mandatory prerequisite for every learner: see the [learning paths](../../docs/LEARNING_PATHS.md).

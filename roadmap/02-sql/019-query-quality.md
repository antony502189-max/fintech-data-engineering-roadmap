# 019. SQL quality checks and control totals

## Learning outcome

Write checks that return violating rows.

## How it works

A data test can be a query whose successful result is empty and whose failures identify keys and reasons. Test nullability, uniqueness, relationships, ranges, and monetary invariants separately. Equal row counts do not prove identical records or amounts.

## Fintech example

Two records exchange currencies: count stays constant while USD and EUR totals become incorrect.

## Implementation steps

1. Define the invariant
2. Query violating rows
3. Create a defective fixture
4. Confirm detection.

## Practical assignment

Run sql/solutions/05-ledger.sql, then corrupt a posting in a separate temporary database.

## Common mistake and its consequences

Running checks only after publication allows consumers to read invalid data first.

## Verify the result

Quality gates precede readiness markers; failures identify event and currency.

## Self-check question

Which controls beyond row count are needed for a payment batch?

## Further reading

- [dbt data tests](https://docs.getdbt.com/docs/build/data-tests) — primary documentation; find the section relevant to this lesson.
- [PostgreSQL documentation](https://www.postgresql.org/docs/current/) — primary documentation; find the section relevant to this lesson.

## Deliverable and navigation

Save your solution in your own fork under `portfolio/019-query-quality/`. Include the problem, a minimal example, the check from “Verify the result,” and your answer to the self-check question. Design exercises may produce an ADR, diagram, or experiment table; distinguish a proposal from an implemented service.

[Previous step](../02-sql/018-dedup-sql.md) · [Next step](../02-sql/020-sql-review.md) · [Full roadmap](../README.md)

**Module:** SQL and databases. **Estimated time:** 2–4 hours for a first pass; deeper practice and a project take additional time. The previous step defines reading order, not an equally mandatory prerequisite for every learner: see the [learning paths](../../docs/LEARNING_PATHS.md).

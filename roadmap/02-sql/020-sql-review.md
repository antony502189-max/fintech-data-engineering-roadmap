# 020. SQL review and dialect portability

## Learning outcome

Review semantics, performance, and compatibility together.

## How it works

SQLite supports local learning, but types, time functions, locks, and SQL constructs differ from PostgreSQL and cloud warehouses. Porting requires explicit semantic verification. Review grain first, then joins, NULL, currencies, boundaries, tests, and rebuild plans.

## Fintech example

QUALIFY is available in some warehouses; SQLite examples use a ROW_NUMBER subquery. A teaching query is not automatically a production dbt model.

## Implementation steps

1. Build a checklist
2. Verify keys and totals
3. Mark dialect-specific functions
4. Explain historical recomputation.

## Practical assignment

Port a window exercise to PostgreSQL as an extension. State whether you actually executed that version.

## Common mistake and its consequences

Implicit casts and local timezones change results after migration without causing syntax errors.

## Verify the result

Clearly distinguish verified SQLite behavior from an unexecuted alternative.

## Self-check question

How can you verify temporal filter semantics when moving between warehouse engines?

## Further reading

- [PostgreSQL documentation](https://www.postgresql.org/docs/current/) — primary documentation; find the section relevant to this lesson.
- [Python sqlite3](https://docs.python.org/3.12/library/sqlite3.html) — primary documentation; find the section relevant to this lesson.

## Deliverable and navigation

Save your solution in your own fork under `portfolio/020-sql-review/`. Include the problem, a minimal example, the check from “Verify the result,” and your answer to the self-check question. Design exercises may produce an ADR, diagram, or experiment table; distinguish a proposal from an implemented service.

[Previous step](../02-sql/019-query-quality.md) · [Next step](../03-modeling/021-architecture.md) · [Full roadmap](../README.md)

**Module:** SQL and databases. **Estimated time:** 2–4 hours for a first pass; deeper practice and a project take additional time. The previous step defines reading order, not an equally mandatory prerequisite for every learner: see the [learning paths](../../docs/LEARNING_PATHS.md).

# 013. NULL, missing events, and unknown values

## Learning outcome

Distinguish zero, unknown values, and absent rows.

## How it works

NULL represents missing information, not zero. Use IS NULL; comparisons otherwise involve an unknown logical state. Aggregates often ignore NULL, hiding incompleteness. A right-table filter in WHERE can turn a LEFT JOIN into an effective INNER JOIN.

## Fintech example

A missing settlement row differs from a confirmed zero settlement: one is a completeness problem, while the other may be valid.

## Implementation steps

1. Define each NULL meaning
2. Preserve missing status
3. Put appropriate filters in ON
4. Report aggregate and known-value count together.

## Practical assignment

Add both a zero settlement and a missing payment to the reconciliation example. Compare results before and after COALESCE.

## Common mistake and its consequences

COALESCE(actual,0) makes a missing file look like a confirmed zero payout.

## Verify the result

The output distinguishes matched zero, missing_external, and amount_mismatch.

## Self-check question

Why does a missing refund event not prove that no refund will ever occur?

## Further reading

- [PostgreSQL documentation](https://www.postgresql.org/docs/current/) — primary documentation; find the section relevant to this lesson.

## Deliverable and navigation

Save your solution in your own fork under `portfolio/013-nulls/`. Include the problem, a minimal example, the check from “Verify the result,” and your answer to the self-check question. Design exercises may produce an ADR, diagram, or experiment table; distinguish a proposal from an implemented service.

[Previous step](../02-sql/012-joins.md) · [Next step](../02-sql/014-windows.md) · [Full roadmap](../README.md)

**Module:** SQL and databases. **Estimated time:** 2–4 hours for a first pass; deeper practice and a project take additional time. The previous step defines reading order, not an equally mandatory prerequisite for every learner: see the [learning paths](../../docs/LEARNING_PATHS.md).

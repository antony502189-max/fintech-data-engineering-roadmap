# 012. JOINs and monetary fanout

## Learning outcome

Prove join cardinality before publishing a monetary sum.

## How it works

A many-to-one join is safe only if the right-side key is unique. Joining two one-to-many tables on payment_id creates a cross-product. Aggregate both inputs to the required grain or use a bridge with allocation rules. DISTINCT on the final report usually conceals the defect.

## Fintech example

Two payment attempts and three fees produce six joined rows, repeating capture amounts.

## Implementation steps

1. Check keys on both sides
2. Measure rows before and after
3. Aggregate fees separately
4. Reconcile the capture control total.

## Practical assignment

Build attempts and fees fixtures with cardinalities two and three. Compare an incorrect query with a corrected one.

## Common mistake and its consequences

SUM(DISTINCT amount) removes separate payments that happen to have equal amounts.

## Verify the result

Two distinct captures of 10000 both count; adding fees does not inflate gross capture.

## Self-check question

How does joining a historical dimension differ from joining its current version?

## Further reading

- [PostgreSQL documentation](https://www.postgresql.org/docs/current/) — primary documentation; find the section relevant to this lesson.
- [Kimball dimensional modeling techniques](https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/) — primary documentation; find the section relevant to this lesson.

## Deliverable and navigation

Save your solution in your own fork under `portfolio/012-joins/`. Include the problem, a minimal example, the check from “Verify the result,” and your answer to the self-check question. Design exercises may produce an ADR, diagram, or experiment table; distinguish a proposal from an implemented service.

[Previous step](../02-sql/011-sql-grain.md) · [Next step](../02-sql/013-nulls.md) · [Full roadmap](../README.md)

**Module:** SQL and databases. **Estimated time:** 2–4 hours for a first pass; deeper practice and a project take additional time. The previous step defines reading order, not an equally mandatory prerequisite for every learner: see the [learning paths](../../docs/LEARNING_PATHS.md).

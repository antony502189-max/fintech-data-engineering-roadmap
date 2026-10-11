# 011. SQL: grain before SELECT

## Learning outcome

Define the meaning of a row before writing an aggregation.

## How it works

Grain identifies whether a record represents an event, payment, attempt, or dated balance. SQL can be syntactically valid while mixing these levels. GROUP BY cannot repair duplicated money after a join. Begin with the key and verify its uniqueness.

## Fintech example

One payment has capture, fee, and refund events. COUNT(*) counts those events rather than distinct payments.

## Implementation steps

1. Describe a row
2. Identify the natural key
3. Check uniqueness
4. List valid aggregations.

## Practical assignment

Count events and distinct payments in the lab. Explain the difference and write a query listing each payment's event composition.

## Common mistake and its consequences

An undefined “transaction count” changes when fees are added to an otherwise healthy pipeline.

## Verify the result

The fixture has six events and three payment IDs; document why each number is correct.

## Self-check question

When can DISTINCT payment_id also be the wrong business metric?

## Further reading

- [PostgreSQL documentation](https://www.postgresql.org/docs/current/) — primary documentation; find the section relevant to this lesson.
- [Kimball dimensional modeling techniques](https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/) — primary documentation; find the section relevant to this lesson.

## Deliverable and navigation

Save your solution in your own fork under `portfolio/011-sql-grain/`. Include the problem, a minimal example, the check from “Verify the result,” and your answer to the self-check question. Design exercises may produce an ADR, diagram, or experiment table; distinguish a proposal from an implemented service.

[Previous step](../01-foundations/010-systems.md) · [Next step](../02-sql/012-joins.md) · [Full roadmap](../README.md)

**Module:** SQL and databases. **Estimated time:** 2–4 hours for a first pass; deeper practice and a project take additional time. The previous step defines reading order, not an equally mandatory prerequisite for every learner: see the [learning paths](../../docs/LEARNING_PATHS.md).

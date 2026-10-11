# 014. Window functions and deterministic ordering

## Learning outcome

Use ROW_NUMBER, LAG, and running totals without arbitrary selection.

## How it works

Window functions preserve rows while computing over a partition. A latest-record query needs complete ordering: timestamps may tie, so use a stable source sequence or a contract-approved tie-breaker. ROWS and RANGE behave differently when ordering values are equal.

## Fintech example

Two status versions arrive in the same millisecond. Sorting only by updated_at may select different records across executions.

## Implementation steps

1. Choose the partition key
2. Define the tie-breaker
3. Specify the window frame
4. Test equal timestamps.

## Practical assignment

Compute cumulative net per currency with ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW; reconcile it with GROUP BY totals.

## Common mistake and its consequences

Treating file arrival order as business order creates unstable state.

## Verify the result

Reordering deliveries does not change the result when the source sequence is preserved.

## Self-check question

Why can MAX(timestamp) followed by a join return two “latest” rows?

## Further reading

- [PostgreSQL documentation](https://www.postgresql.org/docs/current/) — primary documentation; find the section relevant to this lesson.

## Deliverable and navigation

Save your solution in your own fork under `portfolio/014-windows/`. Include the problem, a minimal example, the check from “Verify the result,” and your answer to the self-check question. Design exercises may produce an ADR, diagram, or experiment table; distinguish a proposal from an implemented service.

[Previous step](../02-sql/013-nulls.md) · [Next step](../02-sql/015-transactions.md) · [Full roadmap](../README.md)

**Module:** SQL and databases. **Estimated time:** 2–4 hours for a first pass; deeper practice and a project take additional time. The previous step defines reading order, not an equally mandatory prerequisite for every learner: see the [learning paths](../../docs/LEARNING_PATHS.md).

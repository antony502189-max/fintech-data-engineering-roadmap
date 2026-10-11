# 023. Transaction, periodic, and accumulating facts

## Learning outcome

Choose a fact-table type for the consumer's question.

## How it works

Transaction facts record events; periodic snapshots record state on a schedule; accumulating snapshots update process milestones. They have different additivity. Flows can be summed over time, while month-end balances cannot be calculated by summing daily balances.

## Fintech example

Capture and refund are flows; merchant balance on a date is state.

## Implementation steps

1. Define the question
2. Specify each fact's grain
3. Describe additivity
4. Separate flows from balances.

## Practical assignment

Design three fact tables for one payment. Show a query where summing snapshots across days is invalid.

## Common mistake and its consequences

Publishing the sum of daily balances as monthly turnover invents monetary movement.

## Verify the result

State which dimensions permit SUM and why time aggregation of balances is restricted.

## Self-check question

Which questions cannot be answered by an accumulating snapshot without an event history?

## Further reading

- [Kimball dimensional modeling techniques](https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/) — primary documentation; find the section relevant to this lesson.

## Deliverable and navigation

Save your solution in your own fork under `portfolio/023-facts/`. Include the problem, a minimal example, the check from “Verify the result,” and your answer to the self-check question. Design exercises may produce an ADR, diagram, or experiment table; distinguish a proposal from an implemented service.

[Previous step](../03-modeling/022-layers.md) · [Next step](../03-modeling/024-dimensions.md) · [Full roadmap](../README.md)

**Module:** DWH modeling. **Estimated time:** 2–4 hours for a first pass; deeper practice and a project take additional time. The previous step defines reading order, not an equally mandatory prerequisite for every learner: see the [learning paths](../../docs/LEARNING_PATHS.md).

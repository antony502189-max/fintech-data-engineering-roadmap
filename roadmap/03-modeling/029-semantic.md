# 029. Semantic layers and shared metrics

## Learning outcome

Define gross, net, fees, and revenue explicitly.

## How it works

“Net” may mean cash, sales, or revenue. A metric needs grain, numerator, currency, time, and exclusions. A semantic layer centralizes formulas but does not replace agreement with a process owner. Meaning changes require versioned definitions.

## Fintech example

The lab computes captured minus refunded minus fees: synthetic net cash, not company revenue.

## Implementation steps

1. Describe the formula
2. State sign conventions
3. Name the owner
4. Include numerical examples and exclusions.

## Practical assignment

Write metric contracts for gross capture and net cash. Explain separately why revenue is not implemented.

## Common mistake and its consequences

Calling a teaching cash formula profitability ignores costs, FX, and recognition rules.

## Verify the result

The contract separates cash from revenue and matches the lab's numerical output.

## Self-check question

How can a changed definition preserve useful historical comparisons?

## Further reading

- [Kimball dimensional modeling techniques](https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/) — primary documentation; find the section relevant to this lesson.
- [Stripe balance transaction types](https://docs.stripe.com/reports/balance-transaction-types) — primary documentation; find the section relevant to this lesson.

## Deliverable and navigation

Save your solution in your own fork under `portfolio/029-semantic/`. Include the problem, a minimal example, the check from “Verify the result,” and your answer to the self-check question. Design exercises may produce an ADR, diagram, or experiment table; distinguish a proposal from an implemented service.

[Previous step](../03-modeling/028-entity-events.md) · [Next step](../03-modeling/030-model-review.md) · [Full roadmap](../README.md)

**Module:** DWH modeling. **Estimated time:** 2–4 hours for a first pass; deeper practice and a project take additional time. The previous step defines reading order, not an equally mandatory prerequisite for every learner: see the [learning paths](../../docs/LEARNING_PATHS.md).

# 067. Credit lifecycles and debt marts

## Learning outcome

Distinguish disbursements, accruals, repayments, and balances.

## How it works

Disbursement creates a flow and obligation; accruals change debt components; repayments follow an agreed allocation waterfall. Dated outstanding balance is a snapshot, not a sum of daily states. Actual interest and allocation rules are product-specific; the example does not define lending policy.

## Fintech example

Synthetic repayment 1200 allocates fee 100, interest 200, and principal 900 under the teaching order.

## Implementation steps

1. Define loan events
2. Fix allocation order
3. Separate components
4. Verify conservation.

## Practical assignment

Implement allocation against specified amounts due and preserve excess as unallocated.

## Common mistake and its consequences

Subtracting all repayments from principal ignores other components and policy.

## Verify the result

Allocations plus remainder equal payment; no debt component becomes negative.

## Self-check question

Why is summing daily principal balances not a measure of monthly disbursement?

## Further reading

- [Kimball dimensional modeling techniques](https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/) — primary documentation; find the section relevant to this lesson.
- [Python Tutorial](https://docs.python.org/3.12/tutorial/) — primary documentation; find the section relevant to this lesson.

## Deliverable and navigation

Save your solution in your own fork under `portfolio/067-credit/`. Include the problem, a minimal example, the check from “Verify the result,” and your answer to the self-check question. Design exercises may produce an ADR, diagram, or experiment table; distinguish a proposal from an implemented service.

[Previous step](../07-fintech/066-cutoff-close.md) · [Next step](../07-fintech/068-fraud-data.md) · [Full roadmap](../README.md)

**Module:** Financial data and money movement. **Estimated time:** 2–4 hours for a first pass; deeper practice and a project take additional time. The previous step defines reading order, not an equally mandatory prerequisite for every learner: see the [learning paths](../../docs/LEARNING_PATHS.md).

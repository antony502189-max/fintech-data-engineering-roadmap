# 062. Double entry and conservation checks

## Learning outcome

Build paired postings and verify event-level balance.

## How it works

The teaching journal uses signed postings summing to zero per event and currency. This is a conservation model, not a complete accounting chart. Balance is necessary but insufficient: wrong accounts or equally wrong amounts can remain balanced.

## Fintech example

The simplified capture increases processor_receivable and decreases merchant_payable.

## Implementation steps

1. Specify ledger perspective
2. Document signs
3. Generate postings
4. Check balance and independent totals.

## Practical assignment

Create an imbalance, then a balanced incorrect amount. Compare the checks that detect them.

## Common mistake and its consequences

Calling sum=0 proof of financial accuracy overlooks balanced errors.

## Verify the result

Balance tests detect imbalance; reconciliation detects an incorrect amount that conservation missed.

## Self-check question

Which defects remain possible when every posting group balances?

## Further reading

- [Stripe balance transaction types](https://docs.stripe.com/reports/balance-transaction-types) — primary documentation; find the section relevant to this lesson.
- [PostgreSQL documentation](https://www.postgresql.org/docs/current/) — primary documentation; find the section relevant to this lesson.

## Deliverable and navigation

Save your solution in your own fork under `portfolio/062-double-entry/`. Include the problem, a minimal example, the check from “Verify the result,” and your answer to the self-check question. Design exercises may produce an ADR, diagram, or experiment table; distinguish a proposal from an implemented service.

[Previous step](../07-fintech/061-payment-lifecycle.md) · [Next step](../07-fintech/063-reconciliation.md) · [Full roadmap](../README.md)

**Module:** Financial data and money movement. **Estimated time:** 2–4 hours for a first pass; deeper practice and a project take additional time. The previous step defines reading order, not an equally mandatory prerequisite for every learner: see the [learning paths](../../docs/LEARNING_PATHS.md).

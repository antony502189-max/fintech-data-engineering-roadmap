# 063. Internal and external reconciliation

## Learning outcome

Match independent monetary records at an agreed grain.

## How it works

Reconciliation connects expected movement with external confirmation. Agree on currency, identity, cutoff, and signs. An inner join hides missing and unexpected records; preserve both sides. Tolerances require an approved justification, while exact minor-unit comparisons often use zero.

## Fintech example

p3 expects 2500 but receives 2400 externally; p9 exists only externally.

## Implementation steps

1. Agree on grain
2. Check external uniqueness
3. Match the union of keys
4. Classify exceptions.

## Practical assignment

Run reconciliation, correct p3 in a personal external fixture, and explain why p9 still remains an exception.

## Common mistake and its consequences

Matching only by amount combines separate equal-value payments.

## Verify the result

Report matched, mismatch, missing, and unexpected records without dropping either side.

## Self-check question

When does a payout require many-to-many allocation rather than a payment-ID match?

## Further reading

- [Stripe balance transaction types](https://docs.stripe.com/reports/balance-transaction-types) — primary documentation; find the section relevant to this lesson.
- [PostgreSQL documentation](https://www.postgresql.org/docs/current/) — primary documentation; find the section relevant to this lesson.

## Deliverable and navigation

Save your solution in your own fork under `portfolio/063-reconciliation/`. Include the problem, a minimal example, the check from “Verify the result,” and your answer to the self-check question. Design exercises may produce an ADR, diagram, or experiment table; distinguish a proposal from an implemented service.

[Previous step](../07-fintech/062-double-entry.md) · [Next step](../07-fintech/064-refunds.md) · [Full roadmap](../README.md)

**Module:** Financial data and money movement. **Estimated time:** 2–4 hours for a first pass; deeper practice and a project take additional time. The previous step defines reading order, not an equally mandatory prerequisite for every learner: see the [learning paths](../../docs/LEARNING_PATHS.md).

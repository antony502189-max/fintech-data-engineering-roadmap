# 064. Partial refunds, fees, and reversals

## Learning outcome

Separate returning money from correcting a prior representation.

## How it works

A refund returns funds, a reversal compensates a specific posting, and a correction repairs an incorrect representation. Fee refunds may be full, partial, or absent under the product agreement. A universal negative-capture rule is insufficient. Retain original-operation links and reasons.

## Fintech example

Capture 10000, fee 300, and refund 2000 yield synthetic net cash 7700; fee refunds are not automatically modeled.

## Implementation steps

1. Define event kinds
2. Link refunds to captures
3. Check cumulative refunds
4. Document fee policy.

## Practical assignment

Add refund_id and original_capture_id to a proposed schema. Test two partial refunds and over-refund detection.

## Common mistake and its consequences

Counting both refund and chargeback for one movement overstates outflows.

## Verify the result

Check refunds against capture and currency, and identify policy versions.

## Self-check question

How do you distinguish repeated delivery from two equal partial refunds?

## Further reading

- [Stripe balance transaction types](https://docs.stripe.com/reports/balance-transaction-types) — primary documentation; find the section relevant to this lesson.
- [Stripe idempotent requests](https://docs.stripe.com/api/idempotent_requests) — primary documentation; find the section relevant to this lesson.

## Deliverable and navigation

Save your solution in your own fork under `portfolio/064-refunds/`. Include the problem, a minimal example, the check from “Verify the result,” and your answer to the self-check question. Design exercises may produce an ADR, diagram, or experiment table; distinguish a proposal from an implemented service.

[Previous step](../07-fintech/063-reconciliation.md) · [Next step](../07-fintech/065-fx.md) · [Full roadmap](../README.md)

**Module:** Financial data and money movement. **Estimated time:** 2–4 hours for a first pass; deeper practice and a project take additional time. The previous step defines reading order, not an equally mandatory prerequisite for every learner: see the [learning paths](../../docs/LEARNING_PATHS.md).

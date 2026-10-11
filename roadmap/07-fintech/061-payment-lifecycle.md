# 061. The payment lifecycle

## Learning outcome

Distinguish authorization, capture, settlement, refund, and dispute.

## How it works

Authorization confirms permission or capacity; capture establishes confirmed movement or a claim; settlement reflects provider-side clearing. Exact meaning and timing depend on payment methods. Refunds and chargebacks have different causes and lifecycles. Retain explicit stages rather than one universal success flag.

## Fintech example

Capture 10000 and refund 2000 produce a flow of 8000 before fees, while settlement may occur later.

## Implementation steps

1. Define the state machine
2. Separate money and status events
3. Name stage timestamps
4. Document provider-specific limits.

## Practical assignment

Draw p1's timeline from payments() and add a proposed settlement stage on January 3.

## Common mistake and its consequences

Including authorizations in cash turns canceled attempts into fictitious turnover.

## Verify the result

For each stage, identify flow, state, or expected obligation.

## Self-check question

Why are paid, captured, and settled not universal synonyms?

## Further reading

- [Stripe balance transaction types](https://docs.stripe.com/reports/balance-transaction-types) — primary documentation; find the section relevant to this lesson.
- [Stripe webhook delivery](https://docs.stripe.com/webhooks) — primary documentation; find the section relevant to this lesson.

## Deliverable and navigation

Save your solution in your own fork under `portfolio/061-payment-lifecycle/`. Include the problem, a minimal example, the check from “Verify the result,” and your answer to the self-check question. Design exercises may produce an ADR, diagram, or experiment table; distinguish a proposal from an implemented service.

[Previous step](../06-transformation/060-docs-ops.md) · [Next step](../07-fintech/062-double-entry.md) · [Full roadmap](../README.md)

**Module:** Financial data and money movement. **Estimated time:** 2–4 hours for a first pass; deeper practice and a project take additional time. The previous step defines reading order, not an equally mandatory prerequisite for every learner: see the [learning paths](../../docs/LEARNING_PATHS.md).

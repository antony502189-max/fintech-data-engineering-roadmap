# 028. Entity state and event history

## Learning outcome

Model payment transitions without losing meaningful changes.

## How it works

A current payment record is convenient but replaces earlier state. Event history retains transitions and supports replay. Out-of-order deliveries mean latest receipt is not necessarily latest business state. Corrections and reversals have different financial effects.

## Fintech example

A refund arrives before its capture. Temporary missing context must not permanently destroy the eventual history.

## Implementation steps

1. Define a state machine
2. Specify source order
3. Separate financial events
4. Handle out-of-order delivery.

## Practical assignment

Draw authorization, capture, partial-refund, and full-refund transitions. Mark which move money.

## Common mistake and its consequences

Selecting final state by latest received_at lets a delayed authorization replace a capture.

## Verify the result

Changing delivery order preserves monetary totals; invalid transitions appear in quality output.

## Self-check question

Why is a “successful” status insufficient to calculate money movement?

## Further reading

- [Stripe webhook delivery](https://docs.stripe.com/webhooks) — primary documentation; find the section relevant to this lesson.
- [Stripe balance transaction types](https://docs.stripe.com/reports/balance-transaction-types) — primary documentation; find the section relevant to this lesson.

## Deliverable and navigation

Save your solution in your own fork under `portfolio/028-entity-events/`. Include the problem, a minimal example, the check from “Verify the result,” and your answer to the self-check question. Design exercises may produce an ADR, diagram, or experiment table; distinguish a proposal from an implemented service.

[Previous step](../03-modeling/027-data-vault.md) · [Next step](../03-modeling/029-semantic.md) · [Full roadmap](../README.md)

**Module:** DWH modeling. **Estimated time:** 2–4 hours for a first pass; deeper practice and a project take additional time. The previous step defines reading order, not an equally mandatory prerequisite for every learner: see the [learning paths](../../docs/LEARNING_PATHS.md).

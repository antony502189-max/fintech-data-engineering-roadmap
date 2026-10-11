# 033. Webhooks: signatures, repeats, and ordering

## Learning outcome

Design reception with safe acknowledgments.

## How it works

Verify signatures against original bytes, then durably save the event or enqueue it before returning success. Duplicates and out-of-order delivery are normal. A signature authenticates payload origin but does not prove the complete event set. Reconcile with API or settlement evidence.

## Fintech example

The provider repeats e1 after losing the response. Acknowledgment must not create another monetary movement.

## Implementation steps

1. Verify before parsing
2. Retain delivery metadata
3. Enqueue durably
4. Deduplicate business identity.

## Practical assignment

Draw a timeout-after-enqueue sequence. Implement a real HTTP endpoint only as an extension; the lab does not include one.

## Common mistake and its consequences

Returning 200 before durable storage can lose an event permanently after a crash.

## Verify the result

Every acknowledged event exists durably in the crash matrix.

## Self-check question

Why does a valid signature not authorize applying a repeat again?

## Further reading

- [Stripe webhook delivery](https://docs.stripe.com/webhooks) — primary documentation; find the section relevant to this lesson.
- [Stripe idempotent requests](https://docs.stripe.com/api/idempotent_requests) — primary documentation; find the section relevant to this lesson.

## Deliverable and navigation

Save your solution in your own fork under `portfolio/033-webhooks/`. Include the problem, a minimal example, the check from “Verify the result,” and your answer to the self-check question. Design exercises may produce an ADR, diagram, or experiment table; distinguish a proposal from an implemented service.

[Previous step](../04-ingestion/032-api-connectors.md) · [Next step](../04-ingestion/034-cdc-basics.md) · [Full roadmap](../README.md)

**Module:** Ingestion and CDC. **Estimated time:** 2–4 hours for a first pass; deeper practice and a project take additional time. The previous step defines reading order, not an equally mandatory prerequisite for every learner: see the [learning paths](../../docs/LEARNING_PATHS.md).

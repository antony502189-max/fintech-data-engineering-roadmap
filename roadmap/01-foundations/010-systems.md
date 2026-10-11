# 010. Distributed systems without magic

## Learning outcome

Describe the boundaries of delivery and persistence guarantees.

## How it works

The network can lose a response after a successful write, leaving the client uncertain. At-least-once permits repeats; at-most-once permits loss. Exactly-once claims need a defined boundary and atomicity mechanism. A broker transaction does not automatically include an arbitrary external database.

## Fintech example

A consumer writes a payment to the warehouse and crashes before acknowledging the offset. Redelivery must encounter a durable deduplication key.

## Implementation steps

1. Mark commit points
2. Enumerate crash locations
3. Define permitted repeats
4. Choose identity and transaction boundaries.

## Practical assignment

Build a crash matrix covering before insert, after insert, after commit, and after acknowledgment.

## Common mistake and its consequences

Claiming end-to-end exactly-once from producer configuration alone ignores external side effects.

## Verify the result

For each failure point, specify sink state, redelivery behavior, and the recovery result.

## Self-check question

What additional condition makes replay safe when a repeated ID carries a changed payload?

## Further reading

- [Apache Kafka documentation](https://kafka.apache.org/documentation/) — primary documentation; find the section relevant to this lesson.
- [Stripe idempotent requests](https://docs.stripe.com/api/idempotent_requests) — primary documentation; find the section relevant to this lesson.

## Deliverable and navigation

Save your solution in your own fork under `portfolio/010-systems/`. Include the problem, a minimal example, the check from “Verify the result,” and your answer to the self-check question. Design exercises may produce an ADR, diagram, or experiment table; distinguish a proposal from an implemented service.

[Previous step](../01-foundations/009-time-money.md) · [Next step](../02-sql/011-sql-grain.md) · [Full roadmap](../README.md)

**Module:** Engineering foundations. **Estimated time:** 2–4 hours for a first pass; deeper practice and a project take additional time. The previous step defines reading order, not an equally mandatory prerequisite for every learner: see the [learning paths](../../docs/LEARNING_PATHS.md).

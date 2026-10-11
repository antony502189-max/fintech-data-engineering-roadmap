# 038. Transactional outbox

## Learning outcome

Explain atomic state changes and publication intent.

## How it works

Write an outbox entry in the same database transaction as the business change. A relay publishes it and may repeat delivery. This closes the gap between OLTP commit and message publication but does not remove consumer deduplication requirements. Ordering needs explicit sequence and partition rules.

## Fintech example

Capture commits with its outbox entry; a relay crash does not lose publication intent.

## Implementation steps

1. Define the outbox schema
2. Commit it with business state
3. Make the relay retryable
4. Validate consumer identity.

## Practical assignment

Write the transaction and a crash matrix for publish-before-mark and mark-before-publish.

## Common mistake and its consequences

Marking an entry published before sending loses it if the relay crashes between steps.

## Verify the result

Publication can repeat, but a business commit cannot lack its required outbox entry.

## Self-check question

Why does outbox not guarantee exactly-once in an external sink?

## Further reading

- [PostgreSQL documentation](https://www.postgresql.org/docs/current/) — primary documentation; find the section relevant to this lesson.
- [Apache Kafka documentation](https://kafka.apache.org/documentation/) — primary documentation; find the section relevant to this lesson.

## Deliverable and navigation

Save your solution in your own fork under `portfolio/038-outbox/`. Include the problem, a minimal example, the check from “Verify the result,” and your answer to the self-check question. Design exercises may produce an ADR, diagram, or experiment table; distinguish a proposal from an implemented service.

[Previous step](../04-ingestion/037-schema-evolution.md) · [Next step](../04-ingestion/039-replay.md) · [Full roadmap](../README.md)

**Module:** Ingestion and CDC. **Estimated time:** 2–4 hours for a first pass; deeper practice and a project take additional time. The previous step defines reading order, not an equally mandatory prerequisite for every learner: see the [learning paths](../../docs/LEARNING_PATHS.md).

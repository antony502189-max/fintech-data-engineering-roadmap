# 049. Stream state and checkpoint recovery

## Learning outcome

Explain checkpoint recovery and its guarantee boundary.

## How it works

Stateful processing stores aggregates, timers, and progress. A consistent checkpoint links state with source positions. External sinks need compatible commit semantics; checkpoints alone cannot prevent repeated side effects. Deduplication retention limits the safe replay horizon.

## Fintech example

A consumer restores yesterday's state, but an external settlement notification was already sent.

## Implementation steps

1. Describe state
2. Choose durable checkpoint storage
3. Verify sink protocol
4. Test replay beyond retention.

## Practical assignment

Design event-ID deduplication with a seven-day TTL and a thirty-day replay request.

## Common mistake and its consequences

Expiring identity keys before the replay horizon lets old captures count again.

## Verify the result

Align TTL with replay horizons or retain durable uniqueness in the sink.

## Self-check question

Which external side effects are not covered by restoring stream state?

## Further reading

- [Flink event time](https://nightlies.apache.org/flink/flink-docs-stable/docs/concepts/time/) — primary documentation; find the section relevant to this lesson.
- [Apache Kafka documentation](https://kafka.apache.org/documentation/) — primary documentation; find the section relevant to this lesson.

## Deliverable and navigation

Save your solution in your own fork under `portfolio/049-state-checkpoints/`. Include the problem, a minimal example, the check from “Verify the result,” and your answer to the self-check question. Design exercises may produce an ADR, diagram, or experiment table; distinguish a proposal from an implemented service.

[Previous step](../05-storage/048-event-time.md) · [Next step](../05-storage/050-storage-decision.md) · [Full roadmap](../README.md)

**Module:** Storage and processing. **Estimated time:** 2–4 hours for a first pass; deeper practice and a project take additional time. The previous step defines reading order, not an equally mandatory prerequisite for every learner: see the [learning paths](../../docs/LEARNING_PATHS.md).

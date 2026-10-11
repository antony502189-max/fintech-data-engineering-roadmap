# 047. Kafka partitions, offsets, and ordering

## Learning outcome

Define ordering scope and a safe offset acknowledgment point.

## How it works

Kafka orders records within a partition, not globally across partitions. Producer partitioning maps keys to partitions. Consumer groups distribute partitions across consumers. An offset is a position, not business identity; repeated reading must be safe in the sink.

## Fintech example

Capture and refund for one payment need a defined order, while unrelated payments usually need no global order.

## Implementation steps

1. Select keys
2. Define consumer groups
3. Draw commit order
4. Test rebalance recovery.

## Practical assignment

Describe crashes before sink commit and after sink commit but before offset acknowledgment.

## Common mistake and its consequences

Using offsets as event IDs confuses delivery position with identity across topics or repartitioning.

## Verify the result

The crash matrix explains repeat delivery without doubled monetary totals.

## Self-check question

How can changing partition count affect assumptions about key ordering?

## Further reading

- [Apache Kafka documentation](https://kafka.apache.org/documentation/) — primary documentation; find the section relevant to this lesson.

## Deliverable and navigation

Save your solution in your own fork under `portfolio/047-streaming/`. Include the problem, a minimal example, the check from “Verify the result,” and your answer to the self-check question. Design exercises may produce an ADR, diagram, or experiment table; distinguish a proposal from an implemented service.

[Previous step](../05-storage/046-skew-joins.md) · [Next step](../05-storage/048-event-time.md) · [Full roadmap](../README.md)

**Module:** Storage and processing. **Estimated time:** 2–4 hours for a first pass; deeper practice and a project take additional time. The previous step defines reading order, not an equally mandatory prerequisite for every learner: see the [learning paths](../../docs/LEARNING_PATHS.md).

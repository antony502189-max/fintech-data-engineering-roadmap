# 048. Event time, watermarks, and late data

## Learning outcome

Separate window progress from data completeness.

## How it works

Event time describes business activity; processing time describes execution. A watermark estimates temporal progress under stream rules and does not prove every event arrived. Late records may require updates, retractions, or corrections. Financial close still needs independent completeness evidence.

## Fintech example

e6 arrives two days late and changes an earlier daily total; closing a stream window does not make it disappear.

## Implementation steps

1. Choose lateness tolerance
2. Define a side output
3. Specify correction policy
4. Reconcile stream and batch results.

## Practical assignment

Draw e1 and e6 timelines with provisional, updated, and closed totals.

## Common mistake and its consequences

Treating a watermark as proof of no future arrivals silently drops late captures.

## Verify the result

Events beyond allowed lateness have a verifiable processing route.

## Self-check question

When is a separate correction report an acceptable treatment of late events?

## Further reading

- [Flink event time](https://nightlies.apache.org/flink/flink-docs-stable/docs/concepts/time/) — primary documentation; find the section relevant to this lesson.

## Deliverable and navigation

Save your solution in your own fork under `portfolio/048-event-time/`. Include the problem, a minimal example, the check from “Verify the result,” and your answer to the self-check question. Design exercises may produce an ADR, diagram, or experiment table; distinguish a proposal from an implemented service.

[Previous step](../05-storage/047-streaming.md) · [Next step](../05-storage/049-state-checkpoints.md) · [Full roadmap](../README.md)

**Module:** Storage and processing. **Estimated time:** 2–4 hours for a first pass; deeper practice and a project take additional time. The previous step defines reading order, not an equally mandatory prerequisite for every learner: see the [learning paths](../../docs/LEARNING_PATHS.md).

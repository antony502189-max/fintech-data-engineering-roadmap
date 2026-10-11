# 035. Snapshots and the handoff to streaming

## Learning outcome

Verify bootstrap and CDC restart completeness.

## How it works

A consistent snapshot represents state at a log boundary. Streaming must continue without a gap. Large snapshots can stress the source and retain resources. Partial restart behavior depends on the connector and mode; do not assume all implementations behave alike.

## Fintech example

The merchant tariff changes while its table is being scanned. Snapshot and stream must produce an explainable version.

## Implementation steps

1. Choose snapshot mode
2. Preserve positions
3. Measure source impact
4. Inject a mid-snapshot restart.

## Practical assignment

Plan verification using key counts, checksums, and changes made during the snapshot.

## Common mistake and its consequences

Mixing restarted snapshot generations without identification combines different states.

## Verify the result

The result reconciles to source state at the chosen position; raw generations are identifiable.

## Self-check question

How do you prove there is no gap between snapshot and change stream?

## Further reading

- [Debezium PostgreSQL connector](https://debezium.io/documentation/reference/stable/connectors/postgresql.html) — primary documentation; find the section relevant to this lesson.

## Deliverable and navigation

Save your solution in your own fork under `portfolio/035-cdc-snapshots/`. Include the problem, a minimal example, the check from “Verify the result,” and your answer to the self-check question. Design exercises may produce an ADR, diagram, or experiment table; distinguish a proposal from an implemented service.

[Previous step](../04-ingestion/034-cdc-basics.md) · [Next step](../04-ingestion/036-cdc-deletes.md) · [Full roadmap](../README.md)

**Module:** Ingestion and CDC. **Estimated time:** 2–4 hours for a first pass; deeper practice and a project take additional time. The previous step defines reading order, not an equally mandatory prerequisite for every learner: see the [learning paths](../../docs/LEARNING_PATHS.md).

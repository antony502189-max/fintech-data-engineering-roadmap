# 040. Audit metadata and completeness evidence

## Learning outcome

Retain enough context to investigate ingestion.

## How it works

Run metadata connects partitions, input hashes, code revisions, schema versions, parameters, accepted counts, and rejected records. Audit information needs stable identity, protection against silent alteration, and suitable retention. Do not place credentials or unnecessary payload in logs.

## Fintech example

Explaining p3's late appearance needs event_time, received_at, and the processing run.

## Implementation steps

1. Define the run schema
2. Separate technical and business totals
3. Retain rejected counts
4. Attach manifests to output.

## Practical assignment

Create a lab manifest showing six accepted events, zero rejects, and six replay duplicates.

## Common mistake and its consequences

Duration and status=success alone cannot establish monetary completeness.

## Verify the result

Every output period has input hashes, transformation versions, and currency-specific controls.

## Self-check question

How would you detect a successful ingestion of an incomplete file?

## Further reading

- [OpenTelemetry concepts](https://opentelemetry.io/docs/concepts/) — primary documentation; find the section relevant to this lesson.
- [PostgreSQL documentation](https://www.postgresql.org/docs/current/) — primary documentation; find the section relevant to this lesson.

## Deliverable and navigation

Save your solution in your own fork under `portfolio/040-ingestion-audit/`. Include the problem, a minimal example, the check from “Verify the result,” and your answer to the self-check question. Design exercises may produce an ADR, diagram, or experiment table; distinguish a proposal from an implemented service.

[Previous step](../04-ingestion/039-replay.md) · [Next step](../05-storage/041-columnar.md) · [Full roadmap](../README.md)

**Module:** Ingestion and CDC. **Estimated time:** 2–4 hours for a first pass; deeper practice and a project take additional time. The previous step defines reading order, not an equally mandatory prerequisite for every learner: see the [learning paths](../../docs/LEARNING_PATHS.md).

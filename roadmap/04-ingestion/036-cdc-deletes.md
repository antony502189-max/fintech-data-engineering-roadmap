# 036. Deletes, tombstones, and retention

## Learning outcome

Separate current-state deletion from historical preservation.

## How it works

A delete event reports removal of a row. A compaction tombstone is not a business refund. Current projections usually reflect deletion; historical records follow approved retention and protection policies. Personal-data handling depends on classification and jurisdiction.

## Fintech example

Deleting a customer profile must not invent a refund for a previously posted payment.

## Implementation steps

1. Define current projection
2. Separate deletion from reversal
3. Check history policy
4. Preserve appropriate lineage keys.

## Practical assignment

Compare hard profile deletion, soft merchant deletion, and payment refund. Specify different warehouse outcomes.

## Common mistake and its consequences

Cascading dimension deletion destroys monetary facts; tombstones become fictitious zero amounts.

## Verify the result

Current state is correct, no financial event is invented, and history policy is explicit.

## Self-check question

How can monetary evidence be retained while minimizing personal attributes?

## Further reading

- [Debezium PostgreSQL connector](https://debezium.io/documentation/reference/stable/connectors/postgresql.html) — primary documentation; find the section relevant to this lesson.

## Deliverable and navigation

Save your solution in your own fork under `portfolio/036-cdc-deletes/`. Include the problem, a minimal example, the check from “Verify the result,” and your answer to the self-check question. Design exercises may produce an ADR, diagram, or experiment table; distinguish a proposal from an implemented service.

[Previous step](../04-ingestion/035-cdc-snapshots.md) · [Next step](../04-ingestion/037-schema-evolution.md) · [Full roadmap](../README.md)

**Module:** Ingestion and CDC. **Estimated time:** 2–4 hours for a first pass; deeper practice and a project take additional time. The previous step defines reading order, not an equally mandatory prerequisite for every learner: see the [learning paths](../../docs/LEARNING_PATHS.md).

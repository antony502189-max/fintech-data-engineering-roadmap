# 018. Deduplication and conflicting keys

## Learning outcome

Distinguish a safe repeat from an identity violation.

## How it works

Deduplication requires a stable key and payload comparison policy. Event_id identifies the business event; received_at describes delivery. A repeated key with a different amount is a conflict, not a harmless duplicate. Hashes require canonical types and field ordering.

## Fintech example

The provider resends e1 a day later. That is safe; e1 with 10001 instead of 10000 needs investigation.

## Implementation steps

1. Normalize payloads
2. Exclude delivery metadata
3. Compare business fields
4. Make conflicts visible.

## Practical assignment

Change received_at and amount_minor separately, then explain the different ingest outcomes.

## Common mistake and its consequences

INSERT OR IGNORE hides identity collisions and changed monetary values.

## Verify the result

Redelivery returns duplicates=1; a changed business field raises an error and rolls back the batch.

## Self-check question

Why is payment_id insufficient to deduplicate both refunds and fees?

## Further reading

- [Stripe idempotent requests](https://docs.stripe.com/api/idempotent_requests) — primary documentation; find the section relevant to this lesson.
- [PostgreSQL documentation](https://www.postgresql.org/docs/current/) — primary documentation; find the section relevant to this lesson.

## Deliverable and navigation

Save your solution in your own fork under `portfolio/018-dedup-sql/`. Include the problem, a minimal example, the check from “Verify the result,” and your answer to the self-check question. Design exercises may produce an ADR, diagram, or experiment table; distinguish a proposal from an implemented service.

[Previous step](../02-sql/017-incremental-sql.md) · [Next step](../02-sql/019-query-quality.md) · [Full roadmap](../README.md)

**Module:** SQL and databases. **Estimated time:** 2–4 hours for a first pass; deeper practice and a project take additional time. The previous step defines reading order, not an equally mandatory prerequisite for every learner: see the [learning paths](../../docs/LEARNING_PATHS.md).

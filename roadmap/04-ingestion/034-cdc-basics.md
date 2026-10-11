# 034. CDC, WAL, and state changes

## Learning outcome

Distinguish snapshots, row changes, and business events.

## How it works

CDC reads database changes, including inserts, updates, and deletes. WAL positions order database modifications, not necessarily payment business time. Updating a technical column need not create a financial event. Initial snapshot and streaming require a consistent boundary.

## Fintech example

Changing payment status is not another capture posting; otherwise maintenance updates inflate turnover.

## Implementation steps

1. Identify source tables
2. Define the snapshot boundary
3. Retain operations and positions
4. Separate state CDC from domain events.

## Practical assignment

Draw PostgreSQL → Debezium → Kafka → raw. Identify source and delivery semantics for each field.

## Common mistake and its consequences

Treating all CDC inserts as new payments counts existing snapshot records again.

## Verify the result

Explain how snapshot records avoid double counting and how deletion changes current state.

## Self-check question

When can CDC not recover the entire business history from a current OLTP table?

## Further reading

- [Debezium PostgreSQL connector](https://debezium.io/documentation/reference/stable/connectors/postgresql.html) — primary documentation; find the section relevant to this lesson.

## Deliverable and navigation

Save your solution in your own fork under `portfolio/034-cdc-basics/`. Include the problem, a minimal example, the check from “Verify the result,” and your answer to the self-check question. Design exercises may produce an ADR, diagram, or experiment table; distinguish a proposal from an implemented service.

[Previous step](../04-ingestion/033-webhooks.md) · [Next step](../04-ingestion/035-cdc-snapshots.md) · [Full roadmap](../README.md)

**Module:** Ingestion and CDC. **Estimated time:** 2–4 hours for a first pass; deeper practice and a project take additional time. The previous step defines reading order, not an equally mandatory prerequisite for every learner: see the [learning paths](../../docs/LEARNING_PATHS.md).

# 037. Schema evolution and compatibility

## Learning outcome

Handle contract changes before corrupted data is published.

## How it works

An additional field may be compatible, but a strict consumer needs an explicit unknown-field policy. Changing amount units or currency meaning is breaking even when the name stays unchanged. Contract versions, dual readers, and a migration window decouple producers and consumers.

## Fintech example

A provider changes integer cents to decimal major-unit strings. Old code introduces a hundredfold error.

## Implementation steps

1. Define compatibility
2. Add schema versions
3. Test old and new fixtures
4. Plan switching and rollback.

## Practical assignment

Extend your validator copy and design migration between two payload versions.

## Common mistake and its consequences

Automatic casts conceal lost precision and changed units.

## Verify the result

Unknown versions are quarantined; supported versions produce equal minor-unit values.

## Self-check question

Why does an unchanged column name not prove compatibility?

## Further reading

- [Debezium PostgreSQL connector](https://debezium.io/documentation/reference/stable/connectors/postgresql.html) — primary documentation; find the section relevant to this lesson.
- [dbt data tests](https://docs.getdbt.com/docs/build/data-tests) — primary documentation; find the section relevant to this lesson.

## Deliverable and navigation

Save your solution in your own fork under `portfolio/037-schema-evolution/`. Include the problem, a minimal example, the check from “Verify the result,” and your answer to the self-check question. Design exercises may produce an ADR, diagram, or experiment table; distinguish a proposal from an implemented service.

[Previous step](../04-ingestion/036-cdc-deletes.md) · [Next step](../04-ingestion/038-outbox.md) · [Full roadmap](../README.md)

**Module:** Ingestion and CDC. **Estimated time:** 2–4 hours for a first pass; deeper practice and a project take additional time. The previous step defines reading order, not an equally mandatory prerequisite for every learner: see the [learning paths](../../docs/LEARNING_PATHS.md).

# 059. Model migrations and compatibility

## Learning outcome

Release new schemas without breaking all consumers at once.

## How it works

Expand-contract adds the new representation, migrates readers, and then retires the old one. Overlap depends on usage and retention. Destructive changes need data migration and recovery: reverting code cannot recreate deleted columns. Versioned datasets support comparison.

## Fintech example

Introducing presentment_currency makes the former currency field ambiguous and motivates settlement_currency.

## Implementation steps

1. Add the new field
2. Backfill history
3. Migrate readers
4. Retire the old field after usage checks.

## Practical assignment

Plan migration to two explicit currency fields with acceptance and recovery steps.

## Common mistake and its consequences

Renaming in one deployment breaks consumers outside the visible DAG.

## Verify the result

Old and new readers work during overlap; removal is a distinct reviewed step.

## Self-check question

When can deployment rollback not recover the previous data?

## Further reading

- [dbt data tests](https://docs.getdbt.com/docs/build/data-tests) — primary documentation; find the section relevant to this lesson.
- [PostgreSQL documentation](https://www.postgresql.org/docs/current/) — primary documentation; find the section relevant to this lesson.

## Deliverable and navigation

Save your solution in your own fork under `portfolio/059-deployments/`. Include the problem, a minimal example, the check from “Verify the result,” and your answer to the self-check question. Design exercises may produce an ADR, diagram, or experiment table; distinguish a proposal from an implemented service.

[Previous step](../06-transformation/058-environments.md) · [Next step](../06-transformation/060-docs-ops.md) · [Full roadmap](../README.md)

**Module:** Transformations and orchestration. **Estimated time:** 2–4 hours for a first pass; deeper practice and a project take additional time. The previous step defines reading order, not an equally mandatory prerequisite for every learner: see the [learning paths](../../docs/LEARNING_PATHS.md).

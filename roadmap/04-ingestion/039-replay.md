# 039. Replay, backfill, and historical corrections

## Learning outcome

Make repeated processing a controlled operation.

## How it works

Replay processes retained input again. Backfill fills missing history or recomputes it under new logic. Define scope, code version, manifest, resource limits, and checks before consumer switching. Results must not silently depend on current clocks or unversioned reference data.

## Fintech example

A fee bug affects January. Rebuild should preserve the old published dataset and show a candidate diff.

## Implementation steps

1. Identify affected partitions
2. Build shadow output
3. Reconcile totals
4. Publish under explicit controls.

## Practical assignment

Write separate plans for late e6 and a changed fee sign. The latter needs a new dataset version.

## Common mistake and its consequences

Deleting the live mart before rebuilding exposes a partial month.

## Verify the result

Old and candidate totals, acceptance criteria, and rollback targets exist before publication.

## Self-check question

When can replaying identical input still produce a different result?

## Further reading

- [Airflow best practices](https://airflow.apache.org/docs/apache-airflow/stable/best-practices.html) — primary documentation; find the section relevant to this lesson.
- [dbt data tests](https://docs.getdbt.com/docs/build/data-tests) — primary documentation; find the section relevant to this lesson.

## Deliverable and navigation

Save your solution in your own fork under `portfolio/039-replay/`. Include the problem, a minimal example, the check from “Verify the result,” and your answer to the self-check question. Design exercises may produce an ADR, diagram, or experiment table; distinguish a proposal from an implemented service.

[Previous step](../04-ingestion/038-outbox.md) · [Next step](../04-ingestion/040-ingestion-audit.md) · [Full roadmap](../README.md)

**Module:** Ingestion and CDC. **Estimated time:** 2–4 hours for a first pass; deeper practice and a project take additional time. The previous step defines reading order, not an equally mandatory prerequisite for every learner: see the [learning paths](../../docs/LEARNING_PATHS.md).

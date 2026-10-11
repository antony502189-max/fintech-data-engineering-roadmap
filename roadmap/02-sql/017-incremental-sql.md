# 017. Incremental models and window boundaries

## Learning outcome

Make incremental output equivalent to a full rebuild.

## How it works

Incremental models read part of the input and update affected results. An event-time watermark misses late delivery of an old event. Receipt-time progress selects new deliveries, but their business dates determine which partitions need rebuilding. A lookback is bounded; older corrections need backfill.

## Fintech example

Capture e6 belongs to January 1 but arrives on January 3. The new run must update January 1.

## Implementation steps

1. Persist receipt progress
2. Identify affected event dates
3. Recompute them atomically
4. Compare with a full rebuild.

## Practical assignment

Split payments() into early and late inputs. Implement affected-day recomputation in your fork.

## Common mistake and its consequences

Adding today's totals to yesterday's aggregate increases the result on each replay.

## Verify the result

Incremental and full outputs both produce USD 12200 for January 1 after the late event.

## Self-check question

How should a correction older than the configured lookback be handled?

## Further reading

- [dbt data tests](https://docs.getdbt.com/docs/build/data-tests) — primary documentation; find the section relevant to this lesson.
- [PostgreSQL documentation](https://www.postgresql.org/docs/current/) — primary documentation; find the section relevant to this lesson.

## Deliverable and navigation

Save your solution in your own fork under `portfolio/017-incremental-sql/`. Include the problem, a minimal example, the check from “Verify the result,” and your answer to the self-check question. Design exercises may produce an ADR, diagram, or experiment table; distinguish a proposal from an implemented service.

[Previous step](../02-sql/016-indexes.md) · [Next step](../02-sql/018-dedup-sql.md) · [Full roadmap](../README.md)

**Module:** SQL and databases. **Estimated time:** 2–4 hours for a first pass; deeper practice and a project take additional time. The previous step defines reading order, not an equally mandatory prerequisite for every learner: see the [learning paths](../../docs/LEARNING_PATHS.md).

# 052. dbt incremental models and late updates

## Learning outcome

Design a repeatable incremental model.

## How it works

A unique_key defines matching for supported strategies; it does not ensure unique source input. Append and merge behave differently under replay. Late data needs receipt-based selection or lookback plus deeper backfill. Compare full refresh with incremental results.

## Fintech example

A late capture changes an old day that a today-only merge will miss.

## Implementation steps

1. Choose an adapter-supported strategy
2. Define the unique key
3. Identify affected periods
4. Verify full-refresh equivalence.

## Practical assignment

Write a model sketch and test plan for two successive runs with e6.

## Common mistake and its consequences

Assuming unique_key cleans duplicate input causes ambiguous merges or failures.

## Verify the result

Incremental and full outputs agree after replay and late delivery.

## Self-check question

When can an incremental predicate exclude the target row that needs updating?

## Further reading

- [dbt data tests](https://docs.getdbt.com/docs/build/data-tests) — primary documentation; find the section relevant to this lesson.

## Deliverable and navigation

Save your solution in your own fork under `portfolio/052-dbt-incremental/`. Include the problem, a minimal example, the check from “Verify the result,” and your answer to the self-check question. Design exercises may produce an ADR, diagram, or experiment table; distinguish a proposal from an implemented service.

[Previous step](../06-transformation/051-dbt-basics.md) · [Next step](../06-transformation/053-orchestration.md) · [Full roadmap](../README.md)

**Module:** Transformations and orchestration. **Estimated time:** 2–4 hours for a first pass; deeper practice and a project take additional time. The previous step defines reading order, not an equally mandatory prerequisite for every learner: see the [learning paths](../../docs/LEARNING_PATHS.md).

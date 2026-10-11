# 006. Testing functions and financial invariants

## Learning outcome

Choose checks that detect real consequences of a change.

## How it works

Unit tests cover individual functions; integration tests cover interactions; contract tests cover source boundaries. A financial invariant checks properties such as balanced postings per event and currency. Snapshots can verify output shape but can also preserve an incorrect result if updated without analysis.

## Fintech example

A repeated webhook must not double turnover. A missing side of a posting must fail verification.

## Implementation steps

1. Run unittest
2. Change a posting by one minor unit
3. Confirm a meaningful failure
4. Restore the implementation and rerun.

## Practical assignment

Add a test deleting all postings for an event. Remaining groups can sum to zero even though journal completeness has failed.

## Common mistake and its consequences

Checking only sum=0 misses events absent from the GROUP BY result.

## Verify the result

The checks distinguish an incorrect balance, a missing journal, and a valid replay.

## Self-check question

Why is row count weak evidence that monetary totals are correct?

## Further reading

- [Python Tutorial](https://docs.python.org/3.12/tutorial/) — primary documentation; find the section relevant to this lesson.
- [dbt data tests](https://docs.getdbt.com/docs/build/data-tests) — primary documentation; find the section relevant to this lesson.

## Deliverable and navigation

Save your solution in your own fork under `portfolio/006-testing/`. Include the problem, a minimal example, the check from “Verify the result,” and your answer to the self-check question. Design exercises may produce an ADR, diagram, or experiment table; distinguish a proposal from an implemented service.

[Previous step](../01-foundations/005-git.md) · [Next step](../01-foundations/007-http.md) · [Full roadmap](../README.md)

**Module:** Engineering foundations. **Estimated time:** 2–4 hours for a first pass; deeper practice and a project take additional time. The previous step defines reading order, not an equally mandatory prerequisite for every learner: see the [learning paths](../../docs/LEARNING_PATHS.md).

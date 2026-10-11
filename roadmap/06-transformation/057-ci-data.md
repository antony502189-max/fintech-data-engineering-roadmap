# 057. CI for code, contracts, and models

## Learning outcome

Check financial changes before merge.

## How it works

CI should run fast unit tests, fixture transformations, and documentation checks. Synthetic fixtures need no production credentials. Schema changes require old and new payloads; monetary changes need explicit expected amounts. Link checking verifies navigation, not technical truth.

## Fintech example

A changed fee sign should fail an amount assertion, not merely pass SQL syntax validation.

## Implementation steps

1. Run unit tests
2. Verify SQL outputs
3. Check local links
4. Review business-result differences.

## Practical assignment

Change the fee sign in your fork and confirm a meaningful assertion fails.

## Common mistake and its consequences

Checking only that a query returned a row accepts incorrect totals.

## Verify the result

CI rejects monetary defects and missing documentation paths.

## Self-check question

Which properties cannot be convincingly tested on a tiny fixture?

## Further reading

- [Pro Git book](https://git-scm.com/book/en/v2) — primary documentation; find the section relevant to this lesson.
- [dbt data tests](https://docs.getdbt.com/docs/build/data-tests) — primary documentation; find the section relevant to this lesson.

## Deliverable and navigation

Save your solution in your own fork under `portfolio/057-ci-data/`. Include the problem, a minimal example, the check from “Verify the result,” and your answer to the self-check question. Design exercises may produce an ADR, diagram, or experiment table; distinguish a proposal from an implemented service.

[Previous step](../06-transformation/056-publish.md) · [Next step](../06-transformation/058-environments.md) · [Full roadmap](../README.md)

**Module:** Transformations and orchestration. **Estimated time:** 2–4 hours for a first pass; deeper practice and a project take additional time. The previous step defines reading order, not an equally mandatory prerequisite for every learner: see the [learning paths](../../docs/LEARNING_PATHS.md).

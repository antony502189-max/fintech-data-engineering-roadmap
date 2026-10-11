# 056. Atomic publication and readiness markers

## Learning outcome

Prevent consumers from seeing partial results.

## How it works

Computation and publication are separate stages. Build a candidate, check it, then expose it with an atomic pointer, view switch, or supported table commit. A readiness marker identifies version and scope. The mechanism must match the platform's actual guarantees.

## Fintech example

USD is ready but EUR is still computing. The day's report must not appear final.

## Implementation steps

1. Build a candidate version
2. Run quality and reconciliation
3. Switch the reference
4. Retain the prior version.

## Practical assignment

Design a daily-cash manifest covering both currencies under one published version.

## Common mistake and its consequences

Writing live consumer rows individually exposes incomplete output.

## Verify the result

A reader observes either the complete old result or the complete new result in failure scenarios.

## Self-check question

How can several dependent marts be published consistently?

## Further reading

- [Apache Iceberg documentation](https://iceberg.apache.org/docs/latest/) — primary documentation; find the section relevant to this lesson.
- [PostgreSQL documentation](https://www.postgresql.org/docs/current/) — primary documentation; find the section relevant to this lesson.

## Deliverable and navigation

Save your solution in your own fork under `portfolio/056-publish/`. Include the problem, a minimal example, the check from “Verify the result,” and your answer to the self-check question. Design exercises may produce an ADR, diagram, or experiment table; distinguish a proposal from an implemented service.

[Previous step](../06-transformation/055-backfills-dag.md) · [Next step](../06-transformation/057-ci-data.md) · [Full roadmap](../README.md)

**Module:** Transformations and orchestration. **Estimated time:** 2–4 hours for a first pass; deeper practice and a project take additional time. The previous step defines reading order, not an equally mandatory prerequisite for every learner: see the [learning paths](../../docs/LEARNING_PATHS.md).

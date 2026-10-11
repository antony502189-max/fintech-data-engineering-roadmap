# 071. Completeness, accuracy, freshness, and consistency

## Learning outcome

Separate independent quality dimensions.

## How it works

Freshness measures delay; completeness measures expected coverage; accuracy measures correctness; consistency compares representations. Passing one check says little about the others. Explicit invariants and an expected universe are more useful than an opaque aggregate score.

## Fintech example

A timely file can omit p3; a complete file can contain wrong amounts.

## Implementation steps

1. Define expected coverage
2. Select checks
3. Separate critical and informational outcomes
4. Establish publication gates.

## Practical assignment

Create late, missing, wrong-amount, and conflicting-currency fixtures.

## Common mistake and its consequences

Using the maximum timestamp as proof of completeness lets one fresh event hide many missing records.

## Verify the result

Each fixture fails the relevant check instead of disappearing inside an average score.

## Self-check question

How can you establish expected coverage when the source supplies no manifest?

## Further reading

- [dbt data tests](https://docs.getdbt.com/docs/build/data-tests) — primary documentation; find the section relevant to this lesson.
- [OpenTelemetry concepts](https://opentelemetry.io/docs/concepts/) — primary documentation; find the section relevant to this lesson.

## Deliverable and navigation

Save your solution in your own fork under `portfolio/071-quality-dimensions/`. Include the problem, a minimal example, the check from “Verify the result,” and your answer to the self-check question. Design exercises may produce an ADR, diagram, or experiment table; distinguish a proposal from an implemented service.

[Previous step](../07-fintech/070-fintech-review.md) · [Next step](../08-reliability/072-freshness.md) · [Full roadmap](../README.md)

**Module:** Quality and reliability. **Estimated time:** 2–4 hours for a first pass; deeper practice and a project take additional time. The previous step defines reading order, not an equally mandatory prerequisite for every learner: see the [learning paths](../../docs/LEARNING_PATHS.md).

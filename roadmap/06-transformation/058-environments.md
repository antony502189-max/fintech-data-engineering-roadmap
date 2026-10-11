# 058. Development, staging, and production

## Learning outcome

Separate environments and minimize development access.

## How it works

Environments need distinct identities, namespaces, and published outputs. Synthetic development reduces risk and expense but does not replace representative performance tests. Masking must consider reidentification through combined fields. Copying production data is a governed decision.

## Fintech example

A developer tests refunds without names or card details.

## Implementation steps

1. Define development data
2. Separate namespaces
3. Assign permissions
4. Prevent accidental production publication.

## Practical assignment

Create an environment matrix with sources, sinks, identities, retention, and allowed actions.

## Common mistake and its consequences

One schema variable points a development job at a production table.

## Verify the result

Without a production identity, the development run cannot write production output.

## Self-check question

Why is masked data not necessarily anonymous?

## Further reading

- [AWS Well Architected](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html) — primary documentation; find the section relevant to this lesson.
- [PostgreSQL documentation](https://www.postgresql.org/docs/current/) — primary documentation; find the section relevant to this lesson.

## Deliverable and navigation

Save your solution in your own fork under `portfolio/058-environments/`. Include the problem, a minimal example, the check from “Verify the result,” and your answer to the self-check question. Design exercises may produce an ADR, diagram, or experiment table; distinguish a proposal from an implemented service.

[Previous step](../06-transformation/057-ci-data.md) · [Next step](../06-transformation/059-deployments.md) · [Full roadmap](../README.md)

**Module:** Transformations and orchestration. **Estimated time:** 2–4 hours for a first pass; deeper practice and a project take additional time. The previous step defines reading order, not an equally mandatory prerequisite for every learner: see the [learning paths](../../docs/LEARNING_PATHS.md).

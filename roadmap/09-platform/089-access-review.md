# 089. Access review, audit, and exports

## Learning outcome

Review the entire data path, including downloaded copies.

## How it works

Warehouse permissions do not automatically protect exported CSVs. Each export creates another copy with readers and retention. Audit should record identities, actions, and resources without secrets. Periodic reviews check whether access remains necessary.

## Fintech example

A raw export in a public bucket bypasses the purpose of a restricted mart.

## Implementation steps

1. Inventory export paths
2. Assign owners
3. Limit destinations
4. Manage copy lifecycles.

## Practical assignment

Map warehouse, notebooks, CSVs, and BI extracts; mark every new copy.

## Common mistake and its consequences

Reviewing warehouse IAM alone misses public export links.

## Verify the result

All destinations have access and retention rules; untracked exports are explicit gaps.

## Self-check question

What are the limitations of revoking access after data has been copied?

## Further reading

- [AWS Well Architected](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html) — primary documentation; find the section relevant to this lesson.
- [PostgreSQL documentation](https://www.postgresql.org/docs/current/) — primary documentation; find the section relevant to this lesson.

## Deliverable and navigation

Save your solution in your own fork under `portfolio/089-access-review/`. Include the problem, a minimal example, the check from “Verify the result,” and your answer to the self-check question. Design exercises may produce an ADR, diagram, or experiment table; distinguish a proposal from an implemented service.

[Previous step](../09-platform/088-ownership.md) · [Next step](../09-platform/090-platform-review.md) · [Full roadmap](../README.md)

**Module:** Platform and security. **Estimated time:** 2–4 hours for a first pass; deeper practice and a project take additional time. The previous step defines reading order, not an equally mandatory prerequisite for every learner: see the [learning paths](../../docs/LEARNING_PATHS.md).

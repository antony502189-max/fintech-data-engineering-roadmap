# 085. Retention, deletion, and holds

## Learning outcome

Implement approved policy without inventing universal deadlines.

## How it works

Retention depends on data category, purpose, and applicable policy. Engineers implement rules and evidence; there is no universal fintech retention period. Approved holds may suspend deletion. Include backups and derived datasets in scope.

## Fintech example

Profiles and ledger evidence can follow different retention rules.

## Implementation steps

1. Obtain policy inputs
2. Define expiry
3. Apply holds
4. Include derivatives and backups.

## Practical assignment

For synthetic records, implement keep/delete decisions from supplied expiry dates and hold flags. This is not legal advice.

## Common mistake and its consequences

Deleting only raw data leaves personal fields in marts, logs, and backups.

## Verify the result

Each decision records policy version, reason, and lineage scope.

## Self-check question

Who should resolve contradictory preservation and deletion requirements?

## Further reading

- [AWS Well Architected](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html) — primary documentation; find the section relevant to this lesson.
- [PostgreSQL documentation](https://www.postgresql.org/docs/current/) — primary documentation; find the section relevant to this lesson.

## Deliverable and navigation

Save your solution in your own fork under `portfolio/085-retention/`. Include the problem, a minimal example, the check from “Verify the result,” and your answer to the self-check question. Design exercises may produce an ADR, diagram, or experiment table; distinguish a proposal from an implemented service.

[Previous step](../09-platform/084-encryption.md) · [Next step](../09-platform/086-iac.md) · [Full roadmap](../README.md)

**Module:** Platform and security. **Estimated time:** 2–4 hours for a first pass; deeper practice and a project take additional time. The previous step defines reading order, not an equally mandatory prerequisite for every learner: see the [learning paths](../../docs/LEARNING_PATHS.md).

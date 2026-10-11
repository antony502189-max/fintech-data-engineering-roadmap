# 084. Encryption, keys, and access boundaries

## Learning outcome

Separate transport protection, storage encryption, and authorization.

## How it works

TLS protects transport; encryption at rest protects stored data; IAM governs actions. They complement one another. Authorized readers can still obtain plaintext, so encryption cannot replace access controls. Key ownership and recovery are separate concerns.

## Fintech example

An encrypted raw bucket remains accessible to an overly broad analyst role.

## Implementation steps

1. Map trust boundaries
2. Identify TLS hops
3. Assign key owners
4. Check decrypt permissions.

## Practical assignment

Model threats along source→raw→mart→export and one failure at each boundary.

## Common mistake and its consequences

“Everything is encrypted” ends review without checking who can decrypt it.

## Verify the result

Document identities, locations, and authorized decryption paths.

## Self-check question

How does losing an encryption key affect backup recovery?

## Further reading

- [AWS Well Architected](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html) — primary documentation; find the section relevant to this lesson.

## Deliverable and navigation

Save your solution in your own fork under `portfolio/084-encryption/`. Include the problem, a minimal example, the check from “Verify the result,” and your answer to the self-check question. Design exercises may produce an ADR, diagram, or experiment table; distinguish a proposal from an implemented service.

[Previous step](../09-platform/083-secrets.md) · [Next step](../09-platform/085-retention.md) · [Full roadmap](../README.md)

**Module:** Platform and security. **Estimated time:** 2–4 hours for a first pass; deeper practice and a project take additional time. The previous step defines reading order, not an equally mandatory prerequisite for every learner: see the [learning paths](../../docs/LEARNING_PATHS.md).

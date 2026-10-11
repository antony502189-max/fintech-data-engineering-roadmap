# 083. Secrets, rotation, and diagnostics

## Learning outcome

Keep credentials outside code, fixtures, and logs.

## How it works

Secrets have owners and lifecycles and should be delivered through an approved mechanism. Environment variables can help local setup but are not a complete protection strategy. Rotation needs consumer verification and overlap rules. After exposure, deleting a line from the latest commit is insufficient; revoke the credential.

## Fintech example

Webhook signing secrets and API keys never belong in issue reproductions.

## Implementation steps

1. Name owners
2. Define retrieval
3. Verify redaction
4. Plan rotation.

## Practical assignment

Create a synthetic configuration schema listing variable names without values. Inspect exception logging.

## Common mistake and its consequences

Printing a request object with authorization headers leaks credentials into shared diagnostics.

## Verify the result

Examples contain placeholders only; rotation has verifiable steps.

## Self-check question

Why does hiding a secret in a log viewer not remove it from underlying storage?

## Further reading

- [AWS Well Architected](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html) — primary documentation; find the section relevant to this lesson.
- [Pro Git book](https://git-scm.com/book/en/v2) — primary documentation; find the section relevant to this lesson.

## Deliverable and navigation

Save your solution in your own fork under `portfolio/083-secrets/`. Include the problem, a minimal example, the check from “Verify the result,” and your answer to the self-check question. Design exercises may produce an ADR, diagram, or experiment table; distinguish a proposal from an implemented service.

[Previous step](../09-platform/082-pii.md) · [Next step](../09-platform/084-encryption.md) · [Full roadmap](../README.md)

**Module:** Platform and security. **Estimated time:** 2–4 hours for a first pass; deeper practice and a project take additional time. The previous step defines reading order, not an equally mandatory prerequisite for every learner: see the [learning paths](../../docs/LEARNING_PATHS.md).

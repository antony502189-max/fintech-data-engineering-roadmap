# 007. HTTP, APIs, and pagination

## Learning outcome

Retrieve a complete API event set without losing pages.

## How it works

A 200 response confirms page delivery, not dataset completeness. Cursor pagination records a source position; offset pagination over changing data can skip records. A timeout does not reveal whether the server completed an operation. Retry decisions depend on the operation's idempotency.

## Fintech example

A provider returns 100 payments per page while new payments arrive during retrieval. The first page's length is not the daily total.

## Implementation steps

1. Read the pagination contract
2. Persist the cursor and query parameters
3. Handle rate limits
4. Compare counts and amounts with independent controls.

## Practical assignment

Simulate three JSON pages and a failure after the second. Prove that resuming preserves the third page without doubling the first two.

## Common mistake and its consequences

Saving a cursor before committing the page allows a crash to skip unprocessed records.

## Verify the result

After failures at each selected point, the final event ID set equals the reference set.

## Self-check question

How should retry behavior differ for a GET and a POST that creates a payment?

## Further reading

- [Stripe webhook delivery](https://docs.stripe.com/webhooks) — primary documentation; find the section relevant to this lesson.
- [Stripe idempotent requests](https://docs.stripe.com/api/idempotent_requests) — primary documentation; find the section relevant to this lesson.

## Deliverable and navigation

Save your solution in your own fork under `portfolio/007-http/`. Include the problem, a minimal example, the check from “Verify the result,” and your answer to the self-check question. Design exercises may produce an ADR, diagram, or experiment table; distinguish a proposal from an implemented service.

[Previous step](../01-foundations/006-testing.md) · [Next step](../01-foundations/008-containers.md) · [Full roadmap](../README.md)

**Module:** Engineering foundations. **Estimated time:** 2–4 hours for a first pass; deeper practice and a project take additional time. The previous step defines reading order, not an equally mandatory prerequisite for every learner: see the [learning paths](../../docs/LEARNING_PATHS.md).

# 054. Retries, timeouts, and idempotent tasks

## Learning outcome

Assign retries by failure class and time budget.

## How it works

Retries help temporary failures but cannot repair invalid contracts. Attempt timeouts limit execution; a retry budget limits total delay. Tasks must survive repeats after uncertain commit results. Retrying ingestion differs from rebuilding data or changing a business rule.

## Fintech example

A SQL insert succeeds but the worker loses the acknowledgment.

## Implementation steps

1. Classify failures
2. Define attempt timeouts
3. Bound backoff
4. Test post-commit replay.

## Practical assignment

Choose retry, quarantine, or fail for rate limit, invalid currency, deadlock, missing file, and identity collision.

## Common mistake and its consequences

Retrying every exception repeatedly blocks work and increases load.

## Verify the result

Every error has an action, a maximum budget, and an owner-facing signal.

## Self-check question

Why does an unknown COMMIT outcome require sink idempotency?

## Further reading

- [Airflow best practices](https://airflow.apache.org/docs/apache-airflow/stable/best-practices.html) — primary documentation; find the section relevant to this lesson.
- [Stripe idempotent requests](https://docs.stripe.com/api/idempotent_requests) — primary documentation; find the section relevant to this lesson.

## Deliverable and navigation

Save your solution in your own fork under `portfolio/054-retry-design/`. Include the problem, a minimal example, the check from “Verify the result,” and your answer to the self-check question. Design exercises may produce an ADR, diagram, or experiment table; distinguish a proposal from an implemented service.

[Previous step](../06-transformation/053-orchestration.md) · [Next step](../06-transformation/055-backfills-dag.md) · [Full roadmap](../README.md)

**Module:** Transformations and orchestration. **Estimated time:** 2–4 hours for a first pass; deeper practice and a project take additional time. The previous step defines reading order, not an equally mandatory prerequisite for every learner: see the [learning paths](../../docs/LEARNING_PATHS.md).

# 032. API connectors and backpressure

## Learning outcome

Limit ingestion speed without sacrificing completeness.

## How it works

Connectors must respect limits, timeouts, and source retry policies. Exponential backoff with jitter reduces synchronized retry storms. Backpressure slows reads when the sink is overloaded; an unbounded memory queue only postpones failure. Completeness also needs cursor persistence and independent controls.

## Fintech example

Thousands of hourly merchant polls restart together after an outage.

## Implementation steps

1. Identify rate limits
2. Bound concurrency
3. Use a bounded queue
4. Save cursors after persistence.

## Practical assignment

Simulate 429 responses and timeouts in a mock API. Record attempts, maximum queue size, and final keys.

## Common mistake and its consequences

Unlimited retries permanently block a batch and obscure stale output.

## Verify the result

The rate limit is respected, the queue bounded, and exhausted retries produce a visible failure.

## Self-check question

Why can more workers reduce useful throughput?

## Further reading

- [Stripe webhook delivery](https://docs.stripe.com/webhooks) — primary documentation; find the section relevant to this lesson.
- [Python Tutorial](https://docs.python.org/3.12/tutorial/) — primary documentation; find the section relevant to this lesson.

## Deliverable and navigation

Save your solution in your own fork under `portfolio/032-api-connectors/`. Include the problem, a minimal example, the check from “Verify the result,” and your answer to the self-check question. Design exercises may produce an ADR, diagram, or experiment table; distinguish a proposal from an implemented service.

[Previous step](../04-ingestion/031-batch-ingestion.md) · [Next step](../04-ingestion/033-webhooks.md) · [Full roadmap](../README.md)

**Module:** Ingestion and CDC. **Estimated time:** 2–4 hours for a first pass; deeper practice and a project take additional time. The previous step defines reading order, not an equally mandatory prerequisite for every learner: see the [learning paths](../../docs/LEARNING_PATHS.md).

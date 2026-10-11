# 078. Performance and capacity planning

## Learning outcome

Connect data growth to deadlines and costs.

## How it works

Capacity depends on volume, key distribution, row width, concurrency, and backlog. Average rates hide peaks. Evaluate throughput together with latency and recovery after outages. Benchmarks must specify environments and repeated measurements rather than one favorable run.

## Fintech example

A two-hour backlog must clear before close while new arrivals continue.

## Implementation steps

1. Measure steady throughput
2. Simulate peaks
3. Estimate backlog draining
4. Test contention.

## Practical assignment

Calculate recovery for arrival 1000/s and processing 1500/s after two hours of outage.

## Common mistake and its consequences

Dividing backlog by total processing rate ignores ongoing arrivals and understates recovery time.

## Verify the result

Use spare capacity; if processing does not exceed arrivals, backlog cannot shrink.

## Self-check question

Why does doubling workers not necessarily double useful throughput?

## Further reading

- [Spark SQL performance tuning](https://spark.apache.org/docs/latest/sql-performance-tuning.html) — primary documentation; find the section relevant to this lesson.
- [OpenTelemetry concepts](https://opentelemetry.io/docs/concepts/) — primary documentation; find the section relevant to this lesson.

## Deliverable and navigation

Save your solution in your own fork under `portfolio/078-performance-ops/`. Include the problem, a minimal example, the check from “Verify the result,” and your answer to the self-check question. Design exercises may produce an ADR, diagram, or experiment table; distinguish a proposal from an implemented service.

[Previous step](../08-reliability/077-backup.md) · [Next step](../08-reliability/079-chaos.md) · [Full roadmap](../README.md)

**Module:** Quality and reliability. **Estimated time:** 2–4 hours for a first pass; deeper practice and a project take additional time. The previous step defines reading order, not an equally mandatory prerequisite for every learner: see the [learning paths](../../docs/LEARNING_PATHS.md).

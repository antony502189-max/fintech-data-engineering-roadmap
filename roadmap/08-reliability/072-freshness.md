# 072. Freshness and latency percentiles

## Learning outcome

Measure latency over a defined event population.

## How it works

Latency requires explicit endpoints such as source, receipt, transformation, and publication time. Percentiles need a defined calculation and denominator. Maximum event time does not measure each event's delay. Distinguish an idle source from broken ingestion using heartbeats or expected volume.

## Fintech example

Most payments arrive quickly, but e6 is two days late.

## Implementation steps

1. Define timestamps
2. Normalize UTC
3. Select the percentile method
4. Distinguish idle and failed sources.

## Practical assignment

Calculate fixture delays and nearest-rank p95. Explain the limitations of estimating production tails from tiny samples.

## Common mistake and its consequences

Mixing business and local-server clocks, then clipping negative delay to zero, hides clock defects.

## Verify the result

Report count, units, percentile method, and invalid timestamps.

## Self-check question

When is an absence of new events expected source behavior?

## Further reading

- [OpenTelemetry concepts](https://opentelemetry.io/docs/concepts/) — primary documentation; find the section relevant to this lesson.
- [Python Tutorial](https://docs.python.org/3.12/tutorial/) — primary documentation; find the section relevant to this lesson.

## Deliverable and navigation

Save your solution in your own fork under `portfolio/072-freshness/`. Include the problem, a minimal example, the check from “Verify the result,” and your answer to the self-check question. Design exercises may produce an ADR, diagram, or experiment table; distinguish a proposal from an implemented service.

[Previous step](../08-reliability/071-quality-dimensions.md) · [Next step](../08-reliability/073-observability.md) · [Full roadmap](../README.md)

**Module:** Quality and reliability. **Estimated time:** 2–4 hours for a first pass; deeper practice and a project take additional time. The previous step defines reading order, not an equally mandatory prerequisite for every learner: see the [learning paths](../../docs/LEARNING_PATHS.md).

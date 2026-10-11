# 002. Requirements, SLAs, and the cost of errors

## Learning outcome

Turn an ambiguous request into a measurable data contract.

## How it works

Start with the consumer's decision, not a Kafka deployment. Requirements include latency, completeness, availability, correction horizon, and retention. An SLA is an external commitment, an SLO an operational target, and an SLI its measurement. “Real time” without a threshold cannot be verified.

## Fintech example

A sales dashboard may tolerate an hour; fraud features may require seconds. Both use payments but have different consequences when data arrives late.

## Implementation steps

1. Describe the business decision
2. Define the measurement window
3. Separate freshness from completeness
4. State the budget and consequences of failure.

## Practical assignment

Write a daily settlement contract covering readiness by 08:00 UTC, evidence of completeness, and the response to a missing file.

## Common mistake and its consequences

Using average latency hides rare outages lasting hours behind a reassuring number.

## Verify the result

The contract includes a numerical target, the SLI denominator, a measurement window, and an exception owner.

## Self-check question

Why do 99% successful job executions not imply 99% correct reports?

## Further reading

- [OpenTelemetry concepts](https://opentelemetry.io/docs/concepts/) — primary documentation; find the section relevant to this lesson.

## Deliverable and navigation

Save your solution in your own fork under `portfolio/002-requirements/`. Include the problem, a minimal example, the check from “Verify the result,” and your answer to the self-check question. Design exercises may produce an ADR, diagram, or experiment table; distinguish a proposal from an implemented service.

[Previous step](../01-foundations/001-roles.md) · [Next step](../01-foundations/003-python.md) · [Full roadmap](../README.md)

**Module:** Engineering foundations. **Estimated time:** 2–4 hours for a first pass; deeper practice and a project take additional time. The previous step defines reading order, not an equally mandatory prerequisite for every learner: see the [learning paths](../../docs/LEARNING_PATHS.md).

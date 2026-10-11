# 073. Logs, metrics, traces, and lineage

## Learning outcome

Select observation methods for a concrete diagnosis.

## How it works

Logs describe events; metrics summarize signals; traces follow execution across components. Data lineage connects model inputs and outputs. No channel replaces all others. Correlation IDs join runs, batches, and events, while sensitive fields should stay out of diagnostics.

## Fintech example

p3's discrepancy links to delivery e6, a run ID, and settlement-file version.

## Implementation steps

1. Choose correlation IDs
2. Define structured logs
3. Separate monetary metrics
4. Include lineage references.

## Practical assignment

Write synthetic ingestion and reconciliation log examples without unnecessary personal detail.

## Common mistake and its consequences

Logging complete sensitive payloads makes diagnosis another exposure path.

## Verify the result

An event ID leads to its run and source version without exposing credentials.

## Self-check question

Why does a successful HTTP trace not prove warehouse completeness?

## Further reading

- [OpenTelemetry concepts](https://opentelemetry.io/docs/concepts/) — primary documentation; find the section relevant to this lesson.

## Deliverable and navigation

Save your solution in your own fork under `portfolio/073-observability/`. Include the problem, a minimal example, the check from “Verify the result,” and your answer to the self-check question. Design exercises may produce an ADR, diagram, or experiment table; distinguish a proposal from an implemented service.

[Previous step](../08-reliability/072-freshness.md) · [Next step](../08-reliability/074-alerts.md) · [Full roadmap](../README.md)

**Module:** Quality and reliability. **Estimated time:** 2–4 hours for a first pass; deeper practice and a project take additional time. The previous step defines reading order, not an equally mandatory prerequisite for every learner: see the [learning paths](../../docs/LEARNING_PATHS.md).

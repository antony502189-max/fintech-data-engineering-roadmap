# 030. Model review and lineage

## Learning outcome

Review explainability and rebuild capability.

## How it works

Lineage identifies sources and transformations behind a column. Include rule versions, dates, and controls rather than just table arrows. Review grain, keys, historical behavior, additivity, unknown members, and permissions to change closed periods.

## Fintech example

Explaining p3 requires tracing settlement, raw capture, and posting amounts.

## Implementation steps

1. Choose a monetary column
2. Follow its lineage
3. Identify lost history
4. Document the rebuild procedure.

## Practical assignment

Create a mart_daily_cash dossier covering input events, formulas, checks, limits, and run commands.

## Common mistake and its consequences

An attractive ERD without grain or correction policy gives false confidence.

## Verify the result

An independent reader reconstructs January 1 USD 12200 from raw events.

## Self-check question

What minimum information makes a report explainable a year later?

## Further reading

- [Kimball dimensional modeling techniques](https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/) — primary documentation; find the section relevant to this lesson.
- [dbt data tests](https://docs.getdbt.com/docs/build/data-tests) — primary documentation; find the section relevant to this lesson.

## Deliverable and navigation

Save your solution in your own fork under `portfolio/030-model-review/`. Include the problem, a minimal example, the check from “Verify the result,” and your answer to the self-check question. Design exercises may produce an ADR, diagram, or experiment table; distinguish a proposal from an implemented service.

[Previous step](../03-modeling/029-semantic.md) · [Next step](../04-ingestion/031-batch-ingestion.md) · [Full roadmap](../README.md)

**Module:** DWH modeling. **Estimated time:** 2–4 hours for a first pass; deeper practice and a project take additional time. The previous step defines reading order, not an equally mandatory prerequisite for every learner: see the [learning paths](../../docs/LEARNING_PATHS.md).

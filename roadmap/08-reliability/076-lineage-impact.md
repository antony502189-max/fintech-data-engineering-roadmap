# 076. Lineage and change impact

## Learning outcome

Identify consumers affected by a column change.

## How it works

Table lineage gives a broad dependency map; column lineage ties specific formulas together. Exports, spreadsheets, and ML datasets may sit outside automatic graphs. Impact analysis needs metadata, owners, and actual usage. Versioned outputs support historical scoping.

## Fintech example

Changing the fee sign affects net cash but not distinct payment counts.

## Implementation steps

1. Map dependencies
2. Identify metric columns
3. Add external consumers
4. Find affected versions.

## Practical assignment

Build reachability for fee→daily cash→report alongside an independent payment-count branch.

## Common mistake and its consequences

Declaring every source change affects everything, or trusting incomplete automatic lineage, produces poor scope.

## Verify the result

List direct and indirect effects and explicitly unknown consumers.

## Self-check question

When is table-level lineage too coarse for a safe backfill?

## Further reading

- [dbt data tests](https://docs.getdbt.com/docs/build/data-tests) — primary documentation; find the section relevant to this lesson.
- [OpenTelemetry concepts](https://opentelemetry.io/docs/concepts/) — primary documentation; find the section relevant to this lesson.

## Deliverable and navigation

Save your solution in your own fork under `portfolio/076-lineage-impact/`. Include the problem, a minimal example, the check from “Verify the result,” and your answer to the self-check question. Design exercises may produce an ADR, diagram, or experiment table; distinguish a proposal from an implemented service.

[Previous step](../08-reliability/075-incident.md) · [Next step](../08-reliability/077-backup.md) · [Full roadmap](../README.md)

**Module:** Quality and reliability. **Estimated time:** 2–4 hours for a first pass; deeper practice and a project take additional time. The previous step defines reading order, not an equally mandatory prerequisite for every learner: see the [learning paths](../../docs/LEARNING_PATHS.md).

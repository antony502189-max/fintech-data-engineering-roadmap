# 022. Raw, staging, core, and marts

## Learning outcome

Give each layer a specific responsibility.

## How it works

Raw preserves evidence of receipt; staging normalizes types; core models durable entities and events; marts answer consumer questions. Layer count matters less than clear input, rule version, and reproduction paths. Raw data still requires protection and retention controls.

## Fintech example

A provider event becomes a typed capture, then journal entries and daily net cash.

## Implementation steps

1. Define layer responsibilities
2. Name keys
3. Specify raw retention
4. Trace lineage to the report.

## Practical assignment

Map raw_events, ledger_entries, and mart_daily_cash to the architecture. Identify the layer the lab simplifies.

## Common mistake and its consequences

Copying a formula into staging and marts makes corrections diverge between consumers.

## Verify the result

A net_minor value has one explainable provenance path and an explicit sign rule.

## Self-check question

Where should a fee rule live, and why?

## Further reading

- [Kimball dimensional modeling techniques](https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/) — primary documentation; find the section relevant to this lesson.
- [dbt data tests](https://docs.getdbt.com/docs/build/data-tests) — primary documentation; find the section relevant to this lesson.

## Deliverable and navigation

Save your solution in your own fork under `portfolio/022-layers/`. Include the problem, a minimal example, the check from “Verify the result,” and your answer to the self-check question. Design exercises may produce an ADR, diagram, or experiment table; distinguish a proposal from an implemented service.

[Previous step](../03-modeling/021-architecture.md) · [Next step](../03-modeling/023-facts.md) · [Full roadmap](../README.md)

**Module:** DWH modeling. **Estimated time:** 2–4 hours for a first pass; deeper practice and a project take additional time. The previous step defines reading order, not an equally mandatory prerequisite for every learner: see the [learning paths](../../docs/LEARNING_PATHS.md).

# 026. Bitemporal data and past knowledge

## Learning outcome

Separate business validity from warehouse knowledge.

## How it works

Valid time states when information applies to the business. System time states when the warehouse knew a version. Valid-time SCD2 cannot reconstruct old knowledge after correction. Audit queries require both time axes and an explicit as-known-at rule.

## Fintech example

A tariff applying since January 1 is corrected on February 5. The report sent January 31 must remain reproducible.

## Implementation steps

1. Add recorded intervals
2. Preserve previous knowledge
3. Define as-of queries
4. Separate original and restated reports.

## Practical assignment

Design a tariff table with two intervals and queries for current truth, business-date truth, and knowledge at submission time.

## Common mistake and its consequences

Calling the lab's simple SCD2 an audit trail ignores that earlier knowledge was replaced.

## Verify the result

Original reporting returns the earlier tariff; restated reporting returns the correction with a separate version.

## Self-check question

How do you select a tariff whose effective date precedes its receipt?

## Further reading

- [PostgreSQL documentation](https://www.postgresql.org/docs/current/) — primary documentation; find the section relevant to this lesson.
- [Kimball dimensional modeling techniques](https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/) — primary documentation; find the section relevant to this lesson.

## Deliverable and navigation

Save your solution in your own fork under `portfolio/026-bitemporal/`. Include the problem, a minimal example, the check from “Verify the result,” and your answer to the self-check question. Design exercises may produce an ADR, diagram, or experiment table; distinguish a proposal from an implemented service.

[Previous step](../03-modeling/025-scd2.md) · [Next step](../03-modeling/027-data-vault.md) · [Full roadmap](../README.md)

**Module:** DWH modeling. **Estimated time:** 2–4 hours for a first pass; deeper practice and a project take additional time. The previous step defines reading order, not an equally mandatory prerequisite for every learner: see the [learning paths](../../docs/LEARNING_PATHS.md).

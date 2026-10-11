# 087. FinOps and cost per useful result

## Learning outcome

Estimate workload cost and establish spending controls.

## How it works

Cost per run, GB, or published dataset links expense to useful output. Account for scans, compute, storage, egress, and retries separately. Estimates state prices explicitly and reconcile with actual billing. Teaching prices are scenarios, not current tariffs.

## Fintech example

A yearly backfill costs more than a daily run and needs a separate budget.

## Implementation steps

1. Identify components
2. Supply synthetic prices
3. Compare normal and backfill cost
4. Establish budget gates.

## Practical assignment

Implement estimates from specified GB and compute-hour prices. Check units and rounding.

## Common mistake and its consequences

Free storage trials conceal egress and ongoing compute costs.

## Verify the result

Record assumptions, currency, and volume instead of describing the system as cheap.

## Self-check question

Why can reduced runtime still increase cost on a higher-priced compute tier?

## Further reading

- [BigQuery documentation](https://cloud.google.com/bigquery/docs) — primary documentation; find the section relevant to this lesson.
- [Snowflake documentation](https://docs.snowflake.com/en/) — primary documentation; find the section relevant to this lesson.

## Deliverable and navigation

Save your solution in your own fork under `portfolio/087-cost/`. Include the problem, a minimal example, the check from “Verify the result,” and your answer to the self-check question. Design exercises may produce an ADR, diagram, or experiment table; distinguish a proposal from an implemented service.

[Previous step](../09-platform/086-iac.md) · [Next step](../09-platform/088-ownership.md) · [Full roadmap](../README.md)

**Module:** Platform and security. **Estimated time:** 2–4 hours for a first pass; deeper practice and a project take additional time. The previous step defines reading order, not an equally mandatory prerequisite for every learner: see the [learning paths](../../docs/LEARNING_PATHS.md).

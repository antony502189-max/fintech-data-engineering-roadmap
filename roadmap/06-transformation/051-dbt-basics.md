# 051. dbt models, dependencies, and contracts

## Learning outcome

Separate transformation from source delivery.

## How it works

dbt builds SQL models and expresses dependencies using references and sources. It is not a universal ingestion service. Successful queries show execution; successful tests show only tested properties. Deployment needs a supported adapter/warehouse combination and separated environments.

## Fintech example

Ingestion persists raw events; dbt produces capture facts and monetary marts.

## Implementation steps

1. Declare source tables
2. Define references
3. Add tests
4. Separate development and production.

## Practical assignment

Express mart_daily_cash as a proposed dbt model. Identify the adapter and required fixture checks.

## Common mistake and its consequences

Publishing because SQL succeeded ignores an incomplete upstream batch.

## Verify the result

Document grain and verify freshness and completeness independently.

## Self-check question

Which ingestion responsibilities does dbt not solve by itself?

## Further reading

- [dbt data tests](https://docs.getdbt.com/docs/build/data-tests) — primary documentation; find the section relevant to this lesson.

## Deliverable and navigation

Save your solution in your own fork under `portfolio/051-dbt-basics/`. Include the problem, a minimal example, the check from “Verify the result,” and your answer to the self-check question. Design exercises may produce an ADR, diagram, or experiment table; distinguish a proposal from an implemented service.

[Previous step](../05-storage/050-storage-decision.md) · [Next step](../06-transformation/052-dbt-incremental.md) · [Full roadmap](../README.md)

**Module:** Transformations and orchestration. **Estimated time:** 2–4 hours for a first pass; deeper practice and a project take additional time. The previous step defines reading order, not an equally mandatory prerequisite for every learner: see the [learning paths](../../docs/LEARNING_PATHS.md).

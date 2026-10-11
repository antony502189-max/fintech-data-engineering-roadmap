# 024. Dimensions, keys, and unknown members

## Learning outcome

Keep facts when reference data arrives late.

## How it works

Natural keys come from sources; surrogate keys belong to the warehouse. Source namespaces prevent collisions between systems. An unknown member retains a fact until the dimension arrives, after which an explicit repair rule updates the relationship. Unknown and anonymized members have different meanings.

## Fintech example

A capture precedes the merchant profile. An INNER JOIN must not remove that money.

## Implementation steps

1. Define the namespace
2. Choose surrogate keys
3. Define the unknown member
4. Plan late-dimension repair.

## Practical assignment

Simulate a missing merchant and prove the monetary total survives the dimension join.

## Common mistake and its consequences

Using a dimension as a filter discards valid money during temporary reference-data gaps.

## Verify the result

Fact totals agree before and after the join; unknown members are visible separately.

## Self-check question

Why do identical merchant IDs from two providers not necessarily identify one merchant?

## Further reading

- [Kimball dimensional modeling techniques](https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/) — primary documentation; find the section relevant to this lesson.

## Deliverable and navigation

Save your solution in your own fork under `portfolio/024-dimensions/`. Include the problem, a minimal example, the check from “Verify the result,” and your answer to the self-check question. Design exercises may produce an ADR, diagram, or experiment table; distinguish a proposal from an implemented service.

[Previous step](../03-modeling/023-facts.md) · [Next step](../03-modeling/025-scd2.md) · [Full roadmap](../README.md)

**Module:** DWH modeling. **Estimated time:** 2–4 hours for a first pass; deeper practice and a project take additional time. The previous step defines reading order, not an equally mandatory prerequisite for every learner: see the [learning paths](../../docs/LEARNING_PATHS.md).

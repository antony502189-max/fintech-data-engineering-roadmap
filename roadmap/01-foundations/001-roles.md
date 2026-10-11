# 001. The data engineer's role and DWH boundaries

## Learning outcome

Distinguish the responsibilities of data engineers, analytics engineers, analysts, and financial process owners.

## How it works

Data engineers make delivery and reproduction reliable. Analytics engineers turn inputs into agreed models; analysts answer business questions. A warehouse is an analytical representation, not a replacement for the operational payment system. A team may combine roles, but ownership of a financial definition must still be explicit.

## Fintech example

“How much did we earn yesterday?” requires definitions of revenue, fees, refunds, and recognition dates. Counting successful authorizations cannot answer it.

## Implementation steps

1. Identify the consumer and decision
2. Specify the grain and monetary event
3. Name the definition owner
4. Agree on data availability deadlines.

## Practical assignment

Create a RACI matrix for changing a source, approving net revenue, fixing duplicates, closing a period, and recovering a mart.

## Common mistake and its consequences

Treating the job owner as the owner of business meaning produces two technically healthy marts with contradictory financial totals.

## Verify the result

Every activity has exactly one accountable owner. State separately who accepts the reconciliation result.

## Self-check question

Who can authorize reissuing a closed financial report, and why is a green CI run insufficient?

## Further reading

- [Kimball dimensional modeling techniques](https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/) — primary documentation; find the section relevant to this lesson.

## Deliverable and navigation

Save your solution in your own fork under `portfolio/001-roles/`. Include the problem, a minimal example, the check from “Verify the result,” and your answer to the self-check question. Design exercises may produce an ADR, diagram, or experiment table; distinguish a proposal from an implemented service.

[Previous step](../../docs/START_HERE.md) · [Next step](../01-foundations/002-requirements.md) · [Full roadmap](../README.md)

**Module:** Engineering foundations. **Estimated time:** 2–4 hours for a first pass; deeper practice and a project take additional time. The previous step defines reading order, not an equally mandatory prerequisite for every learner: see the [learning paths](../../docs/LEARNING_PATHS.md).

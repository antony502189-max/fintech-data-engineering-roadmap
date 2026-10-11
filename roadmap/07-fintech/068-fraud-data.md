# 068. Fraud data, delayed labels, and leakage

## Learning outcome

Build features available when a decision was made.

## How it works

Fraud labels may arrive weeks later, making business and knowledge time essential. Features must use information available to the decision system at that instant. Random splits can mix future patterns into past evaluation. Define temporal splits and label maturity explicitly.

## Fintech example

A February dispute labels a January payment; its February status cannot be a January feature.

## Implementation steps

1. Define decision_at
2. Track feature availability
3. Specify label maturity
4. Verify temporal splits.

## Practical assignment

Compare capture_total_at for e6 before and after receipt, then design a label table.

## Common mistake and its consequences

Filtering event_time alone allows late knowledge into historical features.

## Verify the result

p3 is zero before arrival and 2500 afterward; training contracts include a knowledge cutoff.

## Self-check question

How do delayed labels affect evaluation of the most recent weeks?

## Further reading

- [Feast point in time joins](https://docs.feast.dev/getting-started/concepts/point-in-time-joins) — primary documentation; find the section relevant to this lesson.

## Deliverable and navigation

Save your solution in your own fork under `portfolio/068-fraud-data/`. Include the problem, a minimal example, the check from “Verify the result,” and your answer to the self-check question. Design exercises may produce an ADR, diagram, or experiment table; distinguish a proposal from an implemented service.

[Previous step](../07-fintech/067-credit.md) · [Next step](../07-fintech/069-kyc-data.md) · [Full roadmap](../README.md)

**Module:** Financial data and money movement. **Estimated time:** 2–4 hours for a first pass; deeper practice and a project take additional time. The previous step defines reading order, not an equally mandatory prerequisite for every learner: see the [learning paths](../../docs/LEARNING_PATHS.md).

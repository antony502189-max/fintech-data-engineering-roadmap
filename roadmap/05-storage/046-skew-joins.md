# 046. Skew, broadcast, and join strategies

## Learning outcome

Choose a join strategy from sizes and distributions.

## How it works

Broadcast distributes a small join side to workers, reducing shuffle but requiring memory and size estimates. Skew overloads partitions with hot keys. Salting can help selected workloads but needs correct recombination and compatible join rules.

## Fintech example

The unknown merchant groups many facts and becomes the hottest key.

## Implementation steps

1. Estimate dimension size
2. Identify frequent keys
3. Check broadcast memory
4. Measure the new plan.

## Practical assignment

Compare strategies for 1 MB and 5 GB dimensions. Explain why one forced broadcast rule is unsuitable for both.

## Common mistake and its consequences

Broadcasting a large dimension causes memory failures across executors.

## Verify the result

Document memory assumptions, key distribution, and hot-key test results.

## Self-check question

Why does random fact salting without a matching dimension rule break joins?

## Further reading

- [Spark SQL performance tuning](https://spark.apache.org/docs/latest/sql-performance-tuning.html) — primary documentation; find the section relevant to this lesson.

## Deliverable and navigation

Save your solution in your own fork under `portfolio/046-skew-joins/`. Include the problem, a minimal example, the check from “Verify the result,” and your answer to the self-check question. Design exercises may produce an ADR, diagram, or experiment table; distinguish a proposal from an implemented service.

[Previous step](../05-storage/045-spark.md) · [Next step](../05-storage/047-streaming.md) · [Full roadmap](../README.md)

**Module:** Storage and processing. **Estimated time:** 2–4 hours for a first pass; deeper practice and a project take additional time. The previous step defines reading order, not an equally mandatory prerequisite for every learner: see the [learning paths](../../docs/LEARNING_PATHS.md).

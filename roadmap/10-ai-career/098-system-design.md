# 098. Fintech DWH system-design interviews

## Learning outcome

Explain designs through requirements, invariants, and tradeoffs.

## How it works

Begin with consumers, volume, latency, sources, and budgets. Then define grain, delivery guarantees, history, verification, and recovery. A tool list is weaker than a simple design with explicit failure behavior. Identify unknown requirements and how to resolve them.

## Fintech example

Design daily settlement and near-real-time fraud with consistent monetary history.

## Implementation steps

1. Clarify requirements
2. Draw data flow
3. Analyze crashes
4. Estimate costs and ownership.

## Practical assignment

Conduct a thirty-minute mock interview. Record five assumptions and three alternatives.

## Common mistake and its consequences

Drawing Kafka→Spark→Snowflake without explaining missing-payment detection leaves the central problem unanswered.

## Verify the result

Cover discrepancies, late data, versioned publication, and recovery drills.

## Self-check question

How does the design change when past knowledge must be reconstructed?

## Further reading

- [AWS Well Architected](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html) — primary documentation; find the section relevant to this lesson.
- [Apache Kafka documentation](https://kafka.apache.org/documentation/) — primary documentation; find the section relevant to this lesson.
- [Kimball dimensional modeling techniques](https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/) — primary documentation; find the section relevant to this lesson.

## Deliverable and navigation

Save your solution in your own fork under `portfolio/098-system-design/`. Include the problem, a minimal example, the check from “Verify the result,” and your answer to the self-check question. Design exercises may produce an ADR, diagram, or experiment table; distinguish a proposal from an implemented service.

[Previous step](../10-ai-career/097-ml-pipelines.md) · [Next step](../10-ai-career/099-portfolio.md) · [Full roadmap](../README.md)

**Module:** AI, ML and portfolio. **Estimated time:** 2–4 hours for a first pass; deeper practice and a project take additional time. The previous step defines reading order, not an equally mandatory prerequisite for every learner: see the [learning paths](../../docs/LEARNING_PATHS.md).

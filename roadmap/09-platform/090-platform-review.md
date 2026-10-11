# 090. Platform review and scaling plans

## Learning outcome

Match requirements to components and operational cost.

## How it works

Architecture review considers failures, ownership, security, cost, and migration. More tools mean more integrations and version combinations. Begin with the smallest sufficient platform and measurable reasons to expand it. Local tests confirm principles, not cloud behavior.

## Fintech example

SQLite batch is useful for learning; multi-tenant production needs different isolation and scale.

## Implementation steps

1. Write an ADR
2. State assumptions
3. Separate measured and untested claims
4. Define scaling triggers.

## Practical assignment

Plan synthetic lab→PostgreSQL→managed warehouse transitions using measured limitations.

## Common mistake and its consequences

Deploying Kubernetes, Kafka, and lakehouse together without operating capacity creates avoidable complexity.

## Verify the result

The ADR defines transition conditions, costs, migration scope, and recovery.

## Self-check question

Which measurement proves compute is the bottleneck rather than source or sink?

## Further reading

- [AWS Well Architected](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html) — primary documentation; find the section relevant to this lesson.
- [Spark SQL performance tuning](https://spark.apache.org/docs/latest/sql-performance-tuning.html) — primary documentation; find the section relevant to this lesson.

## Deliverable and navigation

Save your solution in your own fork under `portfolio/090-platform-review/`. Include the problem, a minimal example, the check from “Verify the result,” and your answer to the self-check question. Design exercises may produce an ADR, diagram, or experiment table; distinguish a proposal from an implemented service.

[Previous step](../09-platform/089-access-review.md) · [Next step](../10-ai-career/091-ai-assistant.md) · [Full roadmap](../README.md)

**Module:** Platform and security. **Estimated time:** 2–4 hours for a first pass; deeper practice and a project take additional time. The previous step defines reading order, not an equally mandatory prerequisite for every learner: see the [learning paths](../../docs/LEARNING_PATHS.md).

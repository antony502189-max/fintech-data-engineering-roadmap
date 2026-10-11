# 050. Choosing batch or streaming

## Learning outcome

Connect architecture to decision deadlines and operating cost.

## How it works

Batch is often simpler to rebuild and reconcile. Streaming reduces latency while adding state, lateness, and continuous-operation requirements. Frequent microbatches may suffice. Mixed architectures need explicit responsibilities for provisional operations and verified financial output.

## Fintech example

Fraud needs seconds; daily settlement waits for a cutoff. One path may not serve both equally.

## Implementation steps

1. Clarify latency budget
2. Define completeness evidence
3. Estimate on-call cost
4. Choose the smallest sufficient design.

## Practical assignment

Write an ADR for daily finance and online fraud, including behavior during a stream outage.

## Common mistake and its consequences

Maintaining two independent authoritative net metrics without reconciliation creates competing truths.

## Verify the result

The ADR states selection criteria and how provisional and final outputs reconcile.

## Self-check question

What measured benefit would justify moving hourly batch processing to streaming?

## Further reading

- [Apache Kafka documentation](https://kafka.apache.org/documentation/) — primary documentation; find the section relevant to this lesson.
- [Airflow best practices](https://airflow.apache.org/docs/apache-airflow/stable/best-practices.html) — primary documentation; find the section relevant to this lesson.

## Deliverable and navigation

Save your solution in your own fork under `portfolio/050-storage-decision/`. Include the problem, a minimal example, the check from “Verify the result,” and your answer to the self-check question. Design exercises may produce an ADR, diagram, or experiment table; distinguish a proposal from an implemented service.

[Previous step](../05-storage/049-state-checkpoints.md) · [Next step](../06-transformation/051-dbt-basics.md) · [Full roadmap](../README.md)

**Module:** Storage and processing. **Estimated time:** 2–4 hours for a first pass; deeper practice and a project take additional time. The previous step defines reading order, not an equally mandatory prerequisite for every learner: see the [learning paths](../../docs/LEARNING_PATHS.md).

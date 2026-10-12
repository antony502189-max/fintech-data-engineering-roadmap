# Learning paths

## Beginner: a sample 24-week schedule

| Weeks | Focus | Deliverable |
|---|---|---|
| 1–3 | Lessons 001–010 | E01–E04: functions, tests, time, money, Git |
| 4–6 | 011–020 | E05–E08: grain, joins, incremental behavior |
| 7–9 | 021–030 | E09–E12: facts, dimensions, history |
| 10–12 | 031–040 | E13–E16: contracts and recovery matrices |
| 13–15 | 041–050 | E17–E20: storage, partitions, lateness |
| 16–17 | 051–060 | E21–E24: DAGs, retries, publication, migration |
| 18–20 | 061–080 | E25–E32: money, reconciliation, quality, incidents |
| 21–22 | 081–100 | E33–E40: access, AI, point-in-time features |
| 23–24 | Capstone | Independent code, evidence, recovery, limitations |

The pace is illustrative. A first pass may take 200–400 hours, with projects requiring more. At ten hours a week, the upper bound exceeds 24 weeks. Adjust the schedule using completed artifacts rather than elapsed weeks.

## Analyst to analytics/data engineer

Start with E05–E08 even if you write SQL daily, then lessons 021–040 and 051–080. Python and tests remain essential: E01–E04 and lessons 003, 006, 009, 010. Understand storage and platform decisions before specializing in a stack. Settlement is a suitable capstone.

## Backend engineer to data engineer

Begin with SQL semantics and facts, lessons 011–030, then CDC, outbox, replay, Kafka, and checkpoints in 031–050. HTTP and transaction experience does not replace understanding financial additivity. Complete 061–080 and build settlement or fraud data.

## Experienced data engineer to fintech

Start with 061–070, E25–E28, and [money correctness](MONEY_CORRECTNESS.md). Include bitemporal lesson 026, point-in-time lesson 096, and publication/close lessons 056 and 066. Review 071–080 and ownership 088. Challenge assumptions about revenue, cutoffs, FX, and completeness.

## Essential versus deeper specialization

Essential: Python, SQL, grain, history, exact money, idempotency, independent reconciliation, tests, recovery, and permissions. One warehouse and one orchestrator suffice for a first capstone.

Specialize when needed in Vault, Iceberg, Spark internals, Kafka/Flink state, Terraform, feature stores, or RAG. Learn mechanisms and limits before choosing products. Certifications can complement, but not replace, a verifiable project.

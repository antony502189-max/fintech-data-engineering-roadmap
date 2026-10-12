# Capstones: build a data product

Choose a project and implement it in your fork or a separate repository. These are specifications and acceptance criteria, not delivered production services.

| Project | Outcome | Prerequisites |
|---|---|---|
| [Settlement warehouse](SETTLEMENT.md) | Ingestion, history, and reconciliation | Lessons 001–080, E01–E32 |
| [Fraud features](FRAUD.md) | Point-in-time datasets and delayed labels | 026, 068, 096–097, E37 |
| [Credit mart](CREDIT.md) | Flows, balances, repayment allocation | 023, 067, E28 |
| [RAG catalog](RAG.md) | Evidence-based answers with retrieval ACLs | 091–095, E38–E39 |

Start with SQLite and synthetic fixtures; migration is a separate milestone. Include a problem, contract, executable instructions, tests, a failure drill, recovery, an ADR, and limitations. Tool count is not the goal.

## Acceptance rubric: 100 points

| Criterion | Points | Evidence |
|---|---:|---|
| Grain, meaning, currency, time | 20 | Contract and numerical examples |
| Reproducible startup | 15 | Clean command and fixed fixtures |
| Meaningful correctness checks | 25 | Positive/negative cases and independent expectations |
| History and recovery | 15 | Replay, backfill, or late-data before/after |
| Permissions and minimization | 10 | Denied cases and synthetic data |
| Decisions and scope | 15 | ADR, lineage, measured versus untested claims |

A project without startup instructions and tests is unfinished regardless of presentation. Verify supported tool combinations and never publish credentials.

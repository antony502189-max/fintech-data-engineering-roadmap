# Frequently asked questions

**Do I need paid cloud services?** No. The baseline and E01–E40 work offline. Check actual prices, limits, and permissions before managed-warehouse experiments; extensions do not provision resources automatically.

**Why SQLite?** It makes financial invariants executable with one command. It does not measure production throughput, distributed consistency, or cloud IAM.

**Where are SQL tasks?** E05–E08 execute SQL in memory. The additional journal task is `sql/exercises/05-ledger.sql`, with a reference in `sql/solutions/05-ledger.sql`. SQL lessons include further assignments.

**What comes after the small exercises?** Use [C01–C08](../challenges/README.md): multi-stage ingestion, historical joins, payout reconciliation, schema migration, bitemporal reporting, real backup recovery, a runnable SQL bug hunt, and training-data assembly. C07 asks you to repair an incorrect query rather than fill in a blank function.

**Why does grade fail after init?** `solve` intentionally contains TODO. Implement it; `reference` executes the provided solution instead of assessing your work.

**Can I open solutions immediately?** Yes, but attempt the task first. After reading a reference, add a new negative case and explain it independently.

**Why do Python exercises not start Kafka?** Platform tasks model principles offline. [Extensions](../labs/STACK_EXTENSIONS.md) describe integrations requiring their own runtime and verification.

**Why do demo ingestion statistics change on replay?** The database persists under `--out`. Use a fresh directory for baseline statistics; monetary totals should stay unchanged.

**Can I publish real banking data?** Use synthetic examples. Do not publish customer records, card details, documents, credentials, or production payloads.

**Is this a complete accounting ledger?** No. Signed postings demonstrate conservation. Full accounts, balances, settlement protocols, permissions, and accounting policy require separate design.

**Does this replace tool documentation?** No. Lessons explain mechanisms and practice; verify exact versions and settings in primary documentation.

**How should links be updated?** Resource PRs identify old and replacement URLs, authors, and reasons. Local path checks do not validate internet content quality.

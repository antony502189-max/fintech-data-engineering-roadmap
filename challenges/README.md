# Eight scenario labs: from functions to complete workflows

Finish the foundation exercises, then practice multi-stage state and failure recovery before a capstone. These labs use synthetic inputs and Python's standard library. Several execute real SQLite queries, transactions, and backups; they do not start a cloud platform.

```bash
python challenges/run.py list
python challenges/run.py init C01
python challenges/run.py grade C01
python challenges/run.py reference C01
python challenges/run.py verify
```

`grade` tests your personal implementation. `reference` and `verify` test provided solutions. C07 is a bug hunt with executable incorrect SQL; other starters intentionally fail until implemented.

| Lab | Skill |
|---|---|
| [C01. Multi-batch payments, replay, and rollback](C01.md) | A JSON trace plus a crash matrix explaining which transaction owns each write. |
| [C02. Late dimensions and a historical SQL join](C02.md) | The temporal join, its query plan, and totals proving that unknown members do not lose money. |
| [C03. Grouped payouts and independent reconciliation](C03.md) | A payout reconciliation report with an unallocated-payment exception queue. |
| [C04. Dual schema migration without double counting](C04.md) | A migration trace and a compatibility table for old, new, invalid, and conflicting payloads. |
| [C05. Original and restated bitemporal reports](C05.md) | Two report snapshots and an overlap detector with exact-boundary evidence. |
| [C06. Backup restore with an atomic checkpoint](C06.md) | A restoration trace, an actual backup operation, and proof that failed attempts never advance progress. |
| [C07. Debug a plausible but wrong SQL report](C07.md) | A corrected query, a minimal counterexample, and a before/after review note. |
| [C08. Leakage-safe training data with delayed labels](C08.md) | A training manifest, row-level event provenance, and negative examples showing leakage and label exclusion. |

## Completion rubric

1. Pass all named scenarios without hardcoding fixture values or mutating input.
2. Add a meaningful new negative or boundary case.
3. Explain the transaction, grain, or knowledge boundary that prevents the defect.
4. Preserve evidence of failure and recovery where applicable.
5. State which production properties remain untested.

Inputs and expected outputs are public learning fixtures, not a secure examination system. The grader runs trusted local Python code; it is not a sandbox. Integration-heavy properties need the [stack extensions](../labs/STACK_EXTENSIONS.md).

Further reading: [SQLite transactions and backup API](https://docs.python.org/3.12/library/sqlite3.html), [Kimball late-arriving facts](https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/late-arriving-fact/), and [Stripe bank reconciliation](https://docs.stripe.com/bank-reconciliation). These sources provide mechanisms and domain context; the synthetic tasks are original.

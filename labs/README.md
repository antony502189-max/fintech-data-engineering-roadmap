# Runnable payments lab

```bash
python -m fintech_lab --out work/lab-first-run
python -m unittest discover -s tests -v
```

The demo writes a SQLite database and JSON report. Use a new output directory for a clean baseline; repeats deliberately show duplicates. Trace p1, p2, p3, and p9 through the [dictionary](../docs/DATA_DICTIONARY.md) and [monetary walkthrough](../docs/MONEY_CORRECTNESS.md).

## Try these changes

- Add a late event and observe its old business day.
- Repeat an event with a new receipt timestamp and verify unchanged amounts.
- Change an accepted ID's amount and observe rollback.
- Delete a posting and trigger a failed invariant.
- Insert a late SCD2 change and inspect boundaries.
- Change external confirmation and compare mismatch, missing, and unexpected outcomes.
- Compare feature values before and after knowledge time.

Keep personal scripts under `work/`, import lab functions, and use separate temporary databases. Do not modify public fixtures merely to pass checks.

[Fault drills](fault-drills.md) provide snippets; [forty exercises](../practice/README.md) provide starters and grading; [extensions](STACK_EXTENSIONS.md) connect principles with real tools.

For longer workflows, use the [scenario labs](../challenges/README.md). They combine transaction boundaries, historical lookup, reconciliation, backup recovery, and training-data availability rather than testing one rule at a time.

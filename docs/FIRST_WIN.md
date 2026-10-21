# Your first win: find the missing dollar

**Question:** Your payment journal balances. Does that mean the processor paid the correct amount?

In this experiment, you will ingest six synthetic events, replay them without
double counting, and find two settlement exceptions. No package installation,
cloud account, API key, or SQL knowledge is needed. Requires Python 3.12+ with
`sqlite3` and Git.

## Run it

```bash
git clone https://github.com/antony502189-max/fintech-data-engineering-roadmap.git
cd fintech-data-engineering-roadmap
python -m fintech_lab.quickstart
```

On Windows, use `py -3` if `python` is unavailable. Run from the repository root.
Every invocation uses a new in-memory database and writes no files, so running
the command again gives the same result.

## Read the evidence

The first delivery inserts six events. The repeated delivery inserts zero and
recognizes six duplicates. Each event has a balanced pair of journal entries.
Yet the external settlement still contains these exceptions:

| Payment | Currency | Expected minor units | External minor units | External minus expected | Result |
|---|---|---:|---:|---:|---|
| p1 | USD | 7700 | 7700 | 0 | Matched |
| p2 | EUR | 4900 | 4900 | 0 | Matched |
| p3 | USD | 2500 | 2400 | -100 | Amount mismatch |
| p9 | USD | Unknown | 500 | Unknown | Unexpected external payment |

For p1, capture minus fee minus refund is `10000 - 300 - 2000 = 7700`.
For p3, the processor reports $24.00 against an expected $25.00: a $1.00 shortfall.
For p9, there is no internal payment; a missing amount is unknown, not zero.
USD and EUR remain separate. This simplified teaching journal uses signed pairs;
it is not a production bank ledger.

**Takeaway:** replay safety, journal balance, and settlement reconciliation are
three different checks. Passing one does not establish the others.

## Make one change

Before editing, predict the result. In [the synthetic fixture](../fintech_lab/synthetic.py),
change p3's settlement `net_minor` from `2400` to `2500`, then run the command again.
p3 should become `matched`, while p9 remains `unexpected_external`.
Restore `2400` afterward; repository tests expect the original deliberate defect.

## Choose your next step

- New to Python: initialize [E01](../practice/E01.md), implement `solve(data)`, and grade it.
- Comfortable with SQL: try [E05](../practice/E05.md) on event versus payment grain.
- Want a harder investigation: open [the scenario guide](../challenges/README.md) and try C07's SQL bug hunt.
- Want saved evidence: run `python -m fintech_lab --out work/first-win` to write a database and JSON report, including late-event features.

If this helped, a voluntary star makes the project easier to find again. A useful
bug report includes the command, Python version, and expected versus actual output.
See [contribution guidance](../CONTRIBUTING.md) and [learning paths](LEARNING_PATHS.md).

"""A repeatable first success: replay payments and explain settlement exceptions."""
from .reconcile import reconcile
from .synthetic import payments, settlement
from .warehouse import assert_balanced, connect, ingest


def run_demo():
    """Use a fresh in-memory database so every run has the same starting point."""
    db = connect()
    try:
        first = ingest(db, payments())
        replay = ingest(db, payments())
        assert_balanced(db)
        rows = reconcile(db, settlement())
        return {"first": first, "replay": replay, "reconciliation": rows}
    finally:
        db.close()


def main():
    report = run_demo()
    print("PAYMENTS REPLAY: a five-minute fintech data experiment")
    print("Synthetic data | integer minor units | fresh in-memory SQLite")
    print()
    print(f"First delivery: {report['first']['inserted']} events inserted")
    print(f"Same delivery again: {report['replay']['inserted']} inserted, "
          f"{report['replay']['duplicates']} duplicates")
    print("Journal check: balanced for every event and currency")
    print()
    print("Payment  Currency  Expected  External  Delta  Status")
    for row in report["reconciliation"]:
        def amount(key):
            value = row[key]
            return "n/a" if value is None else str(value)
        print(f"{row['payment_id']:<8} {row['currency']:<9} "
              f"{amount('expected_minor'):>8} {amount('actual_minor'):>9} "
              f"{amount('delta_minor'):>6}  {row['status']}")
    print()
    print("Explain it: p3 is short by 100 USD minor units ($1.00).")
    print("p9 exists only in the external settlement; its delta is unknown.")
    print("A balanced journal does not prove that external settlement matches.")
    print("Next: docs/FIRST_WIN.md, then practice E05 or scenario C07.")


if __name__ == "__main__":
    main()

"""Run the complete local teaching lab; write reproducible, synthetic artifacts."""
import argparse
import json
from pathlib import Path
from .warehouse import connect, ingest, daily, assert_balanced
from .synthetic import payments, settlement
from .reconcile import reconcile
from .scd import apply_change, tier_at
from .features import capture_total_at

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, default=Path("work/demo"))
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)
    db = connect(args.out / "warehouse.db")
    try:
        first = ingest(db, payments())
        replay = ingest(db, payments())
        assert_balanced(db)
        apply_change(db, "c1", "standard", "2026-01-01T00:00:00Z")
        apply_change(db, "c1", "premium", "2026-01-02T00:00:00Z")
        report = {"ingestion": first, "replay": replay, "daily": daily(db),
                  "reconciliation": reconcile(db, settlement()),
                  "tier_on_boundary": tier_at(db, "c1", "2026-01-02T00:00:00Z"),
                  "late_event_feature_before_arrival": capture_total_at(db, "p3", "USD", "2026-01-02T00:00:00Z"),
                  "late_event_feature_after_arrival": capture_total_at(db, "p3", "USD", "2026-01-04T00:00:00Z")}
        (args.out / "report.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
        print(json.dumps(report, indent=2))
    finally:
        db.close()

if __name__ == "__main__":
    main()

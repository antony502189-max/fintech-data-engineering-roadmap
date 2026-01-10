"""Idempotent ingestion and atomic postings, with explicit conflicting duplicates."""
import json
import sqlite3
from pathlib import Path
from .contracts import validate

class ConflictingEvent(ValueError):
    pass

def connect(path=":memory:"):
    db = sqlite3.connect(path)
    db.row_factory = sqlite3.Row
    db.executescript(Path(__file__).with_name("schema.sql").read_text(encoding="utf-8"))
    return db

def postings(event):
    amount = event["amount_minor"]
    if event["kind"] == "captured":
        return [("processor_receivable", amount), ("merchant_payable", -amount)]
    if event["kind"] == "refunded":
        return [("processor_receivable", -amount), ("merchant_payable", amount)]
    return [("processor_receivable", -amount), ("processing_expense", amount)]

def ingest(db, events):
    """One transaction per batch. Invalid schemas quarantine; conflicts roll back batch."""
    stats = {"inserted": 0, "duplicates": 0, "quarantined": 0}
    with db:
        for raw in events:
            try:
                event = validate(raw)
            except (ValueError, TypeError) as exc:
                db.execute("INSERT INTO quarantine(payload,reason) VALUES(?,?)",
                           (json.dumps(raw, sort_keys=True), str(exc)))
                stats["quarantined"] += 1
                continue
            payload = json.dumps(event, sort_keys=True)
            # Arrival timestamp is delivery metadata, not business event identity.
            business = {k: v for k, v in event.items() if k != "received_at"}
            previous = db.execute("SELECT payload FROM raw_events WHERE event_id=?",
                                  (event["event_id"],)).fetchone()
            if previous:
                old = json.loads(previous["payload"])
                old.pop("received_at")
                if old != business:
                    raise ConflictingEvent(f"Event identity collision: {event['event_id']}")
                stats["duplicates"] += 1
                continue
            db.execute("INSERT INTO raw_events VALUES(?,?,?,?,?,?,?,?)",
                       (*[event[k] for k in ("event_id", "payment_id", "kind", "amount_minor",
                                             "currency", "event_time", "received_at")], payload))
            db.executemany("INSERT INTO ledger_entries VALUES(?,?,?,?)",
                           [(event["event_id"], account, event["currency"], value)
                            for account, value in postings(event)])
            stats["inserted"] += 1
    return stats

def daily(db):
    return [dict(row) for row in db.execute("SELECT * FROM mart_daily_cash ORDER BY event_date,currency")]

def assert_balanced(db):
    bad = db.execute("""SELECT event_id,currency FROM ledger_entries
        GROUP BY event_id,currency HAVING sum(signed_minor) != 0 OR count(*) != 2""").fetchall()
    missing = db.execute("""SELECT event_id FROM raw_events WHERE event_id NOT IN
        (SELECT event_id FROM ledger_entries)""").fetchall()
    if bad or missing:
        raise AssertionError("Unbalanced or missing journal entries")

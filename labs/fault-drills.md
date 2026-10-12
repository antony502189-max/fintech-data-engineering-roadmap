# Seven safe fault drills

Save snippets as `work/drill.py` and run from the root. Use synthetic input only. Record baseline, defect, detector, and recovery for each experiment.

## 1. Replay

```python
from fintech_lab.warehouse import connect, ingest, daily
from fintech_lab.synthetic import payments
db=connect()
ingest(db,payments())
before=daily(db)
print(ingest(db,payments()))
assert daily(db)==before
db.close()
```

Expect zero inserts, six duplicates, and unchanged totals.

## 2. Conflict after a new event

```python
from fintech_lab.warehouse import connect,ingest,ConflictingEvent
from fintech_lab.synthetic import payments,event
db=connect()
ingest(db,[payments()[0]])
try:
    ingest(db,[event('new','new','captured',100),dict(payments()[0],amount_minor=10001)])
except ConflictingEvent:
    print('conflict detected')
assert db.execute('SELECT count(*) FROM raw_events').fetchone()[0]==1
db.close()
```

The new event must roll back with the conflicting batch.

## 3. Missing journal

```python
from fintech_lab.warehouse import connect,ingest,assert_balanced
from fintech_lab.synthetic import payments
db=connect(); ingest(db,payments())
db.execute("DELETE FROM ledger_entries WHERE event_id='e1'")
try:
    assert_balanced(db)
    raise RuntimeError('detector missed failure')
except AssertionError:
    print('missing journal detected')
db.rollback()
assert_balanced(db)
db.close()
```

A group-only sum check would miss an entirely removed event.

## 4. Late arrival

Ingest `payments()[:-1]`, record daily totals, then ingest `payments()[-1:]`. January 1 USD changes from 9700 to 12200. January 3 does not appear as an event-time day. Compare against a separate full rebuild.

## 5. Quarantine

Pass `dict(payments()[0], amount_minor=True)`. Expect one quarantined record, no raw event, and no postings. A later valid delivery can be accepted; the rejected row remains evidence.

## 6. Feature leakage

After full ingestion, p3 at `2026-01-02T00:00:00Z` has feature zero; at `2026-01-04T00:00:00Z` it has 2500. Remove the receipt constraint in a personal implementation and confirm a negative test detects leakage.

## 7. Backup and replay

Use `db.backup(target_db)` to preserve e1–e5. Restore separately and replay six events: five duplicates plus one insert must recover baseline totals. Arbitrary active-file copying does not replace a consistent backup API.

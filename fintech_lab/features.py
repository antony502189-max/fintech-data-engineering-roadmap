"""A tiny point-in-time feature: filter on business time AND knowledge time."""
from .contracts import parse_time

def capture_total_at(db, payment_id, currency, decision_at):
    cutoff = parse_time(decision_at).isoformat()
    return db.execute("""SELECT coalesce(sum(amount_minor),0) FROM raw_events
        WHERE payment_id=? AND currency=? AND kind='captured'
        AND event_time < ? AND received_at <= ?""", (payment_id, currency, cutoff, cutoff)).fetchone()[0]

"""Valid-time SCD2 intervals rebuilt from ordered effective changes.

This is not bitemporal: historical warehouse knowledge is not retained here.
"""
from .contracts import parse_time

def apply_change(db, customer_id, tier, effective_at):
    stamp = parse_time(effective_at).isoformat()
    if not customer_id or not tier:
        raise ValueError("customer_id and tier required")
    with db:
        existing = db.execute("SELECT tier FROM customers_history WHERE customer_id=? AND valid_from=?",
                              (customer_id, stamp)).fetchone()
        if existing:
            if existing["tier"] != tier:
                raise ValueError("Conflicting effective-time change")
            return
        changes = [(row["valid_from"], row["tier"]) for row in db.execute(
            "SELECT valid_from,tier FROM customers_history WHERE customer_id=? ORDER BY valid_from", (customer_id,))]
        changes.append((stamp, tier))
        changes.sort()
        db.execute("DELETE FROM customers_history WHERE customer_id=?", (customer_id,))
        for i, (start, value) in enumerate(changes):
            end = changes[i+1][0] if i+1 < len(changes) else None
            db.execute("INSERT INTO customers_history VALUES(?,?,?,?)", (customer_id, value, start, end))

def tier_at(db, customer_id, at):
    stamp = parse_time(at).isoformat()
    row = db.execute("""SELECT tier FROM customers_history WHERE customer_id=?
        AND valid_from <= ? AND (valid_to IS NULL OR ? < valid_to)""", (customer_id, stamp, stamp)).fetchone()
    return row["tier"] if row else None

"""Small deterministic fixture: two currencies, refund, fee and late arrival."""

def event(event_id, payment_id, kind, amount, currency="USD", day="2026-01-01", arrival=None):
    stamp = f"{day}T12:00:00+00:00"
    return {"event_id": event_id, "payment_id": payment_id, "kind": kind,
            "amount_minor": amount, "currency": currency,
            "event_time": stamp, "received_at": arrival or stamp}

def payments():
    return [
        event("e1", "p1", "captured", 10000),
        event("e2", "p1", "fee", 300),
        event("e3", "p1", "refunded", 2000, day="2026-01-02"),
        event("e4", "p2", "captured", 5000, "EUR"),
        event("e5", "p2", "fee", 100, "EUR"),
        event("e6", "p3", "captured", 2500, arrival="2026-01-03T12:00:00+00:00"),
    ]

def settlement():
    # Independent external fixture. Deliberate p3 shortfall and unrecognized p9.
    return [
        {"payment_id": "p1", "currency": "USD", "net_minor": 7700},
        {"payment_id": "p2", "currency": "EUR", "net_minor": 4900},
        {"payment_id": "p3", "currency": "USD", "net_minor": 2400},
        {"payment_id": "p9", "currency": "USD", "net_minor": 500},
    ]

"""Strict ingress contract for the synthetic event stream."""
from datetime import datetime, timezone
from .money import EXPONENTS

FIELDS = {"event_id", "payment_id", "kind", "amount_minor", "currency", "event_time", "received_at"}
KINDS = {"captured", "refunded", "fee"}

def parse_time(value: str) -> datetime:
    if not isinstance(value, str):
        raise ValueError("Timestamp must be a string")
    try:
        stamp = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise ValueError("Invalid timestamp") from exc
    if stamp.tzinfo is None:
        raise ValueError("Timestamp requires an offset")
    return stamp.astimezone(timezone.utc)

def validate(event: dict) -> dict:
    if not isinstance(event, dict) or set(event) != FIELDS:
        raise ValueError("Unexpected or missing fields")
    out = dict(event)
    for key in ("event_id", "payment_id"):
        if not isinstance(out[key], str) or not out[key] or len(out[key]) > 80:
            raise ValueError(f"Invalid {key}")
    if out["kind"] not in KINDS or out["currency"] not in EXPONENTS:
        raise ValueError("Unsupported kind or currency")
    amount = out["amount_minor"]
    if type(amount) is not int or not 0 < amount <= 9_000_000_000_000_000:
        raise ValueError("amount_minor must be a positive bounded integer")
    for key in ("event_time", "received_at"):
        out[key] = parse_time(out[key]).isoformat()
    if out["received_at"] < out["event_time"]:
        raise ValueError("received_at precedes event_time")
    return out

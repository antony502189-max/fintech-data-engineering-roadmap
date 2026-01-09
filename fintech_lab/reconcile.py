"""Full outer reconciliation at payment/currency grain, exact minor units."""

def reconcile(db, external):
    expected = {(r["payment_id"], r["currency"]): r["net_minor"] for r in db.execute("""
        SELECT payment_id,currency,
        sum(CASE WHEN kind='captured' THEN amount_minor ELSE -amount_minor END) AS net_minor
        FROM raw_events GROUP BY payment_id,currency""")}
    actual = {}
    for row in external:
        key = (row["payment_id"], row["currency"])
        if key in actual:
            raise ValueError("Duplicate settlement key")
        if type(row["net_minor"]) is not int:
            raise ValueError("Settlement amount must be integer")
        actual[key] = row["net_minor"]
    result = []
    for key in sorted(expected.keys() | actual.keys()):
        left, right = expected.get(key), actual.get(key)
        status = ("unexpected_external" if left is None else "missing_external" if right is None
                  else "matched" if left == right else "amount_mismatch")
        result.append({"payment_id": key[0], "currency": key[1], "expected_minor": left,
                       "actual_minor": right, "delta_minor": None if left is None or right is None
                       else right-left, "status": status})
    return result

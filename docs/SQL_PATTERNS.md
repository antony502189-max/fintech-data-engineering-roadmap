# SQL patterns for financial data

Examples use SQLite fixtures. Other warehouses require dialect and temporal-function verification.

## Grain and independent aggregation

```sql
SELECT payment_id, currency,
       SUM(CASE WHEN kind='captured' THEN amount_minor ELSE -amount_minor END) AS net_minor,
       COUNT(*) AS event_count
FROM raw_events
GROUP BY payment_id, currency;
```

This converts event grain to payment/currency grain. Joining one-to-many attempts before SUM multiplies amounts. Aggregate each input to the target grain first. SUM(DISTINCT amount_minor) does not fix fanout: distinct equal-value payments must both count.

## Missing versus zero

```sql
SELECT payment_id, COUNT(*) AS events,
       SUM(CASE WHEN kind='captured' THEN 1 ELSE 0 END) AS captures
FROM raw_events
GROUP BY payment_id;
```

A zero amount over known records differs from missing data. `reconcile.py` preserves missing and unexpected sides. SQLite FULL OUTER JOIN support depends on runtime version; the lab explicitly unions keys in Python instead of assuming a dialect version.

## Deterministic latest record

```sql
SELECT * FROM (
    SELECT *, ROW_NUMBER() OVER (
        PARTITION BY payment_id
        ORDER BY event_time DESC, event_id DESC
    ) AS rn
    FROM raw_events
) WHERE rn=1;
```

This selects the last row under a stated technical order, not a universally correct business state. A lifecycle needs source sequence and transition rules. Event-ID tie-breaking is valid only when the contract permits that interpretation.

## SCD2 lookup

```sql
SELECT customer_id, tier FROM customers_history
WHERE customer_id = ? AND valid_from <= ?
  AND (valid_to IS NULL OR ? < valid_to);
```

[from,to) prevents two versions at one transition instant. Check overlap before joining or facts can multiply. Valid-time SCD2 does not preserve historical system knowledge after corrections.

## Violating-row checks

```sql
SELECT event_id, currency
FROM ledger_entries
GROUP BY event_id, currency
HAVING SUM(signed_minor) <> 0 OR COUNT(*) <> 2;
```

Entirely missing journals do not appear in this query. Add a raw-to-postings anti-join. Implement both conditions in the [ledger exercise](../sql/exercises/05-ledger.sql).

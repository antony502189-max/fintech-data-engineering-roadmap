PRAGMA foreign_keys = ON;
CREATE TABLE IF NOT EXISTS raw_events (
    event_id TEXT PRIMARY KEY,
    payment_id TEXT NOT NULL,
    kind TEXT NOT NULL CHECK(kind IN ('captured','refunded','fee')),
    amount_minor INTEGER NOT NULL CHECK(amount_minor > 0),
    currency TEXT NOT NULL,
    event_time TEXT NOT NULL,
    received_at TEXT NOT NULL,
    payload TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS ledger_entries (
    event_id TEXT NOT NULL REFERENCES raw_events(event_id),
    account TEXT NOT NULL,
    currency TEXT NOT NULL,
    signed_minor INTEGER NOT NULL,
    PRIMARY KEY(event_id, account)
);
CREATE TABLE IF NOT EXISTS quarantine (
    id INTEGER PRIMARY KEY,
    payload TEXT NOT NULL,
    reason TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS customers_history (
    customer_id TEXT NOT NULL,
    tier TEXT NOT NULL,
    valid_from TEXT NOT NULL,
    valid_to TEXT,
    PRIMARY KEY(customer_id, valid_from),
    CHECK(valid_to IS NULL OR valid_to > valid_from)
);
CREATE INDEX IF NOT EXISTS raw_events_payment ON raw_events(payment_id, event_time);
CREATE VIEW IF NOT EXISTS mart_daily_cash AS
SELECT substr(event_time, 1, 10) AS event_date, currency,
       sum(CASE WHEN kind = 'captured' THEN amount_minor ELSE -amount_minor END) AS net_minor,
       count(*) AS event_count
FROM raw_events GROUP BY substr(event_time, 1, 10), currency;

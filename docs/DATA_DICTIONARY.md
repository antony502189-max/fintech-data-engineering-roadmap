# Local data dictionary

| Table / field | Meaning | Constraint |
|---|---|---|
| raw_events.event_id | Stable business event key | Primary key; conflicting payloads are not ignored |
| payment_id | Groups capture, refund, fee | Not event identity |
| kind | captured / refunded / fee | Three teaching event types |
| amount_minor | Positive integer magnitude | Sign comes from kind; booleans rejected |
| currency | USD / EUR / JPY / KWD | Extension requires contract changes |
| event_time | Business timestamp in UTC | Input must have an offset |
| received_at | First accepted delivery time in UTC | Not before event_time; excluded from business identity |
| payload | Canonical validated JSON | Synthetic fields only |
| ledger_entries.signed_minor | Signed posting amount | Event/account primary key |
| account | Teaching account | Not a complete accounting chart |
| quarantine.reason | Schema-rejection cause | Identity collisions roll back the batch |
| customers_history.valid_from | Valid interval start | Inclusive |
| valid_to | Valid interval end | Exclusive; NULL means open |
| mart_daily_cash.net_minor | Capture − refund − fee | Event-date/currency grain; not revenue |
| event_count | Financial-event count | Not payment count |

## Fixed fixture

| Event | Payment | Kind | Currency | Minor units | Event day | Arrival day |
|---|---|---|---|---:|---|---|
| e1 | p1 | captured | USD | 10000 | 01-01 | 01-01 |
| e2 | p1 | fee | USD | 300 | 01-01 | 01-01 |
| e3 | p1 | refunded | USD | 2000 | 01-02 | 01-02 |
| e4 | p2 | captured | EUR | 5000 | 01-01 | 01-01 |
| e5 | p2 | fee | EUR | 100 | 01-01 | 01-01 |
| e6 | p3 | captured | USD | 2500 | 01-01 | 01-03 |

Dates are in 2026 at 12:00 UTC. Payment aggregates: p1=7700 USD minor, p2=4900 EUR minor, p3=2500 USD minor. External p3=2400 and p9=500; p9 exists only externally. The external fixture is independently specified rather than derived from expected totals.

Currency exponents: USD/EUR=2, JPY=0, KWD=3. Decimal input amounts are strings. Never sum different currencies without an explicit FX contract.

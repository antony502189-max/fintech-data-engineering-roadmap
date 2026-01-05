# Словарь локальной схемы

| Таблица / поле | Смысл | Ограничение |
|---|---|---|
| raw_events.event_id | Устойчивый business event key | PK; конфликт payload не игнорируется |
| payment_id | Группирует capture, refund, fee | Не является event identity |
| kind | captured / refunded / fee | Только три учебных типа |
| amount_minor | Положительная integer величина события | Знак определяется kind, bool запрещён |
| currency | USD / EUR / JPY / KWD | Другие валюты требуют расширения contract |
| event_time | UTC время бизнес-события | ISO с offset на входе |
| received_at | UTC время получения первой принятой доставки | Не раньше event_time; не часть business identity |
| payload | Канонический JSON после validation | Только synthetic поля в этой lab |
| ledger_entries.signed_minor | Signed posting | PK event/account; source amount сохраняется отдельно |
| ledger_entries.account | Условный ledger account | Учебная перспектива, не полный chart of accounts |
| quarantine.reason | Причина schema rejection | Schema conflict с существующим ID откатывает batch |
| customers_history.valid_from | Начало valid interval | Включено |
| valid_to | Конец valid interval | Исключено; NULL = open |
| mart_daily_cash.net_minor | capture − refund − fee | Event-day/currency grain; не revenue |
| event_count | Количество денежных событий | Не число платежей |

## Fixture

| Event | Payment | Kind | Currency | Minor | Event day | Arrival day |
|---|---|---|---|---:|---|---|
| e1 | p1 | captured | USD | 10000 | 01-01 | 01-01 |
| e2 | p1 | fee | USD | 300 | 01-01 | 01-01 |
| e3 | p1 | refunded | USD | 2000 | 01-02 | 01-02 |
| e4 | p2 | captured | EUR | 5000 | 01-01 | 01-01 |
| e5 | p2 | fee | EUR | 100 | 01-01 | 01-01 |
| e6 | p3 | captured | USD | 2500 | 01-01 | 01-03 |

Все даты относятся к 2026 году; clocks — 12:00 UTC. p1 aggregate = 7700 USD minor, p2 = 4900 EUR minor, p3 = 2500 USD minor. External p3=2400; p9=500 exists only externally. Это независимый synthetic fixture, не результат повторного вычисления expected side.

Для валют exponent: USD/EUR=2, JPY=0, KWD=3. Decimal source amount должен быть строкой. Minor amounts не складываются между валютами без отдельного FX contract.

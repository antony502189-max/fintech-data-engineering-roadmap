# SQL patterns для денежных данных

Все запросы ниже проверяются на SQLite fixture. Перенос в другой warehouse требует проверки dialect и временных функций.

## Grain и независимые агрегаты

```sql
SELECT payment_id, currency,
       SUM(CASE WHEN kind='captured' THEN amount_minor ELSE -amount_minor END) AS net_minor,
       COUNT(*) AS event_count
FROM raw_events
GROUP BY payment_id, currency;
```

Это event→payment aggregation. Если присоединить attempts one-to-many до SUM, суммы размножатся. Сначала агрегируй каждую сторону до payment/currency, затем соединяй. SUM(DISTINCT amount_minor) не исправляет fanout: два разных платежа одинаковой суммы должны учитываться оба.

## Missing и zero

```sql
SELECT payment_id, COUNT(*) AS events,
       SUM(CASE WHEN kind='captured' THEN 1 ELSE 0 END) AS captures
FROM raw_events
GROUP BY payment_id;
```

Нулевая сумма известного набора — другое утверждение, чем отсутствие набора. Сверка в `reconcile.py` сохраняет missing/unexpected стороны. SQLite поддержка FULL OUTER JOIN зависит от version; локальная lab использует явное объединение keys в Python и не полагается на неизвестный runtime dialect.

## Детерминированная последняя запись

```sql
SELECT * FROM (
    SELECT *, ROW_NUMBER() OVER (
        PARTITION BY payment_id
        ORDER BY event_time DESC, event_id DESC
    ) AS rn
    FROM raw_events
) WHERE rn=1;
```

Этот query выбирает последнюю строку по **заданному техническому порядку**, а не универсально правильный business state. Для production lifecycle нужен source sequence и правила переходов. Event_id tie-breaker допустим только если контракт разрешает такую интерпретацию.

## SCD2 join

```sql
SELECT customer_id, tier FROM customers_history
WHERE customer_id = ? AND valid_from <= ?
  AND (valid_to IS NULL OR ? < valid_to);
```

Граница `[from,to)` предотвращает две versions на одном instant. Перед join проверяй overlap; иначе факты размножаются. Valid-time SCD2 не сохраняет прошлое system knowledge после коррекции.

## Violating-row check

```sql
SELECT event_id, currency
FROM ledger_entries
GROUP BY event_id, currency
HAVING SUM(signed_minor) <> 0 OR COUNT(*) <> 2;
```

Этот запрос не видит полностью потерянный journal. Дополнительный anti-join raw→postings необходим. В [SQL задании](../sql/exercises/05-ledger.sql) реализуй оба условия.

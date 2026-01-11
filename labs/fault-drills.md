# Семь безопасных fault drills

Сохрани каждый snippet в `work/drill.py` и запусти `python work/drill.py` из root. Используй только синтетику. После каждого опыта запиши baseline, нарушение, detector и recovery.

## 1. Replay

```python
from fintech_lab.warehouse import connect, ingest, daily
from fintech_lab.synthetic import payments
db=connect()
ingest(db,payments())
before=daily(db)
print(ingest(db,payments()))
assert daily(db)==before
db.close()
```

Ожидается inserted=0, duplicates=6; totals прежние.

## 2. Conflict после частичного batch

```python
from fintech_lab.warehouse import connect,ingest,ConflictingEvent
from fintech_lab.synthetic import payments,event
db=connect()
ingest(db,[payments()[0]])
try:
    ingest(db,[event('new','new','captured',100),dict(payments()[0],amount_minor=10001)])
except ConflictingEvent:
    print('conflict detected')
assert db.execute('SELECT count(*) FROM raw_events').fetchone()[0]==1
db.close()
```

Новая запись `new` должна откатиться вместе с конфликтующим batch.

## 3. Потерянный journal

```python
from fintech_lab.warehouse import connect,ingest,assert_balanced
from fintech_lab.synthetic import payments
db=connect(); ingest(db,payments())
db.execute("DELETE FROM ledger_entries WHERE event_id='e1'")
try:
    assert_balanced(db)
    raise RuntimeError('detector missed failure')
except AssertionError:
    print('missing journal detected')
db.rollback()
assert_balanced(db)
db.close()
```

Один sum=0 query не обнаружил бы полностью удалённое событие.

## 4. Late arrival

Загрузи `payments()[:-1]`, сохрани daily totals, затем `payments()[-1:]`. До late delivery USD за 1 января=9700; после=12200. Day 3 января не появляется в event-time mart. Сверь с полным rebuild в другой базе.

## 5. Quarantine

Передай `dict(payments()[0], amount_minor=True)`. Ожидается quarantined=1, raw count=0, postings count=0. Исправление входа новой корректной delivery допускается; rejected row остаётся evidence.

## 6. Feature leakage

После полного ingest вызови `capture_total_at(db,'p3','USD','2026-01-02T00:00:00Z')`: 0. На `2026-01-04T00:00:00Z`: 2500. Удали received_at condition в личной копии и убедись, что negative test обнаруживает утечку.

## 7. Backup и replay

Используй `db.backup(target_db)` из sqlite3, сохрани fixture e1–e5. После восстановления replay все шесть events; пять повторов и один insert должны дать full baseline totals. Копирование активного DB file не заменяет согласованный backup API. Выполняй в отдельных synthetic paths.

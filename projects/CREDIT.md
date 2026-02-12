# Проект 3: credit flows и balance snapshots

## Постановка

Synthetic loan имеет disbursement, scheduled due, fee, interest accrual, payment и reversal. Учебный payment waterfall: fee→interest→principal. Financial reader хочет видеть ежедневный остаток и потоки периода.

## План

1. Раздели loan identity, versioned product policy и events.
2. Храни amounts в minor units с currency.
3. Реализуй deterministic allocation с unallocated remainder.
4. Построй daily snapshots и отдельно flow facts.
5. Добавь correction/reversal и объясни, как пересчитываются snapshots.
6. Сделай контроль principal roll-forward и independent fixture totals.

## Сценарии

Payment 1200 при due fee=100, interest=200, principal=1000 распределяется 100/200/900. Payment 2000 оставляет 700 unallocated. Partial payment не делает due components отрицательными. Replay payment_id/event_id не применяет allocation второй раз. Late payment перестраивает affected snapshots.

## Приёмка

Allocated plus unallocated = received. Closing = opening + disbursement − principal payments + specified corrections. Flow за месяц суммируется; balances по дням не складываются как оборот. Каждая строка имеет policy version и lineage. Отчёт явно использует synthetic правила и не задаёт реальные кредитные условия или требования закона.

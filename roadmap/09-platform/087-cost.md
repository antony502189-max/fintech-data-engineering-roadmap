# 087. FinOps и цена полезного результата

## Результат обучения

Оценить затраты на workload и установить контроль расходов.

## Как это работает

Cost per run, per GB и per published dataset помогают связать технические расходы с полезной работой. Scanned bytes, compute duration, storage, egress и retries учитываются отдельно. Estimate использует явно заданные цены, а actual сверяется с billing. Учебные числа — сценарий, не текущие тарифы.

## Пример из финтеха

Backfill за год стоит больше обычного daily run и требует отдельного бюджета.

## Порядок реализации

1. Назови cost components
2. Подставь synthetic prices
3. Рассчитай normal и backfill
4. Добавь budget gate.

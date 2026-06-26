# 055. Оркестрация backfill и ресурсные лимиты

## Результат обучения

Пересчитать историю без вытеснения ежедневной критической нагрузки.

## Как это работает

Backfill создаёт конкуренцию за source, warehouse и scheduler. Pools, concurrency limits и отдельные workloads позволяют ограничить ущерб. Пересчёт следует публиковать целостными units, а не произвольными chunks. Можно начать с небольшого canary period и сравнить контрольные итоги.

## Пример из финтеха

Месяц исправлений запускает 31 job и лишает ресурсов сегодняшний settlement.

## Порядок реализации

1. Назови priority
2. Ограничь concurrency
3. Проверь canary day
4. Публикуй по согласованному scope.

## Практическое задание

Составь run plan на месяц с batch size, stop condition и rollback dataset.

## Типичная ошибка и её последствия

Backfill запускают с тем же SLA и unlimited parallelism; источник OLTP перегружается.

## Проверка результата

Plan включает daily workload reservation, ETA assumption и измеримый abort threshold.

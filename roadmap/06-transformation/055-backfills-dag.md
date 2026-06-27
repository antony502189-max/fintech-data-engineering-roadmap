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

## Вопрос для самопроверки

Когда безопаснее сделать shadow rebuild, чем обновлять partitions на месте?

## Что читать дальше

- [Airflow best practices](https://airflow.apache.org/docs/apache-airflow/stable/best-practices.html) — первичная документация; ищи раздел по теме урока.
- [dbt data tests](https://docs.getdbt.com/docs/build/data-tests) — первичная документация; ищи раздел по теме урока.

# 076. Lineage и оценка радиуса изменения

## Результат обучения

Определить, какие consumers затронуты изменением колонки.

## Как это работает

Табличный lineage даёт начальную карту зависимостей; column lineage точнее связывает формулы. Внешние exports, spreadsheets и ML datasets часто отсутствуют в автоматическом графе. Change impact требует metadata, owners и поиска фактического использования. Версии отчетов позволяют оценить ретроспективный ущерб.

## Пример из финтеха

Изменение fee sign затрагивает net cash, но не count distinct payments.

## Порядок реализации

1. Создай dependency graph
2. Отметь metric columns
3. Добавь внешние consumers
4. Выдели affected versions.

## Практическое задание

Построй reachability для raw fee → daily cash → report и независимой payment count ветки.

## Типичная ошибка и её последствия

Любое изменение raw объявляют влияющим на всё либо доверяют неполному автоматическому graph.

## Проверка результата

Scope содержит прямо и косвенно затронутые продукты и явно неизвестные consumers.

## Вопрос для самопроверки

Когда table lineage слишком груб для планирования безопасного backfill?

## Что читать дальше

- [dbt data tests](https://docs.getdbt.com/docs/build/data-tests) — первичная документация; ищи раздел по теме урока.
- [OpenTelemetry concepts](https://opentelemetry.io/docs/concepts/) — первичная документация; ищи раздел по теме урока.

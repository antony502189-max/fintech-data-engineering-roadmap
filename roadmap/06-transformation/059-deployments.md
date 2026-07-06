# 059. Миграции моделей и обратная совместимость

## Результат обучения

Выпустить новую схему без одновременного отключения consumers.

## Как это работает

Expand-contract добавляет новую форму, переводит consumers и затем удаляет старую. Длительность overlap определяется использованием и retention. Destructive schema change требует миграции данных и rollback strategy; revert кода не восстанавливает удалённые колонки. Versioned dataset облегчает сравнение.

## Пример из финтеха

currency переименовывают в settlement_currency, потому что появляется presentment_currency.

## Порядок реализации

1. Добавь новую колонку
2. Backfill old data
3. Переведи consumers
4. Удали old после проверки использования.

## Практическое задание

Составь migration plan с шагами, acceptance и recoverability для двух валютных полей.

## Типичная ошибка и её последствия

Ренейм колонок деплоят одним PR; внешние consumers, которых нет в DAG, падают.

## Проверка результата

Старый и новый reader работают в overlap; удаления имеют отдельное решение.

## Вопрос для самопроверки

Когда rollback deployment не может восстановить прежние данные?

## Что читать дальше

- [dbt data tests](https://docs.getdbt.com/docs/build/data-tests) — первичная документация; ищи раздел по теме урока.
- [PostgreSQL documentation](https://www.postgresql.org/docs/current/) — первичная документация; ищи раздел по теме урока.

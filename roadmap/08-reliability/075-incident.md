# 075. Расследование инцидента и containment

## Результат обучения

Восстановить доверие к данным через scope и проверку исправления.

## Как это работает

Сначала ограничь распространение неверного output и сохрани evidence. Затем определи affected periods, consumers и причины. Recovery должен проверяться по независимому эталону. Postmortem объясняет contributing factors, а не обвиняет человека. Исправление кода без пересчёта старых данных оставляет последствия.

## Пример из финтеха

Ошибочный знак fee опубликован в течение недели; нужно найти все report versions и downstream extracts.

## Порядок реализации

1. Заморозь affected publish
2. Зафиксируй scope
3. Построй shadow correction
4. Проверь и сообщи владельцам.

## Практическое задание

Напиши incident timeline для sign bug, включая обнаружение, containment, repair и verification.

## Типичная ошибка и её последствия

После deploy fix считают инцидент закрытым; старые выгрузки остаются неверными.

## Проверка результата

Есть affected consumer list, before-after totals и проверка восстановленного периода.

## Вопрос для самопроверки

Как различить root cause и событие, которое лишь обнаружило ошибку?

## Что читать дальше

- [OpenTelemetry concepts](https://opentelemetry.io/docs/concepts/) — первичная документация; ищи раздел по теме урока.
- [Airflow best practices](https://airflow.apache.org/docs/apache-airflow/stable/best-practices.html) — первичная документация; ищи раздел по теме урока.

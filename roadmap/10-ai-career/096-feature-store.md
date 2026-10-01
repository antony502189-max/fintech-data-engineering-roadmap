# 096. Feature store и point-in-time корректность

## Результат обучения

Согласовать определения offline и online признаков.

## Как это работает

Feature store помогает управлять definitions, materialization и serving, но не гарантирует правильный event/knowledge cutoff автоматически. Online value и training value должны иметь согласованные semantics. TTL, late arrivals и entity keys влияют на доступность. Leakage test нужен независимо от продукта.

## Пример из финтеха

Признак p3 не должен содержать capture, который ещё не был получен системой.

## Порядок реализации

1. Определи entity и feature
2. Назови cutoff
3. Проверь availability
4. Сравни online и historical semantics.

## Практическое задание

Запусти features tests и расширь свою реализацию rolling window с received_at constraint.

## Типичная ошибка и её последствия

Offline feature использует исправленную историю, недоступную online в момент решения.

## Проверка результата

Для каждого decision_at набор использованных событий имеет допустимые timestamps.

## Вопрос для самопроверки

Какие отличия между event_time и ingestion_time должны быть записаны в feature definition?

## Что читать дальше

- [Feast point in time joins](https://docs.feast.dev/getting-started/concepts/point-in-time-joins) — первичная документация; ищи раздел по теме урока.

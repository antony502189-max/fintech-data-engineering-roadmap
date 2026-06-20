# 052. dbt incremental, unique key и late updates

## Результат обучения

Спроектировать повторяемую incremental модель.

## Как это работает

unique_key задаёт match при поддерживаемой incremental strategy, но не заменяет тест уникальности входа. Append и merge имеют разные последствия при replay. Late arrivals требуют arrival-based selection или lookback плюс процедура глубокого backfill. Full refresh надо проверять на эквивалентность incremental output.

## Пример из финтеха

Late capture обновляет старый день; merge по сегодняшней дате его не исправляет.

## Порядок реализации

1. Выбери strategy для adapter
2. Назови unique_key
3. Найди affected periods
4. Проверь full refresh equivalence.

## Практическое задание

Напиши pseudo dbt model и тест-план для двух последовательных runs с e6.

## Типичная ошибка и её последствия

Дубликаты source приводят к неопределённому merge или ошибке; unique_key считают очисткой входа.

## Проверка результата

На fixture incremental и full outputs совпадают после replay и late event.

## Вопрос для самопроверки

Когда incremental_predicate может исключить нужную целевую строку из merge?

## Что читать дальше

- [dbt data tests](https://docs.getdbt.com/docs/build/data-tests) — первичная документация; ищи раздел по теме урока.

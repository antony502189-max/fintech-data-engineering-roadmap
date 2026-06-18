# 052. dbt incremental, unique key и late updates

## Результат обучения

Спроектировать повторяемую incremental модель.

## Как это работает

unique_key задаёт match при поддерживаемой incremental strategy, но не заменяет тест уникальности входа. Append и merge имеют разные последствия при replay. Late arrivals требуют arrival-based selection или lookback плюс процедура глубокого backfill. Full refresh надо проверять на эквивалентность incremental output.

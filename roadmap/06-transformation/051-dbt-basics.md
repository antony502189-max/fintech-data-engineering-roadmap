# 051. dbt, зависимости моделей и контракты

## Результат обучения

Отделить преобразование данных от их доставки.

## Как это работает

dbt строит SQL models и зависимости, выражаемые через references и sources. Он не заменяет универсальный ingestion service. Успешный run показывает выполнение query, а успешные tests — только проверенные свойства. Deployment требует поддерживаемой пары adapter и warehouse и согласованных environments.

## Пример из финтеха

Ingestion сохраняет raw events, dbt model собирает capture fact и денежную витрину.

## Порядок реализации

1. Назови source tables
2. Определи refs
3. Добавь tests
4. Раздели dev и production.

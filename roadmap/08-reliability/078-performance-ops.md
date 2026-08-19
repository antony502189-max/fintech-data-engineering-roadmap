# 078. Производительность и capacity planning

## Результат обучения

Связать рост данных с временем готовности и стоимостью.

## Как это работает

Capacity зависит от объёма, распределения ключей, ширины records, concurrency и worst-case backlog. Среднее число событий скрывает peaks. Предел throughput важен вместе с latency и recovery after outage. Benchmark должен описывать окружение и повторения, а не только удачное число одного запуска.

## Пример из финтеха

После двухчасового outage backlog надо обработать до daily close, не перегрузив источник.

## Порядок реализации

1. Измерь steady throughput
2. Смоделируй peak
3. Оцени backlog drain
4. Проверь contention.

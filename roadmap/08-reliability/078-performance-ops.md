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

## Практическое задание

Построй таблицу для arrival rate 1000/s и processing 1500/s: как долго разгружать 2h backlog при продолжающемся потоке?

## Типичная ошибка и её последствия

Делят backlog на общий processing rate, забывая новые arrivals; ETA слишком оптимистична.

## Проверка результата

Расчёт использует spare capacity и указывает, что при processing<=arrival backlog не сокращается.

## Вопрос для самопроверки

Почему doubling workers не гарантирует doubling useful throughput?

## Что читать дальше

- [Spark SQL performance tuning](https://spark.apache.org/docs/latest/sql-performance-tuning.html) — первичная документация; ищи раздел по теме урока.
- [OpenTelemetry concepts](https://opentelemetry.io/docs/concepts/) — первичная документация; ищи раздел по теме урока.

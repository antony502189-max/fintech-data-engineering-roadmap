# 034. CDC, WAL и изменения состояния

## Результат обучения

Различать snapshot, change event и business event.

## Как это работает

CDC считывает изменения database log, включая insert, update и delete. WAL position задаёт порядок изменения базы, но не обязательно бизнес-время платежа. Row update может менять технический атрибут, не создавая денежного события. Начальный snapshot и последующий stream требуют согласованной границы.

## Пример из финтеха

Update статуса payment не равен новой capture проводке. Иначе каждая служебная правка увеличит оборот.

## Порядок реализации

1. Назови source tables
2. Определи snapshot boundary
3. Сохраняй operation и source position
4. Раздели CDC state и domain events.

## Практическое задание

Нарисуй поток PostgreSQL → Debezium → Kafka → raw. Для каждого поля укажи source или delivery semantics.

## Типичная ошибка и её последствия

Все CDC inserts принимают за новые платежи, включая snapshot существующих записей.

## Проверка результата

Документ объясняет, как snapshot не создаёт двойной счёт, и как delete меняет current state.

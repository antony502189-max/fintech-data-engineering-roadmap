# 049. Состояние stream и checkpoint recovery

## Результат обучения

Объяснить, что восстанавливается из checkpoint и где заканчивается гарантия.

## Как это работает

Stateful processor хранит агрегаты, timers и progress. Consistent checkpoint связывает состояние с позициями источника. Sink должен поддерживать нужную commit semantics, иначе checkpoint не предотвращает повтор внешней записи. Retention state и ключей дедупликации ограничивает горизонт безопасного replay.

## Пример из финтеха

Consumer восстановился из вчерашнего checkpoint, но external settlement email уже был отправлен.

## Порядок реализации

1. Опиши state
2. Назови durable checkpoint storage
3. Проверь sink protocol
4. Смоделируй replay за retention.

## Практическое задание

Составь state lifecycle для dedup event_id с TTL 7 дней и replay за 30 дней.

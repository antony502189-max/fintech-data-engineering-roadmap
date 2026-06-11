# 049. Состояние stream и checkpoint recovery

## Результат обучения

Объяснить, что восстанавливается из checkpoint и где заканчивается гарантия.

## Как это работает

Stateful processor хранит агрегаты, timers и progress. Consistent checkpoint связывает состояние с позициями источника. Sink должен поддерживать нужную commit semantics, иначе checkpoint не предотвращает повтор внешней записи. Retention state и ключей дедупликации ограничивает горизонт безопасного replay.

# 043. Iceberg, snapshots и эволюция таблиц

## Результат обучения

Различать snapshot таблицы, файлы данных и catalog.

## Как это работает

Table format управляет metadata, snapshots и набором файлов, видимым читателю. Atomic commit меняет metadata pointer; файлы могут существовать до публикации. Schema и partition evolution требуют поддержки движка и version compatibility. Snapshot retention и orphan cleanup — эксплуатационные операции с последствиями.

## Пример из финтеха

Исправленный январь публикуется новым snapshot, читатели получают целостную версию.

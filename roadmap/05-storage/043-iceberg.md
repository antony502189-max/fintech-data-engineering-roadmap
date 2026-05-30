# 043. Iceberg, snapshots и эволюция таблиц

## Результат обучения

Различать snapshot таблицы, файлы данных и catalog.

## Как это работает

Table format управляет metadata, snapshots и набором файлов, видимым читателю. Atomic commit меняет metadata pointer; файлы могут существовать до публикации. Schema и partition evolution требуют поддержки движка и version compatibility. Snapshot retention и orphan cleanup — эксплуатационные операции с последствиями.

## Пример из финтеха

Исправленный январь публикуется новым snapshot, читатели получают целостную версию.

## Порядок реализации

1. Опиши catalog
2. Назови read и write engines
3. Зафиксируй format compatibility
4. Запланируй maintenance.

## Практическое задание

Спроектируй payments Iceberg table и процесс shadow backfill; обозначь, что local SQLite lab не реализует Iceberg.

## Типичная ошибка и её последствия

Удаляют «старые» files вручную, не проверяя ссылки активных snapshots.

## Проверка результата

План cleanup содержит retention, активные readers и dry run review.

## Вопрос для самопроверки

Почему time travel перестаёт работать после удаления нужных snapshots и файлов?

## Что читать дальше

- [Apache Iceberg documentation](https://iceberg.apache.org/docs/latest/) — первичная документация; ищи раздел по теме урока.

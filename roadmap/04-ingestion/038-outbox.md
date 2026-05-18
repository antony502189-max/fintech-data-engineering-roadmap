# 038. Transactional outbox и публикация событий

## Результат обучения

Объяснить атомарность записи бизнес-состояния и намерения публикации.

## Как это работает

Outbox записывается в той же database transaction, что и бизнес-изменение. Отдельный relay публикует записи и допускает повтор. Это закрывает окно между commit OLTP и отправкой сообщения, но не отменяет необходимость consumer dedup. Порядок событий требует sequence и partition policy.

## Пример из финтеха

Payment capture фиксируется вместе с outbox entry; падение relay не теряет намерение сообщить о capture.

## Порядок реализации

1. Определи outbox schema
2. Запиши в одной transaction
3. Сделай relay retryable
4. Добавь consumer identity check.

## Практическое задание

Составь SQL transaction и crash matrix для publish-before-mark и mark-before-publish.

## Типичная ошибка и её последствия

Сначала ставят published=true, потом отправляют; сбой между действиями теряет событие.

## Проверка результата

Публикация может повторяться, но успешный бизнес commit не остаётся без outbox entry.

## Вопрос для самопроверки

Почему outbox не даёт автоматическое exactly-once во внешнем sink?

## Что читать дальше

- [PostgreSQL documentation](https://www.postgresql.org/docs/current/) — первичная документация; ищи раздел по теме урока.
- [Apache Kafka documentation](https://kafka.apache.org/documentation/) — первичная документация; ищи раздел по теме урока.

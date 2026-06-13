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

## Типичная ошибка и её последствия

TTL удаляет ключи раньше допустимого replay; старые capture учитываются повторно.

## Проверка результата

План связывает TTL с replay horizon или сохраняет persistent sink uniqueness.

## Вопрос для самопроверки

Какие внешние side effects не покрывает восстановление streaming state?

## Что читать дальше

- [Flink event time](https://nightlies.apache.org/flink/flink-docs-stable/docs/concepts/time/) — первичная документация; ищи раздел по теме урока.
- [Apache Kafka documentation](https://kafka.apache.org/documentation/) — первичная документация; ищи раздел по теме урока.

## Артефакт и маршрут

Сохрани решение в своём форке: `portfolio/049-state-checkpoints/`. Включи постановку, минимальный пример, проверку из раздела «Проверка результата» и вывод по вопросу для самопроверки. Для проектных уроков допустимы ADR, схема и таблица экспериментов; не выдавай проект за работающий сервис.

[Предыдущий шаг](../05-storage/048-event-time.md) · [Следующий шаг](../05-storage/050-storage-decision.md) · [Вся карта](../README.md)

**Модуль:** Хранилища и вычисления. **Оценка времени:** 2–4 часа на первый проход; углубление и проект требуют дополнительного времени. Предыдущий шаг задаёт последовательность чтения, а не означает, что все темы одинаково обязательны: см. [маршруты](../../docs/LEARNING_PATHS.md).

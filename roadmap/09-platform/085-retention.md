# 085. Retention, deletion и legal hold как policy

## Результат обучения

Реализовать утверждённые правила хранения без произвольных сроков.

## Как это работает

Retention зависит от категории данных, целей и применимой политики. Инженер реализует правила и evidence их применения; универсальный срок для всего финтеха не существует. Legal hold или другие утверждённые исключения могут приостанавливать deletion. Backups и производные datasets тоже входят в scope.

## Пример из финтеха

Profile projection и ledger evidence могут иметь разные сроки и ограничения.

## Порядок реализации

1. Собери policy input
2. Определи expiry
3. Учти hold
4. Проверь derivatives и backups.

## Практическое задание

На synthetic records реализуй decision delete/keep по заданной дате expiry и hold; это не юридическая рекомендация.

## Типичная ошибка и её последствия

Удаляют только raw, оставляя PII в marts, logs и резервных копиях.

## Проверка результата

Каждое решение содержит policy version, reason и lineage scope.

## Вопрос для самопроверки

Какие владельцы должны согласовать противоречие retention и preservation требований?

## Что читать дальше

- [AWS Well Architected](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html) — первичная документация; ищи раздел по теме урока.
- [PostgreSQL documentation](https://www.postgresql.org/docs/current/) — первичная документация; ищи раздел по теме урока.

# 080. Приёмка надёжности data product

## Результат обучения

Собрать доказательства эксплуатации и назвать непроверенные свойства.

## Как это работает

Надёжность включает правильность, полноту, своевременность и способность восстанавливаться. Unit tests и tiny fixture не доказывают нагрузочную устойчивость, распределённую атомарность или compliance. Readiness review связывает требования с проверками и owners. Непроверенное следует явно обозначить как риск или последующую работу.

## Пример из финтеха

Local lab проходит tests, но не тестирует реальный webhook signature, Kafka rebalance и cloud permissions.

## Порядок реализации

1. Сопоставь requirements и evidence
2. Назови missing checks
3. Определи owner каждого gap
4. Реши учебный или operational status.

## Практическое задание

Составь readiness matrix для capstone с колонками requirement, evidence, scope и limitation.

## Типичная ошибка и её последствия

README называет систему production-ready только потому, что CI зелёный.

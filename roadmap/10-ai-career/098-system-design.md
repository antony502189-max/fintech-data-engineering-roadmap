# 098. Системный дизайн финтех DWH на собеседовании

## Результат обучения

Объяснить архитектуру через требования, инварианты и компромиссы.

## Как это работает

Начни с потребителей, объёма, latency, источников и бюджета. Затем опиши grain, ingestion guarantees, history, checks и recovery. Детальный список технологий без failure scenario слабее простой архитектуры с проверяемыми гарантиями. Укажи, какие требования неизвестны и как их выяснить.

## Пример из финтеха

Спроектируй daily settlement и near-real-time fraud, сохранив согласованную денежную историю.

## Порядок реализации

1. Уточни requirements
2. Нарисуй data flow
3. Разбери crash points
4. Оцени cost и ownership.

## Практическое задание

Проведи 30-minute design interview с самим собой; запиши пять assumptions и три альтернативы.

## Типичная ошибка и её последствия

Сразу рисуют Kafka→Spark→Snowflake и не объясняют, как обнаружится пропавший платёж.

## Проверка результата

Ответ включает mismatch handling, late data, versioned publish и recovery drill.

## Вопрос для самопроверки

Как поменяется дизайн при требовании восстановить прошлое знание, а не только текущую истину?

## Что читать дальше

- [AWS Well Architected](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html) — первичная документация; ищи раздел по теме урока.
- [Apache Kafka documentation](https://kafka.apache.org/documentation/) — первичная документация; ищи раздел по теме урока.
- [Kimball dimensional modeling techniques](https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/) — первичная документация; ищи раздел по теме урока.

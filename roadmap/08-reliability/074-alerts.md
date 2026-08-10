# 074. Алерты, владельцы и бюджет ошибок

## Результат обучения

Сделать сигнал полезным для конкретного действия.

## Как это работает

Alert должен указывать affected data product, impact, owner и первый diagnostic step. Warning статистического отклонения и critical financial mismatch требуют разных действий. Шумные алерты учат игнорировать сигнал. Error budget помогает обсуждать надёжность и темп изменений, но не оправдывает незамеченные денежные дефекты.

## Пример из финтеха

p3 mismatch на 100 minor units имеет конкретное денежное воздействие; падение dev notebook — другое.

## Порядок реализации

1. Определи severity
2. Назови owner
3. Добавь runbook link
4. Проверь false positive cases.

## Практическое задание

Составь alert для missing settlement и amount mismatch с units и cutoffs.

## Типичная ошибка и её последствия

Алерт «job failed» не сообщает, какой период отчёта недоступен и кто страдает.

## Проверка результата

Получатель понимает affected date/currency и действие без чтения всего DAG.

## Вопрос для самопроверки

Почему доля успешных tasks может улучшиться, а пользовательская надёжность ухудшиться?

## Что читать дальше

- [OpenTelemetry concepts](https://opentelemetry.io/docs/concepts/) — первичная документация; ищи раздел по теме урока.
- [Airflow best practices](https://airflow.apache.org/docs/apache-airflow/stable/best-practices.html) — первичная документация; ищи раздел по теме урока.

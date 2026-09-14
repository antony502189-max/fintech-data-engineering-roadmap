# 089. Access review, аудит и exports

## Результат обучения

Проверить доступ по всему пути данных, включая выгрузки.

## Как это работает

Правила warehouse не защищают скачанный CSV автоматически. Exports создают новые copies с отдельными readers и retention. Access audit должен видеть identities, действия и resources, но не записывать секреты. Периодический review проверяет актуальность роли и необходимость доступа.

## Пример из финтеха

Reader создал full raw export в публично доступном bucket, обходя смысл restricted mart.

## Порядок реализации

1. Перечисли export paths
2. Назначь owners
3. Ограничь destination
4. Проверь lifecycle копий.

## Практическое задание

Сделай data-flow inventory для warehouse, notebook, CSV и BI extract; отметь каждую новую копию.

## Типичная ошибка и её последствия

Проверяют только IAM в DWH и забывают публичные URLs выгрузок.

## Проверка результата

Для всех destination есть access policy и retention; неучтённые exports видны как gap.

## Вопрос для самопроверки

Как отзывать доступ к уже скопированным данным и какие ограничения у этого действия?

## Что читать дальше

- [AWS Well Architected](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html) — первичная документация; ищи раздел по теме урока.
- [PostgreSQL documentation](https://www.postgresql.org/docs/current/) — первичная документация; ищи раздел по теме урока.

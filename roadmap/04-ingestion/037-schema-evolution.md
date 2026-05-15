# 037. Эволюция схемы и совместимость

## Результат обучения

Обработать изменение контракта до публикации повреждённых данных.

## Как это работает

Additive field может быть совместимым, но strict consumer должен явно решить, принимать ли неизвестные поля. Изменение типа amount или смысла currency — breaking change даже при прежнем имени. Contract version, dual read и период миграции позволяют изменить producer и consumers независимо.

## Пример из финтеха

Провайдер меняет amount с integer cents на decimal string major units; прежний код увеличивает или уменьшает суммы в сто раз.

## Порядок реализации

1. Опиши compatibility policy
2. Добавь schema version
3. Проверь старый и новый fixtures
4. Запланируй switch и rollback.

## Практическое задание

Измени payload в копии validate и напиши migration plan для двух versions.

## Типичная ошибка и её последствия

Схему «лечат» автоматическим cast; потерянная точность и масштаб не замечены.

## Проверка результата

Неизвестная версия попадает в quarantine; обе поддержанные версии дают одинаковые minor units.

## Вопрос для самопроверки

Почему сохранение имени колонки не доказывает совместимость контракта?

## Что читать дальше

- [Debezium PostgreSQL connector](https://debezium.io/documentation/reference/stable/connectors/postgresql.html) — первичная документация; ищи раздел по теме урока.
- [dbt data tests](https://docs.getdbt.com/docs/build/data-tests) — первичная документация; ищи раздел по теме урока.

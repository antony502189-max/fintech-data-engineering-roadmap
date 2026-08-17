# 077. Backups, RPO, RTO и проверка восстановления

## Результат обучения

Доказать, что резервная копия пригодна для возврата к работе.

## Как это работает

RPO ограничивает допустимую потерю данных во времени, RTO — время восстановления сервиса. Backup без restore drill не доказывает recoverability. Нужны metadata, schema, permissions и ключи доступа, а не только data files. Recovery должен сверить totals и определить replay после backup boundary.

## Пример из финтеха

После backup e1-e5 пришёл e6; restore требует безопасного replay e6.

## Порядок реализации

1. Зафиксируй recovery point
2. Восстанови в отдельном namespace
3. Применяй журнал после boundary
4. Сверь итог.

## Практическое задание

Скопируй synthetic SQLite DB безопасным sqlite backup API, добавь e6 и восстанови с replay в отдельный файл.

## Типичная ошибка и её последствия

Копируют активный DB file произвольно, игнорируя journal/WAL и consistency.

## Проверка результата

Восстановленный dataset равен эталону, время drill и остаточная потеря измерены.

## Вопрос для самопроверки

Какие metadata могут сделать сохранённые data files практически бесполезными?

## Что читать дальше

- [Python sqlite3](https://docs.python.org/3.12/library/sqlite3.html) — первичная документация; ищи раздел по теме урока.
- [AWS Well Architected](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html) — первичная документация; ищи раздел по теме урока.

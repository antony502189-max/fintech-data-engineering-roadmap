# 077. Backups, RPO, RTO и проверка восстановления

## Результат обучения

Доказать, что резервная копия пригодна для возврата к работе.

## Как это работает

RPO ограничивает допустимую потерю данных во времени, RTO — время восстановления сервиса. Backup без restore drill не доказывает recoverability. Нужны metadata, schema, permissions и ключи доступа, а не только data files. Recovery должен сверить totals и определить replay после backup boundary.

## Пример из финтеха

После backup e1-e5 пришёл e6; restore требует безопасного replay e6.

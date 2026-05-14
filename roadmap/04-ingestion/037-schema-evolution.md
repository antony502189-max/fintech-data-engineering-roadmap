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

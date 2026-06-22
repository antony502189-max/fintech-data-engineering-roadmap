# 053. Оркестрация: dependencies и data intervals

## Результат обучения

Определить DAG по готовности данных, а не только по расписанию.

## Как это работает

Orchestrator управляет зависимостями, retries, наблюдаемостью и запуском. Logical data interval задаёт обрабатываемый период; текущий wall clock не должен незаметно менять его. Schedule не доказывает наличие источника. Данные становятся ready после checks, а не после старта upstream job.

## Пример из финтеха

Daily mart за 1 января строится 3 января при backfill и должна сохранить январский interval.

## Порядок реализации

1. Определи interval
2. Вырази dependencies
3. Добавь source-ready condition
4. Передавай параметры явно.

## Практическое задание

Нарисуй DAG ingest → checks → transform → reconciliation → publish, укажи входной период каждой задачи.

## Типичная ошибка и её последствия

Каждая task вычисляет yesterday от now; backfill пересчитывает один и тот же вчерашний день.

## Проверка результата

Повтор запуска одного interval выбирает тот же input manifest и dataset scope.

# 073. Logs, metrics, traces и data lineage

## Результат обучения

Выбрать наблюдаемость для диагностики конкретного сбоя.

## Как это работает

Logs дают детали события, metrics — агрегированные сигналы, traces — путь исполнения между компонентами. Data lineage связывает вход и выход модели. Ни один канал не заменяет все остальные. Correlation identifiers помогают связать run с batch и event, а чувствительные поля не должны попадать в диагностический поток.

## Пример из финтеха

Mismatch p3 связывается с delivery e6, run_id и settlement file version.

## Порядок реализации

1. Определи correlation IDs
2. Установи structured log schema
3. Выдели финансовые metrics
4. Добавь lineage reference.

## Практическое задание

Напиши sample JSON logs для ingest и reconcile без payment details сверх synthetic identifiers.

## Типичная ошибка и её последствия

Логируют полный payload, включая реквизиты; диагностика создаёт новую утечку.

## Проверка результата

По одному event_id можно найти run и input version; logs не содержат секретов.

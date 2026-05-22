# 040. Audit metadata и доказательство полноты

## Результат обучения

Сохранить достаточную информацию для расследования загрузки.

## Как это работает

Run metadata связывает source partition, input hash, code revision, schema version, параметры, число принятых и rejected records. Audit полезен, если данные нельзя незаметно подменить и записи удерживаются нужный срок. Одного лог-файла без стабильного run_id недостаточно. Секреты и лишний payload в audit не нужны.

## Пример из финтеха

Финансовая команда спрашивает, почему p3 появился в отчёте позже: нужны event_time, received_at и run_id.

## Порядок реализации

1. Задай run schema
2. Раздели operational и business totals
3. Сохраняй rejected count
4. Прикрепи manifest к published output.

## Практическое задание

Создай sample manifest для лаборатории с 6 accepted, 0 rejected и 6 duplicate при replay.

## Типичная ошибка и её последствия

Логи содержат только duration и status=success; полноту денежных событий проверить нельзя.

## Проверка результата

Для каждого итогового периода доступны hash входа, версия преобразования и контрольные суммы по валюте.

## Вопрос для самопроверки

Как обнаружить «успешную» загрузку неполного файла?

## Что читать дальше

- [OpenTelemetry concepts](https://opentelemetry.io/docs/concepts/) — первичная документация; ищи раздел по теме урока.
- [PostgreSQL documentation](https://www.postgresql.org/docs/current/) — первичная документация; ищи раздел по теме урока.

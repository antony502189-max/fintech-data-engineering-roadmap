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

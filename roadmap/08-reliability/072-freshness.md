# 072. Свежесть и percentiles задержки

## Результат обучения

Измерить распределение latency по определённому набору событий.

## Как это работает

Latency имеет старт и конец: source time, received_at, transformed_at или published_at. Percentile требует конкретного определения и знаменателя. Максимальная event_time в таблице не показывает задержку каждой записи. Idle source нужно отличать от broken ingestion через heartbeat или expected volume.

## Пример из финтеха

Большинство платежей приходит за секунду, но e6 запаздывает на два дня.

## Порядок реализации

1. Определи timestamps
2. Нормализуй UTC
3. Выбери percentile rule
4. Раздели idle и failure.

## Практическое задание

Посчитай delays fixture и nearest-rank p95. Объясни, почему tiny dataset плохо оценивает production tail.

## Типичная ошибка и её последствия

Смешивают business time и server-local time; негативную задержку заменяют нулём.

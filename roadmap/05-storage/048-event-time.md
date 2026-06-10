# 048. Event time, watermarks и поздние события

## Результат обучения

Различать временные окна и полноту результата.

## Как это работает

Event time описывает время действия, processing time — время обработки. Watermark оценивает прогресс времени по правилам stream, но не доказывает, что все события прибыли. Late events могут требовать update, retraction или отдельного correction stream. Финансовое закрытие нуждается в независимой полноте.

## Пример из финтеха

e6 приходит через два дня и относится к старому daily total; закрытое окно не делает его несуществующим.

## Порядок реализации

1. Выбери allowed lateness
2. Определи side output
3. Назови correction policy
4. Свяжи stream total с batch reconciliation.

## Практическое задание

Нарисуй timeline e1 и e6; покажи provisional, updated и closed totals.

## Типичная ошибка и её последствия

Watermark называют гарантией отсутствия будущих событий и теряют поздние capture.

## Проверка результата

Для события за пределом lateness есть проверяемый маршрут, а не silent drop.

## Вопрос для самопроверки

Когда допустимо оставить late event только в аналитическом correction report?

## Что читать дальше

- [Flink event time](https://nightlies.apache.org/flink/flink-docs-stable/docs/concepts/time/) — первичная документация; ищи раздел по теме урока.

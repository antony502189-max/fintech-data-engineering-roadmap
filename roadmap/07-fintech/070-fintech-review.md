# 070. Финансовый data product: приёмка

## Результат обучения

Оценить готовность витрины по доказательствам, а не числу инструментов.

## Как это работает

Приёмка требует scope, формулы, валюты, grain, completeness, timeliness, reconciliation и объяснимой истории исправлений. Согласованный net cash не доказывает revenue. Операционный SLA не заменяет финконтроль. Production launch должен иметь owners и recovery procedure.

## Пример из финтеха

Fixture показывает matched p1,p2, mismatch p3 и unexpected p9; публикация final должна учитывать exceptions.

## Порядок реализации

1. Собери metric contract
2. Выполни financial checks
3. Классифицируй exceptions
4. Реши provisional или blocked publish.

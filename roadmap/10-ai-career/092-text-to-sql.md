# 092. Text-to-SQL и ограниченный доступ

## Результат обучения

Спроектировать аналитический запрос с контролем полномочий и стоимости.

## Как это работает

LLM output — недоверенный текст. Production query execution требует parser/AST controls, read-only identity, allowlisted schema, timeout и resource budget. Простое регулярное выражение SELECT недостаточно для безопасности. Семантические определения должны ограничивать двусмысленность вопросов; unknown answer лучше выдуманной метрики.

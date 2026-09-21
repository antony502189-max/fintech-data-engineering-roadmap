# 092. Text-to-SQL и ограниченный доступ

## Результат обучения

Спроектировать аналитический запрос с контролем полномочий и стоимости.

## Как это работает

LLM output — недоверенный текст. Production query execution требует parser/AST controls, read-only identity, allowlisted schema, timeout и resource budget. Простое регулярное выражение SELECT недостаточно для безопасности. Семантические определения должны ограничивать двусмысленность вопросов; unknown answer лучше выдуманной метрики.

## Пример из финтеха

Пользователь спрашивает «прибыль», а доступна только mart net cash; система должна уточнить смысл или отказать в таком расчёте.

## Порядок реализации

1. Назови разрешённые metrics
2. Ограничь database identity
3. Валидируй AST
4. Выполни bounded query.

## Практическое задание

Создай design spec и adversarial test list; не запускай произвольные AI SQL в своей базе.

## Типичная ошибка и её последствия

Зелёный read-only query всё равно раскрывает raw PII и сканирует огромный набор.

## Проверка результата

Tests покрывают unknown metric, forbidden table, expensive query и unsupported statement.

## Вопрос для самопроверки

Почему read-only identity не защищает от раскрытия лишних данных?

## Что читать дальше

- [OWASP LLM applications project](https://owasp.org/www-project-top-10-for-large-language-model-applications/) — первичная документация; ищи раздел по теме урока.
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) — первичная документация; ищи раздел по теме урока.

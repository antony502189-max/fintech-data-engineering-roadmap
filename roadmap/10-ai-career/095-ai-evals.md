# 095. Evals: correctness, grounding и abstention

## Результат обучения

Проверить ИИ на стабильном наборе задач и негативных примерах.

## Как это работает

Evaluation dataset должен отражать реальные вопросы, ambiguous cases и forbidden requests. SQL correctness проверяется результатом на fixtures, а не сходством текста. Grounding проверяет поддержку утверждения источником. Abstention оценивает отказ выдумывать ответ. Метрики нужно показывать отдельно по типам, чтобы средний score не скрывал критическую ошибку.

## Пример из финтеха

Модель правильно считает net cash, но выдумывает законный срок хранения KYC; это разные виды риска.

## Порядок реализации

1. Собери cases
2. Определи rubric
3. Раздели critical failures
4. Сохрани model и prompt versions.

## Практическое задание

В offline eval scorecard посчитай pass rate и число forbidden disclosures для набора ответов.

## Типичная ошибка и её последствия

Один общий average выглядит хорошо, хотя критический forbidden case провален.

## Проверка результата

Scorecard отдельно показывает financial correctness, citation validity и critical failure count.

## Вопрос для самопроверки

Почему тестирование на вопросах, созданных тем же prompt, может завысить оценку?

## Что читать дальше

- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) — первичная документация; ищи раздел по теме урока.
- [OWASP LLM applications project](https://owasp.org/www-project-top-10-for-large-language-model-applications/) — первичная документация; ищи раздел по теме урока.

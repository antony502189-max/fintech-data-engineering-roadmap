# ИИ в работе инженера

## Безопасный учебный workflow

1. Дай модели synthetic schema, grain, sign convention, dialect и expected examples.
2. Попроси назвать assumptions и недостающие business definitions.
3. Получи SQL или test draft, прочитай его как недоверенный вклад.
4. Запусти на positive и negative fixtures. Проверь одинаковые суммы разных платежей, late arrival, NULL, две валюты и exact boundary.
5. Сравни с independent expected result и проверь query plan на большом наборе.
6. Сохрани model/prompt version, результат проверки и ручное решение по diff.

## Пример prompt для JOIN review

```text
Dialect: SQLite. Facts grain: one financial event per event_id.
Each payment has several attempts and several fee events.
Money is integer minor units plus currency.
Review the proposed query for fanout, missing data and mixed currencies.
Do not invent columns or equate net cash with revenue.
Give one minimal counterexample and a corrected query.
Mark unverified assumptions explicitly.
```

Текст model answer не доказывает правильность. Counterexample с двумя одинаковыми capture ловит опасное предложение SUM(DISTINCT amount), даже если объяснение выглядит убедительно.

## Text-to-SQL

Система должна иметь ограниченную identity, allowlisted semantic metrics, AST validation, timeout и budget. Даже SELECT может раскрыть лишние данные и дорого сканировать таблицы. Regex check в toy example не является security boundary. Не подключай произвольный model output к production warehouse.

## RAG и injection

Document ACL применяется до передачи context. Документ не может выдавать новые полномочия tool или identity. Citation должна ссылаться на retrieved fragment и его version. Удаление документа требует обновления индекса и caches. Если подтверждения нет, система должна сказать, что не знает.

## Evals

Разделяй financial correctness, grounding, abstention, forbidden disclosure и cost. Один average скрывает critical failures. E38 показывает offline scorecard; E39 — ACL фильтрацию. Полноценная реализация потребует adversarial evaluation, provider/version records и real access integration.

Ориентиры для дальнейшей работы: [OWASP LLM project](https://owasp.org/projects/top-10-for-large-language-model-applications) и [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework). Здесь нет вызовов платной модели и не нужен API key.

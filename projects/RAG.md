# Проект 4: RAG по каталогу данных

## Постановка

Каталог synthetic DWH содержит определения метрик, owners, runbooks и restricted fraud notes. Finance и support имеют разные права. Ассистент должен отвечать с источниками и отказываться при отсутствии подтверждения.

## Offline baseline

1. Храни документы с id, version, allowed_roles и content.
2. Фильтруй ACL **до** retrieval context.
3. Реализуй простую lexical retrieval, чтобы отделить доступ от выбора модели.
4. В ответе указывай только IDs реально использованных документов.
5. Создай eval set: known metric, ambiguous revenue, missing definition, forbidden request, injection внутри документа.
6. Подсчитай grounding pass и critical disclosures отдельно.

## Приёмка

Support context никогда не содержит restricted fraud chunk. Документ с инструкцией export raw не создаёт authority. Unknown revenue вызывает abstention или уточнение, а не выдуманный net cash. Citation имеет valid document version. Deleted document отсутствует в retrieval и cache. Eval baseline сохранён в repository.

## Дальнейшая реализация

Подключение реальной LLM опционально и требует provider config, cost budget и согласованной policy данных. API key хранится вне Git. Text-to-SQL требует AST validation, read-only scoped identity и query budget; lexical filter или regex не выдавай за security boundary. Начни с [E38](../practice/E38.md) и [E39](../practice/E39.md).

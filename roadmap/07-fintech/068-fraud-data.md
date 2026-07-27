# 068. Антифрод, delayed labels и утечка будущего

## Результат обучения

Подготовить признаки, доступные в момент принятия решения.

## Как это работает

Fraud label может появиться спустя недели, поэтому время действия и время знания важны для train set. Признак должен использовать только сведения, доступные decision system тогда. Random split может смешать будущие patterns с прошлым; временные splits и label maturity требуют явного дизайна.

## Пример из финтеха

Dispute в феврале сообщает о риске январского платежа; февральский статус нельзя включить в январский feature.

## Порядок реализации

1. Определи decision_at
2. Сохрани feature availability
3. Назови label maturity
4. Проверь temporal split.

## Практическое задание

Используй capture_total_at для e6 и сравни decision до и после arrival; спроектируй label table.

## Типичная ошибка и её последствия

Event_time filter проходит, но received_at не проверяется; позднее знание проникает в историю.

## Проверка результата

До arrival feature p3=0, после=2500; training contract содержит knowledge cutoff.

## Вопрос для самопроверки

Как delayed label влияет на оценку последних недель модели?

## Что читать дальше

- [Feast point in time joins](https://docs.feast.dev/getting-started/concepts/point-in-time-joins) — первичная документация; ищи раздел по теме урока.

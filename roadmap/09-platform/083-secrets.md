# 083. Секреты, ротация и диагностика

## Результат обучения

Отделить credentials от кода, fixtures и логов.

## Как это работает

Секреты выдаются identity через одобренный механизм и имеют жизненный цикл. Environment variables удобны для локального примера, но не полноценная стратегия защиты сами по себе. Ротация требует проверить consumers и overlap. После утечки удаления строки из последнего коммита недостаточно: credential нужно отозвать.

## Пример из финтеха

Webhook signing secret и API key не должны появляться в issue reproduction.

## Порядок реализации

1. Назови secret owner
2. Определи retrieval
3. Проверь redaction
4. Составь rotation sequence.

## Практическое задание

Сделай synthetic config schema с именами переменных без значений; проверь exception logging.

## Типичная ошибка и её последствия

Печатают полный requests object с headers; authorization попадает в общий лог.

## Проверка результата

Repo и sample logs содержат только placeholders; rotation не зависит от одного ручного шага.

## Вопрос для самопроверки

Почему скрытие секрета в UI логов не отменяет его попадание в backend storage?

## Что читать дальше

- [AWS Well Architected](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html) — первичная документация; ищи раздел по теме урока.
- [Pro Git book](https://git-scm.com/book/en/v2) — первичная документация; ищи раздел по теме урока.

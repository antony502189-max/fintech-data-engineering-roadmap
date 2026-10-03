# 097. ML datasets, labels и версии эксперимента

## Результат обучения

Сделать train dataset воспроизводимым и объяснимым.

## Как это работает

Model version без data version не воспроизводит эксперимент. Dataset manifest фиксирует sources, cutoff, feature definitions, label maturity и split. Monitoring отслеживает coverage, distributions и delayed performance. Training code не должен незаметно переопределять бизнес-метрики источника.

## Пример из финтеха

Fraud model обучается на январских решениях с labels, известными к марту; это фиксированный horizon.

## Порядок реализации

1. Сохрани dataset manifest
2. Зафиксируй split
3. Определи label maturity
4. Добавь leakage checks.

## Практическое задание

Создай synthetic train manifest с temporal split и запиши, какие последние decisions исключены из-за незрелых labels.

## Типичная ошибка и её последствия

Каждый retrain читает latest tables; изменение истории делает старые experiments неповторимыми.

## Проверка результата

Manifest позволяет получить тот же set entity/decision keys и labels.

## Вопрос для самопроверки

Почему version model artifact недостаточна для аудита ML решения?

## Что читать дальше

- [Feast point in time joins](https://docs.feast.dev/getting-started/concepts/point-in-time-joins) — первичная документация; ищи раздел по теме урока.
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) — первичная документация; ищи раздел по теме урока.

## Артефакт и маршрут

Сохрани решение в своём форке: `portfolio/097-ml-pipelines/`. Включи постановку, минимальный пример, проверку из раздела «Проверка результата» и вывод по вопросу для самопроверки. Для проектных уроков допустимы ADR, схема и таблица экспериментов; не выдавай проект за работающий сервис.

[Предыдущий шаг](../10-ai-career/096-feature-store.md) · [Следующий шаг](../10-ai-career/098-system-design.md) · [Вся карта](../README.md)

**Модуль:** ИИ, ML и портфолио. **Оценка времени:** 2–4 часа на первый проход; углубление и проект требуют дополнительного времени. Предыдущий шаг задаёт последовательность чтения, а не означает, что все темы одинаково обязательны: см. [маршруты](../../docs/LEARNING_PATHS.md).

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

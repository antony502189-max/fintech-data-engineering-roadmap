# 097. ML datasets, labels и версии эксперимента

## Результат обучения

Сделать train dataset воспроизводимым и объяснимым.

## Как это работает

Model version без data version не воспроизводит эксперимент. Dataset manifest фиксирует sources, cutoff, feature definitions, label maturity и split. Monitoring отслеживает coverage, distributions и delayed performance. Training code не должен незаметно переопределять бизнес-метрики источника.

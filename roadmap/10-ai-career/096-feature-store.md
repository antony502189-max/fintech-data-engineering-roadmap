# 096. Feature store и point-in-time корректность

## Результат обучения

Согласовать определения offline и online признаков.

## Как это работает

Feature store помогает управлять definitions, materialization и serving, но не гарантирует правильный event/knowledge cutoff автоматически. Online value и training value должны иметь согласованные semantics. TTL, late arrivals и entity keys влияют на доступность. Leakage test нужен независимо от продукта.

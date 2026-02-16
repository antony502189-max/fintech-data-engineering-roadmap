# Runbook: конкретный сигнал

**Alert:** ... **Severity:** ... **Owner:** ... **Affected product/period:** ...

## Диагностика

1. Зафиксировать report/input versions и время обнаружения.
2. Выполнить точную diagnostic command/query в правильном namespace.
3. Сравнить expected/actual control totals и ключи.
4. Установить boundary ошибки: source, ingestion, model, publish или consumer.

## Containment и восстановление

Publish rule, candidate scope, права на correction, rollback target, replay budget и независимая проверка результата. Не выполняй destructive action по неуточнённому пути.

## Завершение

Evidence исправленного состояния, affected consumers, owner decision, follow-up с измеримым acceptance и дата следующей проверки runbook.

# Проект 1: settlement warehouse

## Постановка

Три synthetic providers присылают capture, refund, fee и settlement files. Доставка содержит повторы, поздние события, отсутствующий файл и исправленный batch. Finance нужен ежедневный net cash с доказательством полноты и исключениями.

## Milestones

1. Contract events и batch manifest: identity, version, hash, count, totals by currency.
2. Raw/staging/core: сохраняй original accepted payload и normalized values; карантин schema defects.
3. Ledger и payment/currency net; проверяй completeness, conservation и independent match.
4. Physical daily mart с affected partitions incremental; full rebuild equivalence.
5. Candidate publish с gate и previous version, original/restated report trail.
6. Runbook missing file, mismatch, late event и duplicate collision.

## Готовые сценарии входа

Расширь `payments()` до 10000 событий deterministic seed. Внешний fixture создавай отдельно с явными expected totals. Сценарии: replay всех events; late event старого дня; conflicting ID; отсутствующий provider batch; две одинаковые суммы разных платежей; исправленный settlement version; refund без capture.

## Приёмка

Replay не меняет сумму. Conflict не делает silent overwrite. Incremental и full совпадают после late data. Missing batch блокирует final publish. Каждое исключение имеет ключ, валюту, delta и owner. Published version имеет source manifest и code revision. Перед исправлением закрытого периода сохранён original report.

## Расширение

Перенеси в PostgreSQL, затем выбранный dbt adapter. Добавь source-position ingest и настоящий orchestrator только после baseline. Benchmark на большом synthetic dataset должен фиксировать runtime, hardware и distribution. Не заявляй production readiness по tiny sample.

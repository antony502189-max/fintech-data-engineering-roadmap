# Capstone: собери свой data product

Выбери один проект и реализуй его в своём fork или самостоятельном repository. Это specifications и acceptance criteria; готовый production сервис не выдаётся вместе с roadmap.

| Проект | Основной результат | Prerequisites |
|---|---|---|
| [Settlement warehouse](SETTLEMENT.md) | Полная версия загрузки, истории и сверки | Уроки 001–080, E01–E32 |
| [Fraud feature pipeline](FRAUD.md) | Point-in-time dataset и delayed labels | 026, 068, 096–097, E37 |
| [Credit data mart](CREDIT.md) | Потоки и остатки долга с распределением оплаты | 023, 067, E28 |
| [RAG data catalog](RAG.md) | Answers with citations и ACL before retrieval | 091–095, E38–E39 |

Начни с dependency-free SQLite и synthetic fixtures; перенос в другой stack — отдельный milestone. Проверяемые результаты важнее количества технологий. Для каждого проекта: постановка, contract, README с командами, tests, один failure drill, восстановление, ADR и limitations.

## Рубрика: 100 баллов

| Критерий | Баллы | Доказательство |
|---|---:|---|
| Grain, смыслы, валюта и время | 20 | Contract плюс численные examples |
| Воспроизводимый запуск | 15 | Clean environment command, fixed fixtures |
| Meaningful correctness checks | 25 | Positive/negative cases и независимые expected outputs |
| История и recovery | 15 | Replay/backfill/late scenario с before-after |
| Доступы и minimization | 10 | Denied cases и отсутствие реальных sensitive fields |
| Объяснение решений | 15 | ADR, lineage, scope, measured и untested отдельно |

Без reproducible startup и tests проект не завершён, даже если сумма баллов по красивому описанию высокая. По real stack проверяй supported versions и integrations. Не включай credentials в repository или screenshot.

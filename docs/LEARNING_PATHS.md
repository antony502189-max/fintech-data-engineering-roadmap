# Маршруты по исходному опыту

## С нуля: 24 недели по 10–15 часов

| Недели | Основной фокус | Готовый результат |
|---|---|---|
| 1–3 | Уроки 001–010 | E01–E04; функции, тесты, время, деньги, Git |
| 4–6 | 011–020 | E05–E08; объяснение grain, JOIN и incremental |
| 7–9 | 021–030 | E09–E12; модель facts/dimensions и история |
| 10–12 | 031–040 | E13–E16; контракт загрузки и recovery matrix |
| 13–15 | 041–050 | E17–E20; выбор storage, partition и late policy |
| 16–17 | 051–060 | E21–E24; DAG, retries, publish, migration |
| 18–20 | 061–080 | E25–E32; деньги, сверка, quality, incidents |
| 21–22 | 081–100 | E33–E40; доступы, ИИ, point-in-time, портфолио |
| 23–24 | Capstone | Самостоятельный код, evidence, recovery, limitations |

Темп примерный: 100 уроков могут занять 200–400 часов, плюс практика и проекты. При 10 часах в неделю верхняя граница потребует больше 24 недель. Корректируй план по выполненным артефактам.

## Аналитик → analytics/data engineer

Проверь E05–E08, даже если пишешь SQL каждый день. Затем 021–040 и 051–080. База Python и tests обязательна: E01–E04 плюс уроки 003, 006, 009, 010. Storage и platform сначала изучай на уровне решения и эксплуатации, потом углубляй выбранный стек. Рекомендуемый capstone — settlement warehouse.

## Backend-разработчик → data engineer

Начни с SQL semantics и facts: 011–030. Затем CDC, outbox, replay, Kafka и checkpoint boundaries: 031–050. В distributed systems знания HTTP и transactions не заменяют grain и финансовую аддитивность. Пройди 061–080 и сделай settlement или fraud feature capstone.

## Действующий DE → финтех

Начни с 061–070, E25–E28 и [Money correctness](MONEY_CORRECTNESS.md). Пройди бивремя 026, point-in-time 096 и publish/close 056,066. Проверь reliability 071–080 и ownership 088. Сравни с собственными assumptions о revenue, cutoff, FX и независимой полноте.

## Что обязательно, а что углубление

Обязательно: Python, SQL, grain, история, exact money, idempotency, independent reconciliation, tests, recovery, permissions. Один warehouse и один orchestrator достаточно для первого capstone.

Углубление по потребности: Data Vault, Iceberg, Spark internals, Kafka/Flink production state, Terraform, полноценный feature store, RAG service. Изучай механизм и ограничения до выбора продукта. Certification может быть дополнительным путём, но не заменяет проверяемый проект.

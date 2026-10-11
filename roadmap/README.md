# Карта обучения

100 уроков, 10 модулей. Начни с [входного гида](../docs/START_HERE.md).

## Инженерная база

- [ ] [001. Роль инженера данных и границы DWH](01-foundations/001-roles.md)
- [ ] [002. Требования, SLA и стоимость ошибки](01-foundations/002-requirements.md)
- [ ] [003. Python для надёжных пайплайнов](01-foundations/003-python.md)
- [ ] [004. Терминал, процессы и коды завершения](01-foundations/004-cli-linux.md)
- [ ] [005. Git, ревью и воспроизводимость](01-foundations/005-git.md)
- [ ] [006. Тестирование от функций до финансовых инвариантов](01-foundations/006-testing.md)
- [ ] [007. HTTP, API и пагинация](01-foundations/007-http.md)
- [ ] [008. Контейнеры и локальное окружение](01-foundations/008-containers.md)
- [ ] [009. Время, валюты и единицы измерения](01-foundations/009-time-money.md)
- [ ] [010. Распределённые системы без магии](01-foundations/010-systems.md)

## SQL и базы данных

- [ ] [011. SQL: сначала grain, потом SELECT](02-sql/011-sql-grain.md)
- [ ] [012. JOIN и размножение денежных сумм](02-sql/012-joins.md)
- [ ] [013. NULL, отсутствующие события и неизвестные значения](02-sql/013-nulls.md)
- [ ] [014. Оконные функции и детерминированный порядок](02-sql/014-windows.md)
- [ ] [015. Транзакции и атомарность batch](02-sql/015-transactions.md)
- [ ] [016. Индексы и планы запросов](02-sql/016-indexes.md)
- [ ] [017. Инкрементальные модели и границы окна](02-sql/017-incremental-sql.md)
- [ ] [018. Дедупликация и конфликтующие ключи](02-sql/018-dedup-sql.md)
- [ ] [019. SQL-проверки качества и контрольные итоги](02-sql/019-query-quality.md)
- [ ] [020. Ревью SQL и переносимость диалектов](02-sql/020-sql-review.md)

## Моделирование DWH

- [ ] [021. OLTP, DWH, lake и lakehouse](03-modeling/021-architecture.md)
- [ ] [022. Raw, staging, core и marts](03-modeling/022-layers.md)
- [ ] [023. Факты: transaction, snapshot, accumulating](03-modeling/023-facts.md)
- [ ] [024. Измерения, ключи и неизвестный участник](03-modeling/024-dimensions.md)
- [ ] [025. SCD2 и полуоткрытые интервалы](03-modeling/025-scd2.md)
- [ ] [026. Битемпоральность и «что мы знали тогда»](03-modeling/026-bitemporal.md)
- [ ] [027. Data Vault: hubs, links и satellites](03-modeling/027-data-vault.md)
- [ ] [028. Состояние сущности и история событий](03-modeling/028-entity-events.md)
- [ ] [029. Семантический слой и единые показатели](03-modeling/029-semantic.md)
- [ ] [030. Ревью модели и карта lineage](03-modeling/030-model-review.md)

## Загрузка и CDC

- [ ] [031. Batch ingestion и контроль партий](04-ingestion/031-batch-ingestion.md)
- [ ] [032. Коннекторы API и backpressure](04-ingestion/032-api-connectors.md)
- [ ] [033. Webhooks: подпись, повтор и порядок](04-ingestion/033-webhooks.md)
- [ ] [034. CDC, WAL и изменения состояния](04-ingestion/034-cdc-basics.md)
- [ ] [035. Snapshot и переход к потоку](04-ingestion/035-cdc-snapshots.md)
- [ ] [036. Deletes, tombstones и retention](04-ingestion/036-cdc-deletes.md)
- [ ] [037. Эволюция схемы и совместимость](04-ingestion/037-schema-evolution.md)
- [ ] [038. Transactional outbox и публикация событий](04-ingestion/038-outbox.md)
- [ ] [039. Replay, backfill и исправление истории](04-ingestion/039-replay.md)
- [ ] [040. Audit metadata и доказательство полноты](04-ingestion/040-ingestion-audit.md)

## Хранилища и вычисления

- [ ] [041. Колончатое хранение и Parquet](05-storage/041-columnar.md)
- [ ] [042. Партиционирование и правильный ключ](05-storage/042-partitioning.md)
- [ ] [043. Iceberg, snapshots и эволюция таблиц](05-storage/043-iceberg.md)
- [ ] [044. Облачный DWH: стоимость, роли и эксплуатация](05-storage/044-cloud-dwh.md)
- [ ] [045. Spark: partitions, shuffle и память](05-storage/045-spark.md)
- [ ] [046. Skew, broadcast и стратегии JOIN](05-storage/046-skew-joins.md)
- [ ] [047. Kafka: partitions, offsets и порядок](05-storage/047-streaming.md)
- [ ] [048. Event time, watermarks и поздние события](05-storage/048-event-time.md)
- [ ] [049. Состояние stream и checkpoint recovery](05-storage/049-state-checkpoints.md)
- [ ] [050. Выбор batch или stream без переусложнения](05-storage/050-storage-decision.md)

## Трансформации и оркестрация

- [ ] [051. dbt, зависимости моделей и контракты](06-transformation/051-dbt-basics.md)
- [ ] [052. dbt incremental, unique key и late updates](06-transformation/052-dbt-incremental.md)
- [ ] [053. Оркестрация: dependencies и data intervals](06-transformation/053-orchestration.md)
- [ ] [054. Retries, timeouts и идемпотентные задачи](06-transformation/054-retry-design.md)
- [ ] [055. Оркестрация backfill и ресурсные лимиты](06-transformation/055-backfills-dag.md)
- [ ] [056. Атомарная публикация и ready-marker](06-transformation/056-publish.md)
- [ ] [057. CI для кода, контрактов и моделей](06-transformation/057-ci-data.md)
- [ ] [058. Dev, stage и production данные](06-transformation/058-environments.md)
- [ ] [059. Миграции моделей и обратная совместимость](06-transformation/059-deployments.md)
- [ ] [060. Документация как часть эксплуатационного контракта](06-transformation/060-docs-ops.md)

## Финтех и движение денег

- [ ] [061. Жизненный цикл платежа](07-fintech/061-payment-lifecycle.md)
- [ ] [062. Двойная запись и контроль сохранения суммы](07-fintech/062-double-entry.md)
- [ ] [063. Сверка внутренних и внешних денег](07-fintech/063-reconciliation.md)
- [ ] [064. Частичные возвраты, комиссии и reversals](07-fintech/064-refunds.md)
- [ ] [065. FX, presentment и settlement currencies](07-fintech/065-fx.md)
- [ ] [066. Cutoff, закрытие дня и переиздание отчёта](07-fintech/066-cutoff-close.md)
- [ ] [067. Кредитный lifecycle и витрины задолженности](07-fintech/067-credit.md)
- [ ] [068. Антифрод, delayed labels и утечка будущего](07-fintech/068-fraud-data.md)
- [ ] [069. KYC/AML данные и происхождение решений](07-fintech/069-kyc-data.md)
- [ ] [070. Финансовый data product: приёмка](07-fintech/070-fintech-review.md)

## Качество и эксплуатация

- [ ] [071. Полнота, точность, свежесть и согласованность](08-reliability/071-quality-dimensions.md)
- [ ] [072. Свежесть и percentiles задержки](08-reliability/072-freshness.md)
- [ ] [073. Logs, metrics, traces и data lineage](08-reliability/073-observability.md)
- [ ] [074. Алерты, владельцы и бюджет ошибок](08-reliability/074-alerts.md)
- [ ] [075. Расследование инцидента и containment](08-reliability/075-incident.md)
- [ ] [076. Lineage и оценка радиуса изменения](08-reliability/076-lineage-impact.md)
- [ ] [077. Backups, RPO, RTO и проверка восстановления](08-reliability/077-backup.md)
- [ ] [078. Производительность и capacity planning](08-reliability/078-performance-ops.md)
- [ ] [079. Fault injection и проверка recovery](08-reliability/079-chaos.md)
- [ ] [080. Приёмка надёжности data product](08-reliability/080-reliability-review.md)

## Платформа и безопасность

- [ ] [081. IAM, least privilege и разделение ролей](09-platform/081-iam.md)
- [ ] [082. Минимизация персональных данных и tokenization](09-platform/082-pii.md)
- [ ] [083. Секреты, ротация и диагностика](09-platform/083-secrets.md)
- [ ] [084. Шифрование, ключи и границы доступа](09-platform/084-encryption.md)
- [ ] [085. Retention, deletion и legal hold как policy](09-platform/085-retention.md)
- [ ] [086. Infrastructure as Code и безопасное изменение](09-platform/086-iac.md)
- [ ] [087. FinOps и цена полезного результата](09-platform/087-cost.md)
- [ ] [088. Платформа как продукт и ownership](09-platform/088-ownership.md)
- [ ] [089. Access review, аудит и exports](09-platform/089-access-review.md)
- [ ] [090. Ревью платформы и план масштабирования](09-platform/090-platform-review.md)

## ИИ, ML и портфолио

- [ ] [091. ИИ как помощник инженера данных](10-ai-career/091-ai-assistant.md)
- [ ] [092. Text-to-SQL и ограниченный доступ](10-ai-career/092-text-to-sql.md)
- [ ] [093. RAG по каталогу данных и права документов](10-ai-career/093-rag.md)
- [ ] [094. Prompt injection и недоверенные документы](10-ai-career/094-prompt-injection.md)
- [ ] [095. Evals: correctness, grounding и abstention](10-ai-career/095-ai-evals.md)
- [ ] [096. Feature store и point-in-time корректность](10-ai-career/096-feature-store.md)
- [ ] [097. ML datasets, labels и версии эксперимента](10-ai-career/097-ml-pipelines.md)
- [ ] [098. Системный дизайн финтех DWH на собеседовании](10-ai-career/098-system-design.md)
- [ ] [099. Портфолио: доказательства вместо списка навыков](10-ai-career/099-portfolio.md)
- [ ] [100. Развитие проекта, сообщество и следующий шаг](10-ai-career/100-growth.md)

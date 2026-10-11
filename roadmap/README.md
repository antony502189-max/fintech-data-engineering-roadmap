# Learning roadmap

100 lessons in 10 modules. Start with the [entry guide](../docs/START_HERE.md).

## Engineering foundations

- [ ] [001. The data engineer's role and DWH boundaries](01-foundations/001-roles.md)
- [ ] [002. Requirements, SLAs, and the cost of errors](01-foundations/002-requirements.md)
- [ ] [003. Python for reliable pipelines](01-foundations/003-python.md)
- [ ] [004. Terminals, processes, and exit codes](01-foundations/004-cli-linux.md)
- [ ] [005. Git, review, and reproducibility](01-foundations/005-git.md)
- [ ] [006. Testing functions and financial invariants](01-foundations/006-testing.md)
- [ ] [007. HTTP, APIs, and pagination](01-foundations/007-http.md)
- [ ] [008. Containers and local environments](01-foundations/008-containers.md)
- [ ] [009. Time, currencies, and units](01-foundations/009-time-money.md)
- [ ] [010. Distributed systems without magic](01-foundations/010-systems.md)

## SQL and databases

- [ ] [011. SQL: grain before SELECT](02-sql/011-sql-grain.md)
- [ ] [012. JOINs and monetary fanout](02-sql/012-joins.md)
- [ ] [013. NULL, missing events, and unknown values](02-sql/013-nulls.md)
- [ ] [014. Window functions and deterministic ordering](02-sql/014-windows.md)
- [ ] [015. Transactions and batch atomicity](02-sql/015-transactions.md)
- [ ] [016. Indexes and query plans](02-sql/016-indexes.md)
- [ ] [017. Incremental models and window boundaries](02-sql/017-incremental-sql.md)
- [ ] [018. Deduplication and conflicting keys](02-sql/018-dedup-sql.md)
- [ ] [019. SQL quality checks and control totals](02-sql/019-query-quality.md)
- [ ] [020. SQL review and dialect portability](02-sql/020-sql-review.md)

## DWH modeling

- [ ] [021. OLTP, warehouses, lakes, and lakehouses](03-modeling/021-architecture.md)
- [ ] [022. Raw, staging, core, and marts](03-modeling/022-layers.md)
- [ ] [023. Transaction, periodic, and accumulating facts](03-modeling/023-facts.md)
- [ ] [024. Dimensions, keys, and unknown members](03-modeling/024-dimensions.md)
- [ ] [025. SCD2 and half-open intervals](03-modeling/025-scd2.md)
- [ ] [026. Bitemporal data and past knowledge](03-modeling/026-bitemporal.md)
- [ ] [027. Data Vault: hubs, links, and satellites](03-modeling/027-data-vault.md)
- [ ] [028. Entity state and event history](03-modeling/028-entity-events.md)
- [ ] [029. Semantic layers and shared metrics](03-modeling/029-semantic.md)
- [ ] [030. Model review and lineage](03-modeling/030-model-review.md)

## Ingestion and CDC

- [ ] [031. Batch ingestion and batch controls](04-ingestion/031-batch-ingestion.md)
- [ ] [032. API connectors and backpressure](04-ingestion/032-api-connectors.md)
- [ ] [033. Webhooks: signatures, repeats, and ordering](04-ingestion/033-webhooks.md)
- [ ] [034. CDC, WAL, and state changes](04-ingestion/034-cdc-basics.md)
- [ ] [035. Snapshots and the handoff to streaming](04-ingestion/035-cdc-snapshots.md)
- [ ] [036. Deletes, tombstones, and retention](04-ingestion/036-cdc-deletes.md)
- [ ] [037. Schema evolution and compatibility](04-ingestion/037-schema-evolution.md)
- [ ] [038. Transactional outbox](04-ingestion/038-outbox.md)
- [ ] [039. Replay, backfill, and historical corrections](04-ingestion/039-replay.md)
- [ ] [040. Audit metadata and completeness evidence](04-ingestion/040-ingestion-audit.md)

## Storage and processing

- [ ] [041. Columnar storage and Parquet](05-storage/041-columnar.md)
- [ ] [042. Partitioning and key selection](05-storage/042-partitioning.md)
- [ ] [043. Iceberg snapshots and table evolution](05-storage/043-iceberg.md)
- [ ] [044. Managed warehouses: cost, roles, and operation](05-storage/044-cloud-dwh.md)
- [ ] [045. Spark partitions, shuffle, and memory](05-storage/045-spark.md)
- [ ] [046. Skew, broadcast, and join strategies](05-storage/046-skew-joins.md)
- [ ] [047. Kafka partitions, offsets, and ordering](05-storage/047-streaming.md)
- [ ] [048. Event time, watermarks, and late data](05-storage/048-event-time.md)
- [ ] [049. Stream state and checkpoint recovery](05-storage/049-state-checkpoints.md)
- [ ] [050. Choosing batch or streaming](05-storage/050-storage-decision.md)

## Transformations and orchestration

- [ ] [051. dbt models, dependencies, and contracts](06-transformation/051-dbt-basics.md)
- [ ] [052. dbt incremental models and late updates](06-transformation/052-dbt-incremental.md)
- [ ] [053. Orchestration dependencies and data intervals](06-transformation/053-orchestration.md)
- [ ] [054. Retries, timeouts, and idempotent tasks](06-transformation/054-retry-design.md)
- [ ] [055. Backfill orchestration and resource limits](06-transformation/055-backfills-dag.md)
- [ ] [056. Atomic publication and readiness markers](06-transformation/056-publish.md)
- [ ] [057. CI for code, contracts, and models](06-transformation/057-ci-data.md)
- [ ] [058. Development, staging, and production](06-transformation/058-environments.md)
- [ ] [059. Model migrations and compatibility](06-transformation/059-deployments.md)
- [ ] [060. Documentation as an operational contract](06-transformation/060-docs-ops.md)

## Financial data and money movement

- [ ] [061. The payment lifecycle](07-fintech/061-payment-lifecycle.md)
- [ ] [062. Double entry and conservation checks](07-fintech/062-double-entry.md)
- [ ] [063. Internal and external reconciliation](07-fintech/063-reconciliation.md)
- [ ] [064. Partial refunds, fees, and reversals](07-fintech/064-refunds.md)
- [ ] [065. FX, presentment, and settlement currencies](07-fintech/065-fx.md)
- [ ] [066. Cutoffs, daily close, and restatement](07-fintech/066-cutoff-close.md)
- [ ] [067. Credit lifecycles and debt marts](07-fintech/067-credit.md)
- [ ] [068. Fraud data, delayed labels, and leakage](07-fintech/068-fraud-data.md)
- [ ] [069. KYC/AML provenance and protected data](07-fintech/069-kyc-data.md)
- [ ] [070. Financial data-product acceptance](07-fintech/070-fintech-review.md)

## Quality and reliability

- [ ] [071. Completeness, accuracy, freshness, and consistency](08-reliability/071-quality-dimensions.md)
- [ ] [072. Freshness and latency percentiles](08-reliability/072-freshness.md)
- [ ] [073. Logs, metrics, traces, and lineage](08-reliability/073-observability.md)
- [ ] [074. Alerts, owners, and error budgets](08-reliability/074-alerts.md)
- [ ] [075. Incident investigation and containment](08-reliability/075-incident.md)
- [ ] [076. Lineage and change impact](08-reliability/076-lineage-impact.md)
- [ ] [077. Backups, RPO, RTO, and restore drills](08-reliability/077-backup.md)
- [ ] [078. Performance and capacity planning](08-reliability/078-performance-ops.md)
- [ ] [079. Fault injection and recovery verification](08-reliability/079-chaos.md)
- [ ] [080. Data-product reliability acceptance](08-reliability/080-reliability-review.md)

## Platform and security

- [ ] [081. IAM, least privilege, and separated roles](09-platform/081-iam.md)
- [ ] [082. Personal-data minimization and tokenization](09-platform/082-pii.md)
- [ ] [083. Secrets, rotation, and diagnostics](09-platform/083-secrets.md)
- [ ] [084. Encryption, keys, and access boundaries](09-platform/084-encryption.md)
- [ ] [085. Retention, deletion, and holds](09-platform/085-retention.md)
- [ ] [086. Infrastructure as Code and safe changes](09-platform/086-iac.md)
- [ ] [087. FinOps and cost per useful result](09-platform/087-cost.md)
- [ ] [088. Platform as a product and ownership](09-platform/088-ownership.md)
- [ ] [089. Access review, audit, and exports](09-platform/089-access-review.md)
- [ ] [090. Platform review and scaling plans](09-platform/090-platform-review.md)

## AI, ML and portfolio

- [ ] [091. AI as a data-engineering assistant](10-ai-career/091-ai-assistant.md)
- [ ] [092. Text-to-SQL and constrained access](10-ai-career/092-text-to-sql.md)
- [ ] [093. RAG over the data catalog and document permissions](10-ai-career/093-rag.md)
- [ ] [094. Prompt injection and untrusted documents](10-ai-career/094-prompt-injection.md)
- [ ] [095. AI evals: correctness, grounding, and abstention](10-ai-career/095-ai-evals.md)
- [ ] [096. Feature stores and point-in-time correctness](10-ai-career/096-feature-store.md)
- [ ] [097. ML datasets, labels, and experiment versions](10-ai-career/097-ml-pipelines.md)
- [ ] [098. Fintech DWH system-design interviews](10-ai-career/098-system-design.md)
- [ ] [099. Portfolio evidence instead of skill lists](10-ai-career/099-portfolio.md)
- [ ] [100. Project growth, community, and next steps](10-ai-career/100-growth.md)

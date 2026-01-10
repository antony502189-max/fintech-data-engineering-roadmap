# Следующий уровень: настоящие инструменты

Основные 40 exercises offline и проверены на standard-library runtime. Ниже **specifications для самостоятельных integrations**, а не уже протестированная полная platform. Указывай реальные installed versions и запускай meaningful checks; не называй sketch работающим сервисом.

## PostgreSQL

Создай локальную database по [официальной инструкции](https://www.postgresql.org/docs/current/tutorial.html). Портируй schema: денежные amounts BIGINT или согласованный NUMERIC, timestamps TIMESTAMPTZ, PK event_id. Повтори ingestion/rollback fixtures, проверь concurrent duplicate writers и isolation. Acceptance: при двух workers один ID создаёт ровно одну пару postings, conflict виден; full/incremental totals совпадают. Сохрани команды создания учебной базы и cleanup отдельно от production.

## dbt

Выбери поддерживаемую пару dbt Core/adapter и warehouse. Создай sources/raw_events, staging, fact_events и daily_cash. Используй references, unique/not_null tests и custom balance/completeness query. Добавь late input, run incremental, full refresh в другом namespace и сравни наборы. Acceptance: identical outputs и blocked publish при failed tests. [Data tests docs](https://docs.getdbt.com/docs/build/data-tests).

## Kafka + Debezium

По официальным setup instructions подними локальный PostgreSQL source и совместимые Kafka/Connect/Debezium versions. Зафиксируй configuration без secrets. Создай snapshot, update, delete и source restart; сохраняй source position и op. Acceptance: snapshot→stream не имеет gaps, delete меняет current projection, domain capture не создаётся из каждого technical update. Consumer crash после sink commit должен приводить к replay без удвоения. [Debezium](https://debezium.io/documentation/reference/stable/connectors/postgresql.html), [Kafka](https://kafka.apache.org/documentation/).

## Spark + Parquet

Сгенерируй большой deterministic dataset, укажи Spark/Java/library versions. Измерь CSV/Parquet projection, partition pruning, hot-key group by и join dimension. Сохраняй physical plans, scanned/shuffle bytes, peak task duration и repeated timings. Acceptance: ускорение подтверждено на declared workload, financial total одинаков, driver collect большого набора не используется. [Spark tuning](https://spark.apache.org/docs/latest/sql-performance-tuning.html).

## Airflow или другой orchestrator

Подними выбранную поддерживаемую версию по docs. DAG: ingestion → quality → transforms → reconciliation → candidate publish. Передавай data interval; wall clock не определяет backfill period. Acceptance: retries и restart безопасны, missing batch blocks final, canary backfill не вытесняет daily workload. [Airflow best practices](https://airflow.apache.org/docs/apache-airflow/stable/best-practices.html).

## Iceberg и object storage

Выбери совместимые catalog и engines; зафиксируй table format version. Напиши raw→candidate→snapshot publish, late partition rewrite и snapshot retention experiment. Acceptance: читатель видит целостный old/new snapshot и documented time-travel boundary. Maintenance не выполняется ручным удалением неизвестных files. [Iceberg docs](https://iceberg.apache.org/docs/latest/).

## Облако и IaC

Cloud exercise начинается с budget, отдельного учебного namespace и scoped identity. Актуальные цены и правила региона проверь в primary provider docs. Покажи IaC plan, denied access cases, query budget и resource inventory; не публикуй state или credentials. Удаление ресурсов не восстанавливает их данные; cleanup выполняй только для своих явно идентифицированных учебных resources.

## Реальная LLM

Сначала сохрани offline eval baseline. Затем подключи модель только к synthetic docs, ограничь tools и budget. Acceptance: ACL before retrieval, citations only from actual context, unknown metric abstention, critical failures отдельно от average. Реальный Text-to-SQL требует AST enforcement и scoped database identity; простой Python filter из упражнений его не реализует.

# Next level: real tools

Core exercises are verified offline standard-library implementations. These are independent integration specifications, not a prevalidated full platform. Record installed versions, execute meaningful checks, and separate proposals from working services.

## PostgreSQL

Create a local database using [official instructions](https://www.postgresql.org/docs/current/tutorial.html). Port monetary fields to BIGINT or an agreed NUMERIC scale, timestamps to TIMESTAMPTZ, and event identity to a primary key. Repeat rollback tests and concurrent duplicate writes. Require one journal pair per accepted ID and explicit conflicts. Compare full/incremental totals. Keep teaching-database creation and cleanup separate from production.

## dbt

Select a supported Core/adapter pair. Define raw sources, staging, event facts, and daily cash. Add references, uniqueness/null tests, and custom conservation/completeness tests. Run incremental after late data and compare with full refresh in another namespace. Require equal results and blocked publication on failure. [Data tests](https://docs.getdbt.com/docs/build/data-tests).

## Kafka and Debezium

Use compatible local PostgreSQL, Kafka, Connect, and Debezium versions. Retain configuration without secrets. Exercise snapshot, update, delete, and restart with source positions. Require no snapshot-to-stream gaps, correct current-state deletion, and no fictitious capture from technical updates. Crash after sink commit and confirm replay does not double money. [Debezium](https://debezium.io/documentation/reference/stable/connectors/postgresql.html), [Kafka](https://kafka.apache.org/documentation/).

## Spark and Parquet

Generate larger deterministic data and record Spark/Java/library versions. Compare projections, pruning, hot-key aggregation, and joins. Retain plans, scanned and shuffled bytes, task durations, and repeated timings. Require identical financial totals and avoid large driver collection. [Performance documentation](https://spark.apache.org/docs/latest/sql-performance-tuning.html).

## Orchestration

Build ingestion → quality → transformation → reconciliation → candidate publication. Pass data intervals explicitly. Require safe retries, missing-input blocks, and canary backfill that respects daily workloads. [Airflow best practices](https://airflow.apache.org/docs/apache-airflow/stable/best-practices.html).

## Iceberg

Choose compatible catalogs and engines and pin table format. Test candidate/snapshot publication, late partition updates, and retention. Readers must see complete versions; document time-travel limits. Never maintain tables by manually deleting unidentified files. [Iceberg](https://iceberg.apache.org/docs/latest/).

## Cloud and IaC

Begin with a budget, separate teaching namespace, and scoped identity. Verify current prices and regional requirements in provider documentation. Review plans, denied-access cases, query limits, and resource inventory. Keep state and credentials outside Git. Deleting infrastructure does not restore its data; cleanup must target only identified teaching resources.

## A real LLM

Retain an offline evaluation baseline before integration. Use synthetic documents, constrained tools, and cost limits. Require ACLs before context, valid citations, abstention for unknown metrics, and separate critical-failure scoring. Real Text-to-SQL needs AST enforcement and database identity constraints; exercise filters do not implement them.

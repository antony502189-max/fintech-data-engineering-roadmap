# Первичная документация

Ссылки на официальные starting points. Многие ведут на current/stable/latest: для проекта фиксируй конкретную installed version и проверяй её документацию. Наличие ссылки не означает полного чтения всего продукта.

| Источник | Для чего |
|---|---|
| [Python Tutorial](https://docs.python.org/3.12/tutorial/) | Язык, исключения, generators, typing и стандартная библиотека |
| [Python sqlite3](https://docs.python.org/3.12/library/sqlite3.html) | Transactions, parameter binding, backup API и локальный runtime |
| [PostgreSQL documentation](https://www.postgresql.org/docs/current/) | SQL, isolation, indexes, WAL и PostgreSQL extensions |
| [Kimball dimensional modeling techniques](https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/) | Facts, dimensions, SCD, аддитивность и modeling vocabulary |
| [Stripe balance transaction types](https://docs.stripe.com/reports/balance-transaction-types) | Различия денежных event types и границы provider semantics |
| [Stripe webhook delivery](https://docs.stripe.com/webhooks) | Delivery, signature, retries и порядок событий |
| [Stripe idempotent requests](https://docs.stripe.com/api/idempotent_requests) | Повтор API операции и область idempotency key |
| [Debezium PostgreSQL connector](https://debezium.io/documentation/reference/stable/connectors/postgresql.html) | Snapshot, source position, update/delete и connector configuration |
| [Apache Kafka documentation](https://kafka.apache.org/documentation/) | Partition order, offsets и transactional semantics |
| [Flink event time](https://nightlies.apache.org/flink/flink-docs-stable/docs/concepts/time/) | Event time, watermarks и late data |
| [Apache Iceberg documentation](https://iceberg.apache.org/docs/latest/) | Snapshots, catalog, schema/partition evolution и maintenance |
| [Spark SQL performance tuning](https://spark.apache.org/docs/latest/sql-performance-tuning.html) | Physical plans, shuffle, joins и performance experiments |
| [dbt data tests](https://docs.getdbt.com/docs/build/data-tests) | Generic/custom data tests; дальше выбирай adapter docs своей версии |
| [Airflow best practices](https://airflow.apache.org/docs/apache-airflow/stable/best-practices.html) | Idempotent tasks, parsing cost и reproducible scheduling |
| [Feast point in time joins](https://docs.feast.dev/getting-started/concepts/point-in-time-joins) | Historical feature retrieval и temporal joins |
| [Pro Git book](https://git-scm.com/book/en/v2) | Коммиты, ветки, review и reproducibility |
| [Docker documentation](https://docs.docker.com/get-started/) | Images, volumes и local containers |
| [AWS Well Architected](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html) | Workload architecture, reliability, security и cost questions |
| [BigQuery documentation](https://cloud.google.com/bigquery/docs) | Warehouse semantics, access и scan/budget controls |
| [Snowflake documentation](https://docs.snowflake.com/en/) | Warehouse configuration, roles и platform semantics |
| [Terraform documentation](https://developer.hashicorp.com/terraform/docs) | Providers, state, plan и lifecycle |
| [OWASP LLM applications project](https://owasp.org/www-project-top-10-for-large-language-model-applications/) | LLM-specific threat categories и guardrails |
| [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) | AI risk framing, evaluation и governance |
| [OpenTelemetry concepts](https://opentelemetry.io/docs/concepts/) | Logs/metrics/traces и instrumentation vocabulary |

## Нормативные и security источники

[PCI SSC document library](https://www.pcisecuritystandards.org/document_library/) — официальный вход к применимым документам. Учебный roadmap не определяет scope организации, сроки retention или её compliance status; эти решения задаёт уполномоченный владелец политики.

## Книги для углубления

[Designing Data-Intensive Applications](https://dataintensive.net/) — distributed systems и data architecture; [Fundamentals of Data Engineering](https://www.oreilly.com/library/view/fundamentals-of-data/9781098108298/) — lifecycle data engineering. Это внешние книги, доступ может быть платным; основной lab и упражнения от них не зависят. Перед покупкой проверь редакцию и содержание у издателя.

Для чтения engineering cases открой [статьи](ARTICLES.md), для YouTube — [видео](VIDEOS.md).

# Glossary

| Term | Meaning |
|---|---|
| Grain | What one row represents |
| Fact | Measurable event or state |
| Dimension | Context for describing and filtering facts |
| CDC | Changes obtained from a database log or another change mechanism |
| WAL | Write-ahead log; not automatically a business event log |
| Idempotency | Repeating an operation has no extra effect beyond the first application |
| Deduplication | Removing repeats under a defined identity policy |
| Outbox | Publication intent committed with the business transaction |
| Watermark | Estimated stream-time progress, not completeness evidence |
| Backfill | Filling or recomputing historical scope |
| Replay | Processing retained input again |
| SCD2 | Attribute versions over valid intervals |
| Bitemporal | Business time and system knowledge time |
| Minor unit | Decimal unit determined by a currency exponent |
| Ledger | Posting journal with explicit perspective and accounts |
| Reconciliation | Comparison of independent monetary representations |
| Cutoff | Business-period or input-receipt boundary |
| Restatement | A newly versioned previous result |
| SLI / SLO / SLA | Measurement / target / external commitment |
| RPO / RTO | Acceptable time-based loss / target restoration time |
| Lineage | Origins and transformation paths |
| Point-in-time join | Joining under temporal availability constraints |
| Leakage | Using information unavailable at decision time |
| RAG | Retrieval of documents for model answers |
| Abstention | Refusing to invent unsupported answers |
| FinOps | Managing cloud workload costs |
| ADR | Architectural decision and its reasoning |

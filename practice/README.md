# Practice: 40 ready-to-solve exercises

Four exercises per module. All run locally without network access, API keys, or paid cloud services. SQL exercises execute real SQLite queries; platform and AI exercises use offline simulations.

```bash
python practice/run.py init E01
python practice/run.py grade E01
python practice/run.py reference E01
python practice/run.py verify
```

`grade` checks your answer, `reference` runs the reference, and `verify` validates all references. Passing `verify` does not mean you have solved the exercises.

## Engineering foundations

- [ ] [E01. Exact money](E01.md)
- [ ] [E02. UTC business date](E02.md)
- [ ] [E03. Boundary contract](E03.md)
- [ ] [E04. Completeness manifest](E04.md)

## SQL and databases

- [ ] [E05. SQL: events and payments](E05.md)
- [ ] [E06. SQL: net cash by currency](E06.md)
- [ ] [E07. SQL: latest version](E07.md)
- [ ] [E08. SQL: uniqueness violations](E08.md)

## DWH modeling

- [ ] [E09. SCD2 boundary lookup](E09.md)
- [ ] [E10. Flow and closing balance](E10.md)
- [ ] [E11. Unknown dimension member](E11.md)
- [ ] [E12. Business time and knowledge time](E12.md)

## Ingestion and CDC

- [ ] [E13. Duplicates and identity conflicts](E13.md)
- [ ] [E14. CDC current projection](E14.md)
- [ ] [E15. Complete pagination](E15.md)
- [ ] [E16. Amount-schema migration](E16.md)

## Storage and processing

- [ ] [E17. Partition pruning](E17.md)
- [ ] [E18. Small-file packing](E18.md)
- [ ] [E19. Hot keys and skew](E19.md)
- [ ] [E20. Watermarks and late output](E20.md)

## Transformations and orchestration

- [ ] [E21. DAG ordering and cycles](E21.md)
- [ ] [E22. Retry policy](E22.md)
- [ ] [E23. Affected incremental days](E23.md)
- [ ] [E24. Publication gate](E24.md)

## Financial data and money movement

- [ ] [E25. Posting balance](E25.md)
- [ ] [E26. Full reconciliation](E26.md)
- [ ] [E27. FX with explicit scale](E27.md)
- [ ] [E28. Loan-payment allocation](E28.md)

## Quality and reliability

- [ ] [E29. P95 latency](E29.md)
- [ ] [E30. Incident impact](E30.md)
- [ ] [E31. Quality with incomplete input](E31.md)
- [ ] [E32. Backup restoration and replay](E32.md)

## Platform and security

- [ ] [E33. RBAC: deny by default](E33.md)
- [ ] [E34. Personal-data allowlist](E34.md)
- [ ] [E35. Scenario cost](E35.md)
- [ ] [E36. Retention and holds](E36.md)

## AI, ML and portfolio

- [ ] [E37. Point-in-time feature](E37.md)
- [ ] [E38. AI evaluation scorecard](E38.md)
- [ ] [E39. RAG access filtering](E39.md)
- [ ] [E40. Capstone report contract](E40.md)

After the exercises, complete the [eight scenario labs](../challenges/README.md), then build a [capstone project](../projects/README.md).

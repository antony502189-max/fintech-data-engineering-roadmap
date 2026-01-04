# Fintech Data Engineering Roadmap

**100 focused lessons, 40 graded exercises, and a runnable synthetic payments warehouse.**

[Russian guide](README.md) · [Curriculum](roadmap/README.md) · [Exercises](practice/README.md) · [Videos](resources/VIDEOS.md) · [Architecture](docs/ARCHITECTURE.md)

Learn the engineering behind trustworthy financial data: SQL grain, dimensional modeling, CDC, idempotency, late arrivals, exact money, double-entry checks, reconciliation, operations, access control, and AI/ML data workflows. The detailed lessons are currently in Russian; code, identifiers and command examples are accessible independently. English translations are welcome.

## Run locally

Python 3.12+ with SQLite support; no third-party runtime dependencies, cloud subscription, or API keys.

```bash
git clone https://github.com/antony502189-max/fintech-data-engineering-roadmap.git
cd fintech-data-engineering-roadmap
python -m fintech_lab --out work/demo
python -m unittest discover -s tests -v
python practice/run.py init E01
python practice/run.py grade E01
```

Edit `work/answers/E01.py` before grading: the starter intentionally raises `NotImplementedError`. Each exercise provides a task, input contract, examples, hints and a reference solution. `python practice/run.py verify` validates references; it does not grade your personal progress.

The lab demonstrates six events, duplicate-safe replay, exact currency totals, a deliberate reconciliation mismatch, SCD2 boundary handling, and a feature that excludes data unavailable at the decision time. Everything is synthetic.

## Ten modules

Foundations → SQL → DWH modeling → ingestion and CDC → storage and processing → transformations and orchestration → financial data → reliability → platform and security → AI and portfolio.

Use the [learning paths](docs/LEARNING_PATHS.md), complete the 40 exercises and choose a [capstone](projects/README.md). Official documentation, YouTube courses and engineering articles are indexed with relevance and caveats in [resources](resources/README.md).

## Scope

This is an educational implementation. Kafka, cloud IAM, streaming and AI exercises are offline simulations, with additional stack practice documented separately. The signed journal is a simplified accounting model; successful balancing alone does not prove correct financial reporting. The project does not claim production readiness or regulatory certification.

The first edition was authored with AI assistance. Commit timestamps are real; section-sized commits document construction of the first edition, not years of development. See [provenance](docs/PROVENANCE.md).

Contributions: reproducible bugs, meaningful edge cases, resource updates and translations. See [CONTRIBUTING](CONTRIBUTING.md). Star the repository if it helps you learn or teach. MIT license; external resources retain their own licenses.

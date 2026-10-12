# YouTube: watch, then build

Resources are in English. CMU links come from its [official Fall 2024 schedule](https://15445.courses.cs.cmu.edu/fall2024/schedule.html); the Zoomcamp playlist comes from the [authors' README](https://github.com/DataTalksClub/data-engineering-zoomcamp). Playback may vary by region and was not checked in full.

| Resource and author | Focus | Practice afterward |
|---|---|---|
| [Data Engineering Zoomcamp playlist](https://www.youtube.com/playlist?list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb), DataTalks.Club | Ingestion, warehouses, transformations, batch, streaming | Build a small pipeline and compare with the synthetic lab |
| [Modern SQL](https://www.youtube.com/watch?v=MzigBKf84aY), CMU, 2024 | Relational query semantics | E05–E08 and event grain |
| [Storage Models & Compression](https://www.youtube.com/watch?v=nhlpwmOBEiE), CMU, 2024 | Row/column layouts and reading cost | E17–E18 and a format benchmark |
| [Indexes & Filters I](https://www.youtube.com/watch?v=scUtG_6M_lU), CMU, 2024 | Indexes and access paths | Lesson 016 with larger synthetic data |
| [Join Algorithms](https://www.youtube.com/watch?v=MFazkaZKs1s), CMU, 2024 | Physical join cost | Lesson 012; separate fanout from performance |
| [Concurrency Control Theory](https://www.youtube.com/watch?v=4y656idl8ZU), CMU, 2024 | Isolation and concurrency | Lesson 015 rollback and crash matrix |
| [Database Logging](https://www.youtube.com/watch?v=mbelzgz-97s), CMU, 2024 | Logs and durability | Lessons 034–035 snapshot/stream boundaries |
| [Database Recovery](https://www.youtube.com/watch?v=yVpzHdAP0TY), CMU, 2024 | Recovery mechanisms | E32 and SQLite backup drill |
| [Distributed OLAP Database Systems](https://www.youtube.com/watch?v=L6E75IyBgpk), CMU, 2024 | Analytical distribution | Batch/stream ADR with costs |
| [Ask Confluent #6: Kafka, Partitions, and Exactly Once](https://www.youtube.com/watch?v=CeDivZQvdcs), Confluent, 2018 | Ordering and guarantee scope | Lessons 047–049 sink/offset crash matrix; verify current settings |
| [Exactly-Once Semantics preview](https://www.youtube.com/watch?v=JPcT1GGzszA), Matthias Sax / Confluent, 2018 | Historical transaction introduction | A preview, not a full course; explain external-sink protocols |

## Pairing Zoomcamp with this roadmap

Use Zoomcamp for real tools and independent projects; this roadmap emphasizes money, history, reconciliation, and failure behavior. The [official repository](https://github.com/DataTalksClub/data-engineering-zoomcamp) contains modules and homework. Tools and folders vary by cohort; do not assume old videos describe current commands.

After warehouse material, study [dbt tests](https://docs.getdbt.com/docs/build/data-tests) and E21–E24. Solve E37 before feature-store reading. Build negative cases in E38–E39 before deeper AI systems: introductory videos cannot substitute for access and financial checks.

## One artifact per video

Retain a query, fixture, ADR, or failing test after each resource. Explain what you checked and what remains assumed. Watching hours alone is not a mastery criterion.

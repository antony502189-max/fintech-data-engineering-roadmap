# YouTube: смотри и сразу проверяй руками

Все материалы ниже — EN. Links CMU получены из [официального расписания Fall 2024](https://15445.courses.cs.cmu.edu/fall2024/schedule.html), DE Zoomcamp playlist — из [README авторов](https://github.com/DataTalksClub/data-engineering-zoomcamp). Доступность playback может зависеть от региона; это не заявление полного просмотра.

| Материал и автор | Что разбирать | После просмотра |
|---|---|---|
| [Data Engineering Zoomcamp — playlist](https://www.youtube.com/playlist?list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb), DataTalks.Club | End-to-end ingestion, warehouse, transformations, batch, streaming | Выбери один блок, сделай собственный mini pipeline и сравни с нашей synthetic lab |
| [Modern SQL](https://www.youtube.com/watch?v=MzigBKf84aY), CMU Database Group, 2024 | Реляционные запросы и SQL semantics | E05–E08; объясни event grain |
| [Storage Models & Compression](https://www.youtube.com/watch?v=nhlpwmOBEiE), CMU Database Group, 2024 | Row/column layouts и стоимость чтения | E17–E18; подготовь file-format benchmark |
| [Indexes & Filters I](https://www.youtube.com/watch?v=scUtG_6M_lU), CMU Database Group, 2024 | Индексные структуры и доступ | Урок 016: измерь EXPLAIN и время на большой синтетике |
| [Join Algorithms](https://www.youtube.com/watch?v=MFazkaZKs1s), CMU Database Group, 2024 | Физическая стоимость соединения | Урок 012: воспроизведи fanout и отличи semantic error от performance issue |
| [Concurrency Control Theory](https://www.youtube.com/watch?v=4y656idl8ZU), CMU Database Group, 2024 | Конкуренция и isolation | Урок 015: crash matrix и rollback |
| [Database Logging](https://www.youtube.com/watch?v=mbelzgz-97s), CMU Database Group, 2024 | Журнал изменений и durability | Уроки 034–035: объясни snapshot→stream boundary |
| [Database Recovery](https://www.youtube.com/watch?v=yVpzHdAP0TY), CMU Database Group, 2024 | Восстановление состояния | E32 плюс SQLite backup drill |
| [Distributed OLAP Database Systems](https://www.youtube.com/watch?v=L6E75IyBgpk), CMU Database Group, 2024 | Аналитические workloads в распределённой системе | Напиши ADR batch/stream и budget assumptions |
| [Ask Confluent #6: Kafka, Partitions, and Exactly Once](https://www.youtube.com/watch?v=CeDivZQvdcs), Confluent, 2018 | Порядок partitions и область гарантий | Уроки 047–049: sink/offset crash matrix; настройки сверяй с нынешними Kafka docs |
| [Exactly-Once Semantics — preview](https://www.youtube.com/watch?v=JPcT1GGzszA), Matthias Sax / Confluent, 2018 | Историческое введение в transactional processing | Короткий preview, не полный курс; объясни, почему внешний sink требует своего protocol |

## Как проходить DE Zoomcamp вместе с этим roadmap

Используй Zoomcamp для настоящего tool stack и самостоятельного project; наш маршрут — для финансовых инвариантов, истории, сверки и failure drills. В [официальном repository](https://github.com/DataTalksClub/data-engineering-zoomcamp) есть modules и homework. Названия tools и структуры меняются между cohorts; не привязывай все нынешние команды к старому playlist.

Для dbt после warehouse блока возьми [официальные data tests docs](https://docs.getdbt.com/docs/build/data-tests) и E21–E24. Для ML point-in-time сначала реши E37, затем читай Feast. Для AI safety сначала создай negative cases E38–E39; видео общего знакомства с LLM не заменяет проверку доступа и финансовой формулы.

## Правило одного артефакта

После каждого видео оставляй query, fixture, ADR или failing test. В README своей работы укажи тему, ссылку, что проверил и какие assumptions остались. «Посмотрел 10 часов» не является критерием освоения.

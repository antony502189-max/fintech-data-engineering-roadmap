# Проверка первого издания

Дата local run: 2026-10-12. Среда: Windows, CPython 3.14.3, стандартная библиотека; network не нужен для учебного кода.

| Проверка | Результат |
|---|---|
| `python -m unittest discover -s tests -v` | 44 tests passed |
| `python practice/run.py verify` | 40 references, 90 cases passed |
| `python scripts/check_sql.py` | Valid, imbalanced и полностью missing journal cases passed |
| `python scripts/check_docs.py` | 177 Markdown files, 100 lessons, local paths и SQL solution pairs checked до добавления этого отчёта |
| `python -m fintech_lab --out work/verified-demo` | Expected currency totals, duplicate-safe replay, deliberate mismatch/unexpected cases |
| История первого издания до этого отчёта | 1089 commits; 0 commits с деревом, идентичным parent |

Roadmap содержит 26559 слов по простой whitespace оценке, 100 уроков по 244–287 слов с навигацией и reading lists. Это структурированные focused lessons; глубокая практика дополняется упражнениями, guides и capstone.

## Что ловят meaningful checks

Float, nonfinite и чрезмерная precision денег; длинные Decimal strings и крайние exponents; duplicate delivery и payload collision; rollback новых событий batch; missing/extra schema fields; naive timestamps и normalization offset; unbalanced и полностью потерянные postings; mixed currencies; mismatch/missing/unexpected settlement; SCD2 exact boundary и late change; feature leakage по received_at; unfinished starter и bool вместо integer answer.

## Remote и непроверенные свойства

Remote matrix настроена для Windows/Ubuntu, Python 3.12/3.14. Её фактический результат находится в [GitHub Actions](https://github.com/antony502189-max/fintech-data-engineering-roadmap/actions). Этот local отчёт не подменяет remote status.

Не проверены настоящие Kafka/CDC/Spark/cloud/LLM integrations, производственная нагрузка, регуляторный scope и реальное бухгалтерское закрытие. Exercises моделируют часть принципов; [расширения](../labs/STACK_EXTENSIONS.md) задают следующий уровень. External YouTube playback не проверен, ссылки атрибутированы официальным course pages и авторами.

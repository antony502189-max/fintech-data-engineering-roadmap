# Verification evidence

Baseline local environment: Windows, CPython 3.14.3, standard library, October 12, 2026. Learning code does not need network access.

| Check | Baseline result |
|---|---|
| `python -m unittest discover -s tests -v` | 44 tests passed |
| `python practice/run.py verify` | Forty references and ninety cases passed |
| `python scripts/check_sql.py` | Valid, imbalanced, and wholly missing journals verified |
| `python scripts/check_docs.py` | One hundred lessons, local paths, and solution pairs checked |
| `python -m fintech_lab --out work/verified-demo` | Expected totals, safe replay, and intentional reconciliation exceptions |
| Initial construction history | 1089 commits before its validation report; zero unchanged-tree commits |

Version 1.1.0 additionally runs `python scripts/check_english.py` across tracked and unignored text. It rejects Cyrillic characters; manual review supplies the English translation itself. Identifiers, fixtures, expected outputs, and executable reference behavior are preserved.

Version 1.2.0 adds `python challenges/run.py verify`: eight references and 28 independently authored scenario cases. The unit suite now has 48 tests, including a real backup reference, retained source evidence after schema rejection, and negative checks for unfinished workflows and runnable defective SQL. These scenarios verify the supplied learning contracts, not every possible input or a distributed production system.

## Meaningful checks

Money tests reject floats, nonfinite values, excess precision, long near-cent values, and extreme exponents. Ingestion tests cover duplicates, collisions, rollback, schema errors, naive timestamps, and equivalent offsets. Financial checks cover imbalance, missing journals, currencies, and reconciliation classifications. History tests cover boundaries and late changes. Feature tests constrain receipt-time knowledge. CLI tests reject unfinished starters and booleans pretending to be integer answers.

## Remote evidence and untested properties

[GitHub Actions](https://github.com/antony502189-max/fintech-data-engineering-roadmap/actions) reports actual Windows/Ubuntu and Python 3.12/3.14 matrix results. The initial publication passed all four combinations; subsequent versions have their own runs.

Real Kafka, CDC, Spark, cloud, and LLM integrations, production load, regulatory scope, and financial close are outside the verified baseline. [Stack extensions](../labs/STACK_EXTENSIONS.md) define further work. YouTube playback has not been checked; links are attributed to course pages and authors.

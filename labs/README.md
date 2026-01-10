# Рабочая payments lab

```bash
python -m fintech_lab --out work/lab-first-run
python -m unittest discover -s tests -v
```

Demo сохраняет SQLite database и JSON report. Для нового baseline используй новый output directory. Повтор в ту же базу намеренно даёт duplicates. По [dictionary](../docs/DATA_DICTIONARY.md) проследи p1, p2, p3 и p9, затем сравни их с [денежным разбором](../docs/MONEY_CORRECTNESS.md).

## Что можно делать руками

- Добавить late event и посмотреть изменение старого event day.
- Повторить event с новым received_at и убедиться, что сумма прежняя.
- Изменить amount существующего ID и увидеть rollback.
- Удалить одну posting и получить failed invariant.
- Вставить late SCD2 change и проверить boundary.
- Изменить external statement и сравнить mismatch/missing/unexpected.
- Проверить ML feature до и после knowledge time.

Чтобы провести опыт, используй короткий Python script в `work/`, импортируй функции из `fintech_lab` и отдельную temporary database. Не меняй публичные эталонные fixtures ради прохождения checks.

[Fault drills](fault-drills.md) дают конкретные snippets. [40 заданий](../practice/README.md) предлагают starters и grading. [Stack extensions](STACK_EXTENSIONS.md) связывают освоенные инварианты с настоящими инструментами.

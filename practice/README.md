# Практикум: 40 готовых заданий

Четыре задания на каждый модуль. Все стартуют локально без network, API key и платного cloud. Реальные SQL выполняется в SQLite; платформенные и ИИ-принципы проверяются offline симуляциями.

```bash
python practice/run.py init E01
python practice/run.py grade E01
python practice/run.py reference E01
python practice/run.py verify
```

`grade` проверяет твою копию, `reference` — эталон; `verify` проверяет все эталоны. Успешный `verify` не означает, что ты решил задания.

## Инженерная база

- [ ] [E01. Точные деньги](E01.md)
- [ ] [E02. День в UTC](E02.md)
- [ ] [E03. Контракт на границе](E03.md)
- [ ] [E04. Manifest полноты](E04.md)

## SQL и базы данных

- [ ] [E05. SQL: события и платежи](E05.md)
- [ ] [E06. SQL: net cash по валюте](E06.md)
- [ ] [E07. SQL: последняя версия](E07.md)
- [ ] [E08. SQL: нарушители уникальности](E08.md)

## Моделирование DWH

- [ ] [E09. SCD2 на границе](E09.md)
- [ ] [E10. Поток и остаток](E10.md)
- [ ] [E11. Unknown dimension](E11.md)
- [ ] [E12. Бизнес-время и время знания](E12.md)

## Загрузка и CDC

- [ ] [E13. Повторы и конфликты](E13.md)
- [ ] [E14. CDC projection](E14.md)
- [ ] [E15. Пагинация без пробела](E15.md)
- [ ] [E16. Миграция amount schema](E16.md)

## Хранилища и вычисления

- [ ] [E17. Partition pruning](E17.md)
- [ ] [E18. Small files: packing](E18.md)
- [ ] [E19. Hot key и skew](E19.md)
- [ ] [E20. Watermark и late side output](E20.md)

## Трансформации и оркестрация

- [ ] [E21. DAG и цикл](E21.md)
- [ ] [E22. Retry policy](E22.md)
- [ ] [E23. Затронутые дни incremental](E23.md)
- [ ] [E24. Publish gate](E24.md)

## Финтех и движение денег

- [ ] [E25. Баланс проводок](E25.md)
- [ ] [E26. Полная сверка](E26.md)
- [ ] [E27. FX с явным масштабом](E27.md)
- [ ] [E28. Распределение оплаты кредита](E28.md)

## Качество и эксплуатация

- [ ] [E29. P95 latency](E29.md)
- [ ] [E30. Радиус инцидента](E30.md)
- [ ] [E31. Checks при неполном входе](E31.md)
- [ ] [E32. Восстановление после backup](E32.md)

## Платформа и безопасность

- [ ] [E33. RBAC deny by default](E33.md)
- [ ] [E34. PII allowlist projection](E34.md)
- [ ] [E35. Сценарная стоимость](E35.md)
- [ ] [E36. Retention и hold](E36.md)

## ИИ, ML и портфолио

- [ ] [E37. Point-in-time feature](E37.md)
- [ ] [E38. AI eval scorecard](E38.md)
- [ ] [E39. RAG с ACL](E39.md)
- [ ] [E40. Capstone: report contract](E40.md)

После практикума собери один из [capstone проектов](../projects/README.md).

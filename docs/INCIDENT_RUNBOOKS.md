# Runbooks для синтетического DWH

## amount_mismatch

**Сигнал:** p3, USD, expected=2500, actual=2400, delta=−100. **Impact:** final settlement result не подтверждён.

1. Зафиксируй report version и оба input manifests.
2. Проверь grain payment/currency, sign convention и cutoff.
3. Выполни query ниже и сравни raw events с external statement.
4. Проверь, fee/partial settlement не был исключён из одной стороны.
5. Не исправляй сумму вручную для получения зелёного результата. Создай synthetic correction scenario; для настоящей системы решение принимает financial owner.

```sql
SELECT event_id,kind,amount_minor,currency,event_time,received_at
FROM raw_events WHERE payment_id='p3' ORDER BY event_time,event_id;
```

## missing_external / unexpected_external

**Первые вопросы:** полный ли файл, совпадает ли период, известны ли все expected providers, была ли смена IDs? Не заменяй missing amount нулём. p9 требует отдельного поиска происхождения; удаление строки из external fixture лишь скрывает исключение.

**Publish:** provisional output может показывать exception count; final output блокируется согласно своему contract. Tutorial demo намеренно сохраняет отчёт с исключениями и не выдаёт его за закрытый финансовый день.

## conflicting event identity

**Сигнал:** `ConflictingEvent`. Сохрани accepted original и conflicting payload на разрешённом synthetic наборе. Убедись, что batch откатился. Проверь producer identity, replay logic и schema version. Если это business correction, введи отдельный version/correction contract; не превращай конфликт в INSERT OR IGNORE.

## Late arrival

e6 получен 3 января и относится к 1 января. Найди affected event_date, пересчитай candidate, сравни full/incremental и выясни, был ли день закрыт. Open period можно обновить по contract; closed требует versioned restatement или adjustment. Для ML cutoff нельзя использовать событие до received_at.

## Восстановление

Сохрани baseline. Восстанавливай backup в отдельное пространство, replay journal после recovery point, запусти balance и reconciliation. Сравни контрольные итоги и version metadata. Код без исправленной истории не завершает recovery. Шаблон — [RUNBOOK](../templates/RUNBOOK.md); безопасные эксперименты — [fault drills](../labs/fault-drills.md).

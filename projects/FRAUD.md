# Проект 2: point-in-time fraud data

## Постановка

Для synthetic decisions собери признаки: captures за час, declines за день, возраст merchant tier. Labels появляются спустя 30 дней по учебной policy. Вход содержит поздние события и исправления профиля.

## План

1. Сохрани entity_id, decision_at, event_time, received_at и label_recorded_at.
2. Определи feature windows с полуоткрытыми границами.
3. Построй historical features только из событий, известных к decision_at.
4. Для изменяемых атрибутов используй valid и system time; простая SCD2 не восстанавливает old knowledge.
5. Применяй temporal train/validation/test split и maturity cutoff.
6. Сохрани dataset manifest и feature versions.

## Negative cases

e6 существует по event_time до decision, но получен позже. Два equal timestamps требуют определённого порядка. Label ещё не созрел. Новая correction профиля не должна появиться в as-known historical dataset. Одно событие другой валюты не попадает в денежный feature.

## Приёмка

Feature before arrival=0, после arrival=2500 на baseline. Для каждой строки можно перечислить использованные event IDs. Latest immature decisions исключены или маркированы по contract. Rebuild manifest даёт те же entity/decision keys. Offline/online definitions согласованы, ограничения toy serving названы.

Модель машинного обучения необязательна: основной результат — доверенный dataset. Если добавишь классификатор, не используй его score как доказательство отсутствия leakage.

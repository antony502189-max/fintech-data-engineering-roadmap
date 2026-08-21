# 079. Fault injection и проверка recovery

## Результат обучения

Воспроизвести отказ до того, как он произойдёт в работе.

## Как это работает

Fault injection выбирает конкретное нарушение: duplicate, missing, late, conflicting, timeout или partial write. На synthetic fixtures безопасно проверить механизм recovery и инварианты. Эксперимент должен иметь ожидаемый эффект, критерий прекращения и способ восстановления. Случайная поломка без измерений мало чему учит.

## Пример из финтеха

После успешного insert повторяют тот же event и проверяют, изменились ли daily totals.

## Порядок реализации

1. Назови failure point
2. Сохрани baseline
3. Внеси одно нарушение
4. Проверь detection и recovery.

## Практическое задание

Пройди drills в labs/fault-drills.md и запиши before-after invariants.

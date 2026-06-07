# 047. Kafka: partitions, offsets и порядок

## Результат обучения

Определить область порядка и безопасный момент commit offset.

## Как это работает

Kafka упорядочивает записи внутри partition; глобального порядка между partitions нет. Key определяет partition mapping с учётом producer partitioner. Consumer group распределяет partitions между consumers. Offset — позиция чтения, не бизнес-ключ; повтор чтения должен быть безопасен для sink.

## Пример из финтеха

Capture и refund одного payment желательно обрабатывать по согласованному порядку, но межплатёжный global order обычно не нужен.

## Порядок реализации

1. Выбери key
2. Определи consumer group
3. Нарисуй commit sequence
4. Проверь rebalance recovery.

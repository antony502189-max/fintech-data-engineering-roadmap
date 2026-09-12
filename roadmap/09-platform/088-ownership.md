# 088. Платформа как продукт и ownership

## Результат обучения

Определить self-service границы и обязанности доменных команд.

## Как это работает

Платформа предоставляет paved paths, общие contracts, observability и безопасные defaults. Доменные команды отвечают за смысл и качество своих моделей. Распределённое ownership требует discoverability и escalation. Каталог без актуальных owners не решает поддержку. Self-service не равен отсутствию review денежных изменений.

## Пример из финтеха

Finance team меняет метрику, platform team поддерживает CI и publish mechanism.

## Порядок реализации

1. Назови users платформы
2. Определи standard path
3. Установи ownership metadata
4. Измерь usability.

## Практическое задание

Напиши service catalog card для daily cash: owner, purpose, contract, dependencies и support.

## Типичная ошибка и её последствия

Платформенная команда становится владельцем всех бизнес-определений и блокирует развитие.

## Проверка результата

Потребитель находит owner и version без личного знакомства с авторами.

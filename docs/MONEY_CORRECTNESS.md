# Доказуемые денежные данные

## Пять уровней проверки

1. **Контракт:** тип, валюта, масштаб, timestamps и identity допустимы.
2. **Доставка:** каждая ожидаемая запись получена; replay не создаёт второе движение.
3. **Модель:** grain и joins сохраняют сумму; правила знака согласованы.
4. **Журнал:** postings полны и balanced на уровне event/currency.
5. **Независимая сверка:** internal movement совпадает с внешним подтверждением при одинаковом scope.

Ни один уровень не заменяет остальные. Правильно подписанный webhook может быть неполным набором. Идеально сбалансированный журнал может использовать неверные amounts. Matching total может скрыть два взаимно компенсирующихся ошибочных платежа.

## Численный разбор

Для p1: capture 10000 − fee 300 − refund 2000 = 7700 USD minor. За 1 января daily USD = p1 capture 10000 − fee 300 + p3 capture 2500 = 12200. Refund p1 относится ко 2 января, поэтому там −2000. Сумма USD across days = 10200; EUR отдельно = 4900.

Внешняя сторона подтверждает p1=7700, p2=4900, но p3=2400. Delta задана как actual−expected и равна −100. p9 — unexpected_external. Inner join оставил бы p9 за пределами расследования. Подмена NULL нулём сделала бы отсутствующую запись похожей на подтверждённый нулевой settlement.

## Почему это не revenue

Net cash описывает заданный поток capture/refund/fee. Revenue зависит от бизнес-модели, правил признания и компонентов, которых нет в fixture. Прибыль требует ещё расходов. DWH engineer согласует определение с финансовым владельцем и хранит versioned contract. Название колонки не делает её бухгалтерским показателем.

## Коррекции

Одинаковый ID с изменённой суммой не следует молча upsert. Можно сохранить correction event с ссылкой на original, или поддержать versioned source record с явной политикой restatement. Выбор определяется source contract и financial process. Старый published report сохраняется; новый содержит reason, source version и affected scope.

## Валюты и округление

Не передавай float в money parser. Курс хранится Decimal string с направлением и временем. Сначала переведи from minor→major, примени курс, затем to major→minor; округление задаётся policy. В E27 ROUND_HALF_EVEN выбран только для учебного контракта. Округление реального продукта согласуется отдельно.

## Минимум для финансового ревью

Нужны grain, sign convention, валюты, даты признания, source coverage, independent control totals, exception ownership, cutoff и procedure correction. Пример такого мышления — [Stripe Ledger engineering article](https://stripe.com/blog/ledger-stripe-system-for-tracking-and-validating-money-movement); наш код не является реализацией Stripe Ledger.

# 009. Time, currencies, and units

## Learning outcome

Define explicit monetary and temporal boundary rules.

## How it works

Store money as fixed-scale decimals or integer minor units with currency. Currency exponents vary; two decimal places are not universal. UTC is useful for events, but a financial day depends on the business calendar. Half-open intervals [start,end) prevent counting a boundary twice.

## Fintech example

An event at 23:30 UTC belongs to the next local day. USD 100 and JPY 100 use different scales and cannot be summed without an FX rule.

## Implementation steps

1. Specify currency and exponent
2. Define the reporting timezone
3. Normalize timestamps
4. Test a day boundary.

## Practical assignment

Run money and history tests. Add a payment at a local-day boundary and document which period receives it.

## Common mistake and its consequences

Using the server date and dividing every currency by 100 creates plausible-looking errors.

## Verify the result

Equivalent instants with different offsets agree; an exponent-zero currency works without division.

## Self-check question

How do event time, receipt time, and revenue recognition time differ?

## Further reading

- [Stripe balance transaction types](https://docs.stripe.com/reports/balance-transaction-types) — primary documentation; find the section relevant to this lesson.
- [Python Tutorial](https://docs.python.org/3.12/tutorial/) — primary documentation; find the section relevant to this lesson.

## Deliverable and navigation

Save your solution in your own fork under `portfolio/009-time-money/`. Include the problem, a minimal example, the check from “Verify the result,” and your answer to the self-check question. Design exercises may produce an ADR, diagram, or experiment table; distinguish a proposal from an implemented service.

[Previous step](../01-foundations/008-containers.md) · [Next step](../01-foundations/010-systems.md) · [Full roadmap](../README.md)

**Module:** Engineering foundations. **Estimated time:** 2–4 hours for a first pass; deeper practice and a project take additional time. The previous step defines reading order, not an equally mandatory prerequisite for every learner: see the [learning paths](../../docs/LEARNING_PATHS.md).

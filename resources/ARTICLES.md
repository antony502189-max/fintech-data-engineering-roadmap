# Engineering articles and review questions

Research date: 2026-10-12. These are first-party engineering publications describing systems at publication time; do not assume the companies still use every cited component.

| Article | Why included | Practical follow-up |
|---|---|---|
| [Ledger: tracking and validating money movement](https://stripe.com/blog/ledger-stripe-system-for-tracking-and-validating-money-movement), Stripe, 2024 | Monetary models and data controls | E25–E26: compare conservation with independent reconciliation |
| [Stripe's payments APIs: the first 10 years](https://stripe.com/blog/payment-api-design), Stripe, 2021 | Evolving payment abstractions | Lesson 061: separate status from final movement |
| [An introduction to Monzo's data stack](https://monzo.com/blog/2021/10/14/an-introduction-to-monzos-data-stack), Monzo, 2021 | Banking platform context | Map sources, transformations, warehouses, and owners; consider its age |
| [Incremental modelling for billions of events](https://monzo.com/blog/how-we-use-incremental-modelling-to-handle-billions-of-events-every-day), Monzo, 2024 | Incremental scope | E23: select by delivery progress and rebuild by event date |
| [A “meshy” approach to Data](https://monzo.com/blog/a-meshy-approach-to-data), Monzo, 2026 | Ownership across teams | Lesson 088: separate domain and platform responsibilities |
| [The Engineering Behind the Platform](https://monzo.com/blog/the-engineering-behind-the-platform), Monzo, 2026 | Platforms as products | Write a catalog card and measurable self-service outcome |
| [Meet Michelangelo](https://www.uber.com/us/en/blog/michelangelo-machine-learning-platform/), Uber Engineering, 2017 | ML workflows and features | Lesson 097: separate model, data, feature, and serving versions |
| [Scaling Michelangelo](https://www.uber.com/gb/en/blog/scaling-michelangelo/), Uber Engineering, 2018 | Standardizing ML platforms | E37–E38: identify what tiny offline examples cannot prove |

## Reading a company case

Identify the initial problem, scale, guarantees, and operators. List three assumptions differing from your project. Finish with an experiment testing whether an idea transfers. Another company's production numbers are not properties of this lab.

# AI in data-engineering work

## A verifiable teaching workflow

1. Supply synthetic schema, grain, signs, dialect, and expected examples.
2. Ask for assumptions and missing business definitions.
3. Review generated SQL or tests as an untrusted contribution.
4. Run positive and negative fixtures: equal amounts on different payments, late delivery, NULL, currencies, and boundaries.
5. Compare with independent expected output and inspect plans on larger datasets.
6. Retain model/prompt versions, evidence, and the reviewed decision.

## Example join-review prompt

```text
Dialect: SQLite. Facts grain: one financial event per event_id.
Each payment has several attempts and several fee events.
Money is integer minor units plus currency.
Review the proposed query for fanout, missing data and mixed currencies.
Do not invent columns or equate net cash with revenue.
Give one minimal counterexample and a corrected query.
Mark unverified assumptions explicitly.
```

A convincing answer is not proof. Two equal captures expose the unsafe SUM(DISTINCT amount) workaround.

## Text-to-SQL

Use a scoped identity, approved metrics, AST validation, timeouts, and budgets. SELECT can disclose unnecessary data or scan enormous tables. Regex checks are not a security boundary. Do not execute arbitrary generated SQL on production data.

## RAG and injection

Apply ACLs before context construction. Documents cannot grant tool authority. Citations must identify actual fragments and versions. Deletion must propagate to indexes and caches. Unsupported answers should abstain.

## Evals

Report financial correctness, grounding, abstention, forbidden disclosure, and cost separately. E38 provides an offline scorecard; E39 filters document access. Full systems need adversarial evaluations and real permission integration.

Use [OWASP's LLM project](https://owasp.org/projects/top-10-for-large-language-model-applications) and [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework) for further study. The baseline makes no paid model calls.

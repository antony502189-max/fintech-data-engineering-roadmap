# 091. AI as a data-engineering assistant

## Learning outcome

Use AI drafts while retaining responsibility for verification.

## How it works

AI can explain concepts, propose fixture tests, and draft SQL. It can also invent columns, links, or guarantees confidently. A draft becomes an acceptable change only after contract, query-plan, and meaningful-test verification. Do not send real payment payloads externally without approved authorization.

## Fintech example

An assistant proposes SUM(DISTINCT amount) to repair fanout and drops distinct equal-value payments.

## Implementation steps

1. Provide synthetic schema
2. Ask for assumptions
3. Verify numerical fixtures
4. Review the diff before merge.

## Practical assignment

Write a join-review prompt and test its suggested query on two equal capture amounts.

## Common mistake and its consequences

Copying a persuasive explanation without execution makes an AI error an official rule.

## Verify the result

Retain schema inputs, versions, test evidence, and a reviewed formula.

## Self-check question

Which financial mistakes can hide in syntactically valid AI-generated SQL?

## Further reading

- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) — primary documentation; find the section relevant to this lesson.
- [dbt data tests](https://docs.getdbt.com/docs/build/data-tests) — primary documentation; find the section relevant to this lesson.

## Deliverable and navigation

Save your solution in your own fork under `portfolio/091-ai-assistant/`. Include the problem, a minimal example, the check from “Verify the result,” and your answer to the self-check question. Design exercises may produce an ADR, diagram, or experiment table; distinguish a proposal from an implemented service.

[Previous step](../09-platform/090-platform-review.md) · [Next step](../10-ai-career/092-text-to-sql.md) · [Full roadmap](../README.md)

**Module:** AI, ML and portfolio. **Estimated time:** 2–4 hours for a first pass; deeper practice and a project take additional time. The previous step defines reading order, not an equally mandatory prerequisite for every learner: see the [learning paths](../../docs/LEARNING_PATHS.md).

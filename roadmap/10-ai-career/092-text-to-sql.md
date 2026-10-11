# 092. Text-to-SQL and constrained access

## Learning outcome

Design query execution with permission and cost controls.

## How it works

Model output is untrusted text. Execution needs parsing or AST controls, a read-only identity, approved schemas, timeouts, and resource budgets. A SELECT regex is not a sufficient boundary. Semantic definitions prevent ambiguous requests from becoming invented metrics.

## Fintech example

A user asks for profit while the only available measure is net cash. Clarify or abstain rather than invent profitability.

## Implementation steps

1. Define allowed metrics
2. Scope database identity
3. Validate syntax trees
4. Execute within limits.

## Practical assignment

Write a design and adversarial test list. Do not run arbitrary generated SQL against production.

## Common mistake and its consequences

A read-only query can still disclose raw personal data or scan enormous tables.

## Verify the result

Cover unknown metrics, forbidden tables, expensive queries, and unsupported statements.

## Self-check question

Why does read-only access not prevent excess disclosure?

## Further reading

- [OWASP LLM applications project](https://owasp.org/www-project-top-10-for-large-language-model-applications/) — primary documentation; find the section relevant to this lesson.
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) — primary documentation; find the section relevant to this lesson.

## Deliverable and navigation

Save your solution in your own fork under `portfolio/092-text-to-sql/`. Include the problem, a minimal example, the check from “Verify the result,” and your answer to the self-check question. Design exercises may produce an ADR, diagram, or experiment table; distinguish a proposal from an implemented service.

[Previous step](../10-ai-career/091-ai-assistant.md) · [Next step](../10-ai-career/093-rag.md) · [Full roadmap](../README.md)

**Module:** AI, ML and portfolio. **Estimated time:** 2–4 hours for a first pass; deeper practice and a project take additional time. The previous step defines reading order, not an equally mandatory prerequisite for every learner: see the [learning paths](../../docs/LEARNING_PATHS.md).

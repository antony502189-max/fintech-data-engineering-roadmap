# 094. Prompt injection and untrusted documents

## Learning outcome

Separate source content from system authority.

## How it works

A retrieved document can contain instructions to change assistant behavior. Those instructions are data, not authorization. Keyword filters do not solve the general problem. Use constrained tools, minimal permissions, trust boundaries, and checks on external actions. An offline example illustrates a boundary rather than proving production security.

## Fintech example

A catalog chunk says to ignore restrictions and export raw data. Retrieval cannot grant that permission.

## Implementation steps

1. Map trust boundaries
2. Limit tools
3. Bind authority to identity
4. Add adversarial cases.

## Practical assignment

Write five synthetic document injections and expected policy decisions.

## Common mistake and its consequences

Detecting one phrase is mistaken for a complete defense; reworded commands bypass it.

## Verify the result

Allowed actions remain independent of retrieved text.

## Self-check question

Why can instructions inside a document not authorize restricted-table access?

## Further reading

- [OWASP LLM applications project](https://owasp.org/www-project-top-10-for-large-language-model-applications/) — primary documentation; find the section relevant to this lesson.

## Deliverable and navigation

Save your solution in your own fork under `portfolio/094-prompt-injection/`. Include the problem, a minimal example, the check from “Verify the result,” and your answer to the self-check question. Design exercises may produce an ADR, diagram, or experiment table; distinguish a proposal from an implemented service.

[Previous step](../10-ai-career/093-rag.md) · [Next step](../10-ai-career/095-ai-evals.md) · [Full roadmap](../README.md)

**Module:** AI, ML and portfolio. **Estimated time:** 2–4 hours for a first pass; deeper practice and a project take additional time. The previous step defines reading order, not an equally mandatory prerequisite for every learner: see the [learning paths](../../docs/LEARNING_PATHS.md).

# 069. KYC/AML provenance and protected data

## Learning outcome

Design decision evidence without inventing legal requirements.

## How it works

Engineers preserve evidence origins, rule versions, and decision states; they do not independently establish legal obligations. Approved policy defines retention, access, and exceptions. Decision history explains what information was available when an action occurred.

## Fintech example

A verified status changes after rechecking. Earlier decisions must point to earlier evidence versions.

## Implementation steps

1. Minimize fields
2. Separate identifiers and evidence
3. Name the policy owner
4. Record version and decision time.

## Practical assignment

Design synthetic kyc_decisions without real documents. Add access and retention matrices.

## Common mistake and its consequences

Copying entire documents into raw, logs, and LLM prompts creates unnecessary exposure.

## Verify the result

Every field has a purpose and access rule, and no real personal information appears.

## Self-check question

Which questions must the compliance owner answer before retention is configured?

## Further reading

- [AWS Well Architected](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html) — primary documentation; find the section relevant to this lesson.
- [PostgreSQL documentation](https://www.postgresql.org/docs/current/) — primary documentation; find the section relevant to this lesson.

## Deliverable and navigation

Save your solution in your own fork under `portfolio/069-kyc-data/`. Include the problem, a minimal example, the check from “Verify the result,” and your answer to the self-check question. Design exercises may produce an ADR, diagram, or experiment table; distinguish a proposal from an implemented service.

[Previous step](../07-fintech/068-fraud-data.md) · [Next step](../07-fintech/070-fintech-review.md) · [Full roadmap](../README.md)

**Module:** Financial data and money movement. **Estimated time:** 2–4 hours for a first pass; deeper practice and a project take additional time. The previous step defines reading order, not an equally mandatory prerequisite for every learner: see the [learning paths](../../docs/LEARNING_PATHS.md).

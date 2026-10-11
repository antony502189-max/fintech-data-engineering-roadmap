# 027. Data Vault: hubs, links, and satellites

## Learning outcome

Explain Data Vault's benefits and operating cost.

## How it works

A hub holds business keys, a link relationships, and a satellite descriptive changes and provenance. Raw Vault preserves source history; Business Vault applies agreed rules. Consumer marts still need useful analytical models. Hash keys require consistent canonicalization and collision handling.

## Fintech example

CRM and processing systems identify merchants differently and maintain changing contract relationships.

## Implementation steps

1. Design hubs
2. Define link grain
3. Separate source satellites
4. Show a dimensional output mart.

## Practical assignment

Compare star and vault designs for three evolving sources. Document extra joins and identity-resolution rules.

## Common mistake and its consequences

Concatenating keys without separators or NULL normalization creates ambiguous hash input.

## Verify the result

Preserve source and load time, and show how analysts reach an understandable mart.

## Self-check question

Which specific problem in your project justifies Vault?

## Further reading

- [Kimball dimensional modeling techniques](https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/) — primary documentation; find the section relevant to this lesson.
- [PostgreSQL documentation](https://www.postgresql.org/docs/current/) — primary documentation; find the section relevant to this lesson.

## Deliverable and navigation

Save your solution in your own fork under `portfolio/027-data-vault/`. Include the problem, a minimal example, the check from “Verify the result,” and your answer to the self-check question. Design exercises may produce an ADR, diagram, or experiment table; distinguish a proposal from an implemented service.

[Previous step](../03-modeling/026-bitemporal.md) · [Next step](../03-modeling/028-entity-events.md) · [Full roadmap](../README.md)

**Module:** DWH modeling. **Estimated time:** 2–4 hours for a first pass; deeper practice and a project take additional time. The previous step defines reading order, not an equally mandatory prerequisite for every learner: see the [learning paths](../../docs/LEARNING_PATHS.md).

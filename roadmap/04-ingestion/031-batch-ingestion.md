# 031. Batch ingestion and batch controls

## Learning outcome

Load a file as an identified, verified batch.

## How it works

A batch has a stable ID, source, coverage period, and manifest. Filenames do not ensure identity: a provider can reissue one with different content. Input hashes distinguish replay from replacement; replacement needs an agreed policy. Publish readiness only after input and output checks.

## Fintech example

A January 1 settlement file arrives twice. Identical content is replay; corrected fees create a new version.

## Implementation steps

1. Define batch identity
2. Save hashes and counts
3. Verify totals
4. Publish readiness after commit.

## Practical assignment

Design a manifest with period, currency totals, content hash, and version. Simulate replay and correction.

## Common mistake and its consequences

Overwriting files without history prevents linking discrepancies to source versions.

## Verify the result

Every version retains provenance; replay leaves totals and counts unchanged.

## Self-check question

When is a changed hash a violation, and when is it an allowed reissue?

## Further reading

- [Python Tutorial](https://docs.python.org/3.12/tutorial/) — primary documentation; find the section relevant to this lesson.
- [PostgreSQL documentation](https://www.postgresql.org/docs/current/) — primary documentation; find the section relevant to this lesson.

## Deliverable and navigation

Save your solution in your own fork under `portfolio/031-batch-ingestion/`. Include the problem, a minimal example, the check from “Verify the result,” and your answer to the self-check question. Design exercises may produce an ADR, diagram, or experiment table; distinguish a proposal from an implemented service.

[Previous step](../03-modeling/030-model-review.md) · [Next step](../04-ingestion/032-api-connectors.md) · [Full roadmap](../README.md)

**Module:** Ingestion and CDC. **Estimated time:** 2–4 hours for a first pass; deeper practice and a project take additional time. The previous step defines reading order, not an equally mandatory prerequisite for every learner: see the [learning paths](../../docs/LEARNING_PATHS.md).

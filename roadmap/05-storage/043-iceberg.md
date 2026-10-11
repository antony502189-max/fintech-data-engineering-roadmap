# 043. Iceberg snapshots and table evolution

## Learning outcome

Distinguish table snapshots, data files, and catalogs.

## How it works

Table formats manage metadata, snapshots, and the files visible to a reader. Atomic commits switch metadata references; files may exist before publication. Schema and partition evolution depend on engine compatibility. Snapshot expiration and orphan cleanup have recovery consequences.

## Fintech example

A corrected January dataset becomes a new snapshot; readers should see a complete version.

## Implementation steps

1. Specify the catalog
2. Identify engines
3. Pin format compatibility
4. Plan maintenance.

## Practical assignment

Design a payments Iceberg table and shadow backfill. State that the SQLite lab does not implement Iceberg.

## Common mistake and its consequences

Manually deleting old-looking files can remove files referenced by active snapshots.

## Verify the result

Cleanup accounts for retention, active readers, and review of a dry run.

## Self-check question

Why does time travel stop working after its required snapshots or files are removed?

## Further reading

- [Apache Iceberg documentation](https://iceberg.apache.org/docs/latest/) — primary documentation; find the section relevant to this lesson.

## Deliverable and navigation

Save your solution in your own fork under `portfolio/043-iceberg/`. Include the problem, a minimal example, the check from “Verify the result,” and your answer to the self-check question. Design exercises may produce an ADR, diagram, or experiment table; distinguish a proposal from an implemented service.

[Previous step](../05-storage/042-partitioning.md) · [Next step](../05-storage/044-cloud-dwh.md) · [Full roadmap](../README.md)

**Module:** Storage and processing. **Estimated time:** 2–4 hours for a first pass; deeper practice and a project take additional time. The previous step defines reading order, not an equally mandatory prerequisite for every learner: see the [learning paths](../../docs/LEARNING_PATHS.md).

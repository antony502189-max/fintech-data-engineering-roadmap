# 079. Fault injection and recovery verification

## Learning outcome

Reproduce failures before they affect operations.

## How it works

Choose concrete faults: duplicate, missing, late, conflicting, timeout, or partial write. Synthetic fixtures safely exercise detection and recovery. Define expected effects, stop conditions, and restoration. Random damage without measurements teaches little.

## Fintech example

Replay an inserted event and verify daily totals remain unchanged.

## Implementation steps

1. Identify a failure point
2. Save baseline
3. Introduce one defect
4. Verify detection and recovery.

## Practical assignment

Complete labs/fault-drills.md and record before/after invariants.

## Common mistake and its consequences

Changing several variables at once makes diagnosis ambiguous.

## Verify the result

Every drill has a failing check and a confirmed restored state.

## Self-check question

Which lab defect requires an independent source to detect?

## Further reading

- [Python Tutorial](https://docs.python.org/3.12/tutorial/) — primary documentation; find the section relevant to this lesson.
- [dbt data tests](https://docs.getdbt.com/docs/build/data-tests) — primary documentation; find the section relevant to this lesson.

## Deliverable and navigation

Save your solution in your own fork under `portfolio/079-chaos/`. Include the problem, a minimal example, the check from “Verify the result,” and your answer to the self-check question. Design exercises may produce an ADR, diagram, or experiment table; distinguish a proposal from an implemented service.

[Previous step](../08-reliability/078-performance-ops.md) · [Next step](../08-reliability/080-reliability-review.md) · [Full roadmap](../README.md)

**Module:** Quality and reliability. **Estimated time:** 2–4 hours for a first pass; deeper practice and a project take additional time. The previous step defines reading order, not an equally mandatory prerequisite for every learner: see the [learning paths](../../docs/LEARNING_PATHS.md).

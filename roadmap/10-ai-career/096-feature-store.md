# 096. Feature stores and point-in-time correctness

## Learning outcome

Align offline and online feature meaning.

## How it works

Feature stores manage definitions, materialization, and serving but do not automatically establish correct event and knowledge cutoffs. Training and serving semantics must agree. TTL, lateness, and entity keys influence availability. Leakage checks are needed regardless of product choice.

## Fintech example

p3's feature must exclude a capture not yet received at decision time.

## Implementation steps

1. Define entity and feature
2. Specify cutoffs
3. Check availability
4. Compare online and historical semantics.

## Practical assignment

Run feature tests and extend your rolling-window copy with receipt-time constraints.

## Common mistake and its consequences

Using corrected offline history introduces information unavailable to historical online decisions.

## Verify the result

Every decision's contributing events satisfy explicit availability timestamps.

## Self-check question

Which event-time and ingestion-time distinctions belong in the feature definition?

## Further reading

- [Feast point in time joins](https://docs.feast.dev/getting-started/concepts/point-in-time-joins) — primary documentation; find the section relevant to this lesson.

## Deliverable and navigation

Save your solution in your own fork under `portfolio/096-feature-store/`. Include the problem, a minimal example, the check from “Verify the result,” and your answer to the self-check question. Design exercises may produce an ADR, diagram, or experiment table; distinguish a proposal from an implemented service.

[Previous step](../10-ai-career/095-ai-evals.md) · [Next step](../10-ai-career/097-ml-pipelines.md) · [Full roadmap](../README.md)

**Module:** AI, ML and portfolio. **Estimated time:** 2–4 hours for a first pass; deeper practice and a project take additional time. The previous step defines reading order, not an equally mandatory prerequisite for every learner: see the [learning paths](../../docs/LEARNING_PATHS.md).

# 097. ML datasets, labels, and experiment versions

## Learning outcome

Make training data reproducible and explainable.

## How it works

Model versions alone cannot reproduce experiments. Dataset manifests record sources, cutoffs, feature definitions, label maturity, and splits. Monitor coverage, distributions, and delayed performance. Training code should not silently redefine source business metrics.

## Fintech example

A fraud model uses January decisions and labels known by March under a fixed horizon.

## Implementation steps

1. Save dataset manifests
2. Fix temporal splits
3. Specify label maturity
4. Check leakage.

## Practical assignment

Build a synthetic training manifest and identify excluded decisions with immature labels.

## Common mistake and its consequences

Reading latest tables on each retrain makes past experiments unreproducible after corrections.

## Verify the result

A manifest reproduces entity/decision keys and labels.

## Self-check question

Why is a versioned model artifact insufficient for auditing a decision?

## Further reading

- [Feast point in time joins](https://docs.feast.dev/getting-started/concepts/point-in-time-joins) — primary documentation; find the section relevant to this lesson.
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) — primary documentation; find the section relevant to this lesson.

## Deliverable and navigation

Save your solution in your own fork under `portfolio/097-ml-pipelines/`. Include the problem, a minimal example, the check from “Verify the result,” and your answer to the self-check question. Design exercises may produce an ADR, diagram, or experiment table; distinguish a proposal from an implemented service.

[Previous step](../10-ai-career/096-feature-store.md) · [Next step](../10-ai-career/098-system-design.md) · [Full roadmap](../README.md)

**Module:** AI, ML and portfolio. **Estimated time:** 2–4 hours for a first pass; deeper practice and a project take additional time. The previous step defines reading order, not an equally mandatory prerequisite for every learner: see the [learning paths](../../docs/LEARNING_PATHS.md).

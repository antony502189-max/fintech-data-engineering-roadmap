# 003. Python for reliable pipelines

## Learning outcome

Write a pure transformation function and separate it from input and output.

## How it works

Separate source reading, contract validation, transformation, and persistence. Pure functions are easier to test at boundaries. A generator supports chunked reading but does not guarantee bounded memory if the next step collects everything into a list. Invalid data and temporary network failures require different handling.

## Fintech example

A provider CSV supplies decimal amounts as strings and currencies separately. Reject excess precision instead of silently rounding it.

## Implementation steps

1. Read fintech_lab/money.py
2. Check Decimal conversion to minor units
3. Separate business defects from infrastructure failures
4. Handle errors at the boundary.

## Practical assignment

Extend your copy of to_minor with a synthetic currency using four decimal places. Test accepted and excessive precision.

## Common mistake and its consequences

Binary floating point introduces rounding errors; a broad exception handler can disguise programming defects as bad source data.

## Verify the result

Cover zero, negative, oversized, nonfinite, and unsupported-currency inputs with explicit expected results.

## Self-check question

How does quarantining one invalid row differ from failing an entire batch?

## Further reading

- [Python Tutorial](https://docs.python.org/3.12/tutorial/) — primary documentation; find the section relevant to this lesson.
- [Python sqlite3](https://docs.python.org/3.12/library/sqlite3.html) — primary documentation; find the section relevant to this lesson.

## Deliverable and navigation

Save your solution in your own fork under `portfolio/003-python/`. Include the problem, a minimal example, the check from “Verify the result,” and your answer to the self-check question. Design exercises may produce an ADR, diagram, or experiment table; distinguish a proposal from an implemented service.

[Previous step](../01-foundations/002-requirements.md) · [Next step](../01-foundations/004-cli-linux.md) · [Full roadmap](../README.md)

**Module:** Engineering foundations. **Estimated time:** 2–4 hours for a first pass; deeper practice and a project take additional time. The previous step defines reading order, not an equally mandatory prerequisite for every learner: see the [learning paths](../../docs/LEARNING_PATHS.md).

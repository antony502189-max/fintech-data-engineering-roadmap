# 004. Terminals, processes, and exit codes

## Learning outcome

Diagnose a failed batch job using its exit code and error stream.

## How it works

A CLI is an automation interface. Standard output carries results, standard error explains problems, and the exit code tells the scheduler whether execution succeeded. Environment variables change process behavior, while the working directory controls relative paths. Printing an error and returning zero misleads automation.

## Fintech example

A job creates an empty settlement.csv and exits successfully. The next task can close the day at zero unless it verifies the file contract.

## Implementation steps

1. Use an explicit input path
2. Check existence and format
3. Return a nonzero code on failure
4. Preserve a structured explanation.

## Practical assignment

Build a CLI accepting a date and file path. Test missing files, empty files, and invalid dates in Bash or PowerShell.

## Common mistake and its consequences

Checking log text alone cannot reliably distinguish the word “failed” from an actual failed process.

## Verify the result

All three invalid inputs return nonzero. A valid input returns zero and creates a verifiable artifact.

## Self-check question

Why are a successful process and a ready dataset different claims?

## Further reading

- [Python Tutorial](https://docs.python.org/3.12/tutorial/) — primary documentation; find the section relevant to this lesson.

## Deliverable and navigation

Save your solution in your own fork under `portfolio/004-cli-linux/`. Include the problem, a minimal example, the check from “Verify the result,” and your answer to the self-check question. Design exercises may produce an ADR, diagram, or experiment table; distinguish a proposal from an implemented service.

[Previous step](../01-foundations/003-python.md) · [Next step](../01-foundations/005-git.md) · [Full roadmap](../README.md)

**Module:** Engineering foundations. **Estimated time:** 2–4 hours for a first pass; deeper practice and a project take additional time. The previous step defines reading order, not an equally mandatory prerequisite for every learner: see the [learning paths](../../docs/LEARNING_PATHS.md).

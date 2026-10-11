# 008. Containers and local environments

## Learning outcome

Explain what a container fixes and what remains an external dependency.

## How it works

An image defines a filesystem and runtime. A volume stores data outside the container layer; deleting the container need not delete the volume. Configuration, network services, and processor architecture remain part of the environment. Floating tags do not make a deployment reproducible.

## Fintech example

A developer validates a model on SQLite while the team uses PostgreSQL. Sharing a Python image does not eliminate differences in SQL or transaction behavior.

## Implementation steps

1. Identify the runtime
2. Pin the image version
3. Separate persistent data
4. Add a health check and verification command.

## Practical assignment

Create a Dockerfile for the lab and compare it with python -m fintech_lab. Record versions and use synthetic data.

## Common mistake and its consequences

A latest tag changes and introduces an incompatible runtime during financial close.

## Verify the result

A clean environment can be created from the instructions and produces the expected fixture results.

## Self-check question

Why is a container with a retained volume not a clean test environment?

## Further reading

- [Docker documentation](https://docs.docker.com/get-started/) — primary documentation; find the section relevant to this lesson.

## Deliverable and navigation

Save your solution in your own fork under `portfolio/008-containers/`. Include the problem, a minimal example, the check from “Verify the result,” and your answer to the self-check question. Design exercises may produce an ADR, diagram, or experiment table; distinguish a proposal from an implemented service.

[Previous step](../01-foundations/007-http.md) · [Next step](../01-foundations/009-time-money.md) · [Full roadmap](../README.md)

**Module:** Engineering foundations. **Estimated time:** 2–4 hours for a first pass; deeper practice and a project take additional time. The previous step defines reading order, not an equally mandatory prerequisite for every learner: see the [learning paths](../../docs/LEARNING_PATHS.md).

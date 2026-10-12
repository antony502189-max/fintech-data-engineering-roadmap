# Capstone 4: RAG over a data catalog

## Problem

A synthetic catalog contains metric definitions, owners, runbooks, and restricted fraud notes. Finance and support have different access. Answers need evidence and abstention when unsupported.

## Offline baseline

1. Store document ID, version, allowed_roles, and content.
2. Filter permissions before context construction.
3. Begin with lexical retrieval to separate access rules from model choice.
4. Cite only documents actually used.
5. Evaluate known metrics, ambiguous revenue, missing definitions, forbidden requests, and injected instructions.
6. Report grounding and critical disclosure separately.

## Acceptance

Support context never contains restricted fraud chunks. Documents cannot authorize raw export. Unknown revenue triggers abstention or clarification. Citations have valid versions. Deleted documents disappear from retrieval and caches. Retain an evaluation baseline.

## Extension

A real LLM is optional and needs configuration, budgets, and approved data policy. Keep keys out of Git. Text-to-SQL needs AST checks, scoped read-only identity, and query budgets; lexical or regex filters are not security boundaries. Start with [E38](../practice/E38.md) and [E39](../practice/E39.md).

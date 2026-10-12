# Capstone 1: settlement warehouse

## Problem

Three synthetic providers deliver capture, refund, fee, and settlement data with duplicates, lateness, missing files, and revised batches. Finance needs daily net cash with completeness evidence and explainable exceptions.

## Milestones

1. Define event and batch contracts: identity, version, hash, counts, and currency totals.
2. Build raw/staging/core with original evidence and normalized fields; quarantine schema defects.
3. Produce postings and payment/currency net; check completeness, conservation, and independent matching.
4. Materialize daily output with affected-day incremental updates and full-rebuild equivalence.
5. Publish gated candidates with previous versions and original/restated reports.
6. Write runbooks for missing files, mismatch, lateness, and collisions.

## Scenarios

Expand payments() to 10000 deterministic events. Specify external expectations independently. Test full replay, an old-day late event, conflicting identity, missing provider batch, equal-value distinct payments, revised settlement, and refund without capture.

## Acceptance

Replay leaves amounts unchanged. Conflicts never silently overwrite. Full and incremental outputs agree after lateness. Missing batches block final publication. Exceptions have identity, currency, delta, and ownership. Published versions link manifests and code revisions; original closed reports survive correction.

## Extension

Port to PostgreSQL and a supported dbt adapter, then add source positions and orchestration. Benchmarks record runtime, hardware, and distribution. Tiny fixtures do not prove production readiness.

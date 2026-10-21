# GitHub Discussion draft: When expected payment amount is unknown

**Status:** AI-assisted draft for maintainer review. Not published.
**Proposed category:** Q&A

## Title

Payment reconciliation: how should a settlement row with no internal payment be represented?

## Body

An internally balanced payment journal can still leave a processor settlement row unresolved. One case is a settlement entry with no corresponding internal payment.

Two synthetic USD examples:

| Payment | Internal record | Processor settlement | Classification |
|---|---|---:|---|
| p3 | Expected 2,500 cents ($25.00) | 2,400 cents ($24.00) | Amount mismatch: −100 cents |
| p9 | No internal row; expected amount unknown | 500 cents ($5.00) | Unexpected external record |

For p9, replacing the missing expected amount with zero makes arithmetic convenient, but it states a financial expectation that the data do not establish. Unless the business contract explicitly defines absence as zero, keep the matching exception separate from amount comparison. A reconciliation output might represent p9 as `unexpected_external`, with `expected_minor` and `delta_minor` unset; p3 can be `amount_mismatch` with a known −100-cent delta.

The distinction is between **expected zero** and **expected amount unavailable**. Those states can lead to different investigation and retry paths.

How do you model this in your reconciliation outputs: separate match and amount statuses, a single exception code, or another shape? What fields help an analyst resolve an external-only row without conflating it with a true zero-value payment?

These examples use synthetic teaching data. The local walkthrough is in the [five-minute first-win guide](https://github.com/antony502189-max/fintech-data-engineering-roadmap/blob/main/docs/FIRST_WIN.md); it does not require paid cloud infrastructure.

## Review notes

- Keep the example labeled synthetic; it is not a production accounting specification.
- Check the example still matches the default branch before posting.
- No star request, promotional CTA, invented maintainer anecdote, or claim of reader feedback.
- Post only after maintainer approval; use the Q&A category if still available and appropriate.

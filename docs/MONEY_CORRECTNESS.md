# Explainable monetary data

## Five verification layers

1. **Contract:** types, currency, scale, timestamps, and identity are valid.
2. **Delivery:** expected records arrive; replay adds no second movement.
3. **Model:** grain and joins preserve amounts; signs follow agreed rules.
4. **Journal:** postings are complete and balanced by event/currency.
5. **Independent reconciliation:** internal movement agrees with external confirmation for the same scope.

No layer replaces another. A signed webhook need not represent a complete set. Balanced postings may contain wrong amounts. Matching total sums may hide compensating errors across individual payments.

## Numerical walkthrough

p1: capture 10000 − fee 300 − refund 2000 = 7700 USD minor. January 1 USD = 10000 − 300 + p3 capture 2500 = 12200. The refund belongs to January 2, whose total is −2000. USD across both days is 10200; EUR remains separate at 4900.

External data confirms p1=7700 and p2=4900 but p3=2400. Delta is actual−expected, giving −100. p9 is unexpected_external. An inner join would hide it; substituting zero for NULL would disguise missing confirmation.

## Cash is not revenue

Net cash describes the specified capture/refund/fee flow. Revenue depends on business model, recognition, and components absent here. Profit also requires expenses. Agree on definitions with financial owners and keep versioned contracts; column names do not establish accounting meaning.

## Corrections

Do not silently upsert a different amount under an existing event ID. A correction can be a linked event or a versioned source record with explicit restatement rules. Preserve previous published reports and record reasons, source versions, and affected scope.

## FX and rounding

Do not pass floats into monetary parsing. Preserve Decimal rate strings with direction and time. Convert source minor→major, apply the rate, then target major→minor. E27 uses ROUND_HALF_EVEN under a teaching contract; actual product rounding needs separate approval.

## Financial review evidence

Require grain, signs, currency, recognition dates, coverage, independent controls, exception owners, cutoffs, and correction procedures. [Stripe's Ledger article](https://stripe.com/blog/ledger-stripe-system-for-tracking-and-validating-money-movement) provides a related engineering case; this code is not Stripe Ledger.

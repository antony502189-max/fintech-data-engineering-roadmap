# Capstone 3: credit flows and balance snapshots

## Problem

Synthetic loans include disbursement, scheduled dues, fees, interest accrual, repayment, and reversal. The teaching allocation order is fee→interest→principal. Readers need dated balances and period flows.

## Plan

1. Separate loan identity, policy versions, and events.
2. Keep minor units with currency.
3. Implement deterministic allocation and unallocated remainder.
4. Build snapshots separately from flow facts.
5. Add correction/reversal and explain snapshot rebuilding.
6. Verify principal roll-forward and independent expectations.

## Scenarios

Payment 1200 against fee=100, interest=200, principal=1000 allocates 100/200/900. Payment 2000 leaves 700 unallocated. Partial payments do not make components negative. Replay cannot allocate twice. Late payments rebuild affected snapshots.

## Acceptance

Allocated plus unallocated equals received payment. Closing principal equals opening plus disbursements minus principal repayments plus defined corrections. Monthly flows sum; daily balances are not turnover. Every row links policy and provenance. Synthetic rules do not establish real lending terms or legal requirements.

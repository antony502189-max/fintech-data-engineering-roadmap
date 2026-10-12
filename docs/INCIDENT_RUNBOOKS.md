# Synthetic DWH incident runbooks

## Amount mismatch

Signal: p3, USD, expected=2500, actual=2400, delta=−100. Impact: final settlement is unconfirmed.

1. Record report versions and both input manifests.
2. Verify payment/currency grain, sign conventions, and cutoff.
3. Run the query below and compare raw events with the statement.
4. Check whether fees or partial settlement are excluded on one side.
5. Do not edit amounts merely to obtain green checks. Use a synthetic correction scenario; real decisions belong to financial owners.

```sql
SELECT event_id,kind,amount_minor,currency,event_time,received_at
FROM raw_events WHERE payment_id='p3' ORDER BY event_time,event_id;
```

## Missing or unexpected external records

Check file completeness, period alignment, expected providers, and identity changes. Missing amounts are not zero. p9 needs provenance investigation; deleting it from the external fixture conceals the exception.

Provisional output may expose exception counts. Final publication follows its contract and may be blocked. The demo intentionally writes a report with exceptions rather than claiming financial close.

## Conflicting event identity

Preserve the accepted original and conflicting synthetic input, and confirm rollback. Check producer identity, replay rules, and schema versions. A legitimate correction needs an explicit versioned contract, not INSERT OR IGNORE.

## Late delivery

e6 arrives January 3 but belongs to January 1. Identify affected dates, rebuild a candidate, compare full and incremental results, and determine whether the period is closed. Open periods follow update policy; closed periods need versioned restatement or adjustment. ML features cannot use the event before receipt.

## Recovery

Retain a baseline. Restore separately, replay after the recovery point, run balance and reconciliation, and compare controls and versions. A code fix without repaired history does not complete recovery. Use the [runbook template](../templates/RUNBOOK.md) and [fault drills](../labs/fault-drills.md).

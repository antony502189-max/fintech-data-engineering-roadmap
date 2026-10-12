"""Normalize two representations before business-identity comparison."""
from fintech_lab.money import to_minor
from fintech_lab.contracts import validate
from challenges.solutions.C01 import solve as run_batches

def normalize(row):
    try:
        required = {'version', 'amount', 'event_id', 'payment_id', 'kind', 'currency', 'event_time', 'received_at'}
        if set(row) != required:
            return {'rejected_source': row}
        version = row['version']
        if type(version) is not int or version not in (1, 2):
            return {'rejected_source': row}
        amount = row['amount'] if version == 1 else to_minor(row['amount'], row['currency'])
        candidate = {**{key: row[key] for key in ('event_id', 'payment_id', 'kind', 'currency', 'event_time', 'received_at')},
                     'amount_minor': amount}
        return validate(candidate)
    except (KeyError, ValueError, TypeError):
        return {'rejected_source': row}

def solve(data):
    return run_batches({'batches': [[normalize(row) for row in batch] for batch in data['batches']]})

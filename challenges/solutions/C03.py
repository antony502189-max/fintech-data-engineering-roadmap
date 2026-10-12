"""Explicit payout allocation: namespaces, currencies, completeness, and totals."""
from collections import defaultdict

def solve(data):
    ledger = {}
    for row in data['ledger']:
        key = (row['provider'], row['payment'], row['currency'])
        if key in ledger:
            return {'error': 'duplicate_ledger'}
        ledger[key] = row['net_minor']
    expected = defaultdict(int)
    allocated = set()
    for row in data['membership']:
        key = (row['provider'], row['payment'], row['currency'])
        if key in allocated:
            return {'error': 'duplicate_allocation'}
        if key not in ledger:
            return {'error': 'unknown_payment'}
        allocated.add(key)
        payout = (row['provider'], row['payout'], row['currency'])
        expected[payout] += ledger[key]
    actual = {}
    for row in data['statements']:
        key = (row['provider'], row['payout'], row['currency'])
        if key in actual:
            return {'error': 'duplicate_statement'}
        actual[key] = row['net_minor']
    payouts = []
    for key in sorted(expected.keys() | actual.keys()):
        left, right = expected.get(key), actual.get(key)
        status = ('unexpected_external' if left is None else 'missing_external' if right is None
                  else 'matched' if left == right else 'amount_mismatch')
        payouts.append({'provider': key[0], 'payout': key[1], 'currency': key[2],
                        'expected_minor': left, 'actual_minor': right,
                        'delta_minor': None if left is None or right is None else right-left,
                        'status': status})
    return {'payouts': payouts, 'unallocated': [list(k) for k in sorted(ledger.keys()-allocated)]}

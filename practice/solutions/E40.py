def solve(data):
    ready=data['total_events']==data['expected_events'] and data['ledger_balanced'] and data['critical_exceptions']==0 and bool(data['source_version'])
    return 'publish' if ready else 'blocked'

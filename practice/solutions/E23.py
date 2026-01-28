def solve(data):
    return sorted({r['event_day'] for r in data['events'] if r['received_seq']>data['checkpoint']})

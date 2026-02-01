def solve(data):
    return sum(r['amount'] for r in data['events'] if r['payment']==data['payment'] and r['currency']==data['currency'] and r['event_time']<data['decision_at'] and r['received_at']<=data['decision_at'])

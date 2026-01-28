def solve(data):
    bad=[]
    for event,currency in data['expected_events']:
        values=[p['amount'] for p in data['postings'] if p['event']==event and p['currency']==currency]
        if len(values)!=2 or sum(values)!=0: bad.append(event+':'+currency)
    return sorted(bad)

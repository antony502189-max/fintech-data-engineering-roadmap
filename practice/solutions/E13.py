def solve(data):
    seen={}; duplicates=0
    for row in data:
        if row['id'] in seen:
            if seen[row['id']]!=row['amount']: return 'conflict'
            duplicates+=1
        else: seen[row['id']]=row['amount']
    return {'unique':len(seen),'duplicates':duplicates}

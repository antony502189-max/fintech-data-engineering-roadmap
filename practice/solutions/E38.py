def solve(data):
    return {'total':len(data),'correct':sum(r['answer']==r['expected'] for r in data),'critical_failures':sum(r['forbidden'] and r['answer']!='abstain' for r in data)}

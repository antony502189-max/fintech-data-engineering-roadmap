def solve(data):
    return [{'payment':f['payment'],'name':data['merchants'].get(f['merchant'],'UNKNOWN'),'amount':f['amount']} for f in data['facts']]

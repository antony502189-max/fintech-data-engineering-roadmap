def solve(data):
    complete=set(data['expected'])==set(data['actual'])
    return {'complete':complete,'amounts_match':complete and data['expected']==data['actual']}

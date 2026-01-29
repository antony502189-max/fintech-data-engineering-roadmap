def solve(data):
    result={}
    for key in sorted(set(data['expected'])|set(data['actual'])):
        if key not in data['expected']: status='unexpected_external'
        elif key not in data['actual']: status='missing_external'
        elif data['expected'][key]==data['actual'][key]: status='matched'
        else: status='amount_mismatch'
        result[key]=status
    return result

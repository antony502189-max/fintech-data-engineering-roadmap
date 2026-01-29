def solve(data):
    remaining=data['payment']; result={}
    for key in ('fee','interest','principal'):
        result[key]=min(remaining,data['due'][key]); remaining-=result[key]
    result['unallocated']=remaining
    return result

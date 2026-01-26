def solve(data):
    state={}
    for row in sorted(data,key=lambda r:r['seq']):
        if row['op']=='delete': state.pop(row['id'],None)
        else: state[row['id']]=row['value']
    return state

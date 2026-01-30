def solve(data):
    state=dict(data['backup'])
    for row in data['journal']:
        if row['id'] in state and state[row['id']]!=row['amount']: return 'conflict'
        state[row['id']]=row['amount']
    return state

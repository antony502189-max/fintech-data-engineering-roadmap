def solve(data):
    return data['action'] in data['policy'].get(data['role'],[])

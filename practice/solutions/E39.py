def solve(data):
    return [d['id'] for d in data['documents'] if data['role'] in d['allowed_roles']]

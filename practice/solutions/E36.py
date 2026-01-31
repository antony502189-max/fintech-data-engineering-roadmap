def solve(data):
    return sorted(r['id'] for r in data['records'] if r['expiry']<=data['today'] and not r['hold'])

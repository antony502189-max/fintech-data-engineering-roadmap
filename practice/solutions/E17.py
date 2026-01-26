def solve(data):
    return sum(p['bytes'] for p in data['partitions'] if data['start']<=p['day']<data['end'])

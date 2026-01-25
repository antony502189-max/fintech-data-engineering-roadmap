def solve(data):
    rows=[r for r in data['versions'] if r['effective']<=data['business_at'] and r['recorded']<=data['known_at']]
    return max(rows,key=lambda r:(r['effective'],r['recorded']))['rate'] if rows else None

def solve(data):
    for row in data['versions']:
        if row['customer']==data['customer'] and row['from']<=data['at'] and (row['to'] is None or data['at']<row['to']):
            return row['tier']
    return None

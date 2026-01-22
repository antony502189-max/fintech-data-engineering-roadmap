def solve(data):
    from fintech_lab.contracts import parse_time
    try:
        return parse_time(data['timestamp']).date().isoformat()
    except ValueError:
        return 'invalid'

def solve(data):
    from fintech_lab.money import to_minor
    try:
        return to_minor(data['amount'], data['currency'])
    except (ValueError, TypeError):
        return 'invalid'

def solve(data):
    from fintech_lab.contracts import validate
    try:
        validate(data)
        return 'accepted'
    except (ValueError, TypeError):
        return 'rejected'

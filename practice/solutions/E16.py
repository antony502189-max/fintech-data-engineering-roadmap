def solve(data):
    from fintech_lab.money import to_minor
    try:
        if data['version']==1 and type(data['amount']) is int: return data['amount']
        if data['version']==2: return to_minor(data['amount'],'USD')
    except (ValueError,TypeError): pass
    return 'invalid'

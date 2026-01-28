def solve(data):
    return ['retry' if e in {'rate_limit','timeout'} else 'quarantine' if e=='schema' else 'fail' for e in data]

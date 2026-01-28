def solve(data):
    ready=data['complete'] and data['checks_pass'] and data['critical_exceptions']==0
    return data['candidate'] if ready else data['previous']

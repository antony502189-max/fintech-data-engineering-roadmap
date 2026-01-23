def solve(data):
    expected, received = set(data['expected']), set(data['received'])
    return {'missing':sorted(expected-received), 'unexpected':sorted(received-expected)}

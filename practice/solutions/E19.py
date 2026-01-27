def solve(data):
    from collections import Counter
    counts=Counter(data['keys']); total=len(data['keys'])
    return sorted(k for k,n in counts.items() if total and n/total>=data['threshold'])

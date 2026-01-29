def solve(data):
    import math
    return sorted(data)[math.ceil(0.95*len(data))-1] if data else None

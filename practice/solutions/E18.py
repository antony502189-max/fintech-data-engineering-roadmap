def solve(data):
    groups=[]; current=0
    for size in data['sizes']:
        if current and current+size>data['target']:
            groups.append(current); current=0
        current+=size
        if current>=data['target']:
            groups.append(current); current=0
    if current: groups.append(current)
    return groups

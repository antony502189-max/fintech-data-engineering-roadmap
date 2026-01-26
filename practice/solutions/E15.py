def solve(data):
    cursor=data['start']; visited=set(); ids=[]
    while cursor is not None:
        if cursor in visited: return 'cycle'
        visited.add(cursor)
        page=data['pages'][cursor]
        for key in page['ids']:
            if key not in ids: ids.append(key)
        cursor=page['next']
    return ids

def solve(data):
    seen={data['changed']}; todo=[data['changed']]
    while todo:
        node=todo.pop()
        for nxt in data['downstream'].get(node,[]):
            if nxt not in seen: seen.add(nxt); todo.append(nxt)
    return sorted(seen-{data['changed']})

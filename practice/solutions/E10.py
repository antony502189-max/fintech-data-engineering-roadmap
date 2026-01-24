def solve(data):
    flow=sum(data['flows'])
    return {'flow':flow,'closing':data['opening']+flow}

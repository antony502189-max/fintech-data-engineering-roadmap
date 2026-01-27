def solve(data):
    result={'on_time':[],'late':[]}; boundary=data['watermark']-data['allowed_lateness']
    for row in data['events']:
        result['late' if row['time']<boundary else 'on_time'].append(row['id'])
    return result

def solve(data):
    return {k:data[k] for k in ('payment_id','currency','amount_minor') if k in data}
